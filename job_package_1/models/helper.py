# -*- coding: utf-8 -*-

def find_dynamic_tags(s, a, b): 

	res = list()
	ls = len(s) 
	la = len(a) 
	lb = len(b)

	x = [0] * ls 
	y = [0] * ls 

	for i in range(ls): 
		
		if (s[i: la + i] == a): 
			x[i] = 1
		if (s[i: lb + i] == b): 
			y[i] = 1
	hash = [] 
	curr_substr = "" 
	for i in range(ls): 
	
		if (x[i]): 
			for j in range( i, ls): 
				if (not y[j]): 
					curr_substr += s[j] 
				if (y[j]):				
					curr_substr += s[j: lb + j] 
					if curr_substr not in hash: 
						if curr_substr.count(a) == 1:
							res.append(curr_substr)
					hash.append(curr_substr) 

			curr_substr = "" 
	return res