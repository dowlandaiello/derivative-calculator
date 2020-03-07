from sympy import *
from random import randint
import numpy as np

x = Symbol('x')

# return a random coefficient.
def coeff():
	return randint(-10000, 10000)

# generate a tuple of a polynomial and its derivative (as strings).
def gen_random_polynomial():	
	f = (coeff()*x**2) + (coeff()*x) + (coeff())
	f_prime = f.diff(x)
	return (str(f), str(f_prime))

# thread-ready method to generate multiple f-f' pairs and write to disk.
def gen_multiple(count, output_file):
	funcs = np.empty(shape=(count, 2), dtype=object) # using np fixed-size array b/c O(1) insertion
	for i in range(count):
		new_func = gen_random_polynomial()
		funcs[i][0] = new_func[0] # f
		funcs[i][1] = new_func[1] # f'
	
	# write to disk
	np.savetxt('data/' + output_file + '.csv', funcs, delimiter=',')
	return funcs

gen_multiple(1000, "set1")
