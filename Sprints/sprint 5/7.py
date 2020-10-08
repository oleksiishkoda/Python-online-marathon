import re
stri = "ownsite@our.c0m"
pattern = r"^[a-zA-Z0-9._]+@[a-z.]+\.com$"
print(re.findall(pattern, stri))
