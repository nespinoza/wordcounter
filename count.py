import numpy as np

f = open('text.txt','r')
nwords = 0
while True:
    line = f.readline()
    if line != '':
        nwords = nwords + len(line.split())
    else:
        break
print 'The text has '+str(nwords)+' words.'
