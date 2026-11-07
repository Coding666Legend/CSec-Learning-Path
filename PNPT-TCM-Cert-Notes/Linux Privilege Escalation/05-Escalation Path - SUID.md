# Introduction
**Escalation Path: SUID (Set User ID) :**
SUID is a Linux file permission bit that allows an executable to run with the privileges of its file owner rather than the privileges of the user executing it. When a binary is owned by `root` and has the SUID bit enabled, it executes with effective UID 0. Attackers can abuse misconfigured SUID binaries, vulnerable programs, or shell-escaping functionality to obtain root privileges. Common enumeration command: `find / -perm -4000 -type f 2>/dev/null` .

Following Commands :
```bash
find / -perm -u=s -type f 2>/dev/null
# files having SUID bit in User(Owner)
```

# Vulnversity

**Room Link :** https://tryhackme.com/room/vulnversity

