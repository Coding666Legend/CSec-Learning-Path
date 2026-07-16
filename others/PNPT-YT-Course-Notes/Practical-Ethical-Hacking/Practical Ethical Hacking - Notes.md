#### Networking Refresher

1. **OSI (Open Systems Interconnection) Model (Layers):**
	Mnemonics - "Please Do Not Throw Sausage Pizza Away" 
    ```
    Physical > Data Link > Network > Transport > Session > Presentation > Application

         1      2          3            4       5      6               7

    Troubleshoot path way -

    Network Level (Recieve Data) ------------------------------------->>>>>>>>>
    <<<<<<<<<-------------------------------- (Transmit Data) Application Level
    ```

2. **IP (Internet Protocol) Addresses:** (Layer 3)
	- IPv4 (inet)
		- Decimal form
		- (8-bits).(8-bits).(8-bits).(8-bits) = 32 bits = 4 bytes 
		- each section is called an octate
		- 128 64 32 16 8 4 2 1 (0's 1's are the switches for each of the numbers)
		- for eg. 11111111.11111111.11111111.11111111 = 255.255.255.255
		- for eg. 00000111.00000111.00000111.00000111 = 7.7.7.7
	- IPv6 (inet6)
		- Hexa-Decimal form
		- 128 bits IP address

**IPv4 Address Classes**

| Class | First Octet Range | Default Subnet Mask | CIDR | Network Bits | Host Bits | Number of Networks | Hosts per Network* | Typical Use |
|-------|--------------------|---------------------|------|--------------|-----------|--------------------|--------------------|-------------|
| A | 1–126 | 255.0.0.0 | /8 | 8 | 24 | 126 | 16,777,214 | Very large networks |
| B | 128–191 | 255.255.0.0 | /16 | 16 | 16 | 16,384 | 65,534 | Medium-sized networks |
| C | 192–223 | 255.255.255.0 | /24 | 24 | 8 | 2,097,152 | 254 | Small networks |
| D | 224–239 | N/A | N/A | N/A | N/A | N/A | N/A | Multicast |
| E | 240–255 | N/A | N/A | N/A | N/A | N/A | N/A | Experimental / Reserved |

\*Usable host addresses exclude the network and broadcast addresses.

**Special Notes**

| Address Range | Purpose |
|---------------|---------|
| 0.0.0.0/8 | "This network" / unspecified address |
| 127.0.0.0/8 | Loopback (localhost) |
| 169.254.0.0/16 | APIPA (Automatic Private IP Addressing) |
| 224.0.0.0–239.255.255.255 | Multicast |
| 240.0.0.0–255.255.255.254 | Reserved/Experimental |
| 255.255.255.255 | Limited broadcast |
**Private IPv4 Address Ranges**

| Class | Private Range                 | CIDR           |
| ----- | ----------------------------- | -------------- |
| A     | 10.0.0.0 – 10.255.255.255     | 10.0.0.0/8     |
| B     | 172.16.0.0 – 172.31.255.255   | 172.16.0.0/12  |
| C     | 192.168.0.0 – 192.168.255.255 | 192.168.0.0/16 |
		
