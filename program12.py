# Python program to print all permutations 

def toString(List):
	return ''.join(List)

# Function to print permutations of string
# This function takes three parameters:
# 1. String
# 2. Starting index of the string
# 3. Ending index of the string.
def permute(s, s_index, length):
	if s_index==length:
		print (toString(s))
	else:
		for i in range(s_index,length):
			s[s_index], s[i] = s[i], s[s_index]
			permute(s, s_index+1, length)
			s[s_index], s[i] = s[i], s[s_index] # backtrack

# Driver program to test the above function
string = "ANT"
n = len(string)
a = list(string)
permute(a, 0, n)