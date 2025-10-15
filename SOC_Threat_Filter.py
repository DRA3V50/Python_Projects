import turtle
import random
import time
from datetime import datetime

# === Setup screen ===
screen = turtle.Screen()                  # Create main window
screen.title("SOC Log Dashboard")         # Set window title
screen.bgcolor("black")                   # Background color
screen.setup(width=900, height=600)       # Set window size
screen.tracer(0)                          # Disable auto-refresh for smoother updates

# === Create turtles ===
title_t = turtle.Turtle(visible=False)    # Turtle for title text
side_t = turtle.Turtle(visible=False)     # Turtle for sidebar info
log_t = turtle.Turtle(visible=False)      # Turtle for log table

# === Common config ===
for t in [title_t, side_t, log_t]:
    t.penup()                             # Don’t draw lines when moving
    t.color("white")                      # Default text color

# === Data setup ===
sources = ["Email", "Web", "Auth", "Cloud"]   # Possible log sources
counts = {"Critical": 0, "Abnormal": 0, "Medium": 0}  # Severity counters
logs = []                                    # List to store log entries

# === Draw main title ===
def draw_title():
    title_t.clear()                         # Clear previous title
    title_t.goto(-120, 250)                 # Move near top center
    title_t.write("SOC Log Dashboard", align="center", font=("Arial", 20, "bold"))  # Write header

# === Draw sidebar with sources and stats ===
def draw_sidebar():
    side_t.clear()                          # Clear old sidebar text
    side_t.goto(-400, 210)                  # Start near top-left
    side_t.write("Sources:", font=("Arial", 14, "bold"))  # Label

    # List all sources
    for i, src in enumerate(sources):
        side_t.goto(-400, 185 - i * 25)     # Step down each line
        side_t.write(f"- {src}", font=("Arial", 12))

    # Show live summary of log severities
    y = 60                                  # Starting Y for stats
    for key in ["Critical", "Abnormal", "Medium"]:
        side_t.goto(-400, y)
        side_t.write(f"{key}: {counts[key]}", font=("Arial", 12))
        y -= 25                             # Move down each stat line

    # Total count at the end
    side_t.goto(-400, y)
    side_t.write(f"Total: {sum(counts.values())}", font=("Arial", 12))

# === Draw log table area ===
def draw_table():
    log_t.clear()                           # Clear logs area
    log_t.goto(-250, 210)                   # Header position
    log_t.write("Time        Source        Severity        Message", font=("Arial", 14, "bold"))  # Column titles

    y = 180                                # Start position for rows
    for entry in logs[-10:]:               # Show only 10 latest logs
        t, src, sev, msg = entry           # Unpack entry data

        # Choose color for severity
        sev_color = {"Critical": "red", "Abnormal": "orange", "Medium": "yellow"}[sev]

        # --- Time column ---
        log_t.goto(-250, y)
        log_t.color("white")
        log_t.write(t, font=("Arial", 12))

        # --- Source column ---
        log_t.goto(-160, y)
        log_t.write(src, font=("Arial", 12))

        # --- Severity column ---
        log_t.goto(-60, y)
        log_t.color(sev_color)
        log_t.write(sev, font=("Arial", 12, "bold"))

        # --- Message column ---
        log_t.goto(40, y)
        log_t.color("white")
        log_t.write(msg, font=("Arial", 12))

        y -= 25                            # Move down one row each time

# === Add a random log entry ===
def add_log():
    now = datetime.now().strftime("%H:%M:%S")               # Current time stamp
    src = random.choice(sources)                            # Random source
    sev = random.choices(["Critical", "Abnormal", "Medium"], [2, 4, 10])[0]  # Weighted severity
    msg = random.choice(["Login fail", "Scan detected", "Suspicious file", "New admin"])  # Random event
    counts[sev] += 1                                        # Increase count
    logs.append((now, src, sev, msg))                       # Store entry

    # Keep max of 10 logs visible
    if len(logs) > 10:
        old = logs.pop(0)                                   # Remove oldest
        counts[old[2]] -= 1                                 # Adjust count

# === Initial setup draw ===
draw_title()        # Show main title
draw_sidebar()      # Draw sources and stats
draw_table()        # Draw empty table
screen.update()     # Update display

# === Main real-time loop ===
while True:
    add_log()                # Add new random log
    draw_sidebar()           # Refresh sidebar stats
    draw_table()             # Redraw table with new data
    screen.update()          # Refresh entire screen
    time.sleep(0.8)          # Short pause for readability