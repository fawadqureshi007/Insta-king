
# 👑 Insta-king

> **Instagram Login Simulation • Security Research Lab**

Insta-king is a lightweight Flask-based lab environment built to analyze authentication request flows, inspect HTTP header signatures, observe client telemetry, and output real-time request logs directly inside your terminal session.

> ⚠️ **Disclaimer:** For educational and authorized lab testing only. Always use dummy credentials during simulation.

---

## ⚡ Quick Start

Clone, set up, and launch the lab environment with a single terminal command:

```bash
git clone [https://github.com/fawadqureshi007/Insta-king.git](https://github.com/fawadqureshi007/Insta-king.git) && cd Insta-king && python3 -m venv venv && source venv/bin/activate && pip install -r requirements.txt && python3 Insta-king.py

```

Access the web interface at **`http://127.0.0.1:5001/`**

---

## 🛠️ Features & Technical Overview

* **Real-Time Terminal Logging:** Captured credentials, timestamps, and IP addresses print automatically in the active console—no extra log files or external tools required.
* **Pixel-Accurate UI:** Instagram-style login interface designed for authentication flow testing and UI analysis.
* **Request & Payload Inspection:** Parses incoming `POST /login` parameters and extracts submitted form data on the fly.
* **Client Telemetry:** Logs client IP addresses, browser User-Agents, and forwarding headers (`X-Forwarded-For`).
* **Multi-Environment Support:** Native binding support for Localhost (`127.0.0.1`), LAN broadcasts (`0.0.0.0`), and remote tunnels (Localtunnel / Cloudflare / ngrok).

---

## 📦 Detailed Setup & Prerequisites

Ensure you have Python 3.8+ and `git` installed on your system before proceeding.

### 1. Clone Repository

```bash
git clone [https://github.com/fawadqureshi007/Insta-king.git](https://github.com/fawadqureshi007/Insta-king.git)
cd Insta-king

```

### 2. Environment Setup

Creating an isolated virtual environment prevents library conflicts across your operating system.

* **Linux / Kali Linux:**
```bash
python3 -m venv venv
source venv/bin/activate

```


* **Windows (PowerShell / CMD):**
```cmd
python -m venv venv
venv\Scripts\activate

```



### 3. Install Dependencies

```bash
# Upgrade pip to prevent build errors
python -m pip install --upgrade pip

# Install project requirements
pip install -r requirements.txt

```

---

## 🚀 Execution Modes

### Mode 1: Local Loopback (Default)

Start the server locally on port `5001`:

```bash
python3 Insta-king.py

```

1. Open **`http://127.0.0.1:5001/`** in your browser.
2. Enter dummy credentials and click **Log In**.
3. Observe the output captured instantly in your active terminal session.

#### 🔧 Port 5001 Busy?

If port `5001` is already in use by another process (e.g., macOS AirPlay Receiver):

```bash
# Locate Process ID (PID) on port 5001
lsof -i :5001

# Terminate process
kill -9 <PID>

# Relaunch server
python3 Insta-king.py

```

---

### Mode 2: Local Area Network (LAN Testing)

To test cross-device requests from mobile phones, tablets, or virtual machines connected to the same network:

1. Open `Insta-king.py` in your editor and update the host parameter:
```python
# Line near bottom of file
app.run(host="0.0.0.0", port=5001)

```


2. Retrieve your host local IP address:
```bash
# Linux / Kali
hostname -I | awk '{print $1}'

# Windows
ipconfig

```


3. Launch server:
```bash
python3 Insta-king.py

```


4. Connect from your authorized test device: `http://<YOUR_LOCAL_IP>:5001/`

---

### Mode 3: Localtunnel Ingress (Remote Testing)

Expose your local instance publicly over a secure URL using `localtunnel`:

1. **Install Node.js & Localtunnel:**
```bash
sudo apt update
sudo apt install -y nodejs npm
sudo npm install -g localtunnel

```


2. **Launch Insta-king:**
```bash
python3 Insta-king.py

```


3. **Spawn Tunnel (in a second terminal):**
```bash
lt --port 5001

```



---

### Mode 4: Cloudflare Tunnel / ngrok Alternatives

* **Cloudflare:**
```bash
cloudflared tunnel --url [http://127.0.0.1:5001](http://127.0.0.1:5001)

```


* **ngrok:**
```bash
ngrok http 5001

```



---

## 📊 Terminal Results & Live Output

When a user interacts with the web interface, HTTP requests and extracted authentication parameters display directly inside your active server terminal session:

```text
kali@hackerfawad)-[~/Instaking]
$ python3 Insta-king.py

 * Serving Flask app "Insta-king"
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment.
 * Running on [http://127.0.0.1:5001](http://127.0.0.1:5001)
Press CTRL+C to quit

127.0.0.1 - - [22/Sep/2026 12:32:33] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [22/Sep/2026 12:32:33] "GET /static/instagramimage.webp HTTP/1.1" 304 -

============================== LOGIN ATTEMPT ==============================
Time : 2026-09-22 12:40:16
IP   : 127.0.0.1
User : hacker_fawad
Pass : mypassword@123
===========================================================================

127.0.0.1 - - [22/Sep/2026 12:40:16] "POST /login HTTP/1.1" 302 -

```

---

## 📁 Repository Structure

```text
Insta-king/
├── Insta-king.py       # Main Flask application & live log display logic
├── requirements.txt    # Python package dependencies
├── README.md           # Documentation & user instructions
├── LICENSE             # Project license agreement
└── static/             # Static UI web assets
    └── instagramimage.webp

```

---

## 🛡️ Responsible Usage & Legal Disclaimer

This tool is created exclusively for educational research, defensive security labs, and authorized awareness training.

* **Allowed:** Authorized penetration testing, isolated lab research, defensive security training.
* **Prohibited:** Malicious credential harvesting, unauthorized deployments, phishing attacks against real users.

---

## 👨‍💻 Author Info

**Fawad Qureshi**

*Offensive Security Researcher & Pentester*

* **GitHub:** [@fawadqureshi007](https://github.com/fawadqureshi007)
* **Instagram:** [@h4cker_fawad](https://instagram.com/h4cker_fawad)

---

## ⚠️ Copyright & Attribution

**Insta-king** is an original open-source project by **Fawad Qureshi**.

* **Allowed:** Fork, modify, and use for learning or research with proper credit linked to the original repo.
* **Prohibited:** Re-uploading under your own name, removing author credits, or claiming the project as your own.

> 🚨 Unauthorized redistribution or claiming ownership will result in DMCA takedown notices and copyright enforcement on GitHub.

---

⭐ **If this project helped your security research, give it a star on GitHub!**
💛 Support

If you want to support my work or access more offensive security tools and research, you can support me here:

Binance UID: "711788725"


