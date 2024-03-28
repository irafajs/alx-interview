#!/usr/bin/python3
"""
Shebang to create a Py script
"""


import sys
import signal

total_file_size = 0
status_code_counts = {
        200: 0,
        301: 0,
        400: 0,
        401: 0,
        403: 0,
        404: 0,
        405: 0,
        500: 0
        }
line_count = 0


def print_statistics():
    """method to handle the logs and count the status code"""
    print(f"File size: {total_file_size}")
    for code, count in sorted(status_code_counts.items()):
        if count > 0:
            print(f"{code}: {count}")


def signal_handler(sig, frame):
    """method to handle the system signal"""
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)
for line in sys.stdin:
    line = line.strip()
    parts = line.split()
    if len(parts) == 9 and parts[4] == "\"GET" and parts[5].startswith(
            "/projects/") and parts[7].isdigit():
        status_code = int(parts[7])
        file_size = int(parts[8])
        total_file_size += file_size
        status_code_counts[status_code] += 1
        line_count += 1
        if line_count % 10 == 0:
            print_statistics()
    else:
        continue
print_statistics()
