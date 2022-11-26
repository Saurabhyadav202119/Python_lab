# Write a program that return all the unique palindromes from a given string
def uniquePalindromes(string):
    x=string.split()
    # note how we put it *outside* the loop, so it persists across each iteration without being reset
    k = []  
    for i in x:
        rev= ''.join(reversed(i))
        if i.casefold() == rev.casefold():
            k.append(i.casefold())  
          
    # now, once all elements have been visited, return the set of unique elements from k
    return set(k)

print(uniquePalindromes("Elle and her friend Bob caught a Girafarig and named it ellE"))