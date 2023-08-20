string1 = input()
string2 = input()

res1 = ""
res2 = ""

for i in range(len(string1)):
    if (string1[i] != '#'):
        res1 += string1[i]
    else:
        res1 = res1[:-1]

for i in range(len(string2)):
    if (string2[i] != '#'):
        res2 += string2[i]
    else:
        res2 = res2[:-1]


print(res1)
print(res2)