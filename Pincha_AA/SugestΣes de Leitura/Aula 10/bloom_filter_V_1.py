#
#   A "toy" bloom filter class
#
#   J. Madeira - November 2016
#
#   Adapted from:
#
#   The Glowing Python - A toy Bloom Filter
#  


class BloomFilter:
    """ Bloom Filter """

    def __init__(self, m, k, hash_fun):
        """
            m, size of the vector
            k, number of hash functions to compute
            hash_fun, hash function to use
        """

        self.m = m

        # initialize the vector, i.e., the Bloom Filter
        # attention: a real implementation should use an actual bit‐array

        self.vector = [0] * m

        self.k = k

        self.hash_fun = hash_fun

        self.data = {}  # data structure to store the data - not usual

        self.false_positive = 0     # for testing

    def insert(self, key, value):
        """ insert the pair (key,value) """

        self.data[key] = value

        for i in range(self.k):

            self.vector[self.hash_fun(key+str(i)) % self.m] = 1

    def contains(self, key):
        """ check if key is contained """

        for i in range(self.k):

            if self.vector[self.hash_fun(key+str(i)) % self.m] == 0:

                return False    # the key doesn't exist

        return True             # the key can be in the data set

    def get(self, key):
        """ return the value associated with key """

        if self.contains(key):

            try:
                return self.data[key]   # actual lookup

            except KeyError:

                self.false_positive += 1


def main(args):

    return 0


if __name__ == '__main__':

    import sys
    sys.exit(main(sys.argv))
