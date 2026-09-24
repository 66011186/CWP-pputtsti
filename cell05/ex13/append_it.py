#!/usr/bin/env python3
import sys

# Check if any arguments were passed (excluding the script name itself)
if len(sys.argv) < 2:
    print("none")
else:
    for arg in sys.argv[1:]:
        # If the word does NOT end with "ism", append "ism" and print
        if not arg.endswith("ism"):
            print(f"{arg}ism")