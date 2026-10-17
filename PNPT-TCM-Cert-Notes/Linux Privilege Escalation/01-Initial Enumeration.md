# System Enumeration
**System Enumeration** is the process of gathering information about a Linux system to identify potential privilege escalation paths. It involves checking users, groups, kernel versions, `sudo` permissions, SUID binaries, running processes, scheduled tasks, and file permissions. The goal is to discover misconfigurations and vulnerabilities that could allow an attacker to gain higher privileges.

Following Commands:
```bash
hostname

uname -a
cat /proc/version
# Shows the kernel information 
# Very Important as far we could find existing exploits on the internet

cat /etc/issue
# Shows the distribution

lscpu
# For cpu architecture info

ps aux
# Shows what all services are running.
```

# Username Enumeration
**Username Enumeration** is the process of identifying valid user accounts on a Linux system by examining `/etc/passwd`, group memberships, running processes, and user directories. It helps determine available accounts, their privileges, and potential targets for further investigation or privilege escalation.

Following Commands:
```bash
whoami
# Current username

id
# Current user id

sudo -l
# List all of the commands that can only by sudo/root user

cat /etc/passwd
# List all of the Users
# (tip) ~$ cat /etc/passwd | cut -d : 1 
# Will return only the usernames (cut out other characters)

cat /etc/shadow
# Stores actual passwords, But is not human-readable

history
# Might be something Juicy History
```

# Network Enumeration
**Network Enumeration** is the process of identifying network interfaces, IP addresses, routing tables, listening ports, active connections, and accessible services. It helps map network exposure and discover potential attack vectors for lateral movement or privilege escalation.

Following Commands:
```bash
ifconfig
ip a
# IP informations

ip route
# If the system seems to be routing to another machine/network

arp -a
ip neigh
# Maps IPv4 addresses to MAC addresses of devices on the local network

netstat
# netstat — Displays network connections, listening ports, routing tables, and network interface statistics on Debian.

netstat -ano
# netstat -ano — Common on Windows; displays all connections and listening ports, numeric addresses, and process IDs. On Debian, use `netstat -tunap` (run with `sudo` to see process information).
```

# Password Hunting
**Password Hunting** is the process of searching for exposed passwords, credentials, and authentication secrets in files, configuration files, scripts, environment variables, and user histories. It helps identify credential exposure that could enable unauthorized access or privilege escalation.

Following Commands:
```bash





```