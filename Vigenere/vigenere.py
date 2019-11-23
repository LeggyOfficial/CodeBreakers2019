#!/usr/bin/env python3
from itertools import cycle


inputText = "kerckhoffs viewed cryptography as a rival to, and a better alternative than, steganographic encoding";
inputText = "USEJWWUVNWORJDTPWWFNOVVSGSIAKMYARQFGJALMKEMDOSFSXYAACISNKPGJGDSXJMONIXDI"
code=""
tableCode ="blaise"

    
    
    
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
inputText = ''.join([i for i in inputText if i.isalpha()]).upper()
tableCode = tableCode.upper()
code=''.join([j for i,j in enumerate(code) if j not in code[:i]]).upper()

print(inputText)
codeAlphabet=code
for letter in alphabet:
    if letter not in code:
        codeAlphabet+=letter
print(codeAlphabet)

alphabetTable =[]
for letter in tableCode:
    idxLetter = codeAlphabet.find(letter)
    alphabetTable.append(codeAlphabet[idxLetter:] + codeAlphabet[:idxLetter])

print(alphabet)
for alpha in alphabetTable:
	print(alpha)

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

    
