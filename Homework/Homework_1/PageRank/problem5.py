import numpy as np
from problem3 import random_walk
from problem4 import compute_S

#-------------------------------------------------------------------------
'''
    Problem 5: Solving sink-region problem in PageRank
    In this problem, we implement the pagerank algorithm which can solve both the sink node problem and sink region problem.
    We will consider a random surfer model where a user has 2 options at every timestep: (option 1) randomly follow a link on the page or (option 2) randomly go to any page in the graph.
    The probabilities are as follows:
        Randomly follow a link with probability alpha, for example, 0.95
        Randomly go to any page in the graph with probability (1 - alpha), for example, 0.05

    How to run the unit tests to test your code?
    1) Test one function in a test file:
       After implementing one function in this file (for example, compute_G), you could test the correctness of your code by typing `nosetests -v test5.py:test_compute_G' in the terminal.
    2) Test all functions in one test file:
       After solving all the functions in a test file (for example, test5.py), you could test the correctness of your code by typing `nosetests -v test5.py' in the terminal.
'''

#--------------------------
def compute_G(A, alpha = 0.95):
    '''
        compute the pagerank transition Matrix G from addjacency matrix A, which solves both the sink node problem and the sing region problem.
        G[j][i] represents the probability of moving from node i to node j.
        If node i is a sink node, S[j][i] = 1/n.
        Input:
                A: adjacency matrix, a (n by n) numpy matrix of binary values. If there is a link from node i to node j, A[j][i] =1. Otherwise A[j][i]=0 if there is no link.
                alpha: a float scalar value, which is the probability of choosing option 1 (randomly follow a link on the page)
        Output:
                G: the transition matrix, a (n by n) numpy matrix of float values.  G[j][i] represents the probability of moving from node i to node j.
                    The values in each column of matrix G should sum to 1.
        Hint: you could solve this problem using 3 lines of code. You could re-use the functions that you have implemented in problem 3 and 4.
    '''
    #########################################
    ## INSERT YOUR CODE HERE
    num_nodes = A.shape[0]
    S = compute_S(A)
    Y = np.ones(S.shape)
    G = (alpha*S)+((1-alpha)*(1/num_nodes)*Y)

    #########################################
    return G

    ''' TEST: Now you can test the correctness of your code above by typing `nosetests -v test5.py:test_compute_G' in the terminal.  '''





#--------------------------
def pagerank(A, alpha = 0.95):
    '''
        The final PageRank algorithm, which solves both the sink node problem and sink region problem.
        Given an adjacency matrix A, compute the pagerank score of all the nodes in the network.
        Input:
                A: adjacency matrix, a numpy matrix of binary values. If there is a link from node i to node j, A[j][i] =1. Otherwise A[j][i]=0 if there is no link.
                alpha: a float scalar value, which is the probability of choosing option 1 (randomly follow a link on the page)
        Output:
                x: the ranking scores, a numpy vector of float values, such as np.array([[.3], [.5], [.7]])
        Hint: you could solve this problem using two lines of code. You could re-use the functions that you have implemented in problem 3 and 4.
    '''

    # Initialize the score vector
    num_nodes = A.shape[0] # get the number of nodes (n)
    x_0 =  np.ones((num_nodes,1))/num_nodes

    #########################################
    ## INSERT YOUR CODE HERE
    # compute the transition matrix G from adjacency matrix A
    G = compute_G(A,alpha)

    # random walk for multiple steps until convergence
    x = random_walk(G, x_0)[0]
    #########################################
    return x



#--------------------------------------------

''' TEST ALL:
        Now you can test the correctness of all the above functions by typing `nosetests -v test3.py' in the terminal.

        If your code passed all the tests, you will see the following message in the terminal:
            ---------- Problem 5 (20 points in total) ------------ ... ok
            (10 points) compute_G() ... ok
            (10 points) pagerank ... ok

            ----------------------------------------------------------------------
            Ran 3 tests in 0.003s

            OK

'''

#--------------------------------------------
