# https://stepik.org/lesson/24470/step/7?unit=6776
import re
import sys

for line in sys.stdin:
    line = line.rstrip()
    if len(re.findall(r'cat', line)) > 1:
        print(line)