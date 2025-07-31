import re

# Define the regex pattern for matching IP addresses (IPv4)
ip_pattern = re.compile(r'\b(?:\d{1,3}\.){3}\d{1,3}\b')

# Read the file and find all IP matches
with open('ipsscrape.txt', 'r') as file:
    content = file.read()
    ips = ip_pattern.findall(content)

# Print matched IPs
with open('ip_list.txt', 'w') as output_file:
    for ip in ips:
        output_file.write(f"{ip}\n")
for ip in ips:
    print(ip)