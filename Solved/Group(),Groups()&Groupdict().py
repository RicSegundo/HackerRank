import re

line_0 = '..12345678910111213141516171820212223'

string = re.search(r"([a-zA-Z0-9])\1+", line_0.strip())
print(string.group(1) if string else -1)

