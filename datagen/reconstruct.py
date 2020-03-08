import os

dirs = os.listdir('data')

data = []
for d in dirs:
	fs = os.listdir('data/' + d)
	for f in fs:
		with open('data/' + d + '/' + f) as fd:
			data.append(fd.read())


with open('master.csv', 'w') as f:
	f.write('\n'.join(data))
