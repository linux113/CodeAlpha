Absolutely! Here's the **full installation guide** you can include in your `README.md` — step-by-step from cloning to running the network sniffer tool, including interface detection and troubleshooting help.

---

## ✅ 🔧 Full Installation Guide (Add to `README.md`)

````markdown
---

## 🛠️ Full Installation Guide

Follow these steps to install and run the Python Network Sniffer on any Linux/macOS system. Windows may require WSL or admin tweaks.

---

### ✅ 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/network-sniffer.git
cd network-sniffer
````

---

### ✅ 2. Set Up Python Environment (Optional but Recommended)

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### ✅ 3. Install Dependencies

```bash
pip install -r requirements.txt
```

> This will install the required library: **Scapy**

---

### ✅ 4. Identify Your Network Interface

Run this to list all interfaces:

```bash
ip a
```

Look for something like:

* `eth0` (Ethernet)
* `wlan0` (Wi-Fi)
* `en0` (macOS Wi-Fi)

---

### ✅ 5. Run the Sniffer

```bash
sudo python3 sniffer.py -i eth0 -f "tcp"
```

* `-i` → Interface (e.g., `eth0`, `wlan0`)
* `-f` → BPF filter (e.g., `"tcp"`, `"udp"`, `"port 80"`)

#### 🔁 Examples:

| Command                                | Description                              |
| -------------------------------------- | ---------------------------------------- |
| `sudo python3 sniffer.py`              | Capture all traffic on default interface |
| `sudo python3 sniffer.py -f "port 80"` | Sniff HTTP traffic                       |
| `sudo python3 sniffer.py -i wlan0`     | Sniff on Wi-Fi interface                 |
| `sudo python3 sniffer.py -f "icmp"`    | Capture only ping packets                |

---

### 📁 Output

Captured packets will show in your terminal and save to:

```
packet_log.txt
```

Each log includes:

* 📅 Timestamp
* 🌐 Source & Destination IPs
* ⚡ Protocol (TCP, UDP, ICMP)
* 📦 Payload (if available)

---

## ⚠️ Troubleshooting

* **Permission error?** → Use `sudo` to run the script.
* **Can't find `eth0`?** → Use `ip a` to list actual interface names.
* **On Windows?** → Use WSL (Ubuntu), or run in a Linux VM for full Scapy support.

---

## 🛡️ Legal Note

This tool is for **educational and ethical use only**. Capturing packets on networks you don’t own or have permission to analyze is **illegal** in many jurisdictions.

````

---

