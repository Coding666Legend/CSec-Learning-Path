#### Active Directory
**What is Active Director?**
  - Directory service developed by Microsoft to manage Windows domain networks
  - Stores information related to objects, such as Computers, Users, Printers, etc.
	  - Think about it as a Phone Book for Windows
  - Authenticates using Kerberos tickets.
	  - Non-Windows devices, such as Linux machines, firewalls, etc. can also authenticate to Active Directory via RADIUS or LDAP
- Can be exploited without without ever attacking patchable exploits
	- Instead, we abuse features, trusts, components, and more.

**Physical AD Components :**
- **Domain Controllers -**
	It is a server with the AD DS (Domain service )server role installed that has specifically been promoted to a domain controller.
	- Host a copy of the AD DS directory store
	- Provide authentication and authorization services
	- Replicate updates to other domain controllers in the domain and forest
	- Allow administrative access to manager user accounts and network resources 
- **AD DS Data Store -**
	It contains the database files and processes that stores and manage directory information for users, services, and applications.
	- Consists of the Ntds.dit file
	- Is stored by default in the %SystemRoot%\NTDS folder on all domain controllers
	- Is accessible only through the domain controller processes and protocols

**Logical AD Components :**
- **AD DS Schema -**
	Defines every type of object that can be stored in the directory. 
	Enforces rules regarding object creation and configuration.

| Object Types     | Function                                      | Examples         |
| ---------------- | --------------------------------------------- | ---------------- |
| Class Object     | What objects can be created in the directory  | User<br>Computer |
| Attribute Object | Information that can be attached to an object | Display name     |
- **Domains -**
	Domains are used to group and manage objects in an organization 
	- An administrative boundary for applying policies to groups of objects
	- A replication boundary for replicating data between domain controllers
	- An authentication and authorization boundary that provides a way to limit the scope of access to resources
- **Trees -**
	A domain tree is a hierarchy of domains in AD DS
	- Share a contiguous namespace with the parent domain
	- Can have additional child domains
	- By default create a two-way transitive trust with other domains
- **Forest -**
	A forest is a collection of one or more domain trees
	- Share a common schema
	- Share a common configuration partition
	- Share a common global catalog to enable searching
	- Enable trusts between all domains in the forest
	- Share the Enterprise Admins and Schema Admins groups
- **Organizational Units (OUs) -**
	OUs are AD containers that can contain users, groups, computers, and other OUs
	- Used to Represent your organization hierarchically and logically
	- Manager a collection of objects in a consistent way
	- Delegate permissions to administer groups of objects
	- Apply policies
- **Trusts -**
	Trusts provide a mechanism for users to gain access to resources in another domain
	- All domains in a forest trust all other domains in the forest
	- Trusts can extent outside the forest

| Types of Trusts | Description                                                                                   |
| --------------- | --------------------------------------------------------------------------------------------- |
| Directional     | The trust direction flows from trusting domain to the trusted domain                          |
| Transitive      | The trust relationship is extended beyond a two-domain trust to include other trusted domains |
- **Objects -**

| Object         | Description                                                                                   |
| -------------- | --------------------------------------------------------------------------------------------- |
| User           | Enables network resources access for a user                                                   |
| InetOrgPerson  | Similar to a user account<br>Used for compatibility with other directory services             |
| Contacts       | Used primarily to assign e-mail addresses to external users<br>Does not enable network access |
| Groups         | Used to simplify the administration of access control                                         |
| Computers      | Enables authentication and auditing of computer access to resources                           |
| Printers       | Used to simplify the process of locating and connecting to printers                           |
| Shared folders | Enable users to search for shared folders based on properties                                 |


AD LAB --
DC ->
PC name - EvilCorp-DC (HYDRA-DC)
NetBIOS domain name - ECORP (MARVEL)
sys pass - Pass123!
root domain name - ECorp.local (MARVEL.local)
DSRM pass - Pass123!

User 1 ->
full name - Elliot Alderson (Frank Castle)
PC name - ElliotA
pass - Elliot@443

