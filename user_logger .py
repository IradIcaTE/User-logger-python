# user_logger.py

import sys

# Get command line arguments
username = sys.argv[1]
email = sys.argv[2]

# Print or process them
print(f"Received Username: {username}")
print(f"Received Email: {email}")

# Optionally write to a file
with open("user_log.txt", "a") as f:
    f.write(f"Username: {username}, Email: {email}\n")
