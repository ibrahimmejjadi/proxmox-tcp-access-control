# Proxmox TCP Access Control System

A homelab project simulating a real network infrastructure using **VMware + Proxmox VE** and **Alpine Linux** virtual machines. A Python TCP socket server controls access to the network — checking a CSV user database and returning **YES** or **NO** to any client that requests a connection.

---

## 📺 Demo Video
▶️ [Watch on YouTube]([https://www.youtube.com/@ibrahimmejjadi](https://youtu.be/dC9JOtZYFDo))

---

## 🏗️ Infrastructure

| VM ID | Hostname | Role |
|-------|----------|------|
| 100 | server | Main TCP server |
| 101 | firewall | Reserved (Phase 2) |
| 102 | IT-Support-admin | Admin client (active) |
| 103 | HR-Admin | Admin client |
| 104 | DIA-Admin | Admin client |
| 201-203 | HR-user-1/2/3 | Users (no access) |
| 301-303 | DIA-user-1/2/3 | Users (no access) |
| 501 | template-admin | Admin VM template |
| 502 | template-user | User VM template |

- **Hypervisor:** Proxmox VE (nested inside VMware Workstation)
- **OS:** Alpine Linux 3.24 on all VMs
- **Language:** Python 3

---

## ⚙️ How It Works

1. **Server (VM 100)** runs `server_script_100-1.py` on port `5001`
2. Server reads `user_database.csv` on startup — loads all usernames and statuses
3. **Admin client** runs `client_script_102-1.py`, enters server IP and username
4. Server checks: does the username exist? Is status `active`?
5. Returns `YES` or `NO`

```
Client → sends username → Server → checks CSV → returns YES/NO
```

---

## 📁 Files

| File | Description |
|------|-------------|
| `server_script_100-1.py` | TCP socket server, reads CSV, handles access logic |
| `client_script_102-1.py` | Client script, sends username, receives response |
| `user_database.csv` | User database (id, username, role, privilege, status) |
| `/etc/init.d/tcp-server` | OpenRC init script — auto-starts server on boot |

---

## 👤 User Database Structure

```csv
id,username,role,privilege,status
100,ibrahim,server,super-admin,active
102,it-support,IT-Support-admin,mini-admin,active
103,hr-admin,HR-Admin,admin,inactive
104,dia-admin,DIA-Admin,admin,inactive
201,hr-user-1,HR-user,user,inactive
...
```

---

## 🚀 Auto-Start on Boot (OpenRC)

The server starts automatically on VM 100 boot via OpenRC:

```bash
# Enable service
rc-update add tcp-server default

# Manual control
rc-service tcp-server start
rc-service tcp-server stop
rc-service tcp-server restart
rc-service tcp-server status
```

> ⚠️ After editing `user_database.csv`, always restart the service so the server reloads the updated database.

---

## 🔮 Planned Improvements (Part 2)

- [ ] Firewall VM (VM 101)
- [ ] IP whitelist for socket listener
- [ ] `last_login` column in CSV
- [ ] Partial access for HR and DIA admins
- [ ] Hidden identity files per VM
- [ ] Packet-level identity embedding
- [ ] Replace template VM 502 with Python3 pre-installed image

---

## 👨‍💻 Author

**Ibrahim Mejjadi** — Digital Infrastructure Student, CMC Tangier 
🔗 [LinkedIn](https://www.linkedin.com/in/ibrahimmejjadi) 
