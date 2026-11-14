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