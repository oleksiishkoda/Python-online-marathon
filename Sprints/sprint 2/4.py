import re
stri = "Thisssssssss isisisis echooooooo stringggg. Replaceaceaceace repeatedededed groupssss of symbolssss"
pattern = r'(.+)(?=.+\1)'
lst = re.split(r' ', stri)
for i in range(len(lst)):
    lst[i] = re.sub(pattern, r'', lst[i])
res = " ".join(lst)
print(res)
(,\s[0-9]{1,4}){4},\s[0-9]{1,3}\.[0-9]

