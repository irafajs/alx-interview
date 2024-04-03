#!/usr/bin/python3
"""
Shebang to create a PY script
"""


def validUTF8(data):
    """method to check if data argument passed is utf encoded"""
    num_following_bytes = 0

    for byte in data:
        if num_following_bytes == 0:
            if byte >> 7 == 0b0:
                continue
            elif byte >> 5 == 0b110:
                num_following_bytes = 1
            elif byte >> 4 == 0b1110:
                num_following_bytes = 2
            elif byte >> 3 == 0b11110:
                num_following_bytes = 3
            else:
                return False
        else:
            if byte >> 6 != 0b10:
                return False
            num_following_bytes -= 1

    return num_following_bytes == 0
