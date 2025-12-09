import random                                         # create random numbers
# ---- Colors for clean output ----
RED = "\033[91m"                                      # shows red text for critical
YELLOW = "\033[93m"                                   # yellow for high
BLUE = "\033[94m"                                     # blue for medium
GREEN = "\033[92m"                                    # green for low
RESET = "\033[0m"                                     # resets back to normal text color
# ---- Makes new numbers change randomly for activities ----
events = [random.randint(0, 250) for _ in range(10)]  # makes 10 random numbers between 0–250
# ---- Find the average (normal base) ----
average = sum(events) / len(events)                   # adds all numbers and divides by how many there are
# ---- Decides what severity level each number is ----
def classify(n):                                      # n means the event number we are checking
    if n > average * 2:                               # if it's more than double the normal amount
        return RED + "CRITICAL" + RESET               # show red alert
    if n > average:                                   # if it's above the normal amount
        return YELLOW + "HIGH" + RESET                # show high alert
    if n > 20:                                        # if it's more than 20
        return BLUE + "MEDIUM" + RESET                # show medium activity
    return GREEN + "LOW" + RESET                      # otherwise, it's low activity & green
# ---- Prints results in a small clean report ----
print("\n=============== ACTIVITY REPORT ===============\n")    # title box
print(f"Total Records : {len(events)}")                         # how many activity numbers we generated
print(f"Average Value : {average:.1f}\n")                       # show the baseline average
print("--------------- Details -----------------------")        # section header
# ---- Show each number with its severity rating ----
for n in events:                                                # loop through every event number
    print(f"Events: {n:>3}  →  {classify(n)}")                  # show the number and its color label
print("\n================================================\n")   # ends report