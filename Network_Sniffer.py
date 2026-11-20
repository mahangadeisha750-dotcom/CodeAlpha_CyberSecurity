
# CodeAlpha Cyber Security Internship
# Project 3: Basic Network Sniffer

import socket

print("===== BASIC NETWORK SNIFFER =====")

# Create a network socket
try:
    sniffer = socket.socket(
        socket.AF_INET,
        socket.SOCK_RAW,
        socket.IPPROTO_IP
    )

    print("Network Sniffer Started!")
    print("Listening for network packets...")

except PermissionError:
    print("Permission denied!")
    print("Administrator access is required.")

except OSError as error:
    print("Network Error:", error)

print("===== PROGRAM ENDED =====")
