# Insta-king

**Insta-king** is a Flask-based Instagram login honeypot designed to capture login attempts for demonstration or testing purposes. It provides a realistic Instagram login interface with console output in a visually appealing colored box.

> ⚠️ **Disclaimer:** This project is for educational/testing purposes only. Do **not** use it to capture credentials without consent.

---

## Features

- Full Instagram login page mockup (HTML/CSS)  
- Colored console output for login attempts  
- Logs all login attempts to `login_attempts.log`  
- Supports static image rendering (`static/Insta.png`)  
- Easy setup with virtual environment and `requirements.txt`  

---

## Repository Structure

Insta-king/
├── Insta-king.py # Main Flask app
├── requirements.txt # Python dependencies
├── README.md # Project documentation
├── LICENSE # License file
├── static/
│ └── Insta.png # Instagram mockup image


---

## Prerequisites

- Python 3.8+  
- `pip` installed  

---

## Setup Instructions

1. **Clone the repository:**

```bash
git clone https://github.com/yourusername/Insta-king.git
cd Insta-king

Create and activate a virtual environment:
python3 -m venv venv
source venv/bin/activate

Ensure your requirements.txt contains:
Flask==2.3.3
colorama==0.4.6

Run the Flask server:
python3 Insta-king.py

Open your browser and go to:
http://127.0.0.1:5001/

Login attempts will be logged in login_attempts.log and printed in the console with a colored box.

Handling "Port Already in Use"

If the server complains that port 5001 is busy, you can kill it with:
sudo kill -9 $(sudo lsof -t -i :5001) 2>/dev/null || true

Then rerun the server:
python3 Insta-king.py

Example Console Output
╔════════════════════════════╗
║  LOGIN ATTEMPT             ║
║  Time : 2025-10-29 14:20:22║
║  IP   : 127.0.0.1          ║
║  User : h4cker_fawad       ║
║  Pass : mypassword@123      ║
╚════════════════════════════╝


Notes

This is a development server. Do not deploy this in production.

Only use for educational or testing purposes.

All login attempts are logged in plain text, handle with caution.
