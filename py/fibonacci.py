class Fibonacci(object):
    """This is a simple fibonacci generator, called implicitly by __iter__()
    example: 
    >>> for x in Fibonacci(5):
            print(X)
    >>> 0
        1
        1
        2
        3
    """
    def __init__(self, count):

        self.count = count

    def __iter__(self):

        a, b = 0, 1

        for x in range(self.count):

            if x < 2:

                yield x

            else:

                c = a + b

                yield c

                a, b = b, c