import pandas as pd                 # For reading and manipulating CSV logs
import tkinter as tk                # For GUI window
from tkinter import ttk             # For table widget
from datetime import datetime       # For timestamp handling
# --- Load CSV logs ---
data_file = r"C:/Users/l3gac/OneDrive/Desktop/Python_Scripts_Practice!/data/simulated_logs.csv"  # Path to CSV
logs = pd.read_csv(data_file)                   # Read CSV into DataFrame
logs['timestamp'] = pd.to_datetime(logs['timestamp'])  # Convert timestamp to datetime

# --- Define severity colors ---
def get_row_color(event_type):
    if event_type == 'MalwareAlert':              # Critical
        return '#FF6961'                         # Red
    elif event_type == 'FailedLogin':            # Abnormal
        return "#F8DC3D"                         # Gold
    else:                                        # Normal
        return '#90EE90'                         # Green
# --- Add severity for sorting ---
severity_order = {'MalwareAlert': 1, 'FailedLogin': 2, 'LoginSuccess': 3}
logs['severity'] = logs['event_type'].map(severity_order)  # Map severity
logs = logs.sort_values('severity')                         # Sort by severity

# --- Tkinter GUI setup ---
root = tk.Tk()                        # Create window
root.title("Log Parse Analyzer")       # Window title
root.geometry("750x500")              # Window size
root.configure(bg="black")            # Make entire window background black

# --- Labels for summary with readable text ---
tk.Label(root, text=f"Total Logs: {len(logs)}", bg="black", fg="white").pack(anchor='w', padx=10)
tk.Label(root, text=f"Critical Events: {len(logs[logs['event_type']=='MalwareAlert'])}", bg="black", fg='red').pack(anchor='w', padx=10)
tk.Label(root, text=f"Abnormal Events: {len(logs[logs['event_type']=='FailedLogin'])}", bg="black", fg='gold').pack(anchor='w', padx=10)

# --- Dark Treeview/Table setup ---
style = ttk.Style()
style.theme_use("default")
style.configure("Treeview",
                background="black",     # Table background
                foreground="white",     # Default text color (will be overridden by row tags)
                fieldbackground="black",
                rowheight=25)
style.map("Treeview",
          background=[("selected", "gray")],  # Highlighted row color
          foreground=[("selected", "white")])
# --- Table setup ---
tree = ttk.Treeview(root, columns=list(logs.columns[:-1]), show='headings')  # Exclude 'severity'
for col in logs.columns[:-1]:
    tree.heading(col, text=col)                    # Column headers
    tree.column(col, width=150, anchor='center')   # Column width & center text
# --- Insert rows with color ---
for _, row in logs.iterrows():
    tree.insert('', 'end', values=list(row[:-1]), tags=(row['event_type'],))  # Skip 'severity' column
# --- Apply colors for events with readable text ---
for event in logs['event_type'].unique():
    tree.tag_configure(event, background=get_row_color(event), foreground='black')  # All text black for readability
tree.pack(expand=True, fill='both')      # Fill window with table
# --- Run GUI ---
root.mainloop()                           # Keep GUI running