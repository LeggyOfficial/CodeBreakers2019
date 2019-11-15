#!/usr/bin/env python3
from itertools import cycle

originalstrips = [
'AONJFXSKMRGUIPTWEBQVZYCHLD',
'BIHPFJQGOERSNDMCATKUVWYZLX',
'CHQJAOMESPRYLNZUVXGFBDIWTK',
'DZRQPVXWIFKAOUBCMYLESNJTHG',
'ECKAYRUTWNFVODISZLQJMPBXGH',
'FDTYHNJXOKALEVWMQGSUBRZICP',
'GUIWKQAHRFYTVCXJEDBOLNZPMS',
'HOMVEZBRCIGYDXLFKTQUJNAPSW',
'IQTGAJNPROBCEVMUKDWSZYHFXL',
'JEDQMVFYISOARZHGWLCNBKUTPX'
]

codeName = 'DJHIBFAGEC'

formingNumber = 12

inputText = 'WARNING ENEMY ARE GOING TO BLOW UP THE BRIDGE SEND RANGERS'


strips = []

for i in codeName:
    for strip in originalstrips:
        if strip[0] == i:
            strips.append(strip)


inputText = ''.join([i for i in inputText if i.isalpha()]).upper()
modulo = len(inputText)%len(codeName)
if(modulo != 0):
    inputText = inputText + (len(codeName)-modulo)*'X'

outputText=''
stripCycle = cycle(strips)
for letter in inputText :
    thisStrip = next(stripCycle)
    idx = thisStrip.find(letter)
    outputText = outputText + thisStrip[(idx+formingNumber)%26]
print(outputText)

