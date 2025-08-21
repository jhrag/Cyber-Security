import socket
import argparse

def scan_ports(host, start_port, end_port):
    print(f"\n[*] Scanning {host} from port {start_port} to {end_port}...\n")
    open_ports = []

    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)  # Timeout for faster scanning
        try:
            result = sock.connect_ex((host, port))  # 0 = open
            if result == 0:
                print(f"[+] Port {port} is OPEN")
                open_ports.append(port)
        except KeyboardInterrupt:
            print("\n[!] Scan aborted by user.")
            break
        except socket.error:
            print("[!] Could not connect to host.")
            break
        finally:
            sock.close()

    print("\n[*] Scan complete.")
    if open_ports:
        print("Open ports:", open_ports)
    else:
        print("No open ports found.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simple Python Port Scanner")
    parser.add_argument("host", help="Target host (IP or domain)")
    parser.add_argument("-s", "--start", type=int, default=1, help="Start port (default: 1)")
    parser.add_argument("-e", "--end", type=int, default=1024, help="End port (default: 1024)")
    args = parser.parse_args()

    scan_ports(args.host, args.start, args.end)