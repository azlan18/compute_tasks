import math
import os
import random
import re
import sys
from collections import Counter

if __name__ == '__main__':
    s = input().strip()

    # Count the occurrences of each character
    char_count = Counter(s)

    # sorting the characters in descending order of occurrence count and then alphabetically
    sorted_chars = sorted(char_count.items(), key=lambda x: (-x[1], x[0]))

    # printing the top three characters with their occurrence count
    for char, count in sorted_chars[:3]:
        print(char, count)
