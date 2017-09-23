import math as m

'''
the function conditional_entropy() accepts an n-gram data structures as an input
that are dictionaries with words/word pairs as keys and the probabilities
of these words/word pairs as values

always test your code
'''

def conditional_entropy(two_gram,one_gram):
    '''
    the phrase under consideration is 'Y X'
    therefore when you split the key into words use the correct order
    y,x = key.split()
    '''
    ent = 0.
    for key in two_gram:
        y,x = key.split()
        ent -= two_gram[key]*m.log(two_gram[key],2)
#	raise NotImplementedError

    for key in one_gram:
        ent += one_gram[key]*m.log(one_gram[key],2)
    return ent

def test_conditional_entropy():
    raise NotImplementedError
    return

if __name__ == "__main__":
    test_conditional_entropy()
