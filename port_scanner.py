#!/usr/bin/env python3
"""
Simple TCP (Transmission Control Protocol) Port Scanner
Author: Katlego Motsoaledi (Cybersecurity Intern)
Purpose: Learn port scanning and socket programming on Kali Linux
"""

import socket
import threading


# ------------------------------------
# Function: scan_port
# ------------------------------------
def scan_port(target, port):
    """
    Attempts to connect to a TCP port on the target.
    If the connection is successful, the port is open.
    """

    try:
        # Create a socket object
        # AF_INET = IPv4
        # SOCK_STREAM = TCP
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Set timeout (prevents hanging)
        s.settimeout(1)

        # Attempt a connection
        result = s.connect_ex((target, port))

        if result == 0:
            print(f"[+] Port {port} is OPEN")
        else:
            print(f"[-] Port {port} is CLOSED")

        # Close socket to free resources
        s.close()

    except socket.error as e:
        print(f"[!] Error scanning port {port}: {e}")


# ------------------------------
# Main Method
# ------------------------------
def main():
    print("=== Simple TCP Port Scanner ===")

    # Ask user for target
    target = input("Enter IP address or hostname: ")

    # Ask user for port range
    start_port = int(input("Enter starting port: "))
    end_port = int(input("Enter ending port: "))

    print(f"\nScanning {target} from port {start_port} to {end_port}...\n")

    # Store threads
    threads = []

    # Loop through ports
    for port in range(start_port, end_port + 1):
        t = threading.Thread(target=scan_port, args=(target, port))
        threads.append(t)
        t.start()

    # Wait for all threads to finish
    for t in threads:
        t.join()

    print("\nScan completed.")


# Run the program
if __name__ == "__main__":
    main()

