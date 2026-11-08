# Passive Reconnaissance
Passive reconnaissance is the process of gathering information about a target without directly interacting with its systems or infrastructure. It uses publicly available sources such as WHOIS, DNS records, search engines, social media, and public repositories to identify potential attack surfaces while minimizing detection.

#### 1. Physical/Social Side -
> It means actually going on site and maybe doing physical engagement or social engineering aspects (like phishing assessment, etc.)

(For example)
1. Location Information -
	Satellite images, drone recon, building layout (badge readers, break-in areas, security, fencing, etc.)
2. Job Information -
	Employees (name, job title, contact numbers, manager, etc.), Pictures (badge pics, desk pics, computer pics, etc)
#### 2. Web/Host Side -
1. Target Validation - (example) WHOIS, nslookup, dnsrecon
2. Finding Subdomains - (example) Google Fu, dig, nmap, sublist3r, bluto, crt.sh, etc
3. Fingerprinting - (example) Nmap, Wappalyzer, whatweb, BuiltWith, Netcat
4. Data Breaches - (example) HaveIBeenPwned, Breach-Parse, WeLeakInfo

# Identifying the target
Identifying the target involves defining the exact systems, domains, IP addresses, networks, applications, and assets included in the penetration test. It also requires reviewing the Rules of Engagement (RoE), which establish the authorized scope, testing boundaries, permitted techniques, testing windows, communication procedures, and prohibited activities. All testing must remain within the explicitly authorized scope.

# Discovering Email Addresses
Discovering publicly available email addresses associated with a target organization using OSINT sources, search engines, and tools like theHarvester. Helps identify employees, email naming conventions, and potential attack vectors for phishing and credential exposure.

# Gathering Breached Credentials
Collecting and extracting exposed usernames, email addresses, and passwords from breach datasets using tools like **Breach-Parse, DeHashed, etc**. Helps identify compromised accounts and potential password reuse risks during authorized credential exposure assessments.

Resources - 
1. Breach-Parse : https://github.com/hmaverickadams/breach-parse
2. DeHashed (paid) : https://dehashed.com/