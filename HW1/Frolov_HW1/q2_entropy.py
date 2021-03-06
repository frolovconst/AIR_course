import math as m

'''
the function entropy() accepts an n-gram data structure as an input
that is a dictionary with words of the vocabulary as keys and the probabilities
of these words as values

always test your code
'''

def entropy(one_gram):
    ent = 0.
    for key in one_gram:
        ent -= one_gram[key]*m.log(one_gram[key],2)
#	raise NotImplementedError
#        use m.log(val,2) for computing logarithm
    return ent

def test_entropy():
#    raise NotImplementedError
    return

if __name__ == "__main__":
    test_entropy()
