#By: Dany Arabo

import re                                          # For pattern matching IPs
from collections import defaultdict                # For counting IP activities
from datetime import datetime, timezone            # For current time in UTC
import json                                        # For saving Jira ticketing details
import os                                          # For direct file operations
import random, string                              # For generating random ticket IDs for Jira

# -------------------------------------------------------------------------
try:
    from colorama import init, Fore                # For colored terminal output
    init(autoreset=True)                           # Auto-reset colors after each print
except ImportError:                                # Will use dummy colors if colorama is not installed
    class Dummy:                                   # Fallback dummy class
        RED = GREEN = YELLOW = Blue = ''           # No color codes
    Fore = Dummy()                                 # Assign dummy class to Fore
# ------------------------------------------------------------------------- 
log_file_name = os.path.join(os.path.dirname(os.path.abspath(__file__)), "SOC.log")
Block_Threshold = 3                                # Threshold for blocking an IP triggers
Escalation_Threshold = 2                           # Threshold for escalating to Jira tickets
Double_Check_Threshold = 1                         # Threshold for double-checking before blocking or escalating
# ------------------------------------------------------------------------
SSH_Fail = re.compile(r"Failed password for .* from (\d+\.\d+\.\d+\.\d+)")                # To match attempted SSH logins (ssh = Secure Shell)
Firewall_Block = re.compile(r"\b(Denied|Drop|Reject|Block)\b.*?(\d+\.\d+\.\d+\.\d+)")     # To match firewall IP blocks
# ------------------------------------------------------------------------
ip_events = defaultdict(int)                       # Dictionary to count events per IP
#------------------------------------------------------------------------
def parse_log(file_path):                          # Log analysis parser
    try:
        with open(file_path) as f:                 # Open log file
            lines = f.readlines()                  # Read all lines
            print(Fore.LIGHTGREEN_EX + f"\nLoaded {len(lines)} log lines from '{file_path}'\n") # File size
            for line in lines:                     # Process the log lines
                ssh = SSH_Fail.search(line)        # Align with SSH attempts
                fw = Firewall_Block.search(line)   # Align with firewall blocks
                if ssh:
                    ip_events[ssh.group(1)] += 1   # Count number of SSH fails
                elif fw and fw.group(2):           # Unless no IP found
                    ip_events[fw.group(2)] += 1    # Count number of firewall blocks
    except FileNotFoundError:                      # Handle missing log file
        print(Fore.RED +f"Log file not found: {file_path}") # Error message for missing file
#------------------------------------------------------------------------
def save_list(filename, ips):                      # Save list of IPs to a file
    with open(filename, "w") as f:                 # Open the file for writing
        for ip in ips:                             # For each IP in list
            f.write(ip + "\n")                     # Write up the IP to the file
#------------------------------------------------------------------------
def Random_Jira_Ticket_ID(prefix="Jira"):
    a = '' .join(random.choices(string.ascii_uppercase, k=3))                                # Three random uppercase letters
    b = '' .join(random.choices(string.ascii_uppercase + string.digits, k=4 or 3 or 2 or 1)) # Random list of 4,3,2 or 1 uppercase letters or digits
    return f"{prefix}-{a}-{b}"                                                               # Return full ticket ID
#------------------------------------------------------------------------
def create_Jira_Ticket(issue_type, ip, count, project="SOC_Log"): # Create a Jira ticket
    os.makedirs("jira_tickets", exist_ok=True)                    # Ensure directory exists, if not, make output directory
    ts = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")    # Timestamp in UTC format (UTC = Coordinated Universal Time)
    ticket_key = Random_Jira_Ticket_ID()                          # Generate a random ticket ID
    ticket = {
        "Key": ticket_key,                                       # Unique ticket ID
        "project":project,                                       # Project name
        "issue_type": issue_type,                                # Issue type (Blocked or Escalated)
        "summary": f"{issue_type} - suspicious IP {ip}",         # Summary line
        "description": f"Auto-generated {issue_type} ticket for IP {ip}. Dectected {count} suspicious events.", # Description of the issue 
        "priority": "High" if issue_type.lower() == "Blocked" else "Medium", # Priority based on issue type
        "created_at": ts                                         # Timestamp of ticket creation
    }   
    fname = f"jira_tickets/{ticket_key}_{ip.replace('.','_')}.json"  # Filename for saving ticket details
    with open(fname, "w", encoding="utf-8") as fh:                   # Open file for writing
        json.dump(ticket, fh, indent=2)                              # Save ticket details in JSON format
        print(f"{Fore.YELLOW} Created ticket {ticket_key} for {ip}") # Notify user of ticket creation
#------------------------------------------------------------------------
def analyze():
    block_list = [(ip, c) for ip, c in ip_events.items() if c >= Block_Threshold] # IPs for blocking
    escalate = [(ip, c) for ip, c in ip_events.items() if Escalation_Threshold <= c < Block_Threshold] # IPs for escalation if not blocked
    double_check = [(ip, c) for ip, c in ip_events.items() if Double_Check_Threshold <= c < Escalation_Threshold] # IPs for double-checking if not escalated

    save_list("blocklist.txt", [ip for ip, _ in block_list])       # Add the blicklist to a file
    save_list("escalate.txt", [ip for ip, _ in escalate])          # Add escalate list to a file
    save_list("double_check.txt", [ip for ip, _ in double_check])  # Add double-check list to a file
#------------------------------------------------------------------------
    if block_list:                                                 # Do we have IPs to block?
     print(Fore.RED + "Blocked IPs (Malicious):")                  # IP block header
     print("-" * 30)                                               # console separator
     for ip, count in block_list:                                  # For each blocked IP
         print(f"{Fore.RED}{ip:<15} Events: {count}")              # display blocked IPs
         create_Jira_Ticket("Blocked", ip, count)                  # Create a Jira ticket for each blocked IP
    else:
        print(Fore.GREEN + "\n--- Blocked IPs (Malicious): None ---")      # No blocked IPs
        print()
#------------------------------------------------------------------------
    if escalate:                                                   # Escalate if we have IPs for escalation
        print(Fore.MAGENTA + "IPs for escalation: ")               # IP escalation header  
        print("-" * 30)                                            # Dash separator
        for ip, count in escalate:                                 # Output each escalated IP
            print(f"{Fore.MAGENTA}{ip:<15} Events: {count}")       # Display escalated IPs
            create_Jira_Ticket("Escalated", ip, count)             # Create a Jira ticket for each escalated IP
    else:
        print(Fore.GREEN + "\n--- IPs for escalation: None ---")           # No IPs for escalation
        print()
#------------------------------------------------------------------------
    if double_check:
        print(Fore.BLUE + "IPs to double-check: ")                # IPs to double-check
        print("-" * 30)                                           # Dash separator
        for ip, count in double_check:                            # Display each IP to double-check
            print(f"{Fore.BLUE}{ip:<15} Events: {count}")         # List of IPs to double-check
    else:
        print(Fore.GREEN + "\n--- IPs to double-check: None ---")         # No IPs to double-check
        print()
#------------------------------------------------------------------------
if __name__ == "__main__":                                        # Begin main program
    print(Fore.LIGHTYELLOW_EX + "Starting SOC Log Analyzer...\n") # Startup confirmation
    parse_log(log_file_name)                                           # Parse the log file
    analyze()                                                     # Analyze the parsed data
    print(Fore.CYAN + "\n=== Analysis Complete ===")              # Completion confirmation