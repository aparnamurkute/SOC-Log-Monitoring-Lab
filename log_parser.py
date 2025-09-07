import re


log_file = 'auth.log'


pattern = r'Failed password for .* from (\d+\.\d+\.\d+\.\d+) port'

failed_attempts = {}

with open(log_file, 'r') as file:
    for line in file:
        match = re.search(pattern, line)
        if match:
            ip = match.group(1)
            failed_attempts[ip] = failed_attempts.get(ip, 0) + 1

print("Brute-force detection report:")
for ip, count in failed_attempts.items():
    print(f"IP {ip} had {count} failed login attempts.")
    if count >= 5:
        print("⚠️ Possible brute-force attack detected!")
