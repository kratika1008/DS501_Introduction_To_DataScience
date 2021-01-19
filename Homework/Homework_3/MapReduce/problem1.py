from mrjob.job import MRJob
#-------------------------------------------------------------------------
'''
    Problem 1:
    In this problem, you will get familiar with the mapreduce framework.
    Please install the following python package:
        * mrjob
    MrJob is the library for writing Python programs that run on Hadoop.
    To install mrjob using pip, you could type `pip3 install mrjob` in the terminal.
    Alternatively, you could install from source code:
        (1) download source code from: https://github.com/Yelp/mrjob
        (2) in the code folder, type "python3 setup.py install" in the terminal.


    Cards Dataset:
    Suppose we have a dataset of cards (cards.txt), each line represents a card.
    For example, "H8" means that the suit of the card is "Heart" and the number on the card is 8.
    "S1" means that the suit of the card is "Spade" and the number on the card is A.
    Now we want to summarize the statistics of the cards using map-reduce framework.
'''

#--------------------------------------------------------------------------------------
class CardsSuitCount(MRJob):
    '''
        Count the number of cards in each suit.
        In the dataset (cards.txt), the input to each mapper is a line of text string (one card):
          KEY, VALUE
        --------------
         null, "H1"             (which means that this card is a "Heart" with number 1)
         null, "H2"
         null, "S1"             (which means that this card is a "Spade" with number 1)
         null, "D4"
         ...

        The outputs of the reducers should be:
          KEY, VALUE
        --------------
          "H", 10         (which means that there are 10 cards with suit "Heart")
          "D", 11
          "S", 12         (which means that there are 12 cards with suit "Spade")
          "C", 13
    '''
    #----------------------
    def mapper(self, in_key, in_value):
        '''
            Mapper function, which process a key-value pair in the data and generate intermediate key-value pair(s).
            Input:
                    in_key: the key of a data record, in this case, is an empty value (null), which can be ignored
                    in_value: the value of a data record, in this example, it is a line of text string in the dataset.
            Yield:
                    (out_key, out_value) :intermediate key-value pair(s).
            Hint: to generate an output key-value pair, you need to use "yield" instead of "return".
        '''
        #########################################
        ## INSERT YOUR CODE HERE
        yield in_value[:1], 1
        #########################################


    #----------------------
    def reducer(self, in_key, in_values):
        '''
            reducer function, which processes a key and value list and produces output key-value pair(s)
            Input:
                    in_key: an intermediate key.
                    in_values: the python list of values associated with the intermediate key.
            Yield:
                    (out_key, out_value) : output key-value pair(s).
                                          In this example, the out_key is the suit, "H", "D", "C" or "S",
                                          and out_value is the count of cards with the same suit, an integer value
            Hint: to generate an output key-value pair, you need to use "yield" instead of "return".
        '''
        #########################################
        ## INSERT YOUR CODE HERE
        yield in_key, sum(in_values)
        #########################################


        ''' TEST: Now you can test the correctness of your code above by typing `nosetests -v test1.py:test_SuitCount' in the terminal.  '''




#--------------------------------------------------------------------------------------
class CardsSuitSum(MRJob):
    '''
        Compute the sum of all card numbers in each suit.
        For example, in the dataset (cards.txt), the input to each mapper is a line of text string (one card):
          KEY, VALUE
        --------------
         null, "H1"             (which means that this card is a "Heart" with number 1)
         null, "H2"
         null, "S1"             (which means that this card is a "Spade" with number 1)
         null, "D4"
         ...


        The result should be:
          KEY, VALUE
        --------------
          "H", 55         (which means that the sum of H1 + H2 + ...+ H10 = 55 with suit "Heart")
          "D", 66
          "S", 78         (which means that the sum of S1 + S2 + ...+ S12 = 78 with suit "Spade")
          "C", 91
    '''
    #----------------------
    def mapper(self, in_key, in_value):
        '''
            Mapper function, which process a key-value pair in the data and generate intermediate key-value pair(s).
            Input:
                    in_key: the key of a data record, in this case, is an empty value, which can be ignored
                    in_value: the value of a data record, (in this example, it is a line of text string in the dataset)
            Yield:
                    (out_key, out_value) :intermediate key-value pair(s).
        '''
        #########################################
        ## INSERT YOUR CODE HERE
        n = len(in_value)
        yield in_value[:1], int(in_value[1:n])
        #########################################


    #----------------------
    def reducer(self, in_key, in_values):
        '''
            reducer function, which processes a key and value list and produces output key-value pair(s)
            Input:
                    in_key: an intermediate key.
                    in_values: the python list of values associated with the intermediate key.
            Yield:
                    (out_key, out_value) : output key-value pair(s).
                                          In this example, the out_key is the suit, "H", "D", "C" or "S",
                                          and out_value is the sum of numbers of cards with the same suit, an integer value
        '''
        #########################################
        ## INSERT YOUR CODE HERE
        yield in_key, sum(in_values)
        #########################################


        ''' TEST: Now you can test the correctness of your code above by typing `nosetests -v test1.py:test_SuitSum' in the terminal.  '''


#--------------------------------------------------------------------------------------


class CardsNumberCount(MRJob):
    '''
        Count the number of cards with the same number in the card.
        For example, in the dataset (cards.txt), the input to each mapper is a line of text string (one card):
          KEY, VALUE
        --------------
         null, "H1"             (which means that this card is a "Heart" with number 1)
         null, "H2"
         null, "S1"             (which means that this card is a "Spade" with number 1)
         null, "D4"
         ...

        The outputs of the reducers should be:
          KEY, VALUE
        --------------
          "1", 4         (which means that there are 4 cards with number "1", because we have 4 suits)
          "2", 4         (which means that there are 4 cards with number "2")
          "3", 4
            ...
         "10", 4
         "11", 3
         "12", 2
         "13", 1
    '''
    #----------------------
    def mapper(self, in_key, in_value):
        '''
            Mapper function, which process a key-value pair in the data and generate intermediate key-value pair(s).
            Input:
                    in_key: the key of a data record, in this case, is an empty value, which can be ignored
                    in_value: the value of a data record, (in this example, it is a line of text string in the dataset)
            Yield:
                    (out_key, out_value) :intermediate key-value pair(s).
        '''
        #########################################
        ## INSERT YOUR CODE HERE
        n = len(in_value)
        yield in_value[1:n], 1
        #########################################


    #----------------------
    def reducer(self, in_key, in_values):
        '''
            reducer function, which processes a key and value list and produces output key-value pair(s)
            Input:
                    in_key: an intermediate key.
                    in_values: the python list of values associated with the intermediate key.
            Yield:
                    (out_key, out_value) : output key-value pair(s).
                                          In this example, the out_key is the number on the card, "1", "2", "3" ... or "10",
                                          and out_value is the count of cards with the same "number", an integer value
        '''
        #########################################
        ## INSERT YOUR CODE HERE
        yield in_key, sum(in_values)
        #########################################


        ''' TEST: Now you can test the correctness of your code above by typing `nosetests -v test1.py:test_NumberCount' in the terminal.  '''



#--------------------------------------------

''' TEST Problem 1:
        Now you can test the correctness of all the above functions by typing `nosetests -v test1.py' in the terminal.

        If your code passed all the tests, you will see the following message in the terminal:
            ----------- Problem 1 (15 points in total)-------------- ... ok
            (5 points) SuitCount ... ok
            (5 points) SuitSum ... ok
            (5 points) NumberCount ... ok
            ----------------------------------------------------------------------
            Ran 4 tests in 0.090s
            OK
'''

#--------------------------------------------
