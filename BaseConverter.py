# 33377223 26677 333328333366 444777 80004444447 4441113333

# A test case that I used
ls = ["33377223","26677","333328333366","444777","80004444447","4441113333"]

# Converts a single digit to an equivalent character
def dig_to_char(n):
    if n < 10:
    	return chr(n + ord('0'))
    else:
    	return chr(n - 10 + ord('a'))


# Converts a number in decimal to a number in a given base (returns a string)
def str_base(n,b):
    if number < 0:
        return '-' + str_base(-n,b)
    else:
        (d,r) = divmod(n,b)
        if d == 0: # d == 0, the we have reached the end
            return dig_to_char(r)
        else: # d != 0
            return str_base(d,b) + dig_to_char(r) # we build the result from the right most digit


# Given a number in string format, its original base in integer
# Returns the number in its desired new base
def base_converter(s,ob,nb):
	temp = int(s,ob)
	rv = str_base(temp,nb)
	return rv


# Similar to base_converter, but handles a list of intergers in string
# And retruns a list of strings
def ls_base_converter(ls,ob,nb):
	rv = range(0,len(ls))
	i = 0
	for num in ls:
		rv[i] = base_converter(num,ob,nb)
		i = i + 1
	return rv

# print(ls_base_converter(ls,9,10))

# For my purpose, I wanted to see the outputs of a list of integers (in strings)
# In different combinations of original bases and new bases
# ob_l is the lowest possible value for the base of ob
# ob_u is the highest possible value for the base of ob
# The same applies to nb, and the function will print the results

def print_nbs(ls,ob_l,ob_u,nb_l,nb_u):
	for a in range(ob_l,ob_u+1):
		for b in range(nb_l,nb_u+1):
			print("Orginal Base: " + str(a) + "  New Base: " + str(b))
			print(ls_base_converter(ls,a,b))

# print_nbs(ls, 9, 10, 16, 36)

# tested
# 9,16 -> 13,36
# 9,20 -> 36,48
# 16,36 -> 13,36

# Possibility
# 11 -> 31  4th pos: noom
# 11 -> 27  5th pos: jmgeaeci
# 11 -> 28  6th pos: ledmemh