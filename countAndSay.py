import re
n = 5
#(1) 1 -> "one 1" -> 11
#(2) 11 -> "two 1s" -> 21
#(3) 21 -> "one 2, then one 1" -> 1211
#(4) 1211 -> 111221
#(5) 111221 -> 312211
#(6) 312211 -> 13112221 -> 1113213211 -> 31131211131221

s = '1'
for _ in range(n-1):
    s = re.sub(r'(.)\1*', lambda m: str(len(m.group(0))) + m.group(1),s)
    print(s)
print(s)