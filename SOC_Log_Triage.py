#By: Dany Arabo

# SOC Triage Dashboard GUI
import turtle               # GUI library
import random               # Random IP simulation
import string               # Ticket ID generation
import time                 # Loop timing
from collections import defaultdict  # Count IP events
from datetime import datetime       # Timestamp logs

# ---------------- Config ----------------
Block_Threshold = 3            # High severity threshold
Escalation_Threshold = 2       # Medium severity threshold
Double_Check_Threshold = 1     # Low severity threshold

# ---------------- Data ----------------
ip_events = defaultdict(int)   # Track IP occurrences
tickets_created = {}           # Store ticket IDs
log_entries = []               # Keep last 15 logs

# ---------------- Turtle Setup ----------------
screen = turtle.Screen()       # Main window
screen.title("SOC Triage Dashboard")  # Window title
screen.bgcolor("black")        # Background color
screen.setup(width=1000, height=600) # Window size
screen.tracer(0)               # Disable auto-refresh

# Create turtles
title_t = turtle.Turtle(visible=False)   # Title turtle
table_t = turtle.Turtle(visible=False)   # Table turtle
sidebar_t = turtle.Turtle(visible=False) # Sidebar turtle

for t in [title_t, table_t, sidebar_t]:
    t.penup()               # No drawing when moving
    t.hideturtle()          # Hide cursor
    t.color("white")        # Default text color

# ---------------- Helper Functions ----------------
def draw_title():
    title_t.clear()                         # Clear old title
    title_t.goto(0, 260)                    # Move near top
    title_t.color("white")                   # White color
    title_t.write("SOC Triage Dashboard", align="center", font=("Arial", 24, "bold")) # Title

def Random_Jira_Ticket_ID(prefix="Jira"):
    a = ''.join(random.choices(string.ascii_uppercase, k=3)) # Random letters
    b = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4)) # Random chars
    return f"{prefix}-{a}-{b}"            # Return ticket ID

def create_ticket(ip):
    if ip not in tickets_created:          # Only create new ticket
        tickets_created[ip] = Random_Jira_Ticket_ID()
    return tickets_created[ip]             # Return ticket ID

def categorize_ips():
    block_list = [(ip, c) for ip, c in ip_events.items() if c >= Block_Threshold]       # High severity
    escalate_list = [(ip, c) for ip, c in ip_events.items() if Escalation_Threshold <= c < Block_Threshold] # Medium
    observed_list = [(ip, c) for ip, c in ip_events.items() if Double_Check_Threshold <= c < Escalation_Threshold] # Low severity
    return block_list, escalate_list, observed_list  # Return lists

def draw_table(block_list, escalate_list, observed_list):
    table_t.clear()                       # Clear previous table
    table_t.goto(-480, 220)               # Table header position
    table_t.color("white")                
    table_t.write(f"{'Time':<10} {'IP':<18} {'Severity':<12} {'Ticket ID':<12}", font=("Courier", 14, "bold")) # Header

    global log_entries
    log_entries = []                       # Reset log entries

    for ip, _ in block_list:
        log_entries.append((ip, "BLOCKED", "red"))          # Red for blocked
    for ip, _ in escalate_list:
        log_entries.append((ip, "ESCALATED", "orange"))     # Orange for escalated
    for ip, _ in observed_list:
        log_entries.append((ip, "OBSERVED", "light blue"))  # Light blue for low severity

    # Show only last 15 logs
    display_logs = log_entries[-15:]
    y = 190                                # Start y-position
    for ip, severity, color in display_logs:
        ticket = create_ticket(ip)          # Get ticket ID
        table_t.goto(-480, y)               # Move to row
        table_t.color(color)                 # Set color
        table_t.write(f"{datetime.now().strftime('%H:%M:%S'):<10} {ip:<18} {severity:<12} {ticket:<12}", font=("Courier", 12))
        y -= 25                              # Move down one row

def draw_sidebar(block_list, escalate_list, observed_list):
    sidebar_t.clear()                     # Clear old sidebar
    x = 250                               # Right side
    start_y = -50                          # Bottom-center position
    spacing = 30

    # Header
    sidebar_t.goto(x, start_y + spacing*4)
    sidebar_t.color("white")
    sidebar_t.write("Counts & Summary:", font=("Arial", 14, "bold"))

    # Blocked
    sidebar_t.goto(x, start_y + spacing*3)
    sidebar_t.color("red")
    sidebar_t.write(f"Blocked: {len(block_list)}", font=("Arial", 12))

    # Escalated
    sidebar_t.goto(x, start_y + spacing*2)
    sidebar_t.color("orange")
    sidebar_t.write(f"Escalated: {len(escalate_list)}", font=("Arial", 12))

    # Observed
    sidebar_t.goto(x, start_y + spacing*1)
    sidebar_t.color("light blue")
    sidebar_t.write(f"Observed: {len(observed_list)}", font=("Arial", 12))

    # Total
    sidebar_t.goto(x, start_y)
    sidebar_t.color("white")
    total = len(block_list) + len(escalate_list) + len(observed_list)
    sidebar_t.write(f"Total IPs: {total}", font=("Arial", 12))

def simulate_log():
    ip = f"192.168.{random.randint(0,255)}.{random.randint(1,254)}" # Random IP
    choice = random.choices(["BLOCKED", "ESCALATED", "OBSERVED"], [2,3,5])[0] # Random severity
    if choice == "BLOCKED":
        ip_events[ip] += random.randint(Block_Threshold, Block_Threshold+1) # Increment high
    elif choice == "ESCALATED":
        ip_events[ip] += random.randint(Escalation_Threshold, Escalation_Threshold+1) # Increment medium
    else:
        ip_events[ip] += 1     # Increment low

# ---------------- Main Loop ----------------
draw_title()                      # Draw dashboard title

while True:
    simulate_log()                              # Simulate new log
    block_list, escalate_list, observed_list = categorize_ips() # Categorize IPs
    draw_table(block_list, escalate_list, observed_list)       # Draw table
    draw_sidebar(block_list, escalate_list, observed_list)    # Draw sidebar
    screen.update()                                         # Refresh screen
    time.sleep(1)                                          # Wait 1 second
    print(Fore.CYAN + "\n=== Analysis Complete ===")              # Completion confirmation
