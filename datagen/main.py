from sympy import *
import numpy as np
import os, threading, hashlib, datetime, random

def get_rand():
	time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S:%f')
	m = hashlib.md5()
	m.update(time.encode())
	return str(m.hexdigest())[0:8]

TCOUNT = 12    # AMOUNT OF THREADS
FCOUNT = 10000 # AMOUNT OF FUNC GENS PER THREAD

data_dir = 'data/' + get_rand() + '/'

os.system('mkdir -p ' + data_dir)

x = Symbol('x')

# return a random coefficient.
def coeff():
	return random.randint(-10000, 10000)

# generate a tuple of a polynomial and its derivative (as strings).
def gen_random_polynomial():	
	f = (coeff()*x**2) + (coeff()*x) + (coeff())
	f_prime = f.diff(x)
	return (str(f).replace(' ', ''), str(f_prime).replace(' ', ''))

# thread-ready method to generate multiple f-f' pairs and write to disk.
def gen_multiple(count, index):
	funcs = np.empty(shape=(count, 2), dtype=object) # using np fixed-size array b/c O(1) insertion
	for i in range(count):
		new_func = gen_random_polynomial()
		funcs[i][0] = new_func[0] # f
		funcs[i][1] = new_func[1] # f'
	
	# write to disk
	np.savetxt(data_dir + "set" + str(index) + '.csv', funcs, delimiter=',', fmt='%s')
	return funcs

# for i in range(10):
# 	gen_multiple(10000, i)

threads = []
for i in range(TCOUNT):
	threads.append(threading.Thread(
		target=gen_multiple,
		args=(FCOUNT, i)
	))

for thread in threads:
	thread.start()
