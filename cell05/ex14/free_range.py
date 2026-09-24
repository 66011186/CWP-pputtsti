#!/usr/bin/env python3
import sys

# Check if exactly two arguments were passed
if len(sys.argv) != 3:
    print("none")
else:
    try:
        start = int(sys.argv[1])
        end = int(sys.argv[2])
        
        # Handle ranges where start is smaller or larger than end
        if start <= end:
            arr = list(range(start, end + 1))
        else:
            arr = list(range(start, end - 1, -1))
            
        print(arr)
    except ValueError:
        print("none")