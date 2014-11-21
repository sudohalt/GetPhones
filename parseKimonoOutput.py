fd = open('kimonoOutput.txt');
k = []
for i in fd:
	k.append(i.split('phones')[0][1:].replace(' ', ''))
print k
