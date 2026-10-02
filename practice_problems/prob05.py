"""
Problem #5:

Post Completion Reflections:
    - python can be really complicated for no effing reason
    
This is your coding interview problem for today. This problem was asked by Jane Street.

cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair. For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

Given this implementation of cons:

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair
Implement car and cdr.

We will be sending the solution tomorrow, along with tomorrow's question. As always, feel free to shoot us an email if there's anything we can help with.

Have a great day!
"""

# =========================== Your Solution Below ========================== #

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair


def car(thing):
    """
    thing should be the output of cons...
    """
    return thing(lambda a, b: a)
    

def cdr(thing):
    """
    """
    return thing(lambda a, b: b)


# =========================== Your Solution Above ========================== #

def test_case():
    """
    """
    assert car(cons(4, 3)) == 4
    assert cdr(cons(4, 3)) == 3

if __name__ == "__main__":
    test_case()

"""
Their Solution:

"""