User 2 ->
full name - Darlene Alderson
PC name - DarleneA
pass - Darlene@80

setting up users, groups and polices -

domain users (DU) ->
user 1 - 
Elliot Alderson (Frank Castle)
login name - EAlderson
pass - EA@DU443

user 2 - 
Darlene Alderson (Peter Parker)
login name - DAlderson
pass - DA@DU80

domain admin (DA)-> 
Tyrell Wellick (Tony Stark)
login name - TWellick
pass - TW@DA2019 (2019 is the server version)

fake domain admin -> (a service account)
SQL Service
login name - SQLService
pass - SS@DA2019 (2019 is the server version)

setting Elliot Alderson to be a local administrator on his machine
setting Elliot Alderson to be a local administrator on Darlene Alderson's machine

---
#### Attacking Active Directory
**Initial AD Attack Vectors :**
- **LLMNR Poisoning :**
	- **what is LLMNR?**
		- LLMNR is Link-Local Multicast Name Resolution (substitute of DNS when DNS fails)
		- Used to identify hosts when DNS fails to do so
		- Previously called NBT-NS (NetBIOS Name Service)
		- Key flaw is that the services utilize a user's username and NTLMv2 (password) hash when appropriately responded to
	- **Steps -**
		- 1. Run Responder
		- 2. An Event Occurs..
		- 3. Get Dem Hashes
		- 4. Crack Dem Hashes (hashcat -m 5600 hashes.txt rockyou.txt)
	- **Hands-On :** (capturing NTLMv2 Hashes)
		- 1. start responder (ge): responder -I eth0 -dwv 
		- 2. [On ElliotA] point to <kali_ip> from the File-exp URL
		- 3. Check the Events of your responder
	- **Hands-On :** (password cracking with hashcat)
		- 1. Copy the entire hash into ntlmhash.txt
		- 2. run (base-os): hashcat -m 5600 ntlmhash.txt rockyou.txt -O
	- **LLMNR Poisoning Mitigation -**
		The best defense in this case is to disable LLMNR and NBT-NS.
		- To disable LLMNR, select "Turn OFF Multicast Name Resolution" under Local Computer Policy > Computer Configuration > Administrative Templates > Network > DNS Client in the Group Policy Editor.
		- To disable NBT-NS, navigate to Network Connections > Network Adapter Properties > TCP/IPv4 Properties > Advanced tab > WINS tab and select "Disable NetBIOS over TCP/IP".
		If a company must use or cannot disable LLMNR/NBT-NS, the best course of action is to:
		- Require Network Access Control
		- Require strong user passwords (e.g., >14 characters and limit common word usage). The more complex and long the password, the harder it is for an attacker to crack the hash.
- **SMB Relay Attacks :**
	- **what is SMB relay?**
		Instead of cracking hashes gathered with Responder, we can instead relay those hashes to specific machines and potentially gain access
		Requirements:
		- SMB signing (packet-level protocol) must be disabled on the target 
		- Relayed user credentials must be admin on machine
	- **Steps -**
		- 1. Turn Off - > SMB HTTP in Responder.conf
		- 2. Run Responder 
		- 3. Set up your relay (configure ntlmrelayx, specify targets)
		- 4. An Event Occurs...
		- 5. Win
	- **Discovering Hosts with SMB signing disabled -**
		nessus scan, nmap (w/ built-in script), or browse for "SMB signing check tool"
		**Steps w/ nmap -**
		- 1.  run : nmap --script=smb2-security-mode.nse -p 445 192.168.122.0/24
		- 2. create `targets.txt`: with ip of 2nd machine
		- 3. turn off SMB HTTP in : /etc/responder/Responder.conf
		- 4. [Terminal 1] start responder (ge): responder -I eth0 -dwv 
		- 4. [Terminal 2] run : impacket-ntlmrelayx -tf targets.txt -smb2support
		- 5.  [On ElliotA] point to <kali_ip> from the File-exp URL
		- 6. Check back Terminal 2