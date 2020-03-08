with open('data.csv') as f:
	t = f.readlines()

clean = []
count = 0
for item in t:
	for inner_item in t:
		if item == inner_item:
			print('COPY OF ' + item)
			count += 1
		else:
			clean.append(item)

with open('clean.csv', 'w') as f:
	f.write('\n'.join(clean))
print(count)
