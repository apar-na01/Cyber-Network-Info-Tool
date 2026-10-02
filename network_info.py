import socket
import subprocess

hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

print("=== Cyber Network Info Tool ===")
print("Hostname:", hostname)
print("Local IP:", ip_address)

print("\n=== Network Configuration ===")

result = subprocess.check_output("ipconfig", text=True)
lines = result.splitlines()

for i, line in enumerate(lines):
    if "Default Gateway" in line:
        for next_line in lines[i:i+3]:
            parts = next_line.strip().split()
            for part in parts:
                if part.count(".") == 3:
                    print("Default Gateway:", part)
                    break
            else:
                continue
            break
        break

print("\n=== DNS Information ===")

dns_result = subprocess.check_output(
    "nslookup google.com",
    text=True
)

for line in dns_result.splitlines():
    if "Address:" in line and "10." in line:
        print("DNS Server:", line.split(":", 1)[1].strip())
        break

print("\n=== Network Connectivity ===")

result = subprocess.run(
    ["ping", "-n", "1", "8.8.8.8"],
    capture_output=True,
    text=True
)

if result.returncode == 0:
    print("Internet Connectivity: Available")
else:
    print("Internet Connectivity: Not Available")
    