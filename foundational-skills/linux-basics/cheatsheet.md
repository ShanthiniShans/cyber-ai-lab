# 🐧 Linux Command Line Cheatsheet for Cybersecurity

A quick reference for essential Linux commands often used in cybersecurity tasks like log analysis, process monitoring, network debugging, and file operations.

---

## 🔍 File & Directory Operations

| Command                         | Description                          |
|----------------------------------|--------------------------------------|
| `ls -l`                         | List files with details              |
| `cd /path/to/dir`              | Change directory                     |
| `pwd`                          | Show current directory               |
| `mkdir logs`                   | Create a new folder                  |
| `touch test.txt`              | Create an empty file                 |
| `cat filename`                | View file contents                   |
| `tail -f /var/log/syslog`     | Live monitor a log file              |
| `cp source dest`              | Copy files or folders                |
| `mv source dest`              | Move or rename                       |
| `rm -rf folder/`              | Delete files/folders (use with care) |

---

## 🔎 System Monitoring

| Command                         | Description                          |
|----------------------------------|--------------------------------------|
| `top` or `htop`                | View system resource usage           |
| `ps aux`                       | List running processes               |
| `kill -9 PID`                  | Terminate a process by PID           |
| `df -h`                        | Disk space usage                     |
| `du -sh *`                     | Size of directories                  |

---

## 🌐 Networking

| Command                         | Description                          |
|----------------------------------|--------------------------------------|
| `ifconfig` / `ip a`             | Show network interfaces              |
| `ping domain.com`              | Check network connectivity           |
| `netstat -tulpn`               | List open ports & services           |
| `ss -tulwn`                    | Another port listing tool            |
| `traceroute domain.com`        | Trace the route to a host            |
| `dig domain.com`               | DNS lookup                           |
| `curl http://site.com`         | Fetch a webpage                      |

---

## 🔐 File Permissions & Ownership

| Command                         | Description                          |
|----------------------------------|--------------------------------------|
| `chmod 755 file.sh`            | Set file permissions                 |
| `chown user:group file`        | Change file ownership                |
| `ls -la`                       | See detailed permissions             |

---

## 📦 Package Management (Debian/Ubuntu)

| Command                         | Description                          |
|----------------------------------|--------------------------------------|
| `sudo apt update`              | Refresh package list                 |
| `sudo apt install toolname`    | Install new tool                     |
| `sudo apt remove toolname`     | Uninstall tool                       |

---

## ⚠️ Log Analysis

| Command                         | Description                          |
|----------------------------------|--------------------------------------|
| `grep "error" /var/log/syslog`  | Search for “error” in log            |
| `awk '{print $5}' filename`     | Extract column from logs             |
| `cut -d':' -f1 file.log`        | Cut specific field by delimiter      |
| `sort`, `uniq`, `wc -l`        | Combine for basic log parsing        |

---

> 🧠 **Pro Tip:** Combine commands with pipes `|` and redirects `>` for powerful one-liners!

```bash
grep "Failed" auth.log | awk '{print $1,$2,$3,$11}' | sort | uniq -c | sort -nr
