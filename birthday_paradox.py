# Provides brute-force calculation for the probabilty of same-birthday 
# occurances in a group of arbitrary number of people. 
# (Birthday paradox: http://en.wikipedia.org/wiki/Birthday_problem)
# Inspired by http://www.weibo.com/2313291734/zvARF0tdX
# Github @hktang

import random, collections

def rand_date():
	'''Generate a random date with mm/dd format.'''
	m = random.randint(1, 12)
	d = random.randint(1, 31)
	o = "%02d/%02d" % (m, d)
	if (o != "02/30" and o != "02/31" and o != "04/31" and o != "06/31" 
	   and o != "09/31" and o != "11/31"):
		return o
	else:
		return rand_date()

def generate_rand_dates(i):
	'''Generate a list holding i random dates.'''
	date_list = []
	for n in range(i):
		date_list.append(rand_date())
	return date_list

def have_same_date(i):
	'''For a random list consisting of i dates, return 1 if one duplicate found
	and 0 otherwise.'''
	dates = generate_rand_dates(i)
	dates_counter = collections.Counter(dates)
	dups = [x for x in dates_counter if dates_counter[x] > 1]
	if len(dups) > 0:
		return 1
	else: 
		return 0

def force_calc_probability(x, y):
	'''For x students in a class, randomize their birthdays by y times 
	(y should reasonably big!) and return the same-birthday probability.'''
	hit = [];
	for i in range(y):
		r = have_same_date(x)
		hit.append(r)
	c = collections.Counter(hit)
	probability = float(c[1])/float(len(hit))
	print probability
	
# Uncomment the last line to run. Warnning! RAM hog below. 
# Run at your own risk. Or consider reducing y.

#force_calc_probability(23,50000)