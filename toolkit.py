import socket
import re
import os
import platform


def port_scanner():
    target = input("Enter target host: ")
    start_port = int(input("Start port: "))
    end_port = int(input("End port: "))

    print(f"\nScanning {target}...\n")

    for port in range(start_port, end_port + 1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)

        result = s.connect_ex((target, port))

        if result == 0:
            print(f"Port {port} OPEN")

        s.close()


def password_checker():
    password = input("Enter password: ")
    score = 0

    if len(password) >= 8:
        score += 1
    if re.search("[A-Z]", password):
        score += 1
    if re.search("[a-z]", password):
        score += 1
    if re.search("[0-9]", password):
        score += 1
    if re.search("[@#$%^&*!]", password):
        score += 1

    print(f"\nPassword security score: {score}/5")


def network_monitor():
    host = input("Enter host to ping: ")

    param = "-n 1" if platform.system().lower() == "windows" else "-c 1"

    command = f"ping {param} {host}"

    response = os.system(command)

    if response == 0:
        print("Host is UP")
    else:
        print("Host is DOWN")


def log_analyzer():
    filename = input("Enter log file name: ")

    try:
        with open(filename) as f:
            for line in f:
                if "Failed password" in line:
                    ip = re.search(r"\d+\.\d+\.\d+\.\d+", line)

                    if ip:
                        print("Suspicious login from:", ip.group())

    except:
        print("Log file not found")


def menu():
    while True:

        print("\n===== Cybersecurity Toolkit =====\n")
        print("1. Port Scanner")
        print("2. Password Strength Checker")
        print("3. Network Monitor")
        print("4. Security Log Analyzer")
        print("5. Exit")

        choice = input("\nSelect option: ")

        if choice == "1":
            port_scanner()

        elif choice == "2":
            password_checker()

        elif choice == "3":
            network_monitor()

        elif choice == "4":
            log_analyzer()

        elif choice == "5":
            break

        else:
            print("Invalid option")


menu()