3. **MAC (Media Access Control) Addresses:** (Layer 2)
    - NIC (Network Interface Card) has the MAC address.
    - MAC addr in `ifconfig` identified as : `ether` 
    - MAC addr 1st 3 pairs - Identifiers (might show Vendor's name, browse web for it)

4. **TCP (Transmission Control Protocol), UDP (User Datagram Protocol) and 3-way Handshake:**
    - TCP is connection oriented - HTTP/S, FTP, etc
    - UDP is connection-less - streaming, DNS, VoIP, etc
    - 3-way handshake - SYN > SYN ACK > ACK packets (clearly visible in Wireshark)

5. **Common Ports and Protocols:**

| TCP Ports               | UDP Ports     |
| ----------------------- | ------------- |
| FTP (21)                | DNS (53)      |
| SSH (22)                | DHCP (67, 68) |
| Telnet (23)             | TFTP (69)     |
| SMTP (25)               | SNMP (161)    |
| POP3 (110)              |               |
| IMAP (143)              |               |
| DNS (53)                |               |
| HTTP (80) / HTTPS (443) |               |
| SMB (139 + 445)         |               |

6. **Subnetting:** (Used to determine number of hosts for a Network)

![[CSec-Learning-Path/others/PNPT-YT-Course-Notes/Practical-Ethical-Hacking/assets/TCM-subnetting-cheatsheet.png]]

|        | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8 (255.0.0.0)         |
| ------ | --- | --- | --- | --- | --- | --- | --- | ---------------------- |
|        | 9   | 10  | 11  | 12  | 13  | 14  | 15  | 16 (255.255.0.0)      |
|        | 17  | 18  | 19  | 20  | 21  | 22  | 23  | 24 (255.255.255.0)    |
|        | 25  | 26  | 27  | 28  | 29  | 30  | 31  | 32 (255.255.255.255)  |
|        |     |     |     |     |     |     |     |                        |
| Hosts  | 128 | 64  | 32  | 16  | 8   | 4   | 2   | 1                      |
| Subnet | 128 | 192 | 224 | 240 | 248 | 252 | 254 | 255                    |

**Notes:**
> CIDR Notation = 192.168.0.1/24 ; CIDR Value = 24
1. Hosts double each increment of a CIDR.
2. Always subtract 2 from Host total.
    - Network ID - First Address (inet - ifconfig)
    - Broadcast - Last Address (broadcast - ifconfig)

**(bonus) tool for CIDR to IP and IP range to CIDR**

https://www.ipaddressguide.com/cidr

more similar IP tools available on:
https://www.ipaddressguide.com/

	
---

#### Kali Linux Overview

Tool to learn about and breakdown shell commands:

https://explainshell.com/

**Users & Privileges:**

**Networking Commands:**

```bash
ip a
ifconfig
iwconfig    # for wireless
```

**ARP tables**

```bash
arp -a
ip n        # modern
```

**Traffic routing**

```bash
route
ip r        # modern
```

**Hosting Web server**

The Python cmd:

```bash
python3 -m http.server 80
```
- this host the web server enabling to access content present in that pwd.

---

#### Bash Scripting

{attach IP sweeper script.sh and the sample log file.}

---

#### Python Scripting

1. **Strings:**
    - triple quotes allows multi-line strings -

    ```python
    print("""This allows
    multi-line strings""")
    ```

2. **Math:**
    - PEDMAS - Parenthesis > Exponent > Divide > Multiply > Add > Subtract
    - the sequence/rule of operations for the operators

    ```
    () ** / * + -
    ```

3. **Lists:**

    1. methods -
        - `.pop()` - removes the last item (pops out the last item)
        - `.pop(index)` - pops out the item present at that index

    2. 2D lists -

        example code:

        ```python
        grades = [["Bob", 82], ["Alice", 90], ["Jeff", 73]]

        bobs_grade = grades[0][1]  # set bob's grade

        # [i][j] - i is Row & J is Column

        print(bobs_grade)

        grades[0][1] = 83  # update bob's grade

        print(grades)
        ```

    3. Tuples -
        - lists which do not change

4. **Looping:**

5. **Advanced Strings:**

    sample code:

    ```python
    sentence = "This is a sentence."

    print(sentence.split())  # delimiter - default is space.

    # A **delimiter** is a character or sequence of characters used to **separate pieces of data**.

    sentence_split = sentence.split()  # deconstructed

    sentence_join = ' '.join(sentence_split)  # re-constructed

    print(sentence_join)  # returns the sentence is it was.
    ```

4. **Dictionaries:**

---

#### Reconnaissance

1. **Passive Recon**

    1. **Physical/Social information -**

        ![[assets/Physical-or-Social-infos.png|334]]

    2. **Web/Host -**

        ![[assets/web-or-host-infos.png|432]]

    **Identifying Our Target**

    **Discovering Email Addresses:**

    tools -

    - https://hunter.io/
    - https://phonebook.cz/
    - clearbit-connect
    - https://tools.verifyemailaddress.io/
    - https://email-checker.net/validate/

    **Gathering/Hunting Breached Credentials:**

! Some things/notes are pending, Must be completed Later !

---

2. **Active Recon:**

    **Nmap Scanning:**

    ```bash
    ~$ nmap -T4 -p- -A <ip_address>
    ```

    - might be used multiple times.

    **Enumerating HTTP(80)/HTTPS(443):**

    1. **Nikto**
        - shows the possible vulnerabilities

        General command:

        ```bash
        nikto -h <hostname>
        ```

        Example:

        ```text
        http://192.168.100.249/
        ```

    2. **Dirbuster**
        - lists the possible directories

        Command:

        ```bash
        dirbuster &
        ```

        Target URL:

        ```text
        <hostname>:<port>/
        ```

        Example:

        ```text
        http://192.168.100.249:80/
        ```

        Sample wordlists:

        ```text
        /usr/share/wordlists/dirbuster/directory-list-2.3-small.txt
        ```

**Enumerating SMB/Samba  (139 + 445):**
	**Metasploit Framework:**
		auxiliary: use auxiliary/scanner/smb/smb_version
		RHOSTS: 192.168.100.249
		result: SMBv1 (for Metasploitable2)  
	**SMBclient:**
	
Enumerating SSH (22):
	SSH:
		
        ```bash
        ssh 192.168.100.249
        ssh 192.168.100.249 -oHostKeyAlgorithms=ssh-rsa
        ```
		
Researching Potential Vulnerabilities:

Nessus:
	It is a Vulnerability Scanner - it is not a pre-installed tool.
	Nessus Essential version - used in this course
	target - metasploitable2 NAT interface (192.168.122.95)
	webUI : https://hostname-or-IP:8834/
	
#### Exploitation Phase
Reverse Shell: (used most of the times...)
	Reverse shell means Target connects to AttackBox
	![[assets/Netcat-Reverse-Shell.png|405]]
Bind Shell:
	![[assets/Netcat-Bind-Shell.png|409]]
Staged vs Non-Staged Payloads:
	Payload - The data or code that performs the intended function after being delivered by a carrier, protocol, or exploit.
	![[assets/staged-non-staged-payloads.png|416]]
Gaining root w/ Metasploit Framework:
	Targeting SMB:
		Samba version - 445/tcp open  netbios-ssn Samba smbd 3.0.20-Debian
		searchsploit result -
		Samba 3.0.20 < 3.0.25rc3 - 'Username' map script' Command Execution (Metasploit) 
		exploit found - exploit/multi/samba/usermap_script
		use the rhosts - 192.168.122.95
		more info on - https://www.rapid7.com/db/modules/exploit/multi/samba/usermap_script/
Manual Exploitation:
	**Manual exploitation** is the process of exploiting a vulnerability by directly interacting with the target using custom commands, scripts, or crafted requests, rather than relying on an automated exploitation framework. It requires understanding the vulnerability, constructing the exploit logic, and controlling each stage of execution.
Brute Force Attacks:
	Hydra:
		syntax: hydra -l <username> -P /usr/share/wordlists/metasploit/unix_passwords.txt ssh://<target-host>:22 -t 4 -V
		note: 
			-l -> login name
			-P -> file of password list
			unix_passwords - is used because the target is Unix/linux based
			-t -> no. of threads
			-V -> verbose
	Msfconsole:
		using - auxiliary/scanner/ssh/ssh_login
		set - USERNAME, PASS_FILE, RHOSTS, THREADS
	Credential Stuffing and Password Spraying:
		Credential Stuffing means Injecting Breached Account Credentials In The Hope Of Account Takeover
		Using Burp Suite:
			1. used FoxyProxy tool to add proxy to the following URL :
			http://127.0.0.1:8080/
			2. Send login form request to Intruder
			3. Select Pitchfork (for multiple positions) or Sniper (for single position).
			4. Add username and/or password positions for payload execution
			5. Add file of list of usernames and/or passwords in the Payload Tab
			6. START ATTACK
			7. tip - can use Grep-Match feature in Settings tab for quickly identifying the error/failure codes/texts
#### Buffer Overflow:
**Buffer Overflow (BoF):** A memory corruption vulnerability where a program writes more data into a fixed-size buffer than it can hold, causing adjacent memory to be overwritten. This can lead to crashes, data corruption, or arbitrary code execution if an attacker controls the overflow.

Steps to conduct a Buffer Overflow:
note: the breaking of vulnserver/immunity debugger can be assumed as, the port/service being vulnerable; As of here Vulnserver broke at TRUN but not at STATS.
1. Spiking	
2. Fuzzing
3. Finding the Offset
4. Overwriting the EIP(Extended Instruction Pointer)
5. Finding Bad Characters
6. Finding the Right Module
7. Generating Shell code
8. Root!
==Need To Study This "Buffer Overflow"Topic Separately .==

#### Course Capstone
==Hands-on pending for the boxes Blue Academy Dev Butler Blackpearl==
==Most of the Notes would be present on Cherrytree(kali)==


