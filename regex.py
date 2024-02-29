#ex1
import re
with open("row.txt") as file:
    word=file.read()
print(re.findall("a.*b",word))

#ex2
import re
with open("row.txt") as file:
    word=file.read()
print(re.findall("a.*bb",word))

#ex3
import re
with open("row.txt") as file:
    word=file.read()
print(re.findall("[a-z]_+[a-z]",word))

#ex4
import re
with open("row.txt") as file:
    word=file.read()
print(re.findall("[A-Z][a-z]+",word))

#ex5
import re
with open("row.txt") as file:
    word=file.read()
print(re.findall("a+.b",word))

#ex6
import re
with open("row.txt") as file:
    word=file.read()
pattern=r'[ ,.]'
print(re.sub(pattern,":",word))

#ex7
import re
with open("forex7.txt") as file:
    word=file.read()
print(re.sub(r"_","",word))

#ex8
import re

with open("forex8.txt") as file:
    word = file.read()
print(re.findall(r"[A-Z][^A-Z]*",word))

#ex9
import re
with open("forex9.txt") as file:
    word = file.read()
find=re.findall(r'[A-Z][a-z]*',word)
print(' '.join(find)) 

#10
import re
with open("forex10.txt") as file:
    words=file.read()
cnt='_'
for i in words:
    if i>='A' and i<='Z':
        cnt+='_'
    cnt+=i
print(cnt)
