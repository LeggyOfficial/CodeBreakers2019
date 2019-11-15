#!/usr/bin/env python3
from itertools import cycle

originalstrips = [
'AMYHEDQBOUSWKJGTLXZRIPNVCF',
'BVLJXHDNTGUIFARESZKPWYCMQO',
'CTNJEYDXIAOWQHZGBPUKMFVLRS',
'DMWNQXCEYBSPJRVHLFGOIKAZUT',
'EINCPGSDMJHFWXRUZLOQBVYATK',
'FEJAPBQCLMYRUDKGOIWZHSNXVT', 
'GRACKEYILBFNQTWHVUZJOSMPDX',
'HEGOCWUYXNTFMVDBZLJQPAIRSK',
'IXUTDHQZPYWBRVNGJMSAKLCOEF',
'JCRHWKBXLSYNEUAFGPIDTVQMOZ'
]

codeName = 'GJEIBDAHCF'

formingNumber = 7

inputText = 'GDOQCIXTAXUCDLPDLZHEWGUIKZTEWAQJIJBDXLTYACDAMFTYWVZRDLEVKYGJRNJHRRMEMLLZJCAVEOXLOYDMFVWSXVKYDAIJCBZP'


strips = []

for i in codeName:
    for strip in originalstrips:
        if strip[0] == i:
            strips.append(strip)


inputText = ''.join([i for i in inputText if i.isalpha()]).upper()

outputText=''
stripCycle = cycle(strips)
for letter in inputText :
    thisStrip = next(stripCycle)
    idx = thisStrip.find(letter)
    outputText = outputText + thisStrip[(idx-formingNumber+26)%26]
print(outputText)

