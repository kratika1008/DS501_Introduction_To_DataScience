import numpy as np
from problem3 import compute_P,random_walk

#-------------------------------------------------------------------------
'''
    Problem 4: Solving sink-node problem in PageRank
    In this problem, we implement the pagerank algorithm which can solve the sink node problem.

    How to run the unit tests to test your code?
    1) Test one function in a test file:
       After implementing one function in this file (for example, compute_S), you could test the correctness of your code by typing `nosetests -v test4.py:test_compute_S' in the terminal.
    2) Test all functions in one test file:
       After solving all the functions in a test file (for example, test4.py), you could test the correctness of your code by typing `nosetests -v test4.py' in the terminal.
'''

#--------------------------
def compute_S(A):
    '''
        compute the transition matrix S from addjacency matrix A, which solves sink node problem by filling the all-zero columns in A.
        S[j][i] represents the probability of moving from node i to node j.
        If node i is a sink node, S[j][i] = 1/n.
        Input:
                A: adjacency matrix, a (n by n) numpy matrix of binary values. If there is a link from node i to node j, A[j][i] =1. Otherwise A[j][i]=0 if there is no link.
        Output:
                S: transition matrix, a (n by n) numpy matrix of float values.  S[j][i] represents the probability of moving from node i to node j.
                   The values in each column of matrix S should sum to 1.
    '''
    #########################################
    ## INSERT YOUR CODE HERE
    num_nodes = A.shape[0]
    P = compute_P(A)
    S=np.copy(P)
    for i in range(len(P)):
        c=np.sum(P, axis=0)[i]
        if(c==0):
            S[:,i]=(1/num_nodes)

    #########################################
    return S

    ''' TEST: Now you can test the correctness of your code above by typing `nosetests -v test4.py:test_compute_S' in the terminal.  '''




#--------------------------
def pagerank_v2(A):
    '''
        A simplified version of PageRank algorithm, which solves the sink node problem.
        Given an adjacency matrix A, compute the pagerank score of all the nodes in the network.
        Input:
                A: adjacency matrix, a numpy matrix of binary values. If there is a link from node i to node j, A[j][i] =1. Otherwise A[j][i]=0 if there is no link.
        Output:
                x: the ranking scores, a numpy vector of float values, such as np.array([[.3], [.5], [.2]])
    '''

    # Initialize the score vector
    num_nodes = A.shape[0]
    x_0 =  np.ones((num_nodes,1))/num_nodes

    #########################################
    ## INSERT YOUR CODE HERE
    # compute the transition matrix S from adjacency matrix A
    S = compute_S(A)

    # random walk
    x = random_walk(S, x_0)[0]
    #########################################

    return x




#--------------------------------------------

''' TEST ALL:
        Now you can test the correctness of all the above functions by typing `nosetests -v test3.py' in the terminal.

        If your code passed all the tests, you will see the following message in the terminal:
                ---------- Problem 4 (10 points in total) ------------ ... ok
                (5 points) compute_S ... ok
                (5 points) pagerank_v2 ... ok

                ----------------------------------------------------------------------
                Ran 3 tests in 0.002s

OK

'''

#--------------------------------------------
