from collections import Counter
import re

# Read log file
with open("sample_log.txt", "r") as file:
    logs = file.readlines()

failed_ips = []

for line in logs:
    if "LOGIN_FAILED" in line:
        ip = re.search(r'IP=(\d+\.\d+\.\d+\.\d+)', line)
        if ip:
            failed_ips.append(ip.group(1))

# Count failed attempts
ip_count = Counter(failed_ips)

# Generate report
with open("security_report.txt", "w") as report:

    report.write("=== SECURITY REPORT ===\n\n")

    report.write(f"Total Failed Logins: {len(failed_ips)}\n\n")

    report.write("Failed Login Attempts by IP:\n")

    for ip, count in ip_count.items():
        report.write(f"{ip} --> {count} attempts\n")

    report.write("\nSuspicious IP Addresses:\n")

    for ip, count in ip_count.items():
        if count >= 3:
            report.write(f"{ip} (Suspicious - {count} failed attempts)\n")

print("Report Generated Successfully!")