import subprocess

for i in range(100):
	subprocess.run(['python3', 'main.py'])
	print("done with round " + str(i))
