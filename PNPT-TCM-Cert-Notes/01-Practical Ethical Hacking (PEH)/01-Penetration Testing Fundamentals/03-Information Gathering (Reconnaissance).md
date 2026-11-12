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

# Hunting Subdomains
Identifying subdomains associated with a target's primary domain using OSINT sources, DNS records, certificate transparency logs, and tools like **Subfinder** and **Amass**. Helps discover hidden assets, forgotten services, and additional attack surfaces within the authorized scope.

Resources -
1. Subfinder
2. Amass
3. Sublist3r
4. Crt.sh (web or CLI)
5. OWASP Amass

> A small fix for Sublist3r
```python
#!/usr/bin/env python3
# paste in /usr/local/bin/sublist3r
import multiprocessing
import runpy

multiprocessing.set_start_method("fork")

runpy.run_path("/usr/bin/sublist3r", run_name="__main__")
```

# Identify Website Technologies

Identifying the technologies used by a website, including its web server, frameworks, CMS, programming languages, libraries, and underlying infrastructure. Tools like **Wappalyzer** and **WhatWeb** help fingerprint the technology stack and identify potential vulnerabilities or outdated components.

Resources -
1. BuiltWith
2. Wappalyzer
3. WhatWeb

# Information Gathering with Burp Suite
Using **Burp Suite** to intercept, inspect, and analyze HTTP/HTTPS traffic between a browser and a web application. It helps identify application endpoints, parameters, cookies, headers, authentication mechanisms, and technologies, providing valuable information for mapping the web application's attack surface.

# Google Fu
Using advanced Google search operators to discover publicly indexed information about a target, such as exposed files, login portals, sensitive documents, and subdomains. Operators like `site:`, `filetype:`, `intitle:`, and `inurl:` help uncover information that may reveal potential attack surfaces.

| Operator      | Syntax                          | Purpose                                                                |
| ------------- | ------------------------------- | ---------------------------------------------------------------------- |
| `site:`       | `site:example.com`              | Restricts results to a specific domain or website.                     |
| `inurl:`      | `inurl:admin`                   | Finds pages containing a specified term in the URL.                    |
| `allinurl:`   | `allinurl:admin login`          | Finds URLs containing all specified terms.                             |
| `intitle:`    | `intitle:"login page"`          | Finds pages containing a specified term in the title.                  |
| `allintitle:` | `allintitle:admin login portal` | Finds pages with all specified terms in the title.                     |
| `intext:`     | `intext:"confidential"`         | Finds pages containing a specified term in their body text.            |
| `allintext:`  | `allintext:employee directory`  | Finds pages containing all specified terms in their body text.         |
| `filetype:`   | `filetype:pdf`                  | Searches for files of a specific format.                               |
| `ext:`        | `ext:xlsx`                      | Searches for files with a specific extension.                          |
| `OR`          | `admin OR administrator`        | Finds results matching either search term.                             |
| `-`           | `site:example.com -www`         | Excludes results containing a specified term.                          |
| `""`          | `"exact phrase"`                | Searches for an exact phrase.                                          |
| `*`           | `"employee * directory"`        | Acts as a wildcard within a quoted phrase.                             |
| `..`          | `2018..2024`                    | Searches within a numerical range.                                     |
| `AROUND(n)`   | `"security" AROUND(5) "audit"`  | Finds terms appearing within approximately n words of each other.      |
| `cache:`      | `cache:example.com`             | Legacy operator for requesting cached webpages; generally unavailable. |
| `related:`    | `related:example.com`           | Legacy operator for finding related websites; unreliable.              |
#### Google Fu — Practical OSINT Dork Examples

|Objective|Dork|
|---|---|
|Find SANS Institute tutorial PDFs|`site:sans.edu filetype:pdf tutorial`|
|Find NIST cybersecurity publications|`site:nist.gov filetype:pdf cybersecurity`|
|Find OWASP security testing guides|`site:owasp.org filetype:pdf "testing guide"`|
|Find MITRE ATT&CK documentation|`site:attack.mitre.org filetype:pdf`|
|Find cybersecurity research papers on IEEE|`site:ieeexplore.ieee.org filetype:pdf cybersecurity`|
|Find publicly indexed security advisories|`site:cisa.gov filetype:pdf "security advisory"`|
|Find GitHub repositories mentioning a specific tool|`site:github.com "Nmap" "README"`|
|Find public bug bounty programs|`site:example.com "bug bounty" OR "vulnerability disclosure"`|
|Find publicly available company annual reports|`site:example.com filetype:pdf "annual report"`|
|Find publicly indexed technology documentation|`site:example.com inurl:docs intitle:"API documentation"`|
# Utilizing Social Media
Gathering intelligence about a target organization or its employees through publicly available social media platforms such as LinkedIn, Facebook, and X. Helps identify employee details, job roles, organizational structure, technologies, relationships, and potential social engineering attack vectors.

| General Social Networking | Professional Networking | Messaging & Community Platforms | Video & Live Streaming | Image & Photography Sharing |
| ------------------------- | ----------------------- | ------------------------------- | ---------------------- | --------------------------- |
| Facebook                  | LinkedIn                | Telegram                        | YouTube                | Pinterest                   |
| Instagram                 | Xing                    | Discord                         | TikTok                 | Flickr                      |
| X (Twitter)               | GitHub                  | WhatsApp                        | Twitch                 | 500px                       |
| Threads                   | GitLab                  | Signal                          | Vimeo                  | Imgur                       |
| VK (VKontakte)            | Behance                 | Skype                           | Dailymotion            | VSCO                        |
| Reddit                    | Dribbble                | Matrix                          | Rumble                 | Snapchat                    |
| Tumblr                    | ResearchGate            | Slack                           | Kick                   | Josh                        |

| Blogging & Publishing | Dating & Social Discovery | Regional & Country-Specific Platforms | Gaming & Virtual Communities | Federated & Decentralized Social Networks |
| --------------------- | ------------------------- | ------------------------------------- | ---------------------------- | ----------------------------------------- |
| Medium                | Tinder                    | Weibo                                 | Steam                        | Mastodon                                  |
| WordPress             | Bumble                    | WeChat                                | Roblox                       | Bluesky                                   |
| Blogger               | Badoo                     | Xiaohongshu (RED)                     | Minecraft                    | Pixelfed                                  |
| Substack              | OkCupid                   | Douyin                                | Epic Games Community         | Lemmy                                     |
| Ghost                 | Hinge                     | Sharechat                             | PlayStation Network          | Diaspora                                  |
| Quora                 | Moj                       | LINE                                  | Xbox Network                 | Misskey                                   |





