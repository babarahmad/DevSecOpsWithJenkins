import os
import subprocess
import sqlite3
import hashlib

DB_NAME = "users.db"

# -----------------------------
# Insecure database connection
# -----------------------------
def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # ❌ SQL without constraints
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)"
    )
    conn.commit()
    conn.close()


# -----------------------------
# Insecure password hashing
# -----------------------------
def hash_password(password):
    # ❌ Weak hashing algorithm (MD5)
    return hashlib.md5(password.encode()).hexdigest()


# -----------------------------
# SQL Injection vulnerability
# -----------------------------
def login_user(username, password):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    hashed = hash_password(password)

    # ❌ SQL Injection vulnerability
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{hashed}'"
    cursor.execute(query)

    user = cursor.fetchone()
    conn.close()

    if user:
        print("Login successful!")
    else:
        print("Invalid credentials!")


# -----------------------------
# Command Injection vulnerability
# -----------------------------
def run_ping():
    host = input("Enter host to ping: ")

    # ❌ Command injection
    os.system("ping -c 1 " + host)


# -----------------------------
# Hardcoded secret
# -----------------------------
def admin_access():
    # ❌ Hardcoded credentials
    admin_password = "admin123"

    pwd = input("Enter admin password: ")
    if pwd == admin_password:
        print("Admin access granted!")
    else:
        print("Access denied!")


# -----------------------------
# Main menu
# -----------------------------
def main():
    init_db()

    print("\n=== Vulnerable Python Application ===")
    print("1. Login")
    print("2. Ping a host")
    print("3. Admin access")

    choice = input("Choose an option: ")

    if choice == "1":
        username = input("Username: ")
        password = input("Password: ")
        login_user(username, password)

    elif choice == "2":
        run_ping()

    elif choice == "3":
        admin_access()

    else:
        print("Invalid option!")


if __name__ == "__main__":
    main()
