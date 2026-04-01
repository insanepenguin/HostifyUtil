##pip install paramiko
# This script sets the inform URL for UniFi devices using SSH.
# Edmond B. 
# Creadted on:2025-7-14
# Last modified: 2025-7-14 
import time
import paramiko
port = 22
cmd = f"/usr/bin/mca-cli-op set-inform http://207.148.11.157/:8080/inform"

input("This script will set the inform URL for all UniFi devices in the list. Press Enter to continue...")

username = input("Enter the username for the devices: ")
pwd = input("Enter the password for the devices: ")

try:
    with open("ip_list.txt") as f:
        listOfIPS = [line.strip() for line in f if line.strip()]
except FileNotFoundError:
    print("The file 'ip_list.txt' does not exist.")
    listOfIPS = []

for ip in listOfIPS:
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(ip, port=port, username=username, password=pwd)
        print(f"Connected to {ip}")
        time.sleep(.5) 
        stdin, stdout, stderr = client.exec_command(cmd)
        print(f"Error command on {ip}: {stderr.read().decode().strip()}")
        print(f"STD Out executed on {ip}: {stdout.read().decode().strip()}")
        client.close()
    except paramiko.AuthenticationException:
        print(f"Authentication failed for {ip}. Please check your credentials.")
    except paramiko.SSHException as e:
        print(f"SSH connection failed for {ip}: {e}")
    except Exception as e:
        print(f"An error occurred with {ip}: {e}")
    finally:
        print(f"Finished processing {ip}\n")
input("Script execution completed.")