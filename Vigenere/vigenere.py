#!/usr/bin/env python3
from itertools import cycle


inputText = "DUPA dasd 2 3sd s";
code="auguste"
tableCode ="KERCKHoFF"

    
    
    
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
inputText = ''.join([i for i in inputText if i.isalpha()]).upper()
tableCode = tableCode.upper()
code=''.join([j for i,j in enumerate(code) if j not in code[:i]]).upper()

codeAlphabet=code

for letter in alphabet:
    if letter not in code:
        codeAlphabet+=letter

alphabetTable =[]
for letter in tableCode:
    idxLetter = codeAlphabet.find(letter)
    alphabetTable.append(codeAlphabet[idxLetter:] + codeAlphabet[:idxLetter])

alphabetCycle = cycle(alphabetTable)

encode = ""
decode = ""
for letter in inputText:
    thisAlphabet = next(alphabetCycle)
    idx = alphabet.find(letter)
    encode += thisAlphabet[idx]
    idx = thisAlphabet.find(letter)
    decode += alphabet[idx]

print(encode)
print(decode)

    
