# 🛡️ Ultimate Cybersecurity Mastery Roadmap

> **A streamlined, step-by-step guide to starting and advancing your cybersecurity career, curated to prevent information overload.**

---

## 🚀 BEGINNER? START HERE — Your First 30 Days

> *Don't open any other section yet. Follow this exact order first.*

This quick-start path gets you from zero to "I know what I'm doing" in 30 days using only **free** resources.

| Week | Focus | Best Free Resource | Daily Time |
|------|-------|-------------------|------------|
| Week 1 | Linux basics | [Linux Journey — Grasshopper section](https://linuxjourney.com/) then [OverTheWire: Bandit](https://overthewire.org/wargames/bandit/) | 1–2 hrs |
| Week 2 | Networking basics | [Professor Messer Network+ (Free)](https://www.professormesser.com/network-plus/n10-008/n10-008-training-course/) | 1–2 hrs |
| Week 3 | Security fundamentals | [TryHackMe Pre-Security Path (Free)](https://tryhackme.com/path/outline/presecurity) | 1–2 hrs |
| Week 4 | First hands-on hacking | [TryHackMe Complete Beginner Path](https://tryhackme.com/path/outline/beginner) | 1–2 hrs |

**After 30 days**, you'll be ready to use this full roadmap. Come back and start at the [Foundation Phase](#foundation-phase).

---

## ⚡ How to Read This Roadmap

Each topic includes:
- **⭐ START HERE** — The single best free resource to begin with (no confusion, just go here first)
- **📚 Full Resources** — Complete list for deeper study
- **✅ Milestones** — Checklist to confirm you've actually learned the topic before moving on
- **🔧 Tools** — Tools to practice with
- **🏋️ Practical Exercises** — Hands-on activities

**Priority Labels:**
- 🔴 **Essential** — Do not skip, foundational to everything else
- 🟡 **Recommended** — Important, do when you can
- 🟢 **Optional** — Specialized, come back to this later

---

## 📋 Table of Contents

- [Beginner? Start Here](#-beginner-start-here--your-first-30-days)
- [Introduction](#introduction)
- [How to Use This Roadmap](#how-to-use-this-roadmap)
- [Roadmap Overview](#roadmap-overview)
- [Foundation Phase](#foundation-phase) *(4–8 weeks)*
- [Technical Skills Phase](#technical-skills-phase) *(8–16 weeks)*
- [Specialization Phase](#specialization-phase) *(12–24 weeks)*
- [Advanced Phase](#advanced-phase) *(Ongoing)*
- [Professional Development](#professional-development)
- [Learning Resources](#learning-resources)
- [Cybersecurity Tools](#cybersecurity-tools)
- [Certifications Guide](#certifications-guide)
- [Career Paths](#career-paths)
- [Cybersecurity Communities](#cybersecurity-communities)
- [Capture The Flag (CTF) Competitions](#capture-the-flag-ctf-competitions)
- [Cybersecurity Labs and Practice Environments](#cybersecurity-labs-and-practice-environments)
- [Security Research Resources](#security-research-resources)
- [Contributing](#contributing)

---

## Introduction

Welcome to the Ultimate Cybersecurity Mastery Roadmap! This comprehensive guide is designed to help you navigate the complex world of cybersecurity, providing a clear path from beginner to expert level. Whether you're just starting your journey or looking to advance your existing skills, this roadmap will guide you through the essential knowledge, skills, and certifications needed to succeed in the cybersecurity field.

Cybersecurity is a vast and rapidly evolving field that requires continuous learning and adaptation. This roadmap is designed to provide structure to your learning journey, helping you build a solid foundation before moving on to more specialized areas.

---

## How to Use This Roadmap

This roadmap is divided into phases, each building upon the previous one. For each topic, you'll find:

- **⭐ START HERE**: The single best free resource — open this first, not five tabs at once
- **Description**: Brief explanation of the topic
- **Learning Resources**: Recommended courses, books, tutorials, and videos
- **Practical Exercises**: Hands-on activities to reinforce your learning
- **✅ Milestones**: Key indicators that you've mastered the topic before moving on
- **🔧 Tools**: Relevant tools to practice with

Progress through each phase sequentially, but feel free to dive deeper into topics that interest you or are relevant to your career goals. Remember that practical experience is crucial in cybersecurity, so make sure to supplement your theoretical knowledge with hands-on practice.

> ⚠️ **Milestone Rule**: Don't move to the next topic until you can check off at least 70% of that section's milestones. These aren't optional — they're your proof of learning.

---

## Roadmap Overview

### Learning Path Progression & Time Estimates

| Phase | Focus | Estimated Time | Priority |
|-------|-------|----------------|----------|
| **1. Foundation** | Computing, networking, basic security | 4–8 weeks | 🔴 Essential |
| **2. Technical Skills** | Practical security skills across domains | 8–16 weeks | 🔴 Essential |
| **3. Specialization** | Offensive or defensive focus | 12–24 weeks | 🔴 Essential |
| **4. Advanced** | Advanced topics and specialized domains | Ongoing | 🟡 Recommended |
| **5. Professional** | Career advancement and continuous learning | Ongoing | 🟡 Recommended |

> 💡 **Time estimates assume 1–2 hours of daily study.** With 3+ hours/day, you can compress timelines significantly.

---

## Foundation Phase
> ⏱️ **Estimated Time: 4–8 weeks** | 🔴 Everything in this phase is Essential — do not skip.

### 1. Computer Fundamentals

---

#### Operating Systems 🔴 Essential
> ⏱️ 1–2 weeks

**⭐ START HERE (Free):** [CS50: Introduction to Computer Science (Harvard — Free on edX)](https://www.edx.org/course/introduction-computer-science-harvardx-cs50x)
> This is the gold standard free intro course. Watch the lectures, do the problem sets. That's it. Don't look for anything else until you finish this.

- [Operating Systems: Three Easy Pieces](http://pages.cs.wisc.edu/~remzi/OSTEP/) *(Free online book — read after CS50)*
- [MIT 6.S081: Operating System Engineering](https://pdos.csail.mit.edu/6.S081/2020/)
- [Introduction to Operating Systems – Georgia Tech (Udacity)](https://www.udacity.com/course/introduction-to-operating-systems--ud923)

**📚 Books:**
- "Modern Operating Systems" by Andrew S. Tanenbaum
- "Computer Systems: A Programmer's Perspective" by Randal E. Bryant
- "Operating System Concepts" – Abraham Silberschatz, et al.

**🏋️ Practical Exercises:**
- Install and explore Windows, Ubuntu, Arch, macOS
- Learn memory management, scheduling, file systems
- Use [QEMU](https://www.qemu.org/) or [VirtualBox](https://www.virtualbox.org/) to spin up VMs
- Describe from memory what happens when you double-click a program (process creation, memory allocation, CPU scheduling)

**✅ Milestones — Can you do these?**
- [ ] Explain the difference between a process and a thread
- [ ] Navigate a Linux filesystem using only the terminal
- [ ] Create, move, copy, and delete files from the command line
- [ ] Explain what RAM, CPU scheduling, and virtual memory do
- [ ] Complete at least 10 levels of OverTheWire Bandit

---

#### Linux Fundamentals 🔴 Essential
> ⏱️ 1–2 weeks

> 💡 **Why Linux before Networking?** Almost every networking tool you'll use — Wireshark, tcpdump, Nmap, netcat — runs from a Linux terminal. Learning Linux first means you can actually run and understand those tools when you hit the Networking section.

**⭐ START HERE — Step 1 (Free, Zero Linux Experience):** [Linux Journey](https://linuxjourney.com/)
> If you have never used a Linux terminal, start here — not Bandit. Linux Journey is free, browser-based, and requires zero setup. Complete the **Grasshopper** section (about 2–3 hours). It covers the filesystem, basic commands, and permissions. Only after you can navigate the terminal confidently should you move to Step 2.

**⭐ START HERE — Step 2 (Free, After Linux Journey Grasshopper):** [OverTheWire: Bandit](https://overthewire.org/wargames/bandit/)
> Now you're ready. Bandit is a game that forces you to apply Linux commands to hack through 34 levels. Don't look at walkthroughs until you've tried each level for at least 20 minutes. This teaches you more than any video — but it only works *after* you've learned the basics in Step 1.

- [Linux Command Line Basics](https://ubuntu.com/tutorials/command-line-for-beginners#1-overview) *(Free — official Ubuntu tutorial, good Step 1 alternative)*
- [Linux Survival](https://linuxsurvival.com/) *(Free — browser-based practice)*
- [Linux From Scratch](https://www.linuxfromscratch.org/)

**📚 Books:**
- "The Linux Command Line" by William Shotts *(Free PDF at [linuxcommand.org](https://linuxcommand.org/))*
- "How Linux Works" by Brian Ward
- "Linux Bible" by Christopher Negus

**🔧 Tools:**
- [VirtualBox](https://www.virtualbox.org/) - Virtualization software *(Free)*
- [Vagrant](https://www.vagrantup.com/) - Development environment management
- [Kali Linux](https://www.kali.org/) - Security-focused Linux distribution

**🏋️ Practical Exercises:**
- Install and configure a Linux distribution
- Master bash scripting for automation
- Set up a LAMP/LEMP stack
- Configure user permissions and security settings

**✅ Milestones — Can you do these?**
- [ ] Navigate the filesystem, create users, set permissions — all from terminal only
- [ ] Write a bash script that takes input and produces output
- [ ] Use `grep`, `awk`, `sed`, `find`, and `chmod` confidently
- [ ] Complete OverTheWire Bandit up to Level 20+
- [ ] Set up a web server on a fresh Linux VM

---

#### Networking Basics 🔴 Essential
> ⏱️ 1–2 weeks

> 💡 **Why Networking after Linux?** You'll use `tcpdump`, `Wireshark`, `nmap`, and `netcat` throughout this section — all terminal-based tools. Having Linux under your belt means you focus on learning *networking concepts* instead of fighting the command line.

**⭐ START HERE (Free):** [Professor Messer Network+ Full Course (Free on YouTube)](https://www.professormesser.com/network-plus/n10-008/n10-008-training-course/)
> This is the clearest, most organized free networking course available. Watch it in order. Take notes. Don't skip videos.

- [Computer Networking: A Top-Down Approach](https://gaia.cs.umass.edu/kurose_ross/index.php)
- [Stanford CS144: Computer Networking](https://cs144.github.io/)
- [Practical Networking](https://www.practicalnetworking.net/) *(Free — excellent visual explanations)*
- [Wireshark Tutorial (YouTube)](https://www.youtube.com/playlist?list=PLW8bTPfXNGdC5Co0VnBK1yVzAwSSphzpJ)
- [Cisco Networking – Packet Tracer](https://www.netacad.com/courses/packet-tracer)

**📚 Books:**
- "TCP/IP Illustrated, Volume 1" by W. Richard Stevens
- "Network Warrior" by Gary A. Donahue
- Computer Networking: Principles, Protocols and Practice – Olivier Bonaventure

**🔧 Tools:**
- [Wireshark](https://www.wireshark.org/) - Network protocol analyzer
- [tcpdump](https://www.tcpdump.org/) - Command-line packet analyzer
- [Cisco Packet Tracer](https://www.netacad.com/courses/packet-tracer) - Network simulation tool *(Free with registration)*
- [GNS3](https://www.gns3.com/)

**🏋️ Practical Exercises:**
- Simulate networks with GNS3 or Packet Tracer
- Analyze packets with Wireshark
- Practice subnetting, DNS, firewall rules

**✅ Milestones — Can you do these?**
- [ ] Explain the OSI model and name all 7 layers without looking
- [ ] Explain what TCP vs UDP is and when each is used
- [ ] Calculate subnets and CIDR notation
- [ ] Capture and read a real packet in Wireshark
- [ ] Explain what DNS, DHCP, HTTP, and HTTPS do
- [ ] Explain what a firewall and NAT do

---

#### Programming Fundamentals 🔴 Essential
> ⏱️ 2–3 weeks

**⭐ START HERE — Step 1 (Free, Zero Experience, Video Learner):** [Python Tutorial for Beginners by Corey Schafer (Free, YouTube)](https://www.youtube.com/playlist?list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU)
> The best free Python video series available. Corey Schafer explains every concept clearly, at the right pace, with real examples. Watch from video 1 in order. If you prefer learning by watching before reading, start here.

**⭐ START HERE — Step 1 (Free, Zero Experience, Structured Course):** [CS50's Introduction to Programming with Python — Harvard (Free)](https://pll.harvard.edu/course/cs50s-introduction-programming-python)
> Harvard's free Python course, taught by David Malan. Completely free to audit on edX. It's structured, rigorous, and beginner-friendly. If you prefer a university-style course with problem sets over a YouTube playlist, start here instead of Corey Schafer — both are excellent, pick one.

**⭐ START HERE — Step 2 (Free, After Either Above):** [Automate the Boring Stuff with Python (Free online)](https://automatetheboringstuff.com/)
> Once you can run a Python script, this is the best free Python book ever written. It's practical, security-relevant, and teaches you by building real tools. Start at Chapter 1 and don't stop until Chapter 10 minimum.

- [Python for Everybody](https://www.py4e.com/) *(Free — good structured alternative)*
- [Codecademy Python Course](https://www.codecademy.com/learn/learn-python-3)
- [freeCodeCamp JavaScript Algorithms and Data Structures](https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/)
- [Harvard CS50's Web Programming with Python and JavaScript](https://cs50.harvard.edu/web/)

**📚 Books:**
- "Python Crash Course" by Eric Matthes
- "Eloquent JavaScript" by Marijn Haverbeke
- "Head First Python" by Paul Barry

**🔧 Tools:**
- [Visual Studio Code](https://code.visualstudio.com/) - Code editor *(Free)*
- [PyCharm](https://www.jetbrains.com/pycharm/) - Python IDE
- [Jupyter Notebooks](https://jupyter.org/) - Interactive computing
- [Replit](https://replit.com/)

**🏋️ Practical Exercises:**
- Build simple security tools (port scanner, password generator)
- Automate repetitive security tasks
- Solve coding challenges on [HackerRank](https://www.hackerrank.com/) or [LeetCode](https://leetcode.com/)

**✅ Milestones — Can you do these?**
- [ ] Write a Python script that reads a file and searches for a keyword
- [ ] Write a basic port scanner using Python sockets
- [ ] Automate a simple task (rename files, send HTTP requests)
- [ ] Understand and use loops, functions, and classes
- [ ] Read someone else's Python code and explain what it does

---

### 2. Information Security Principles

---

#### CIA Triad & Security Fundamentals 🔴 Essential
> ⏱️ 1 week

**⭐ START HERE (Free, No Account Needed):** [NIST Cybersecurity Framework — Online Learning (Free)](https://www.nist.gov/cyberframework/online-learning)
> Read the NIST Cybersecurity Framework Overview document (15 pages, free PDF). It explains the CIA Triad, risk management, and the five security functions (Identify, Protect, Detect, Respond, Recover). This is the real-world foundation that every security professional references. No account, no signup — just open and read.

> 💡 **After reading:** Watch [Professor Messer's Security+ CIA Triad video (Free, YouTube)](https://www.youtube.com/watch?v=SBcDGb9l6yo) — 5 minutes, crystal clear visual explanation.

- [Cybrary Introduction to IT & Cybersecurity](https://www.cybrary.it/course/introduction-to-it-and-cybersecurity/) *(Free tier available)*
- [NIST Cybersecurity Framework](https://www.nist.gov/cyberframework) *(Free — read the overview document)*
- [edX Introduction to Cybersecurity](https://www.edx.org/course/introduction-to-cybersecurity)
- [Coursera Information Security](https://www.coursera.org/specializations/information-security) *(Audit for free)*

**📚 Books:**
- "Computer Security: Principles and Practice" by William Stallings
- "Security Engineering" by Ross Anderson
- "The Art of Deception" by Kevin Mitnick

**🏋️ Practical Exercises:**
- Analyze case studies of security breaches
- Create a security policy for a fictional organization
- Conduct a basic risk assessment

**✅ Milestones — Can you do these?**
- [ ] Explain Confidentiality, Integrity, and Availability with real examples
- [ ] Describe the difference between a threat, vulnerability, and risk
- [ ] Explain what authentication, authorization, and accounting (AAA) mean
- [ ] Name 5 common attack types (phishing, MITM, SQLi, DoS, ransomware)
- [ ] Explain defense-in-depth in your own words

---

#### Cryptography Basics 🟡 Recommended
> ⏱️ 1–2 weeks

**⭐ START HERE (Free):** [Khan Academy Cryptography (Free)](https://www.khanacademy.org/computing/computer-science/cryptography)
> Completely free, no account needed. Teaches symmetric/asymmetric encryption, hashing, and how HTTPS works — all with visual explanations. Do this before anything else in this section.

- [Cryptography I by Stanford University](https://www.coursera.org/learn/crypto) *(Audit free)*
- [Practical Cryptography for Developers](https://cryptobook.nakov.com/) *(Free online book)*
- [Crypto101](https://www.crypto101.io/) *(Free PDF — great companion)*
- [CryptoHack](https://cryptohack.org/) *(Free — learn by solving challenges)*

**📚 Books:**
- "Serious Cryptography" by Jean-Philippe Aumasson
- "Applied Cryptography" by Bruce Schneier
- "Cryptography Engineering" by Niels Ferguson, Bruce Schneier, and Tadayoshi Kohno

**🔧 Tools:**
- [CyberChef](https://gchq.github.io/CyberChef/) - Encryption/decryption tool *(Free — use this daily)*
- [OpenSSL](https://www.openssl.org/) - Cryptography toolkit
- [Hashcat](https://hashcat.net/hashcat/) - Password recovery tool

**🏋️ Practical Exercises:**
- Implement basic encryption/decryption algorithms
- Analyze cryptographic protocols
- Solve cryptography challenges on [Cryptopals](https://cryptopals.com/)

**✅ Milestones — Can you do these?**
- [ ] Explain symmetric vs asymmetric encryption with examples
- [ ] Explain what a hash is and why MD5 is considered weak
- [ ] Explain how HTTPS/TLS protects web traffic
- [ ] Encode and decode base64 using CyberChef
- [ ] Explain what a digital signature does
- [ ] Crack a simple MD5 hash using online tools

---

#### Security Policies & Compliance 🟡 Recommended
> ⏱️ 1 week

**⭐ START HERE (Free):** [SANS Security Policy Templates (Free)](https://www.sans.org/security-resources/policies/)
> Free downloadable policy templates with explanations. Read 3–4 templates, understand their structure, then move on. No course needed to start here.

- [ISO 27001 Overview](https://www.iso.org/isoiec-27001-information-security.html)
- [NIST Special Publications](https://csrc.nist.gov/publications/sp) *(Free — SP 800-53 is the most important)*
- [GDPR Compliance](https://gdpr.eu/)

**📚 Books:**
- "Information Security Policies, Procedures, and Standards" by Thomas R. Peltier
- "The Compliance Guide to the NIST Cybersecurity Framework" by Lars Benson
- "CISSP Study Guide" by Eric Conrad

**🏋️ Practical Exercises:**
- Create a security policy for a fictional organization
- Conduct a gap analysis against a security framework
- Develop an incident response plan

**✅ Milestones — Can you do these?**
- [ ] Explain what ISO 27001, NIST CSF, and GDPR each cover
- [ ] Write a basic acceptable use policy
- [ ] Explain the difference between a policy, a standard, and a procedure
- [ ] Describe what a risk assessment involves

---

### 3. Basic Security Tools

---

#### Security Tool Fundamentals 🔴 Essential
> ⏱️ 1–2 weeks

**⭐ START HERE (Free):** [TryHackMe: Complete Beginner Path (Free rooms)](https://tryhackme.com/path/outline/beginner)
> The free rooms in this path introduce Nmap, Metasploit, and basic tool usage in a guided, browser-based lab. No setup. Best free introduction to security tools available.

- [SANS SEC504: Hacker Tools, Techniques, Exploits, and Incident Handling](https://www.sans.org/cyber-security-courses/hacker-techniques-exploits-incident-handling/)
- [Black Hills Information Security Webcast](https://www.blackhillsinfosec.com/blog/webcasts/) *(Free webcasts)*
- [Cybrary Open Source Intelligence](https://www.cybrary.it/practice-lab/perform-open-source-intelligence)

**📚 Books:**
- "Hacking: The Art of Exploitation" by Jon Erickson
- "The Hacker Playbook 3" by Peter Kim

**🔧 Tools:**
- [Kali Linux](https://www.kali.org/) - Security-focused Linux distribution
- [Metasploit](https://www.metasploit.com/) - Penetration testing framework
- [Nmap](https://nmap.org/) - Network discovery and security auditing

**🏋️ Practical Exercises:**
- Set up a security lab environment
- Perform basic reconnaissance on a target (with permission)
- Use OSINT tools to gather information

**✅ Milestones — Can you do these?**
- [ ] Run an Nmap scan and interpret the results
- [ ] Set up a Kali Linux VM
- [ ] Perform a basic OSINT lookup on a domain
- [ ] Use Metasploit to exploit a vulnerable VM (like Metasploitable)

---

#### Vulnerability Scanning 🟡 Recommended
> ⏱️ 1 week

**⭐ START HERE (Free):** [OpenVAS / Greenbone Community Edition (Free)](https://www.openvas.org/)
> Free and open-source vulnerability scanner. Follow the official setup guide, run it against Metasploitable, and read the report. Doing this once teaches you more than any video.

- [Nessus Essentials Tutorial](https://www.tenable.com/products/nessus/nessus-essentials) *(Free for up to 16 IPs)*
- [OWASP ZAP Getting Started](https://www.zaproxy.org/getting-started/) *(Free — best for web app scanning)*

**📚 Books:**
- "Mastering Kali Linux for Advanced Penetration Testing" by Vijay Kumar Velu
- "The Basics of Hacking and Penetration Testing" by Patrick Engebretson

**🔧 Tools:**
- [OpenVAS](https://www.openvas.org/) - Open-source vulnerability scanner
- [Nessus](https://www.tenable.com/products/nessus) - Vulnerability scanner
- [Nikto](https://cirt.net/Nikto2) - Web server scanner

**🏋️ Practical Exercises:**
- Set up a vulnerable machine (e.g., [Metasploitable](https://sourceforge.net/projects/metasploitable/))
- Perform vulnerability scans and analyze results
- Create vulnerability reports

**✅ Milestones — Can you do these?**
- [ ] Run OpenVAS or Nessus Essentials against a test machine
- [ ] Interpret a vulnerability report and explain the findings
- [ ] Identify Critical vs High vs Medium vs Low severity vulnerabilities
- [ ] Write a one-page summary of a scan result

---

## Technical Skills Phase
> ⏱️ **Estimated Time: 8–16 weeks** | 🔴 Core sections are Essential, 🟡 others Recommended

### 4. Network Security

---

#### Network Protocols & Security 🔴 Essential
> ⏱️ 2–3 weeks

**⭐ START HERE (Free):** [TryHackMe: Pre-Security — Network Fundamentals (Free)](https://tryhackme.com/module/network-fundamentals)
> Free, hands-on, no setup. Goes from "what is a packet" to analyzing real traffic. Start here, then move to Wireshark practice.

- [Professor Messer Network+ Course](https://www.professormesser.com/network-plus/n10-008/n10-008-training-course/)
- [SANS SEC560: Network Penetration Testing and Ethical Hacking](https://www.sans.org/cyber-security-courses/network-penetration-testing-ethical-hacking/)
- [Cybrary Network Security](https://www.cybrary.it/course/cyber-network-security)

**📚 Books:**
- "Network Security Essentials" by William Stallings
- "Practical Packet Analysis" by Chris Sanders
- "Black Hat Python" by Justin Seitz

**🔧 Tools:**
- [Wireshark](https://www.wireshark.org/) - Network protocol analyzer
- [Nmap](https://nmap.org/) - Network discovery and security auditing
- [Bettercap](https://www.bettercap.org/) - Network attack and monitoring tool
- [Zeek](https://zeek.org/) - Network security monitor

**🏋️ Practical Exercises:**
- Perform network reconnaissance with Nmap
- Analyze network traffic for security issues
- Detect and prevent ARP spoofing attacks
- Configure network security monitoring

**✅ Milestones — Can you do these?**
- [ ] Use Nmap to perform host discovery, port scanning, and OS fingerprinting
- [ ] Capture HTTP traffic in Wireshark and read the contents
- [ ] Explain what ARP poisoning and DNS spoofing attacks do
- [ ] Identify suspicious traffic patterns in a packet capture
- [ ] Configure basic firewall rules

---

#### Firewalls & IDS/IPS 🟡 Recommended
> ⏱️ 1–2 weeks

**⭐ START HERE (Free):** [Snort IDS Tutorial on TryHackMe (Free room)](https://tryhackme.com/room/snort)
> Free, hands-on lab. Learn IDS rules by writing them. The best free intro to intrusion detection available online.

- [pfSense Fundamentals](https://www.netgate.com/training/pfsense-fundamentals-and-advanced-application)
- [Suricata IDS/IPS](https://suricata.io/) *(Free and open source)*
- [Cisco Firewall Configuration](https://www.cisco.com/c/en/us/solutions/small-business/resource-center/security/how-to-setup-a-firewall.html)

**📚 Books:**
- "Practical Intrusion Analysis" by Ryan Trost
- "The Practice of Network Security Monitoring" by Richard Bejtlich
- "Firewalls and Internet Security" by William R. Cheswick

**🔧 Tools:**
- [pfSense](https://www.pfsense.org/) - Open-source firewall
- [Snort](https://www.snort.org/) - Network intrusion detection system
- [Suricata](https://suricata.io/) - Network IDS/IPS
- [Security Onion](https://securityonionsolutions.com/) - Security monitoring platform

**🏋️ Practical Exercises:**
- Set up a firewall with pfSense
- Configure and tune IDS/IPS rules
- Analyze and respond to security alerts
- Create custom detection rules

**✅ Milestones — Can you do these?**
- [ ] Install and run Snort or Suricata
- [ ] Write a custom Snort rule that detects a specific pattern
- [ ] Explain the difference between IDS (detect) and IPS (prevent)
- [ ] Set up pfSense and block traffic by port and IP

---

#### VPN & Secure Communications 🟡 Recommended
> ⏱️ 1 week

**⭐ START HERE (Free):** [WireGuard Quick Start Guide (Free official docs)](https://www.wireguard.com/quickstart/)
> WireGuard is the modern VPN standard. The official quickstart is clear, free, and takes about an hour. Set it up on two VMs and you'll understand VPNs better than most.

- [OpenVPN Setup Guide](https://openvpn.net/community-resources/how-to/)
- [IPsec VPN Configuration](https://www.cisco.com/c/en/us/support/docs/routers/1700-series-modular-access-routers/71462-rtr-l2l-ipsec-split.html)
- [SSL/TLS Deep Dive](https://www.feistyduck.com/library/openssl-cookbook/)

**📚 Books:**
- "VPNs Illustrated: Tunnels, VPNs, and IPsec" by Jon C. Snader
- "Implementing SSL/TLS Using Cryptography and PKI" by Joshua Davies

**🔧 Tools:**
- [OpenVPN](https://openvpn.net/) - Open-source VPN solution
- [WireGuard](https://www.wireguard.com/) - Modern VPN protocol
- [Strongswan](https://www.strongswan.org/) - IPsec implementation
- [OpenSSL](https://www.openssl.org/) - SSL/TLS toolkit

**🏋️ Practical Exercises:**
- Set up a site-to-site VPN
- Configure a remote access VPN
- Implement certificate-based authentication
- Analyze VPN traffic for security issues

**✅ Milestones — Can you do these?**
- [ ] Set up a working WireGuard VPN tunnel between two machines
- [ ] Explain how TLS handshake works step by step
- [ ] Inspect an SSL certificate and read its fields
- [ ] Explain the difference between SSL, TLS, and HTTPS

---

### 5. System Security

---

#### Operating System Security 🔴 Essential
> ⏱️ 2–3 weeks

**⭐ START HERE (Free):** [TryHackMe: Windows Fundamentals (Free)](https://tryhackme.com/module/windows-fundamentals) + [Linux Privilege Escalation Room](https://tryhackme.com/room/linprivesc)
> Two free paths — do Windows Fundamentals first, then Linux Privesc. Together they cover what you need to know about securing both OSes from an attacker's perspective.

- [Windows Security Fundamentals](https://learn.microsoft.com/en-us/credentials/certifications/security-compliance-and-identity-fundamentals/?practice-assessment-type=certification) *(Free Microsoft Learn)*
- [Linux Security Fundamentals](https://www.udemy.com/course/linux-security-fundamentals/)
- [macOS Security and Privacy Guide](https://github.com/drduh/macOS-Security-and-Privacy-Guide) *(Free GitHub guide)*
- [SANS SEC505: Securing Windows](https://www.cybersecuritycourses.com/course/sec505-securing-windows-and-powershell-automation/)

**📚 Books:**
- "Windows Internals" by Mark Russinovich
- "Linux Security Cookbook" by Daniel J. Barrett
- "macOS and iOS Internals" by Jonathan Levin

**🔧 Tools:**
- [Microsoft Baseline Security Analyzer](https://learn.microsoft.com/en-us/windows/security/operating-system-security/device-management/windows-security-configuration-framework/mbsa-removal-and-guidance)
- [Lynis](https://cisofy.com/lynis/) - Security auditing tool for Linux *(Free)*
- [OpenSCAP](https://www.open-scap.org/) - Security compliance solution
- [Sysinternals Suite](https://docs.microsoft.com/en-us/sysinternals/) *(Free from Microsoft)*

**🏋️ Practical Exercises:**
- Harden a Windows/Linux server
- Implement security baselines
- Perform security audits
- Configure secure authentication mechanisms

**✅ Milestones — Can you do these?**
- [ ] Run Lynis on a Linux system and fix at least 5 findings
- [ ] Apply CIS Benchmark hardening steps to a Windows VM
- [ ] Explain Windows UAC, AppLocker, and Defender
- [ ] Find and disable unnecessary services on a Linux server
- [ ] Set up SSH key-based authentication and disable password login

---
### 6. Web Application Security

---

#### OWASP Top 10 🔴 Essential
> ⏱️ 2–3 weeks

**⭐ START HERE (Free):** [PortSwigger Web Security Academy (Free)](https://portswigger.net/web-security)
> Completely free. The best web security learning platform in existence — built by the makers of Burp Suite. It covers every OWASP vulnerability with hands-on labs you run in your browser. Start at the beginning and work through it systematically.

- [OWASP Top Ten](https://owasp.org/www-project-top-ten/) *(Free official docs — read alongside PortSwigger)*
- [SANS SEC542: Web App Penetration Testing and Ethical Hacking](https://www.sans.org/cyber-security-courses/web-app-penetration-testing-ethical-hacking/)
- [Kontra OWASP Top 10](https://application.security/free/owasp-top-10) *(Free interactive labs)*

**📚 Books:**
- "The Web Application Hacker's Handbook" by Dafydd Stuttard and Marcus Pinto
- "Web Security for Developers" by Malcolm McDonald
- "Real-World Bug Hunting" by Peter Yaworski

**🔧 Tools:**
- [OWASP ZAP](https://www.zaproxy.org/) - Web application security scanner *(Free)*
- [Burp Suite](https://portswigger.net/burp) - Web vulnerability scanner *(Community edition free)*
- [Nikto](https://cirt.net/Nikto2) - Web server scanner
- [SQLmap](https://sqlmap.org/) - SQL injection tool

**🏋️ Practical Exercises:**
- Set up a vulnerable web application (e.g., [DVWA](https://github.com/digininja/DVWA))
- Identify and exploit common web vulnerabilities
- Implement security controls to prevent attacks
- Perform a web application security assessment

**✅ Milestones — Can you do these?**
- [ ] Explain all 10 OWASP Top 10 categories from memory
- [ ] Manually exploit an SQL injection in DVWA
- [ ] Perform a stored XSS attack in a lab environment
- [ ] Use Burp Suite to intercept and modify an HTTP request
- [ ] Explain IDOR and exploit it in a lab
- [ ] Complete at least 5 PortSwigger Academy labs

---

#### Web Application Penetration Testing 🔴 Essential
> ⏱️ 3–4 weeks

**⭐ START HERE (Free):** [OWASP Juice Shop (Free)](https://owasp.org/www-project-juice-shop/)
> A free intentionally-vulnerable web app. Run it locally with Docker, then try to find and exploit all the vulnerabilities. It's a game with a score board. The best free hands-on web hacking practice available.

- [Burp Suite Academy](https://portswigger.net/web-security) *(Free — work through all modules)*
- [HackTheBox Web Challenges](https://www.hackthebox.eu/) *(Free tier available)*
- [PentesterLab](https://pentesterlab.com/) *(Some free exercises)*

**📚 Books:**
- "Mastering Modern Web Penetration Testing" by Prakhar Prasad
- "Bug Bounty Hunting Essentials" by Shahmeer Amir
- "Web Hacking 101" by Peter Yaworski *(Free PDF available)*

**🔧 Tools:**
- [Burp Suite](https://portswigger.net/burp) - Web vulnerability scanner
- [OWASP ZAP](https://www.zaproxy.org/) - Web application security scanner
- [Dirsearch](https://github.com/maurosoria/dirsearch) - Web path scanner
- [Wfuzz](https://github.com/xmendez/wfuzz) - Web application fuzzer

**🏋️ Practical Exercises:**
- Perform a full web application penetration test
- Write a detailed security report
- Exploit and chain multiple vulnerabilities
- Participate in bug bounty programs

**✅ Milestones — Can you do these?**
- [ ] Complete at least 10 challenges on OWASP Juice Shop
- [ ] Write a professional-style penetration test report
- [ ] Chain two vulnerabilities together in a lab (e.g., XSS + session hijack)
- [ ] Submit a valid bug report on a bug bounty platform (HackerOne, Bugcrowd)

---

#### Secure Coding Practices 🟡 Recommended
> ⏱️ 1–2 weeks

**⭐ START HERE (Free):** [OWASP Secure Coding Practices Quick Reference (Free PDF)](https://owasp.org/www-project-secure-coding-practices-quick-reference-guide/)
> A free, concise 17-page PDF by OWASP. Read it in one sitting — it covers everything a developer needs to know about writing secure code. Then apply each principle to code you've already written.

**⭐ Practice Platform (Free tier):** [Secure Code Warrior](https://www.securecodewarrior.com/)
> Secure Code Warrior is the best hands-on secure coding practice platform available. It teaches you to identify and fix vulnerabilities directly in code, across multiple languages (Python, Java, JS, C#, and more). The free tier gives you access to learning tournaments and challenges. This is where you go to practice what you read in the OWASP guide — don't just read theory, code it.

- [Secure Coding in Python](https://github.com/Ericsson/secure_coding_one_stop_shop_for_python)
- [Secure Coding in Java](https://www.oracle.com/java/technologies/javase/seccodeguide.html)
- [Microsoft Secure Coding Guidelines](https://docs.microsoft.com/en-us/previous-versions/visualstudio/visual-studio-2010/ms182020(v=vs.100))

**📚 Books:**
- "Secure Coding in C and C++" by Robert C. Seacord
- "Iron-Clad Java: Building Secure Web Applications" by Jim Manico
- "Secure Programming Cookbook for C and C++" by John Viega

**🔧 Tools:**
- [SonarQube](https://www.sonarqube.org/) - Code quality and security *(Community edition free)*
- [OWASP Dependency-Check](https://owasp.org/www-project-dependency-check/) - Software composition analysis
- [Snyk](https://snyk.io/) - Open source security platform *(Free tier)*
- [Checkmarx](https://www.checkmarx.com/) - Static application security testing
- [Vulert](https://www.vulert.com) - Detects vulnerabilities in open-source dependencies without accessing your code. Supports JS, PHP, Java, Python, and more.

**🏋️ Practical Exercises:**
- Review code for security vulnerabilities
- Implement secure authentication and authorization
- Secure data storage and transmission
- Integrate security into the development lifecycle

**✅ Milestones — Can you do these?**
- [ ] Identify 5 security bugs in a code review exercise
- [ ] Implement parameterized queries to prevent SQL injection
- [ ] Set up SonarQube and scan a project
- [ ] Explain what input validation and output encoding are

---

## Specialization Phase
> ⏱️ **Estimated Time: 12–24 weeks** | Choose Offensive (Section 7) OR Defensive (Section 8) first, then add the other.

### 7. Offensive Security

---

#### Penetration Testing Methodology 🔴 Essential
> ⏱️ 4–6 weeks

**⭐ START HERE (Free):** 

> The best free end-to-end ethical hacking course available. TCM (The Cyber Mentor) walks you through a complete penetration test from recon to reporting in one video. Watch this first — it gives you the full picture before you go deep on any individual technique. No account needed, just watch.

1. [Practical Ethical Hacking - Part 1](https://www.youtube.com/watch?v=3FNYvj2U0HM)
2. [Practical Ethical Hacking - Part 2 ](https://www.youtube.com/watch?v=sH4JCwjybGs)
3. [Active Directory PentTesing ](https://www.youtube.com/watch?v=VXxH4n684HE)
4. [OSINT (Open-Source Intelligence) ](https://www.youtube.com/watch?v=qwA6MmbeGNo)
5. [Linux Privilege Escalation ](https://www.youtube.com/watch?v=ZTnwg3qCdVM)
6. [Windows Privilege Escalation ](https://www.youtube.com/watch?v=uTcrbNBcoxQ)

> 💡 **Want structured paid training from the same instructor?** [TCM Security Academy](https://academy.tcm-sec.com/) offers affordable courses (Practical Ethical Hacking, Linux Privilege Escalation, Windows Privilege Escalation) for $30 each — among the best-value paid courses in the field.

- [TryHackMe: Jr Penetration Tester Path (Free rooms)](https://tryhackme.com/path/outline/jrpentester) *(After the 12-hour video, use this for structured hands-on practice)*
- [HackTheBox Academy](https://academy.hackthebox.com/) *(Some free modules — complements TryHackMe)*
- [SANS Penetration Testing Roadmap](https://www.sans.org/cyber-security-skills-roadmap/)
- [Offensive Security Certified Professional (OSCP)](https://www.offensive-security.com/pwk-oscp/) *(Paid — the gold standard cert)*
- [HTB CPTS — Certified Penetration Testing Specialist](https://academy.hackthebox.com/preview/certifications/htb-certified-penetration-testing-specialist/) *(Paid — newer, rigorous, more affordable than OSCP, highly respected)*
- [Penetration Testing Execution Standard (PTES)](http://www.pentest-standard.org/) *(Free methodology reference)*

**📚 Books:**
- "The Hacker Playbook 3" by Peter Kim
- "Advanced Penetration Testing" by Wil Allsopp
- "Penetration Testing: A Hands-On Introduction to Hacking" by Georgia Weidman

**🔧 Tools:**
- [Metasploit Framework](https://www.metasploit.com/) - Penetration testing framework
- [Cobalt Strike](https://www.cobaltstrike.com/) - Adversary simulation software
- [Empire](https://github.com/BC-SECURITY/Empire) - Post-exploitation framework
- [Covenant](https://github.com/cobbr/Covenant) - .NET command and control framework

**🏋️ Practical Exercises:**
- Complete CTF challenges on platforms like HackTheBox and TryHackMe
- Perform a full penetration test in a lab environment
- Document findings in a professional penetration testing report
- Practice OSCP-like challenges

**✅ Milestones — Can you do these?**
- [ ] Explain the 5 phases of penetration testing (Recon → Scanning → Exploitation → Post-Exploitation → Reporting)
- [ ] Complete 5 HackTheBox "Easy" machines independently
- [ ] Compromise a machine and escalate privileges on both Windows and Linux
- [ ] Write a professional penetration test report with executive summary and technical findings
- [ ] Perform the attack without Metasploit (manual exploitation)

---

#### Exploitation Techniques 🟡 Recommended
> ⏱️ 4–6 weeks

**⭐ START HERE (Free):** [Metasploit Unleashed by Offensive Security (Free)](https://www.offensive-security.com/metasploit-unleashed/)
> The most comprehensive free Metasploit course available, written by the creators of Kali Linux. Goes from basics to advanced usage. Start at the beginning and follow in order.

- [OSCP Preparation Guide](https://johnjhacking.com/blog/the-oscp-preperation-guide-2020/) *(Free blog — great roadmap)*
- [Exploit Development](https://github.com/wtsxDev/Exploit-Development) *(Free GitHub resource list)*
- [Buffer Overflow Tutorial by TiberSecurity (YouTube)](https://www.youtube.com/watch?v=1S0aBV-Waeo)

**📚 Books:**
- "The Shellcoder's Handbook" by Chris Anley
- "A Guide to Kernel Exploitation" by Enrico Perla
- "Gray Hat Python" by Justin Seitz

**🔧 Tools:**
- [Metasploit Framework](https://www.metasploit.com/) - Penetration testing framework
- [GDB](https://www.gnu.org/software/gdb/) - GNU debugger
- [IDA Pro](https://hex-rays.com/ida-pro/) - Disassembler and debugger
- [Ghidra](https://ghidra-sre.org/) - Software reverse engineering framework *(Free from NSA)*

**🏋️ Practical Exercises:**
- Develop custom exploits for known vulnerabilities
- Analyze and modify public exploits
- Practice buffer overflow exploitation
- Perform post-exploitation activities

**✅ Milestones — Can you do these?**
- [ ] Successfully exploit a buffer overflow vulnerability manually
- [ ] Write shellcode and inject it into a vulnerable process
- [ ] Use GDB to step through an exploit
- [ ] Explain ASLR, DEP/NX, and stack canaries

---

#### Social Engineering 🟡 Recommended
> ⏱️ 1–2 weeks

**⭐ START HERE (Free):** [Social Engineering Framework (Free)](https://www.social-engineer.org/framework/general-discussion/)
> Free online resource from the industry's top social engineering experts. Read the framework start to finish — it's the most organized free resource on the topic. No account needed.

- [The Social-Engineer Toolkit (SET)](https://github.com/trustedsec/social-engineer-toolkit) *(Free open-source tool)*
- [SANS SEC567: Social Engineering for Penetration Testers](https://www.sans.org/cyber-security-courses/social-engineering-security/)

**📚 Books:**
- "Social Engineering: The Art of Human Hacking" by Christopher Hadnagy
- "Phishing Dark Waters" by Christopher Hadnagy and Michele Fincher
- "The Art of Deception" by Kevin Mitnick

**🔧 Tools:**
- [Social-Engineer Toolkit (SET)](https://github.com/trustedsec/social-engineer-toolkit)
- [Gophish](https://getgophish.com/) - Open-source phishing framework *(Free)*
- [King Phisher](https://github.com/securestate/king-phisher) - Phishing campaign toolkit
- [SpiderFoot](https://github.com/smicallef/spiderfoot) - OSINT automation tool

**🏋️ Practical Exercises:**
- Create and execute a phishing campaign (in a controlled environment)
- Develop social engineering scenarios
- Practice pretexting and impersonation techniques
- Analyze successful social engineering attacks

**✅ Milestones — Can you do these?**
- [ ] Set up a Gophish campaign in a lab environment
- [ ] Explain 5 social engineering techniques (phishing, vishing, pretexting, tailgating, baiting)
- [ ] Write a convincing phishing email template
- [ ] Identify red flags in real phishing emails

---
## Advanced Phase
> ⏱️ **Estimated Time: Ongoing** | These are 🟡 Recommended unless they match your career specialty

### 10. Advanced Topics

---

#### Malware Analysis 🟡 Recommended
> ⏱️ 4–6 weeks

**⭐ START HERE (Free):** [ANY.RUN Interactive Malware Sandbox (Free tier)](https://any.run/)
> Free, browser-based, no setup. Upload a malware sample and watch it run in an interactive sandbox. Best way to get your first exposure to malware behavior. Pair with the free REMnux VM for local analysis.

- [Practical Malware Analysis Book Labs](https://nostarch.com/malware) *(Book is paid, but labs files are free on GitHub)*
- [SANS FOR610: Reverse-Engineering Malware](https://www.sans.org/cyber-security-courses/reverse-engineering-malware-malware-analysis-tools-techniques/)
- [Malware Analysis Tutorials](https://fumalwareanalysis.blogspot.com/) *(Free blog series)*
- [OALabs YouTube Channel](https://www.youtube.com/@OALABS) - Free malware analysis walkthroughs

**📚 Books:**
- "Practical Malware Analysis" by Michael Sikorski and Andrew Honig
- "Malware Analyst's Cookbook" by Michael Ligh et al.
- "Learning Malware Analysis" by Monnappa K A

**🔧 Tools:**
- [Ghidra](https://ghidra-sre.org/) - Software reverse engineering framework *(Free from NSA)*
- [IDA Pro](https://hex-rays.com/ida-pro/) - Disassembler and debugger
- [Cuckoo Sandbox](https://cuckoosandbox.org/) - Malware analysis sandbox *(Free)*
- [REMnux](https://remnux.org/) - Linux toolkit for malware analysis *(Free)*

**🏋️ Practical Exercises:**
- Analyze malware samples in a safe environment
- Reverse engineer malicious code
- Create malware analysis reports
- Build automated malware analysis pipelines

**✅ Milestones — Can you do these?**
- [ ] Analyze a malware sample in ANY.RUN and describe its behavior
- [ ] Open a binary in Ghidra and identify the main function
- [ ] Identify C2 communication in a malware network capture
- [ ] Write a malware analysis report with IOCs (Indicators of Compromise)
- [ ] Explain the difference between static and dynamic analysis

---

#### Threat Intelligence 🟡 Recommended
> ⏱️ 2–3 weeks

**⭐ START HERE (Free):** [MITRE ATT&CK Framework (Free)](https://attack.mitre.org/)
> The most important free resource in threat intelligence. Read the overview, then pick one APT group and trace their tactics. This framework is used by every enterprise SOC and threat intel team in the world.

- [SANS FOR578: Cyber Threat Intelligence](https://www.sans.org/cyber-security-courses/cyber-threat-intelligence/)
- [Open Source Intelligence Techniques](https://inteltechniques.com/) *(Free resources section)*
- [Threat Intelligence Platforms](https://www.gartner.com/reviews/market/security-threat-intelligence-services)

**📚 Books:**
- "Intelligence-Driven Incident Response" by Scott J. Roberts and Rebekah Brown
- "The Threat Intelligence Handbook" by Recorded Future
- "Applied Intelligence" by Kris Lovejoy

**🔧 Tools:**
- [MISP](https://www.misp-project.org/) - Threat intelligence platform *(Free)*
- [OpenCTI](https://www.opencti.io/) - Open cyber threat intelligence platform *(Free)*
- [ThreatConnect](https://threatconnect.com/) - Threat intelligence platform
- [Recorded Future](https://www.recordedfuture.com/) - Threat intelligence

**🏋️ Practical Exercises:**
- Collect and analyze threat intelligence
- Map threats to the MITRE ATT&CK framework
- Create threat intelligence reports
- Integrate threat intelligence into security operations

**✅ Milestones — Can you do these?**
- [ ] Map a known attack campaign to MITRE ATT&CK TTPs
- [ ] Set up MISP and add threat indicators
- [ ] Write a threat intelligence report on an APT group
- [ ] Explain the difference between strategic, operational, and tactical intelligence

---

#### Advanced Persistent Threats 🟡 Recommended
> ⏱️ 2–3 weeks

**⭐ START HERE (Free):** [MITRE ATT&CK Groups (Free)](https://attack.mitre.org/groups/)
> Free, detailed profiles on every major APT group with their techniques mapped. Pick APT28 or Lazarus Group, read their full profile, and follow the linked references. This is how threat intel analysts actually research APTs.

- [APT Groups and Operations](https://apt.threattracking.com/) *(Free tracker)*
- [Mandiant APT Reports](https://www.mandiant.com/resources/insights/reports) *(Many free reports)*
- [ThaiCERT APT Encyclopedia](https://apt.etda.or.th/cgi-bin/aptgroups.cgi) *(Free)*

**📚 Books:**
- "Advanced Persistent Threat Hacking" by Tyler Wrightson
- "APT41: A Dual Espionage and Cyber Crime Operation" by FireEye

**🔧 Tools:**
- [Yara](https://virustotal.github.io/yara/) - Pattern matching for malware detection *(Free)*
- [Sigma](https://github.com/SigmaHQ/sigma) - Generic signature format for SIEM systems *(Free)*
- [CyberChef](https://gchq.github.io/CyberChef/) - Data analysis tool *(Free)*

**🏋️ Practical Exercises:**
- Analyze APT campaigns and techniques
- Create detection rules for APT tactics
- Simulate APT attacks in a controlled environment
- Develop APT hunting strategies

**✅ Milestones — Can you do these?**
- [ ] Research one APT group and write a 1-page profile
- [ ] Write a YARA rule that detects a malware family
- [ ] Write a Sigma rule to detect a specific ATT&CK technique
- [ ] Explain the kill chain model and how it differs from ATT&CK

---

### 11. Specialized Security Domains

---

#### IoT Security 🟢 Optional
> ⏱️ 2–3 weeks

**⭐ START HERE (Free):** [OWASP IoT Attack Surface Areas (Free)](https://owasp.org/www-project-internet-of-things/)
> Free OWASP project documenting all IoT attack vectors. Read the project, then use Shodan (free tier) to search for real exposed IoT devices. Seeing real exposed devices makes the concepts concrete.

- [IoT Security Foundation](https://www.iotsecurityfoundation.org/) *(Free guidelines)*
- [NIST IoT Security](https://www.nist.gov/itl/applied-cybersecurity/nist-cybersecurity-iot-program) *(Free)*
- [IoT Security Guidelines](https://www.gsma.com/iot/iot-security/iot-security-guidelines/)

**📚 Books:**
- "Practical IoT Hacking" by Fotios Chantzis et al.
- "IoT Penetration Testing Cookbook" by Aaron Guzman and Aditya Gupta
- "Abusing the Internet of Things" by Nitesh Dhanjani

**🔧 Tools:**
- [Shodan](https://www.shodan.io/) - IoT search engine *(Free tier)*
- [Firmware Analysis Toolkit](https://github.com/attify/firmware-analysis-toolkit) - Firmware security analysis *(Free)*
- [IoTSeeker](https://github.com/rapid7/IoTSeeker) - IoT device scanner

**🏋️ Practical Exercises:**
- Analyze IoT device security
- Perform firmware analysis
- Test IoT communication protocols
- Implement IoT security controls

**✅ Milestones — Can you do these?**
- [ ] Use Shodan to find exposed IoT devices and explain the risks
- [ ] Extract and analyze a firmware image
- [ ] Explain MQTT security issues
- [ ] Describe 3 unique IoT attack vectors not present in traditional IT

---

#### Mobile Security 🟢 Optional
> ⏱️ 2–3 weeks

**⭐ START HERE (Free):** [OWASP Mobile Security Testing Guide (Free)](https://owasp.org/www-project-mobile-security-testing-guide/)
> Completely free, comprehensive, and community-maintained. Read the Android Testing Guide first — it covers everything from static analysis to dynamic testing with practical examples.

- [Mobile Application Security Verification Standard](https://github.com/OWASP/owasp-masvs) *(Free)*
- [Android Security](https://source.android.com/security) *(Free official docs)*
- [iOS Security](https://support.apple.com/guide/security/welcome/web) *(Free Apple guide)*

**📚 Books:**
- "Android Security Internals" by Nikolay Elenkov
- "iOS Application Security" by David Thiel
- "Mobile Application Penetration Testing" by Vijay Kumar Velu

**🔧 Tools:**
- [MobSF](https://github.com/MobSF/Mobile-Security-Framework-MobSF) - Mobile security testing framework *(Free)*
- [Frida](https://frida.re/) - Dynamic instrumentation toolkit *(Free)*
- [Objection](https://github.com/sensepost/objection) - Mobile runtime exploration *(Free)*
- [Drozer](https://github.com/FSecureLABS/drozer) - Android security assessment *(Free)*

**🏋️ Practical Exercises:**
- Perform mobile app penetration testing
- Analyze mobile app permissions and security
- Test mobile authentication mechanisms
- Implement secure mobile development practices

**✅ Milestones — Can you do these?**
- [ ] Decompile an Android APK and read its manifest
- [ ] Run MobSF against an APK and interpret the results
- [ ] Use Frida to hook a function in a running Android app
- [ ] Explain the OWASP Mobile Top 10

---

#### Industrial Control Systems Security 🟢 Optional
> ⏱️ 2–4 weeks

**⭐ START HERE (Free):** [ICS-CERT Training (Free)](https://www.cisa.gov/resources-tools/programs/ics-training-available-through-cisa)
> CISA offers free ICS/SCADA security training. Register and take the free online courses — they're the government-backed baseline for ICS security and cost nothing.

- [SANS ICS410: ICS/SCADA Security Essentials](https://www.sans.org/cyber-security-courses/ics-scada-cyber-security-essentials/)
- [NIST SP 800-82: Guide to ICS Security](https://csrc.nist.gov/publications/detail/sp/800-82/rev-2/final) *(Free PDF)*
- [ISA/IEC 62443 Standards](https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443-series-of-standards)

**📚 Books:**
- "Industrial Network Security" by Eric D. Knapp and Joel Thomas Langill
- "Hacking Exposed Industrial Control Systems" by Clint Bodungen et al.
- "Cybersecurity for SCADA Systems" by William Shaw

**🔧 Tools:**
- [Shodan](https://www.shodan.io/) - ICS device search
- [Wireshark](https://www.wireshark.org/) - Protocol analyzer with ICS protocol support
- [Conpot](https://github.com/mushorg/conpot) - ICS honeypot *(Free)*
- [PLCscan](https://github.com/meeas/plcscan) - PLC scanner

**🏋️ Practical Exercises:**
- Set up an ICS lab environment
- Analyze ICS protocols and vulnerabilities
- Implement ICS security controls
- Perform ICS security assessments

**✅ Milestones — Can you do these?**
- [ ] Explain the Purdue Model for ICS architecture
- [ ] Describe how the Stuxnet attack worked
- [ ] Identify ICS devices on Shodan and explain the risk
- [ ] Explain why air-gapping alone is insufficient for ICS security

---

## Professional Development

### 12. Career Development

---

#### Certifications Planning 🟡 Recommended

**⭐ START HERE (Free):** [Paul Jerimy's Security Certification Roadmap (Free)](https://pauljerimy.com/security-certification-roadmap/)
> A free, visual map of every major cybersecurity certification organized by domain and difficulty. Use this as your planning document before spending money on any cert.

**Certification Path by Career Goal:**

| Goal                | Start With             | Then                               | Advanced         |
| ------------------- | ---------------------- | ---------------------------------- | ---------------- |
| Penetration Testing | none - free resources  | PNPT                               | OSCP or HTB CPTS |
| Red Team            | CompTIA Security+      | CRTO (Certified Red Team Operator) | CRTE → OSED      |
| Cloud Security      | AWS Cloud Practitioner | AWS Security Specialty             | CCSP             |
| Management / GRC    | CISSP Associate        | CISM                               | CISO role        |
| Web App Pentesting  | CompTIA Security+      | eWPT (eLearnSecurity)              | OSWE or BSCP     |

> 💡 **Notes on newer certs worth knowing:**
> - **[HTB CPTS](https://academy.hackthebox.com/preview/certifications/htb-certified-penetration-testing-specialist/)** — HackTheBox's Certified Penetration Testing Specialist. Rigorous, practical, well-respected, and more affordable than OSCP. Excellent alternative or stepping stone.
> - **[eWPT](https://elearnsecurity.com/product/ewpt-certification/)** — eLearnSecurity Web Application Penetration Tester. Great web pentesting cert for those on the OSCP path.
> - **[CRTO](https://training.zeropointsecurity.co.uk/courses/red-team-ops)** — Certified Red Team Operator by Zero-Point Security. The best practical red team cert for beginners to red teaming. Focuses on Cobalt Strike and real C2 operations.
> - **[TCM Security Certifications](https://certifications.tcm-sec.com/)** — PNPT (Practical Network Penetration Tester) is an affordable, practical alternative to CEH. Strong industry recognition for the price.

> 💡 **Best free certification to start with:** [CompTIA Security+ Study with Professor Messer (Free)](https://www.professormesser.com/security-plus/sy0-701/sy0-701-training-course/) — The best free Security+ prep course available. Watch every video, take every practice test, then sit the exam.

- [CompTIA Certification Roadmap](https://www.comptia.org/certifications/which-certification)
- [SANS Certification Roadmap](https://www.sans.org/cyber-security-skills-roadmap/)
- [EC-Council Certifications](https://www.eccouncil.org/programs/)

**📚 Books:**
- "CISSP All-in-One Exam Guide" by Shon Harris and Fernando Maymi
- "CompTIA Security+ Get Certified Get Ahead" by Darril Gibson
- "OSCP Preparation Guide" by TJ_Null

**📌 Resources:**
- [Certification Comparison](https://pauljerimy.com/security-certification-roadmap/)
- [Cybersecurity Certification Guide](https://www.cybersecurityeducation.org/certifications/)
- [Reddit r/cybersecurity Certification Guides](https://www.reddit.com/r/cybersecurity/wiki/index/#wiki_certification_questions)

**🏋️ Practical Exercises:**
- Create a personalized certification roadmap
- Build a study plan for your target certification
- Join study groups and practice exams
- Create practical labs to reinforce certification material

---

#### Building a Professional Network 🟡 Recommended

**⭐ START HERE (Free):** [LinkedIn + Twitter/X Security Community](https://twitter.com/search?q=%23cybersecurity)
> Follow 20 security professionals on Twitter/X and LinkedIn today. Engage with their posts. This is completely free and the fastest way to build a professional network in security. Accounts to start with: @GossiTheDog, @SwiftOnSecurity, @SarahJayneTerp, @johndmaher.

- [Cybersecurity Communities](https://github.com/sbilly/awesome-security#other-awesome-lists-and-repositories)
- [Security Conferences](https://infosec-conferences.com/)
- [OWASP Chapters](https://owasp.org/chapters/) *(Free to attend local chapter meetings)*
- [Cybersecurity Meetups](https://www.meetup.com/topics/cybersecurity/)
- [Women in Cybersecurity (WiCyS)](https://www.wicys.org/)

**📌 Resources:**
- [Building Your Cybersecurity Network](https://cybersecurityguide.org/resources/career-networking-guide/)

**🏋️ Practical Exercises:**
- Join cybersecurity communities and forums
- Attend local meetups and conferences
- Contribute to open-source security projects
- Participate in online discussions and forums
- Create and share cybersecurity content

---

#### Continuous Learning 🟡 Recommended

**⭐ START HERE (Free):** [SANS Internet Stormcast Daily Podcast (Free)](https://isc.sans.edu/podcast.html)
> A free, 5-minute daily podcast covering the latest security news and threats. Listen every morning. After 30 days you'll have a solid grasp of the current threat landscape without spending a minute of extra study time.

- [Cybersecurity Podcasts](https://nordlayer.com/blog/cybersecurity-podcasts-to-check-out/)
- [Security Research Blogs](https://www.akamai.com/blog/security-research)
- [Academic Journals](https://www.scimagojr.com/journalrank.php?category=1712)
- [Security Newsletters](https://www.sans.org/newsletters/) *(Free)*
- [GitHub Security Repositories](https://github.com/topics/security)

**Top Free Security Newsletters to Subscribe to:**
- [SANS NewsBites](https://www.sans.org/newsletters/newsbites/) *(Free)*
- [Krebs on Security](https://krebsonsecurity.com/) *(Free blog)*
- [tl;dr sec](https://tldrsec.com/) *(Free weekly newsletter)*
- [This Week in Security](https://this.weekinsecurity.com/) *(Free)*

**📌 Resources:**
- [Awesome Hacking Resources](https://github.com/vitalysim/Awesome-Hacking-Resources)
- [Cybersecurity Canon](https://icdt.osu.edu/cybercanon/bookreviews)
- [Cybersecurity Learning Paths](https://tryhackme.com/paths)

**🏋️ Practical Exercises:**
- Subscribe to security newsletters and podcasts
- Follow security researchers on social media
- Set up a personal blog to document your learning
- Participate in bug bounty programs
- Contribute to security tools and research

---

## Learning Resources

### Books

- **Beginner**
  - "Cybersecurity for Beginners" by Raef Meeuwisse
  - "The Art of Invisibility" by Kevin Mitnick
  - "Social Engineering: The Science of Human Hacking" by Christopher Hadnagy
  - "Practical Malware Analysis" by Michael Sikorski and Andrew Honig
  - "Cryptography for Dummies" by Chey Cobb
  - "Computer Security: Principles and Practice" by William Stallings and Lawrie Brown
  - "Network Security Essentials" by William Stallings

- **Intermediate**
  - "The Web Application Hacker's Handbook" by Dafydd Stuttard and Marcus Pinto
  - "Blue Team Handbook" by Don Murdoch
  - "Penetration Testing: A Hands-On Introduction to Hacking" by Georgia Weidman
  - "The Tangled Web: A Guide to Securing Modern Web Applications" by Michal Zalewski
  - "Threat Modeling: Designing for Security" by Adam Shostack
  - "Reversing: Secrets of Reverse Engineering" by Eldad Eilam
  - "The Hacker Playbook 3" by Peter Kim

- **Advanced**
  - "The Art of Memory Forensics" by Michael Hale Ligh et al.
  - "Gray Hat Hacking: The Ethical Hacker's Handbook" by Allen Harper et al.
  - "The Shellcoder's Handbook" by Chris Anley et al.
  - "Practical Reverse Engineering" by Bruce Dang et al.
  - "Advanced Penetration Testing" by Wil Allsopp
  - "Black Hat Python" by Justin Seitz
  - "Windows Internals" by Mark Russinovich et al.

- **Specialized**
  - "Cloud Security: A Comprehensive Guide" by Chris Dotson
  - "Industrial Network Security" by Eric D. Knapp and Joel Thomas Langill
  - "iOS Application Security" by David Thiel
  - "Android Security Internals" by Nikolay Elenkov
  - "Container Security" by Liz Rice
  - "Applied Cryptography" by Bruce Schneier
  - "Intelligence-Driven Incident Response" by Scott J. Roberts and Rebekah Brown

### Online Platforms

- **Learning Platforms**
  - [TryHackMe](https://tryhackme.com/) - Interactive cybersecurity training *(Free tier available — best for beginners)*
  - [HackTheBox](https://www.hackthebox.eu/) - Penetration testing labs *(Free tier available)*
  - [HackTheBox Academy](https://academy.hackthebox.com/) - Structured learning paths *(Free modules + paid)*
  - [TCM Security Academy](https://academy.tcm-sec.com/) - Affordable, practical pentesting courses by industry pros *(Best value paid courses — Practical Ethical Hacking is the flagship)*
  - [VulnHub](https://www.vulnhub.com/) - Vulnerable virtual machines *(All free)*
  - [PortSwigger Web Security Academy](https://portswigger.net/web-security) - Web security training *(All free)*
  - [Cybrary](https://www.cybrary.it/) - Free cybersecurity courses
  - [edX Cybersecurity Courses](https://www.edx.org/learn/cybersecurity) - University-level courses
  - [Coursera Cybersecurity Specializations](https://www.coursera.org/browse/information-technology/security) - University-level courses *(Audit free)*
  - [SANS Cyber Aces](https://www.cyberaces.org/) - Free online courses
  - [Offensive Security](https://www.offensive-security.com/) - Professional penetration testing training
  - [INE Security](https://security.ine.com/) - Cybersecurity training *(Free Starter Pass available)*
  - [PentesterLab](https://pentesterlab.com/) - Web penetration testing exercises
  - [RangeForce](https://www.rangeforce.com/) - Hands-on cybersecurity training
  - [Pluralsight](https://www.pluralsight.com/browse/information-cyber-security) - IT and security courses
  - [Udemy](https://www.udemy.com/courses/it-and-software/network-and-security/) - Various security courses

- **Practice Environments**
  - [Damn Vulnerable Web Application (DVWA)](https://github.com/digininja/DVWA) - Vulnerable web application *(Free)*
  - [OWASP Juice Shop](https://owasp.org/www-project-juice-shop/) - Vulnerable web application *(Free)*
  - [WebGoat](https://owasp.org/www-project-webgoat/) - Deliberately insecure web application *(Free)*
  - [Metasploitable](https://sourceforge.net/projects/metasploitable/) - Vulnerable Linux virtual machine *(Free)*
  - [Vulnhub](https://www.vulnhub.com/) - Vulnerable virtual machines *(All free)*
  - [Hack The Box](https://www.hackthebox.eu/) - Online penetration testing platform
  - [PentesterLab](https://pentesterlab.com/) - Web penetration testing exercises
  - [Root Me](https://www.root-me.org/) - Hacking challenges
  - [Hacker101 CTF](https://ctf.hacker101.com/) - CTF challenges by HackerOne *(Free)*
  - [CryptoHack](https://cryptohack.org/) - Cryptography challenges *(Free)*
  - [OverTheWire](https://overthewire.org/wargames/) - Security wargames *(All free)*

### YouTube Channels

> ✅ All links verified and corrected below:

- [John Hammond](https://www.youtube.com/@_JohnHammond) - CTF walkthroughs and security tutorials
- [IppSec](https://www.youtube.com/@ippsec) - HackTheBox walkthroughs
- [The Cyber Mentor (TCM Security)](https://www.youtube.com/@TCMSecurityAcademy) - Penetration testing tutorials
- [David Bombal](https://www.youtube.com/@davidbombal) - Networking and security tutorials
- [NetworkChuck](https://www.youtube.com/@NetworkChuck) - Networking and security tutorials
- [Nahamsec](https://www.youtube.com/@NahamSec) - Bug bounty and web security
- [LiveOverflow](https://www.youtube.com/@LiveOverflow) - Exploit development and CTF
- [STÖK](https://www.youtube.com/@STOKfredrik) - Bug bounty hunting
- [HackerSploit](https://www.youtube.com/@HackerSploit) - Penetration testing tutorials
- [PwnFunction](https://www.youtube.com/@PwnFunction) - Web security animations *(excellent for visual learners)*
- [InsiderPhD](https://www.youtube.com/@InsiderPhD) - Bug bounty and web security
- [Security Weekly](https://www.youtube.com/@SecurityWeekly) - Security news and interviews
- [Black Hat](https://www.youtube.com/@BlackHatOfficialYT) - Conference presentations
- [DEFCONConference](https://www.youtube.com/@DEFCONConference) - Conference presentations
- [SANS Offensive Operations](https://www.youtube.com/@SANSOffensiveOperations) - Offensive security techniques
- [Gerald Auger (Simply Cyber)](https://www.youtube.com/@SimplyCyber) - Career advice and blue team
- [John Strand (Black Hills InfoSec)](https://www.youtube.com/@BlackHillsInformationSecurity) - Free security training webcasts

---

## Cybersecurity Tools

### Reconnaissance & Information Gathering

- [Nmap](https://nmap.org/) - Network discovery and security auditing
- [Shodan](https://www.shodan.io/) - Search engine for Internet-connected devices
- [Recon-ng](https://github.com/lanmaster53/recon-ng) - Web reconnaissance framework
- [theHarvester](https://github.com/laramies/theHarvester) - Email, subdomain and name harvester
- [Maltego](https://www.maltego.com/) - Open source intelligence and forensics
- [SpiderFoot](https://github.com/smicallef/spiderfoot) - OSINT automation tool
- [Amass](https://github.com/OWASP/Amass) - In-depth attack surface mapping and asset discovery
- [Sublist3r](https://github.com/aboul3la/Sublist3r) - Subdomain enumeration tool
- [OWASP Maryam](https://github.com/saeeddhqan/Maryam) - Open-source intelligence framework

### Vulnerability Assessment

- [OpenVAS](https://www.openvas.org/) - Open-source vulnerability scanner
- [Nessus](https://www.tenable.com/products/nessus) - Vulnerability scanner
- [Nikto](https://cirt.net/Nikto2) - Web server scanner
- [Qualys](https://www.qualys.com/) - Cloud-based security and compliance
- [Nexpose](https://www.rapid7.com/products/nexpose/) - Vulnerability management
- [Acunetix](https://www.acunetix.com/) - Web vulnerability scanner
- [Netsparker](https://www.netsparker.com/) - Web application security scanner
- [Nuclei](https://github.com/projectdiscovery/nuclei) - Vulnerability scanner based on templates
- [Vulners Scanner](https://github.com/vulnersCom/nmap-vulners) - NSE script using Vulners.com API

### Web Application Security

- [Burp Suite](https://portswigger.net/burp) - Web vulnerability scanner and proxy
- [OWASP ZAP](https://www.zaproxy.org/) - Web application security scanner
- [Sqlmap](https://sqlmap.org/) - Automatic SQL injection tool
- [Wfuzz](https://github.com/xmendez/wfuzz) - Web application fuzzer
- [Dirsearch](https://github.com/maurosoria/dirsearch) - Web path scanner
- [Nikto](https://cirt.net/Nikto2) - Web server scanner
- [Skipfish](https://github.com/spinkham/skipfish) - Active web application security reconnaissance tool
- [w3af](https://github.com/andresriancho/w3af) - Web Application Attack and Audit Framework
- [Arachni](https://www.arachni-scanner.com/) - Web application security scanner framework

### Exploitation

- [Metasploit](https://www.metasploit.com/) - Penetration testing framework
- [BeEF](https://beefproject.com/) - Browser Exploitation Framework
- [Empire](https://github.com/BC-SECURITY/Empire) - Post-exploitation framework
- [Cobalt Strike](https://www.cobaltstrike.com/) - Adversary simulation software
- [PowerSploit](https://github.com/PowerShellMafia/PowerSploit) - PowerShell post-exploitation framework
- [Pupy](https://github.com/n1nj4sec/pupy) - Cross-platform remote administration and post-exploitation tool
- [Covenant](https://github.com/cobbr/Covenant) - .NET command and control framework
- [Sliver](https://github.com/BishopFox/sliver) - Cross-platform adversary emulation framework

### Password Attacks

- [Hashcat](https://hashcat.net/hashcat/) - Advanced password recovery
- [John the Ripper](https://www.openwall.com/john/) - Password cracking tool
- [Hydra](https://github.com/vanhauser-thc/thc-hydra) - Login cracker
- [Aircrack-ng](https://www.aircrack-ng.org/) - WiFi security auditing tools suite
- [Medusa](https://github.com/jmk-foofus/medusa) - Parallel network login auditor
- [CrackMapExec](https://github.com/byt3bl33d3r/CrackMapExec) - Post-exploitation tool
- [mimikatz](https://github.com/gentilkiwi/mimikatz) - Windows credential dumping
- [RainbowCrack](http://project-rainbowcrack.com/) - Rainbow table implementation
- [Passlord](https://github.com/navnee1h/passlord/) - Profile-based wordlist generator

### Forensics & Incident Response

- [Autopsy](https://www.autopsy.com/) - Digital forensics platform
- [Volatility](https://www.volatilityfoundation.org/) - Memory forensics framework
- [FTK Imager](https://accessdata.com/product-download/ftk-imager-version-4-5) - Forensic imaging tool
- [The Sleuth Kit](https://www.sleuthkit.org/) - Disk analysis tools
- [SANS SIFT](https://digital-forensics.sans.org/community/downloads) - Forensic toolkit
- [Rekall](https://github.com/google/rekall) - Memory analysis framework
- [CAINE](https://www.caine-live.net/) - Computer Aided INvestigative Environment
- [GRR Rapid Response](https://github.com/google/grr) - Remote live forensics
- [TheHive](https://thehive-project.org/) - Security incident response platform

### Defensive Tools

- [Wireshark](https://www.wireshark.org/) - Network protocol analyzer
- [Snort](https://www.snort.org/) - Intrusion detection system
- [OSSEC](https://www.ossec.net/) - Host-based intrusion detection
- [Wazuh](https://wazuh.com/) - Security monitoring solution
- [Security Onion](https://securityonionsolutions.com/) - Security monitoring platform
- [Suricata](https://suricata.io/) - Network IDS/IPS
- [Zeek](https://zeek.org/) - Network security monitor
- [Sysmon](https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon) - Windows system monitoring
- [YARA](https://virustotal.github.io/yara/) - Pattern matching for malware detection

### Cloud Security

- [ScoutSuite](https://github.com/nccgroup/ScoutSuite) - Multi-cloud security auditing tool
- [Prowler](https://github.com/toniblyx/prowler) - AWS security best practices assessment
- [CloudSploit](https://cloudsploit.com/) - Cloud security scanner
- [Pacu](https://github.com/RhinoSecurityLabs/pacu) - AWS exploitation framework
- [CloudGoat](https://github.com/RhinoSecurityLabs/cloudgoat) - Vulnerable AWS environment
- [AzureHound](https://github.com/BloodHoundAD/AzureHound) - Azure security assessment
- [GCP Audit](https://github.com/google/gcp_scanner) - GCP security scanner
- [Falco](https://falco.org/) - Container runtime security
- [Kube-bench](https://github.com/aquasecurity/kube-bench) - Kubernetes security benchmarking

### Mobile Security

- [MobSF](https://github.com/MobSF/Mobile-Security-Framework-MobSF) - Mobile security testing framework
- [Frida](https://frida.re/) - Dynamic instrumentation toolkit
- [Objection](https://github.com/sensepost/objection) - Mobile runtime exploration
- [Drozer](https://github.com/FSecureLABS/drozer) - Android security assessment
- [QARK](https://github.com/linkedin/qark) - Android app vulnerability scanner
- [idb](https://github.com/dmayer/idb) - iOS app security assessment tool
- [Needle](https://github.com/FSecureLABS/needle) - iOS security testing framework
- [Apktool](https://apktool.org/) - Android APK reverse engineering
- [Jadx](https://github.com/skylot/jadx) - Dex to Java decompiler

### OSINT Tools

- [Maltego](https://www.maltego.com/) - Open source intelligence and forensics
- [Shodan](https://www.shodan.io/) - Search engine for Internet-connected devices
- [theHarvester](https://github.com/laramies/theHarvester) - Email, subdomain and name harvester
- [Metagoofil](https://github.com/laramies/metagoofil) - Metadata extraction tool
- [Recon-ng](https://github.com/lanmaster53/recon-ng) - Web reconnaissance framework
- [SpiderFoot](https://www.spiderfoot.net/) - OSINT automation tool
- [OSINT Framework](https://osintframework.com/) - Collection of OSINT tools
- [Sherlock](https://github.com/sherlock-project/sherlock) - Hunt down social media accounts by username
- [IntelTechniques](https://inteltechniques.com/tools/) - OSINT tools collection

---

## Certifications Guide

### Entry-Level Certifications

- **[CompTIA Security+](https://www.comptia.org/certifications/security)** - Foundational cybersecurity certification
  - **Focus Areas**: Network security, threats and vulnerabilities, identity management, cryptography
  - **Prerequisites**: None, but Network+ and 2 years of experience recommended
  - **Exam Format**: 90 questions, 90 minutes, performance-based and multiple choice
  - **Validity**: 3 years, renewable with continuing education
  - **Career Paths**: Security specialist, security administrator, security consultant
  - **⭐ Best Free Prep**: [Professor Messer Security+ Course](https://www.professormesser.com/security-plus/sy0-701/sy0-701-training-course/)

- **[CompTIA Network+](https://www.comptia.org/certifications/network)** - Networking fundamentals
  - **Focus Areas**: Network concepts, infrastructure, operations, security, troubleshooting
  - **Prerequisites**: None, but A+ and 9-12 months of experience recommended
  - **Exam Format**: 90 questions, 90 minutes, performance-based and multiple choice
  - **Validity**: 3 years, renewable with continuing education
  - **Career Paths**: Network administrator, network technician, help desk technician
  - **⭐ Best Free Prep**: [Professor Messer Network+ Course](https://www.professormesser.com/network-plus/n10-008/n10-008-training-course/)

- **[CompTIA A+](https://www.comptia.org/certifications/a)** - IT fundamentals
  - **Focus Areas**: Hardware, operating systems, software troubleshooting, networking, security
  - **Prerequisites**: None, but 9-12 months of experience recommended
  - **Exam Format**: Two exams: Core 1 and Core 2, 90 minutes each
  - **Validity**: 3 years, renewable with continuing education
  - **Career Paths**: Help desk technician, desktop support analyst, field service technician

- **[Certified Information Systems Security Professional (CISSP) Associate](https://www.isc2.org/Certifications/CISSP)** - Entry-level version of CISSP
  - **Focus Areas**: Same as CISSP but for those without the required experience
  - **Prerequisites**: Pass the CISSP exam but have less than 5 years of experience
  - **Exam Format**: Same as CISSP
  - **Validity**: Indefinite until requirements for full CISSP are met
  - **Career Paths**: Stepping stone to security analyst, security consultant roles

### Intermediate Certifications

- **[CompTIA CySA+](https://www.comptia.org/certifications/cybersecurity-analyst)** - Cybersecurity analyst
  - **Focus Areas**: Threat detection, security monitoring, incident response, vulnerability management
  - **Prerequisites**: Network+ and Security+ recommended, 4+ years of experience
  - **Exam Format**: 85 questions, 165 minutes, performance-based and multiple choice
  - **Validity**: 3 years, renewable with continuing education
  - **Career Paths**: Security analyst, threat intelligence analyst, SOC analyst

- **[CompTIA PenTest+](https://www.comptia.org/certifications/pentest)** - Penetration testing
  - **Focus Areas**: Planning and scoping, information gathering, vulnerability identification, attacks and exploits, reporting
  - **Prerequisites**: Network+ and Security+ recommended, 3+ years of experience
  - **Exam Format**: 85 questions, 165 minutes, performance-based and multiple choice
  - **Validity**: 3 years, renewable with continuing education
  - **Career Paths**: Penetration tester, vulnerability assessment analyst, security consultant

- **[Certified Ethical Hacker (CEH)](https://www.eccouncil.org/programs/certified-ethical-hacker-ceh/)** - Ethical hacking and countermeasures
  - **Focus Areas**: Ethical hacking methodology, tools, techniques, countermeasures
  - **Prerequisites**: 2 years of experience or official training
  - **Exam Format**: 125 questions, 4 hours, multiple choice
  - **Validity**: 3 years, renewable with continuing education
  - **Career Paths**: Ethical hacker, security analyst, penetration tester

- **[GIAC Security Essentials (GSEC)](https://www.giac.org/certification/security-essentials-gsec)** - Security essentials
  - **Focus Areas**: Security administration, risk management, cryptography, access controls
  - **Prerequisites**: None
  - **Exam Format**: 180 questions, 5 hours, multiple choice and performance-based
  - **Validity**: 4 years, renewable with continuing education
  - **Career Paths**: Security administrator, security analyst, security engineer

### Advanced Certifications

- **[Offensive Security Certified Professional (OSCP)](https://www.offensive-security.com/pwk-oscp/)** - Penetration testing with Kali Linux
  - **Focus Areas**: Hands-on penetration testing, exploitation, privilege escalation
  - **Prerequisites**: Strong understanding of networking, Linux, and scripting
  - **Exam Format**: 24-hour practical exam with report submission
  - **Validity**: Lifetime
  - **Career Paths**: Penetration tester, red team operator, security consultant
  - **⭐ Best Free Prep**: [TJ_Null's OSCP Prep List](https://docs.google.com/spreadsheets/d/1dwSMIAPIam0PuRBkCiDI88pU3yzrqqHkDtBngUHNCw8/edit#gid=0)

- **[HTB CPTS — Certified Penetration Testing Specialist](https://academy.hackthebox.com/preview/certifications/htb-certified-penetration-testing-specialist/)** - Practical penetration testing by HackTheBox
  - **Focus Areas**: Full penetration test lifecycle, Active Directory attacks, web app testing, reporting
  - **Prerequisites**: Completion of HTB Academy Penetration Tester job-role path
  - **Exam Format**: Realistic 10-day engagement against a corporate lab environment with full report submission
  - **Validity**: Lifetime
  - **Career Paths**: Penetration tester, red team operator, security consultant
  - **Why consider it**: More affordable than OSCP, equally rigorous hands-on exam, covers modern AD attack chains in more depth. Strong alternative or complement to OSCP.
  - **⭐ Best Prep**: [HTB Academy Penetration Tester Path](https://academy.hackthebox.com/path/preview/penetration-tester)

- **[Certified Information Systems Security Professional (CISSP)](https://www.isc2.org/Certifications/CISSP)** - Security management
  - **Focus Areas**: Security and risk management, asset security, security architecture, network security, identity management, security assessment, security operations, software development security
  - **Prerequisites**: 5 years of experience in at least 2 domains
  - **Exam Format**: 100-150 questions, 3 hours, adaptive testing
  - **Validity**: 3 years, renewable with continuing education
  - **Career Paths**: Security manager, security architect, CISO, security consultant

- **[Certified Information Security Manager (CISM)](https://www.isaca.org/credentialing/cism)** - Information security management
  - **Focus Areas**: Information security governance, risk management, program development, incident management
  - **Prerequisites**: 5 years of experience in information security management
  - **Exam Format**: 150 questions, 4 hours, multiple choice
  - **Validity**: 3 years, renewable with continuing education
  - **Career Paths**: Security manager, security director, CISO

- **[GIAC Certified Incident Handler (GCIH)](https://www.giac.org/certification/certified-incident-handler-gcih)** - Incident handling
  - **Focus Areas**: Incident handling process, computer crime investigation, hacker techniques
  - **Prerequisites**: None
  - **Exam Format**: 115 questions, 3 hours, multiple choice
  - **Validity**: 4 years, renewable with continuing education
  - **Career Paths**: Incident responder, SOC analyst, security analyst

### Specialized Certifications

- **[Certified Cloud Security Professional (CCSP)](https://www.isc2.org/Certifications/CCSP)** - Cloud security
  - **Focus Areas**: Cloud concepts, architecture, design, security, operations, legal compliance
  - **Prerequisites**: 5 years of IT experience, 3 years in security, 1 year in cloud security
  - **Exam Format**: 125 questions, 3 hours, multiple choice
  - **Validity**: 3 years, renewable with continuing education
  - **Career Paths**: Cloud security architect, cloud security engineer, cloud security manager

- **[GIAC Certified Forensic Analyst (GCFA)](https://www.giac.org/certification/certified-forensic-analyst-gcfa)** - Digital forensics
  - **Focus Areas**: Digital forensics techniques, incident response, malware analysis
  - **Prerequisites**: None
  - **Exam Format**: 115 questions, 3 hours, multiple choice
  - **Validity**: 4 years, renewable with continuing education
  - **Career Paths**: Digital forensic analyst, incident responder, malware analyst

- **[Offensive Security Certified Expert (OSCE)](https://www.offensive-security.com/ctp-osce/)** - Advanced penetration testing
  - **Focus Areas**: Advanced exploitation techniques, custom exploit development
  - **Prerequisites**: OSCP recommended
  - **Exam Format**: 48-hour practical exam with report submission
  - **Validity**: Lifetime
  - **Career Paths**: Advanced penetration tester, exploit developer, security researcher

- **[Certified Information Systems Auditor (CISA)](https://www.isaca.org/credentialing/cisa)** - Information systems auditing
  - **Focus Areas**: IS audit process, governance, systems acquisition, operations, protection of assets
  - **Prerequisites**: 5 years of experience in IS audit, control, or security
  - **Exam Format**: 150 questions, 4 hours, multiple choice
  - **Validity**: 3 years, renewable with continuing education
  - **Career Paths**: IS auditor, IT audit manager, compliance officer

---

## Career Paths

### Offensive Roles

- **Penetration Tester**
  - **Responsibilities**: Test systems for vulnerabilities through simulated attacks, document findings, recommend remediation
  - **Skills Required**: Ethical hacking, exploitation, scripting, report writing
  - **Certifications**: PNPT, OSCP, CEH, PenTest+
  - **Career Progression**: Senior Penetration Tester → Red Team Lead → Security Consultant

- **Red Team Operator**
  - **Responsibilities**: Simulate advanced adversaries to test defenses, develop custom tools, conduct long-term engagements
  - **Skills Required**: Advanced exploitation, social engineering, evasion techniques, C2 frameworks, Active Directory attacks, custom tool development
  - **Certifications**: OSCP → CRTO (Certified Red Team Operator by Zero-Point Security) → CRTE → OSED/OSEP
  - **Recommended Training**: [TCM Security — Red Team Operations](https://academy.tcm-sec.com/) | [Zero-Point Security Red Team Ops course](https://training.zeropointsecurity.co.uk/courses/red-team-ops)
  - **Career Progression**: Senior Red Team Operator → Red Team Lead → Director of Offensive Security
  - **Key distinction from Pentesting**: Pentesters find and report vulnerabilities. Red teamers run realistic, long-duration adversary simulations designed to test the *entire* security program — people, process, and technology.

- **Vulnerability Researcher**
  - **Responsibilities**: Discover and analyze new vulnerabilities, develop proof-of-concept exploits, research security weaknesses
  - **Skills Required**: Reverse engineering, exploit development, programming, vulnerability analysis
  - **Certifications**: OSCE, GXPN, OSEE
  - **Career Progression**: Senior Vulnerability Researcher → Security Research Lead → Security Director

- **Exploit Developer**
  - **Responsibilities**: Develop exploits for vulnerabilities, create custom attack tools, research exploitation techniques
  - **Skills Required**: Advanced programming, reverse engineering, exploit development, assembly language
  - **Certifications**: OSCE, OSEE, GXPN
  - **Career Progression**: Senior Exploit Developer → Research Lead → Security Director

### Management Roles

- **Chief Information Security Officer (CISO)**
  - **Responsibilities**: Executive responsible for an organization's security strategy, policies, and programs
  - **Skills Required**: Leadership, risk management, security governance, business acumen, communication
  - **Certifications**: CISSP, CISM, CGEIT
  - **Career Progression**: Terminal position, may move to larger organizations or consulting

- **Security Manager**
  - **Responsibilities**: Manage security teams and operations, implement security policies, oversee security projects
  - **Skills Required**: Team management, security operations, project management, risk assessment
  - **Certifications**: CISSP, CISM, PMP
  - **Career Progression**: Security Director → CISO

- **Security Consultant**
  - **Responsibilities**: Advise organizations on security matters, conduct assessments, develop security strategies
  - **Skills Required**: Security assessment, consulting, communication, technical expertise
  - **Certifications**: CISSP, CISA, CISM
  - **Career Progression**: Senior Consultant → Principal Consultant → Practice Lead

- **GRC (Governance, Risk, Compliance) Specialist**
  - **Responsibilities**: Ensure compliance with regulations and standards, conduct risk assessments, develop security policies
  - **Skills Required**: Compliance frameworks, risk assessment, policy development, auditing
  - **Certifications**: CISA, CRISC, CISM
  - **Career Progression**: GRC Manager → Director of Compliance → CISO

### Specialized Roles

- **Digital Forensic Analyst**
  - **Responsibilities**: Investigate digital evidence, recover and analyze data, document findings for legal proceedings
  - **Skills Required**: Digital forensics tools, evidence handling, chain of custody, legal knowledge
  - **Certifications**: GCFA, EnCE, CCFE
  - **Career Progression**: Senior Forensic Analyst → Forensic Manager → Director of Forensics

- **Malware Analyst**
  - **Responsibilities**: Analyze malicious software, reverse engineer malware, develop detection methods
  - **Skills Required**: Reverse engineering, programming, malware analysis tools, sandboxing
  - **Certifications**: GREM, GXPN, GCIH
  - **Career Progression**: Senior Malware Analyst → Threat Research Lead → Security Director

- **Cloud Security Specialist**
  - **Responsibilities**: Secure cloud environments, implement cloud security controls, assess cloud security
  - **Skills Required**: Cloud platforms (AWS, Azure, GCP), cloud security tools, DevSecOps
  - **Certifications**: CCSP, AWS Certified Security, Azure Security Engineer
  - **Career Progression**: Senior Cloud Security Specialist → Cloud Security Architect → CISO

- **Application Security Engineer**
  - **Responsibilities**: Secure software applications, conduct code reviews, implement secure coding practices
  - **Skills Required**: Secure coding, application security testing, programming, SDLC
  - **Certifications**: CSSLP, GWAPT, OSWE
  - **Career Progression**: Senior AppSec Engineer → AppSec Architect → Director of Application Security

---

## Cybersecurity Communities

### Online Communities

- [Reddit r/cybersecurity](https://www.reddit.com/r/cybersecurity/) - General cybersecurity discussions
- [Reddit r/netsec](https://www.reddit.com/r/netsec/) - Network security news and discussions
- [Reddit r/AskNetsec](https://www.reddit.com/r/AskNetsec/) - Questions about network security
- [Stack Exchange Information Security](https://security.stackexchange.com/) - Q&A for information security professionals
- [OWASP Community](https://owasp.org/www-community/) - Web application security community
- [Hack The Box Forum](https://forum.hackthebox.eu/) - Penetration testing and CTF discussions
- [TryHackMe Discord](https://discord.gg/tryhackme) - Community for TryHackMe platform users
- [NetSec Focus](https://www.netsecfocus.com/) - Information security community
- [Bleeping Computer Forums](https://www.bleepingcomputer.com/forums/) - Computer security forums

### Professional Organizations

- [ISACA](https://www.isaca.org/) - Information Systems Audit and Control Association
- [(ISC)²](https://www.isc2.org/) - International Information System Security Certification Consortium
- [ISSA](https://www.issa.org/) - Information Systems Security Association
- [SANS](https://www.sans.org/) - SysAdmin, Audit, Network, and Security Institute
- [EC-Council](https://www.eccouncil.org/) - International Council of E-Commerce Consultants
- [CompTIA](https://www.comptia.org/) - Computing Technology Industry Association
- [CSA](https://cloudsecurityalliance.org/) - Cloud Security Alliance
- [FIRST](https://www.first.org/) - Forum of Incident Response and Security Teams

### Conferences

- [DEF CON](https://www.defcon.org/) - One of the world's largest hacker conventions
- [Black Hat](https://www.blackhat.com/) - Information security conference
- [RSA Conference](https://www.rsaconference.com/) - Cybersecurity conference
- [BSides](http://www.securitybsides.com/) - Community-driven framework for information security events *(Low cost, community-run)*
- [SANS Summits](https://www.sans.org/cyber-security-summit/) - Cybersecurity summits
- [Infosecurity Europe](https://www.infosecurityeurope.com/) - Europe's information security event
- [CyberSecurity Summit](https://cybersecuritysummit.com/) - Cybersecurity leadership summit
- [Women in Cybersecurity Conference](https://www.wicys.org/events/wicys-conference/) - Conference for women in cybersecurity
- [CISO Forum](https://cisoforum.com/) - Chief Information Security Officer forum

---

## Capture The Flag (CTF) Competitions

### Beginner-Friendly CTFs

> **⭐ Where to start:** [PicoCTF](https://picoctf.org/) — Completely free, no account required to browse. Made by Carnegie Mellon for students. Best first CTF by a wide margin.

- [PicoCTF](https://picoctf.org/) - Free, educational CTF for beginners *(Start here)*
- [CTFlearn](https://ctflearn.com/) - Online platform with various CTF challenges
- [Hacker101 CTF](https://ctf.hacker101.com/) - CTF by HackerOne for learning web security
- [CyberDefenders](https://cyberdefenders.org/) - Blue team CTF challenges
- [SANS Holiday Hack Challenge](https://holidayhackchallenge.com/) - Annual holiday-themed CTF
- [Google CTF Beginners Quest](https://capturetheflag.withgoogle.com/) - Beginner-friendly CTF by Google
- [TryHackMe](https://tryhackme.com/) - Learn cybersecurity through CTF-like challenges
- [OverTheWire](https://overthewire.org/wargames/) - Wargames for learning security concepts

### Advanced CTFs

- [DEF CON CTF](https://www.defcon.org/html/links/dc-ctf.html) - One of the oldest and most prestigious CTFs
- [CSAW CTF](https://www.csaw.io/ctf) - CTF competition by NYU Tandon School of Engineering
- [PlaidCTF](https://plaidctf.com/) - Annual CTF by Plaid Parliament of Pwning
- [HITCON CTF](https://ctf.hitcon.org/) - Hacks In Taiwan Conference CTF
- [Dragon CTF](https://dragonsector.pl/) - CTF by Dragon Sector team
- [RuCTF](https://ructf.org/) - Russian CTF
- [0CTF/TCTF](https://ctf.0ops.sjtu.cn/) - International CTF competition
- [Hack.lu CTF](https://hack.lu/) - CTF during the Hack.lu conference

### CTF Resources

- [CTFtime](https://ctftime.org/) - CTF events calendar and team rankings
- [CTF Field Guide](https://trailofbits.github.io/ctf/) - Guide to CTF competitions
- [LiveOverflow YouTube Channel](https://www.youtube.com/@LiveOverflow) - CTF walkthroughs and explanations
- [John Hammond YouTube Channel](https://www.youtube.com/@_JohnHammond) - CTF walkthroughs
- [IppSec YouTube Channel](https://www.youtube.com/@ippsec) - HackTheBox walkthroughs
- [CTF Resources](https://github.com/ctfs/resources) - Collection of CTF resources
- [Awesome CTF](https://github.com/apsdehal/awesome-ctf) - List of CTF frameworks, libraries, resources
- [CTF Tools](https://github.com/zardus/ctf-tools) - Collection of tools for CTF competitions

---

## Cybersecurity Labs and Practice Environments

### Online Practice Environments

- [Hack The Box](https://www.hackthebox.eu/) - Online platform for penetration testing practice
- [TryHackMe](https://tryhackme.com/) - Learn cybersecurity through hands-on exercises *(Free tier — best for beginners)*
- [VulnHub](https://www.vulnhub.com/) - Vulnerable virtual machines for practice *(All free)*
- [PortSwigger Web Security Academy](https://portswigger.net/web-security) - Web security training *(All free)*
- [PentesterLab](https://pentesterlab.com/) - Web penetration testing exercises
- [Root Me](https://www.root-me.org/) - Hacking challenges platform
- [HackThis](https://www.hackthis.co.uk/) - Hacking challenges and tutorials
- [Damn Vulnerable Web Application (DVWA)](https://github.com/digininja/DVWA) - Vulnerable web application *(Free)*
- [OWASP Juice Shop](https://owasp.org/www-project-juice-shop/) - Vulnerable web application *(Free)*

### Building Your Own Lab

- **Virtualization Platforms**
  - [VirtualBox](https://www.virtualbox.org/) - Free virtualization software *(Best free option)*
  - [VMware Workstation/Player](https://www.vmware.com/) - Virtualization software *(Player is free)*
  - [Proxmox VE](https://www.proxmox.com/en/) - Open-source virtualization platform
  - [Hyper-V](https://docs.microsoft.com/en-us/virtualization/hyper-v-on-windows/) - Windows virtualization *(Free with Windows Pro)*

- **Vulnerable Systems**
  - [Metasploitable](https://sourceforge.net/projects/metasploitable/) - Vulnerable Linux virtual machine *(Free)*
  - [DVWA](https://github.com/digininja/DVWA) - Damn Vulnerable Web Application *(Free)*
  - [WebGoat](https://owasp.org/www-project-webgoat/) - Deliberately insecure web application *(Free)*
  - [OWASP Juice Shop](https://owasp.org/www-project-juice-shop/) - Vulnerable web application *(Free)*
  - [Vulnhub Images](https://www.vulnhub.com/) - Collection of vulnerable virtual machines *(All free)*

- **Attack Platforms**
  - [Kali Linux](https://www.kali.org/) - Penetration testing distribution *(Free)*
  - [Parrot Security OS](https://parrotsec.org/) - Security-focused Linux distribution *(Free)*
  - [BlackArch Linux](https://blackarch.org/) - Penetration testing distribution *(Free)*
  - [Commando VM](https://github.com/mandiant/commando-vm) - Windows-based penetration testing VM *(Free)*

- **Network Simulation**
  - [GNS3](https://www.gns3.com/) - Network simulation software *(Free)*
  - [Cisco Packet Tracer](https://www.netacad.com/courses/packet-tracer) - Network simulation tool *(Free with registration)*
  - [EVE-NG](https://www.eve-ng.net/) - Network emulation platform
  - [Netkit](http://wiki.netkit.org/) - Network emulation tool

### Lab Guides and Resources

- [Building a Home Lab for Offensive Security](https://www.offensive-security.com/offsec/tjnulls-home-lab-guide/)
- [Building a Cybersecurity Lab](https://www.cybersecuritydegrees.com/faq/how-to-set-up-a-cyber-security-lab/)
- [Home Lab Setup Guide](https://www.hackingloops.com/kali-linux-virtualbox-pentest-lab-setup/)
- [Network Security Lab Setup](https://www.hackingarticles.in/home-lab-setup/)
- [Building an Active Directory Lab](https://www.labeveryday.com/post/how-to-setup-active-directory-lab-in-windows-server)
- [Cybersecurity Home Lab on a Budget](https://systemoverlord.com/2017/10/24/building-a-home-lab-for-offensive-security-basics.html)

---

## Security Research Resources

### Vulnerability Databases

- [National Vulnerability Database (NVD)](https://nvd.nist.gov/) - U.S. government repository of vulnerability data
- [CVE Details](https://www.cvedetails.com/) - Security vulnerability database
- [Exploit Database](https://www.exploit-db.com/) - Archive of exploits and vulnerable software
- [Vulnerability Lab](https://www.vulnerability-lab.com/) - Vulnerability research and security database
- [Packet Storm](https://packetstormsecurity.com/) - Information security services, news, files, and tools
- [Vulners](https://vulners.com/) - Vulnerability database with API
- [VulDB](https://vuldb.com/) - Vulnerability database
- [Rapid7 Vulnerability & Exploit Database](https://www.rapid7.com/db/) - Vulnerability and exploit database

### Security Blogs and News

- [Krebs on Security](https://krebsonsecurity.com/) - Security news and investigation
- [Schneier on Security](https://www.schneier.com/) - Security blog by Bruce Schneier
- [The Hacker News](https://thehackernews.com/) - Cybersecurity news and analysis
- [Threatpost](https://threatpost.com/) - Information security news
- [Dark Reading](https://www.darkreading.com/) - Cybersecurity news and analysis
- [Naked Security](https://nakedsecurity.sophos.com/) - Security news from Sophos
- [BleepingComputer](https://www.bleepingcomputer.com/) - Information security and technology news
- [Security Affairs](https://securityaffairs.co/wordpress/) - Information security news
- [Graham Cluley](https://grahamcluley.com/) - Computer security news and opinions

### Research Papers and Publications

- [arXiv Cryptography and Security](https://arxiv.org/list/cs.CR/recent) - Preprint research papers
- [IEEE Security & Privacy](https://www.computer.org/csdl/magazine/sp) - Security research journal
- [USENIX Security Symposium](https://www.usenix.org/conferences/byname/108) - Security conference papers
- [ACM CCS](https://www.sigsac.org/ccs.html) - Computer and Communications Security conference
- [NDSS Symposium](https://www.ndss-symposium.org/) - Network and Distributed System Security Symposium
- [Black Hat Briefings](https://www.blackhat.com/html/archives.html) - Security conference presentations *(Free archives)*
- [DEF CON Media](https://media.defcon.org/) - DEF CON conference presentations *(Free archives)*
- [Virus Bulletin](https://www.virusbulletin.com/) - Security research and analysis

### Security Research Tools

- [Shodan](https://www.shodan.io/) - Search engine for Internet-connected devices
- [Censys](https://censys.io/) - Search engine for Internet-connected devices
- [VirusTotal](https://www.virustotal.com/) - Analyze suspicious files and URLs *(Free)*
- [Any.Run](https://any.run/) - Interactive malware analysis *(Free tier)*
- [Hybrid Analysis](https://www.hybrid-analysis.com/) - Free malware analysis service *(Free)*
- [Cuckoo Sandbox](https://cuckoosandbox.org/) - Automated malware analysis *(Free)*
- [MITRE ATT&CK](https://attack.mitre.org/) - Knowledge base of adversary tactics and techniques *(Free)*
- [OWASP](https://owasp.org/) - Open Web Application Security Project resources *(Free)*

---
