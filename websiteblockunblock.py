import ctypes
import os
import sys
import time
from datetime import datetime as dt

#! Check if script is running with admin privileges
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

#! Run the script with elevated privileges if not already running as admin
if not is_admin():
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
    exit()

#! CODE

#! Enter the site name which you want to block
sites_to_block = [
    "www.facebook.com",
    "facebook.com",
    "www.youtube.com",
    "youtube.com",
    "www.gmail.com",
    "gmail.com",
 ]

#! Use the appropriate hosts file path for windows / ubuntu
host_file_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"

def block_websites(duration_minutes):
    end_time = time.time() + (duration_minutes * 60)
    
    while time.time() < end_time:
        try:
            with open(host_file_path, "a") as hostfile:
                for site in sites_to_block:
                    hostfile.write(redirect + " " + site + "\n")
            print("Blocked websites. Waiting for", duration_minutes, "minutes...")
            time.sleep(2)  # Sleep for 2 m  before checking again
        except PermissionError as e:
            print(f"Caught a permission error: Try Running as Admin {e}")
            break

def unblock_website(website):
    try:
        with open(host_file_path, "r") as hostfile:
            lines = hostfile.readlines()
        with open(host_file_path, "w") as hostfile:
            for line in lines:
                if not any(site in line for site in sites_to_block):
                    hostfile.write(line)
        print(f"{website} unblocked.")
    except PermissionError as e:
        print(f"Caught a permission error: Try Running as Admin {e}")

if __name__ == "__main__":
    #! Block websites for 5 minutes
    # block_websites(5)  
    #! Unblock Websites 
    unblock_website("www.youtube.com")
