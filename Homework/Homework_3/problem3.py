import numpy as np
import math
#-------------------------------------------------------------------------
'''
    Problem 3: Item-based recommender systems
    In this problem, you will implement item-based recommender system.

    Reading Material: https://dzone.com/articles/machinex-cosine-similarity-for-item-based-collabor

    Notation:
    R:  a m x n matrix , the movie rating matrix, R[i,j] represents the rating of the j-th user on the i-th movie, the rating could be 1,2,3,4 or 5
        if R[i,j]= 0, it represents that the j-th user has NOT yet rated/watched the i-th movie.

'''

#--------------------------
def cosine_similarity(X, Y):
    '''
        compute the cosine similarity between two vectors X and Y.
        Suppose <X,Y> represents the dot product of the two vectors.
        For example, if X= [1,2], Y = [3,4], then <X,Y> = 1*3+ 2*4 = 9
        The cosine similarity between X and Y is defined as:

            Cosine(X,Y) =  <X,Y>  /  ( sqrt(<X,X>) * sqrt(<Y,Y>) )

        Input:
            X: a float numpy vector of length m
            y: a float numpy vector of length m
        Output:
            S: the cosine similarity between X and Y, a float scalar value between -1 and 1.
        Hint: you could solve this problem using 3 lines of code.
    '''
    #########################################
    ## INSERT YOUR CODE HERE
    Z = np.dot(X,Y)
    mod_X = math.sqrt(np.dot(X,X))
    mod_Y = math.sqrt(np.dot(Y,Y))
    S = Z/(mod_X*mod_Y)
    #########################################
    return S

    ''' TEST: Now you can test the correctness of your code above by typing `nosetests -v test3.py:test_cosine_similarity' in the terminal.  '''


#--------------------------
def pairwise_item_sim(R):
    '''
        compute the pairwise similarity between each pair of items
        Input:
            R: the rating matrix, a float numpy matrix of shape m by n. Here m is the number of movies (items), n is the number of users.
               R[i,j] represents the rating of the j-th user on the i-th movie, and the rating could be 1,2,3,4 or 5
               If R[i,j] is missing (not rated yet), then R[i,j]= None
        Output:
            S: pairwise similarity matrix between items, a numpy matrix of shape m by m
               S[i,j] represents cosine similarity between item i and item j based upon their user ratings.
    '''
    #########################################
    ## INSERT YOUR CODE HERE
    m = len(R)
    S = np.zeros((m,m),dtype=float)
    for i in range(len(S)):
        for j in range(len(S.T)):
            columnsToRemove = []
            X = R[i]
            Y = R[j]
            columnsToRemove.append(np.argwhere((X==None) | (Y==None)))
            X = np.delete(X, columnsToRemove)
            Y = np.delete(Y, columnsToRemove)
            CS = cosine_similarity(X, Y)
            S[i,j]=CS

    #########################################
    return S

    ''' TEST: Now you can test the correctness of your code above by typing `nosetests -v test3.py:test_pairwise_item_sim' in the terminal.  '''



#--------------------------
def weighted_average(X, W):
    '''
        Compute the weighted average of the values in X.
        Input:
            X: a numpy vector of values
            W: a numpy vector of weights, W[i] is the weight the i-th value in X.
        Output:
            a: the weighted average of the values in X, a float scalar

        For example, if the values X = [3,6], and the weights are [0.2, 0.1]
        the weighted average is :
                        (3*0.2 + 6*0.1) / (0.2+0.1) = 4
        Hint: you could solve this problem using one line of code.
    '''
    #########################################
    ## INSERT YOUR CODE HERE
    Z = np.dot(X,W)
    deno = np.sum(W)
    a = Z/deno
    #########################################
    return a


    ''' TEST: Now you can test the correctness of your code above by typing `nosetests -v test3.py:test_weighted_average' in the terminal.  '''



#--------------------------
def predict(R,S,i,j):
    '''
        Use item-based collaborative filtering to predict the rating of the j-th user on the i-th movie (item)
        Predict the value of R[i,j]
        Input:
            R: the rating matrix, a float numpy matrix of shape m by n. Here m is the number of movies (items), n is the number of users.
               R[i,j] represents the rating of the j-th user on the i-th movie, and the rating could be 1,2,3,4 or 5
               If R[i,j] is missing (not rated yet), then R[i,j]= None
            S: pairwise similarity matrix between items, a numpy matrix of shape m by m
               S[i,j] represents cosine similarity between item i and item j based upon their user ratings.
            i: the index of the movie (item) to be predicted
            j: the index of the user to be predicted
        Output:
            p: the predicted rating of R[i,j]
    '''
    #########################################
    ## INSERT YOUR CODE HERE
    numerator=0
    denominator=0
    for k in range(len(R)):
        if R[k,j]!=None:
            numerator += R[k,j]*S[i,k]
            denominator += S[i,k]

    p=numerator/denominator


    #########################################
    return p


    ''' TEST: Now you can test the correctness of your code above by typing `nosetests -v test3.py:test_predict' in the terminal.  '''





#--------------------------------------------

''' TEST Problem 3:
        Now you can test the correctness of all the above functions by typing `nosetests -v test3.py' in the terminal.

        If your code passed all the tests, you will see the following message in the terminal:
            ----------- Problem 3 (25 points in total)-------------- ... ok
            (5 points) cosine_similarity ... ok
            (5 points) pairwise_item_sim ... ok
            (5 points) weighted_average ... ok
            (10 points) predict ... ok
            ----------------------------------------------------------------------
            Ran 4 tests in 0.090s
            OK
'''

#--------------------------------------------
