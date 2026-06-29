#### Networking Refresher - 
1. OSI (open systems interconnection) model (layers):
	Physical > Data Link > Network > Transport > Session > Presentation > Application
	  1                  2                    3                    4                    5                    6                           7
	  Troubleshoot path way -
	  Network Level -------------->>>
	  <<<------------ Application Level 
2. IP (internet protocol)Addresses:
3. MAC (Media Access Control) Addresses:
	NIC (Network interface card) has the MAC address
	MAC addr 1st 3 pairs - Identifiers (might show Vendor's name)
4. TCP (transmission control protocol), UDP (user datagram protocol) and 3-way handshake:
	TCP is connection oriented - HTTP/S, FTP, etc
	UDP is connection-less - streaming, DNS, VoIP, etc
	3-way handshake - SYN > SYN ACK > ACK packets (clearly visible in wireshark)
5. Common Ports and Protocols:

| TCP Ports               | UDP Ports     |
| ----------------------- | ------------- |
| FTP (21)                | DNS (53)      |
| SSH (22)                | DHCP (67, 68) |
| Telnet (23)             | TFTP (69)     |
| SMTP (25)               | SNMP (161)    |
| DNS (53)                |               |
| HTTP (80) / HTTPS (443) |               |
| POP3 (110)              |               |
| SMB (139 + 445)         |               |
| IMAP (143)              |               |
6. Subnetting:
	![[TCM-subnetting-cheatsheet.png]]
	

|        | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   (255.0.0.0)      |
| ------ | --- | --- | --- | --- | --- | --- | --- | -------------------- |
|        | 9   | 10  | 11  | 12  | 13  | 14  | 15  | 16 (255.255.0.0)     |
|        | 17  | 18  | 19  | 20  | 21  | 22  | 23  | 24 (255.255.255.0)   |
|        | 25  | 26  | 27  | 28  | 29  | 30  | 31  | 32 (255.255.255.255) |
|        |     |     |     |     |     |     |     |                      |
| Hosts  | 128 | 64  | 32  | 16  | 8   | 4   | 2   | 1                    |
| Subnet | 128 | 192 | 224 | 240 | 248 | 252 | 254 | 255                  |
Notes: 
1. Hosts double each increment of a CIDR
2. Always subtract 2 from Host total:
	Network ID - First Address (inet - ifconfig)
	Broadcast - Last Address (broadcast - ifconfig)
(bonus) tool for CIDR to IP and IP range to CIDR
https://www.ipaddressguide.com/cidr
more similar IP tools available on: https://www.ipaddressguide.com/

#### Kali Linux Overview - 

Tool to learn about and breakdown shell commands: https://explainshell.com/

Users & Privileges:

Networking Commands:
ip a
ifconfig
iwconfig (for wireless)

ARP tables - 
arp -a
ip n (modern)

Traffic routing -
route
ip r (modern)

Hosting Web server - 
The Python cmd: python3 -m http.server 80
- this host the web server enabling to access content present in that pwd.

#### Bash Scripting - 
{attach IP sweeper script.sh  and the sample log file.}

#### Python Scripting -

1. Strings:
	triple quotes allows multi-line strings - 
	print("""This allows
	multi-line strings""")
2. Math:
	PEDMAS - Parenthesis > Exponent > Divide > Multiply > Add > Subtract
	the sequence/rule of operations for the operators () ** / * + -
3.  Lists:
	1. methods - 
		.pop() - removes the last item (pops out the last item)
		.pop(index) - pops out the item present at that index
	2. 2D lists - 
		example code:
		```
		grades  = [["Bob", 82], ["Alice", 90], ["Jeff", 73]]
		bobs_grade = grades[0][1] #set bob's grade
		# [i][j] - i is Row & J is Column
		print(bobs_grade)
		grades[0][1] = 83 #update bob's grade
		print(grades)
		```
	3. Tuples - lists which do not change

4. Looping:
5. Advanced Strings:
	sample code: 
	```
	sentence = "This is a sentence."
	print(sentence.split()) # delimiter - default is space.
	# A **delimiter** is a character or sequence of characters used to **separate pieces of data**.
	
	sentence_split = sentence.split() # deconstructed
	sentence_join = ' '.join(sentence_split) # re-constructed
	print(sentence_join) # returns the sentence is it was.
	```
4. Dictionaries:

#### Reconnaissance
1. Passive Recon:
	1. **Physical/Social information -** 
		![[Physical-or-Social-infos.png|334]]
	2. **Web/Host -**
		![[web-or-host-infos.png|432]]
		
	**Identifying Our Target**:
	
	**Discovering Email Addresses:**
		tools - https://hunter.io/ ; https://phonebook.cz/ ;  clearbit-connect ; 
		https://tools.verifyemailaddress.io/ ; https://email-checker.net/validate/ ; 
		
	**Gathering/Hunting Breached Credentials:**
		