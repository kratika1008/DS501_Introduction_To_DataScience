from problem1 import *
import sys
import numpy as np

'''
    Unit test 1:
    This file includes unit tests for problem1.py.
    You could test the correctness of your code by typing `nosetests -v test1.py` in the terminal.
'''

#-------------------------------------------------------------------------
def test_terms_and_conditions():
    ''' Read and Agree with Terms and Conditions'''
    assert Terms_and_Conditions() # require reading and agreeing with Terms and Conditions. 


#-------------------------------------------------------------------------
def test_python_version():
    ''' ----------- Problem 1 (30 points in total)--------------'''
    assert sys.version_info[0]==3 # require python 3 (instead of python 2)


#-------------------------------------------------------------------------
def test_compute_EA():
    '''(10 points) compute_EA'''

    # call the function
    EA = compute_EA(RA=100., RB=100.)

    # test whether or not EA is a float number 
    # assert type(EA) == float 

    # check the correctness of the result 
    assert EA == 0.5 
    
    #-------------------------
    # test another example
    EA = compute_EA(RA=100., RB=500.) 
    # check the correctness of the result 
    assert np.allclose(EA, 1.0/11)

    # test another example
    EA = compute_EA(RA=500., RB=100.)

    # check the correctness of the result 
    assert EA == 1./1.1

#-------------------------------------------------------------------------
def test_update_RA():
    '''(10 points) compute_RA'''

    # call the function
    RA_new = update_RA(RA=100., SA=1., EA=1.)

    # test whether or not EA is a float number 
    # assert type(RA_new) == float 

    # check the correctness of the result 
    assert RA_new == 100 
 
    # test another example
    RA_new = update_RA(RA=100., SA=0., EA=0.)
    assert RA_new == 100 

    # test another example
    RA_new = update_RA(RA=100., SA=1., EA=0.)
    assert RA_new == 116 

    # test another example
    RA_new = update_RA(RA=100., SA=0., EA=1.)
    assert RA_new == 84

    # test another example
    RA_new = update_RA(RA=100., SA=0., EA=1., K = 32)
    assert RA_new == 68.

    # test another example
    RA_new = update_RA(RA=100., SA=1., EA=.5, K = 200)
    assert RA_new == 200 



#-------------------------------------------------------------------------
def test_elo_rating():
    '''(10 points) elo_rating'''

    # example game result
    W = [[0, 1]] # Game1: player 0 wins player 1

    # call the function
    R = elo_rating(W, n_player = 2)

    # test data type of the result 
    assert type(R) == list
    #assert type(R[0]) == float 
    assert np.allclose(sum(R), 400*2, atol =1e-2) # the sum of all player's rating should stay the same after a game
    assert R == [408., 392.]

    # test k-factor 
    R = elo_rating(W, n_player = 2, K=32.)
    assert np.allclose(sum(R), 400*2, atol =1e-2) # the sum of all player's rating should stay the same after a game
    assert R == [416., 384.]

    # test another example
    # example game result
    W = [[1, 0], # Game1: player 1 wins player 0
         [2, 1], # Game2: player 2 wins player 1
         [3, 0]] # Game3: player 3 wins player 0

    # call the function
    R = elo_rating(W, n_player = 4)

    assert R[1]>R[0] # because of game 1
    assert R[2]>R[1] # because of game 2
    assert R[3]>R[0] # because of game 3 
    assert R[2]>R[0] # because of game 1 & 2
    assert R[2]>R[3] # because player 2 beats player 1 (higher rating),
                     # player 2 beats player 0 (lower rating)
    assert np.allclose(sum(R), 400*4, atol = 1e-1)

