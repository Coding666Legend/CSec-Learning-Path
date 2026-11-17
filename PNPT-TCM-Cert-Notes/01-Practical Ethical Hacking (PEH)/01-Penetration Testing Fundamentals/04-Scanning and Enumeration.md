# Introduction
Actively probing target systems to identify live hosts, open ports, running services, software versions, and exposed resources using tools like Nmap. Enumeration further extracts detailed information from discovered services, helping identify misconfigurations, vulnerabilities, and potential attack paths.

# Scanning with Nmap
Using Nmap (Network Mapper) to discover live hosts, identify open ports, detect running services and versions, and fingerprint operating systems. It supports network mapping and vulnerability assessment by revealing exposed services and potential entry points within the authorized target scope.

> Note:
> `arp-scan -l` lists all the networking devices present in the network
> `netdiscover -r <net-ip/cidr>` does the same

Commands :
```bash
nmap -T4 -p- -A <target-ip>
# nmap go to snippet...
```

# Enumerating HTTP and HTTPS
Enumerating HTTP/HTTPS services to identify web technologies, directories, virtual hosts, endpoints, headers, certificates, and application functionality. Tools like **Gobuster, Feroxbuster, Nikto, and WhatWeb** help uncover hidden resources, misconfigurations, and potential web application attack surfaces.

> Note :
> Check for possible credentials in view-source code - web page

#### Nikto - A web Vulnerablilty Scanner
```bash
nikto -h <targe-url>
# merely lists possible vulnerablities
```
#### Dirbuster - Directory Busting tool
```bash
Target Url
[target-url] 

File with list of dirs/files (wordlist)
[path-to-wordlist]
# here - /usr/share/wordlists/dirbuster/directory-list-2.3-small.txt
```

# Enumerating SMB
Enumerating **SMB (Server Message Block)** to identify shared folders, accessible files, users, groups, domain information, and SMB configurations. Tools like **Enum4linux-ng, smbclient, and Nmap** help discover exposed shares, weak permissions, and potential credential or information disclosure vulnerabilities.
#### 139 vs 445

|Feature|Port 139|Port 445|
|---|---|---|
|Protocol|NetBIOS Session Service|Direct-hosted SMB|
|Transport|TCP|TCP|
|SMB type|NetBIOS-based SMB|Native SMB|
|NetBIOS dependency|Yes|No|
|Primary purpose|SMB over NetBIOS|SMB directly over TCP/IP|
|Modern usage|Legacy|Modern Windows environments|
#### Metasploit Framework (tool intro)
```bash
msfconsole

# Auxiliary modules - information gathering, service enumeration, vulnerability scanning, authentication testing, and service interaction.

use auxiliary/scanner/smb/smb_version

show options
# displays current settings/attributes

set rhosts <target-ip>

```

#### SMBClient - try connect to SMB server
```bash
smbclient -L \\\\<target-ip>\\
# try anonymous login
# means proceed without any password
# Eventually might list out file shares

smbclient \\\\<target-ip>\\<Sharename>
```

# Enumerating SSH
Enumerating **SSH (Secure Shell)** to identify the SSH service version, supported authentication methods, host keys, algorithms, and configuration weaknesses. Tools like **Nmap** and `ssh-audit` help identify outdated versions, weak cryptographic settings, and potential authentication attack vectors.

```bash
ssh <target-ip>

# Now since this box is old... it shows like "Unable to negotiate"
# Just proceed with the offerings provided
# here:
# Unable to negotiate with 192.168.122.95 port 22: no matching host key type found. Their offer: ssh-rsa,ssh-dss
# So...
ssh -o HostKeyAlgorithms=+ssh-rsa root@192.168.122.95
# Though we quit from here, as we don't know the passwd

# Generally RCE opportunites not found. Hammering with brute force might work
```

# Researching Potential Vulnerablities
Identifying potential vulnerabilities in discovered services, software versions, and technologies by researching CVEs, security advisories, and known exploits. Resources like **NVD, Exploit-DB, and searchsploit** help assess exploitability and identify possible attack paths.

#### Security Testing - Metasploitable 2 machine
Potential Vulnerabilities Research :
1. **HTTP (80)** -
	`80/tcp    open  http        Apache httpd 2.2.8 ((Ubuntu) DAV/2)`
	(from) searchsploit
	Apache mod_ssl < 2.8.7 OpenSSL - 'OpenFuck.c' Remote Buffer Overflow
	https://github.com/heltonWernik/OpenLuck
2.  SMB (139,445) -
	`139/tcp   open  netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)`
	`445/tcp   open  netbios-ssn Samba smbd 3.0.20-Debian (workgroup: WORKGROUP)`
	(from) searchsploit
	Samba 3.0.20 < 3.0.25rc3 - 'Username' map script' Command Execution (Metasploit) 
3. SSH (22) - 
	`22/tcp    open  ssh         OpenSSH 4.7p1 Debian 8ubuntu1 (protocol 2.0)`
	potentially - https://github.com/talha3117/OpenSSH-4.7p1-CVE-2008-5161-Exploit

# Vulnerability Scanning with Nessus
Using **Nessus** to automatically scan target systems for known vulnerabilities, missing patches, outdated software, and security misconfigurations. It identifies potential weaknesses, assigns severity ratings, and generates reports to help prioritize vulnerabilities for further manual validation and exploitation.

> NOTES PENDING....

