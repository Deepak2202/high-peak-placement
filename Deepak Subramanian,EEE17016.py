# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15Y8JDruqkZPNUSMxh1-2aHnifvYDWCWl
"""

inp = open("sample_input.txt", "r")
gd={}
for lc,x in enumerate(inp):
  if lc==0:
    nemp=int(x.split()[-1])
  if lc>3:
    gd[x.split(':')[0]]=int(x.split()[-1])
    #gd.append(int(x.split()[-1]))
print(nemp)
print(gd)
temp=sorted(gd.values())
ngd={}
for i in temp:
  for k in gd.keys():
    if gd[k]==i:
      ngd[k]=gd[k]
print(ngd)
up=len(ngd)-1
lw=up-nemp
key=list(ngd.keys())
val=list(ngd.values())
min=val[up]-val[lw]
while lw>0:
  if min>val[up]-val[lw]:
    min=val[up]-val[lw]
    pup=up
  up=up-1
  lw=lw-1
print(val[pup]-val[pup-nemp+1],val[pup],key[pup])
ofile=open("sample_output.txt",'a')
ofile.write("The goodies selected for distribution are:\n")
ofile.write("\n")
for k in range(pup-nemp+1,pup+1):
  temp=key[k]+':'+str(val[k])+'\n'
  ofile.write(temp)
ofile.write("\n")
temp="And the difference between the chosen goodie with highest price and the lowest price is "+str(val[pup]-val[pup-nemp+1])
ofile.write(temp)





