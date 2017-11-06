import string

def is_pangram(str):
	str = list(set(''.join(sorted(str.lower()))))	
	alpha=list(string.ascii_lowercase)
	return all(x in str for x in alpha)
