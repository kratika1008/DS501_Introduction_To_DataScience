import numpy as np
import math
from problem3 import cosine_similarity,pairwise_item_sim, weighted_average
import problem3 as p3
#-------------------------------------------------------------------------
'''
    Problem 2: User-based recommender systems
    In this problem, you will implement a version of the recommender system using user-based method.

    Notation:
    R:  a m x n matrix , the movie rating matrix, R[i,j] represents the rating of the j-th user on the i-th movie, the rating could be 1,2,3,4 or 5
        if R[i,j]= 0, it represents that the j-th user has NOT yet rated/watched the i-th movie.

'''



#--------------------------
def pairwise_user_sim(R):
    '''
        compute the pairwise similarity between each pair of users
        Input:
            R: the rating matrix, a float numpy matrix of shape m by n. Here m is the number of movies (items), n is the number of users.
               R[i,j] represents the rating of the j-th user on the i-th movie, and the rating could be 1,2,3,4 or 5
               If R[i,j] is missing (not rated yet), then R[i,j]= None
        Output:
            S: pairwise similarity matrix between users, a numpy matrix of shape n by n
               S[i,j] represents cosine similarity between item i and item j based upon their user ratings.
        Hint: You could re-use the functions in problem 3 and solve this problem using one line of code.
    '''
    #########################################
    ## INSERT YOUR CODE HERE
    S = pairwise_item_sim(R.T)
    #########################################
    return S

    ''' TEST: Now you can test the correctness of your code above by typing `nosetests -v test4.py:test_pairwise_user_sim' in the terminal.  '''




#--------------------------
def predict(R, S, i, j):
    '''
        Compute a prediction of the rating of the j-th user on the i-th movie using user-based approach.

        Input:
            R: the rating matrix, a float numpy matrix of shape m by n. Here m is the number of movies, n is the number of users.
               R[i,j] represents the rating of the j-th user on the i-th movie, and the rating could be 1,2,3,4 or 5
                If the user has NOT yet watched/rated the movie,  R[i,j]=0.
            S: the pairwise similarities between users, a numpy matrix of shape n by n.
                S[i,j] represents cosine similarity between user i and user j based upon their ratings.
            i: the index of the movie (item) to be predicted
            j: the index of the user to be predicted
        Output:
            p: the predicted rating of user j on movie i, a float scalar value between 1. and 5.
        Hint: You could re-use the functions in problem 3 and solve this problem using one line of code.
    '''
    #########################################
    ## INSERT YOUR CODE HERE
    p = p3.predict(R.T,S,j,i)
    #########################################
    return p


    ''' TEST: Now you can test the correctness of your code above by typing `nosetests -v test4.py:test_predict' in the terminal.  '''




#--------------------------------------------

''' TEST Problem 4:
        Now you can test the correctness of all the above functions by typing `nosetests -v test4.py' in the terminal.

        If your code passed all the tests, you will see the following message in the terminal:
            ----------- Problem 4 (10 points in total)-------------- ... ok
            (5 points) pairwise_user_sim ... ok
            (5 points) predict ... ok
            ----------------------------------------------------------------------
            Ran 4 tests in 0.090s
            OK
'''

#--------------------------------------------
