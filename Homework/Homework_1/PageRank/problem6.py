import numpy as np
from problem5 import pagerank

#-------------------------------------------------------------------------
'''
    Problem 6: use PageRank (implemented in Problem 5) to compute the ranked list of nodes in a real-world network.
    In this problem, we import a real-world network and use pagerank algorithm to rank the nodes in the network.
    File `network.csv` contains a network adjacency matrix.
    (1) import the network from the file
    (2) compute the pagerank scores for the network

    How to run the unit tests to test your code?
    1) Test one function in a test file:
       After implementing one function in this file (for example, import_A), you could test the correctness of your code by typing `nosetests -v test6.py:test_import_A' in the terminal.
    2) Test all functions in one test file:
       After solving all the functions in a test file (for example, test6.py), you could test the correctness of your code by typing `nosetests -v test6.py' in the terminal.
    3) Test the whole submission:
       After solving all the problems in this HW, you could test all the files by typing `nosetests -v' in the terminal.
'''

#--------------------------
def import_A(filename ='network.csv'):
    '''
        import the addjacency matrix A from a CSV file
        Input:
                filename: the name of csv file, a string
        Output:
                A: the ajacency matrix, a numpy matrix of shape (n by n)
        Hint: you could solve this problem using one line of code.
        Hint: NumPy has a function, called loadtxt(), to load a matrix from text file. To load CSV (Comma Separated Values) files, you could set the delimiter parameter in the function.
    '''
    #########################################
    ## INSERT YOUR CODE HERE
    A = np.loadtxt(filename,delimiter=',')
    #########################################
    return A


#--------------------------
def score2rank(x):
    '''
        compute a list of node IDs sorted by descending order of pagerank scores in x.
        Note the node IDs start from 0. So the IDs of the nodes are 0,1,2,3, ...

        For example, suppose we have 3 nodes, and their pagerank scores are
                0.2
            x=  0.1
                0.3

        Then the sorted ID of these three pages should be

            sorted_ids = [2,0,1]
        Because the node with the largest score (x[2]=0.3) is the last node (index = 2);
                the second largest node (x[0]=0.2) has an index = 0 (the first node)
                the smallest node (x[1]=0.1) has an index = 1 (the first node)

        Input:
                x: the numpy array of pagerank scores, shape (n by 1)
        Output:
                sorted_ids: a python list of node IDs (starting from 0) in descending order of their pagerank scores, a python list of integer values, such as [2,0,1,3].
        Hint: you could solve this problem using 2 lines of code.
    '''
    #########################################
    ## INSERT YOUR CODE HERE
    y = np.copy(x)
    n = len(y)
    sorted_ids = [y for y in range(n)]
    for i in range(n):
        for j in range(n-i-1):
            if(y[j+1]>y[j]):
                y[j][0],y[j+1][0]=y[j+1][0],y[j][0]
                sorted_ids[j],sorted_ids[j+1]=sorted_ids[j+1],sorted_ids[j]
    #########################################
    return sorted_ids

#--------------------------
def node_ranking(filename = 'network.csv', alpha = 0.95):
    '''
        Rank the nodes in the network imported from a CSV file.
        (1) import the adjacency matrix from `filename` file.
        (2) compute pagerank scores of all the nodes
        (3) return a list of node IDs sorted by descending order of pagerank scores

        Input:
                filename: the csv filename for the adjacency matrix, a string.
                alpha: a float scalar value, which is the probability of choosing option 1 (randomly follow a link on the node)

        Output:
                sorted_ids: the list of node IDs (starting from 0) in descending order of their pagerank scores, a python list of integer values, such as [2,0,1,3].
        Hint: you could solve this problem using 3 lines of code.

    '''
    #########################################
    ## INSERT YOUR CODE HERE
    # import the adjacency matrix A from csv file "filename"
    A = import_A(filename)
    # compute the pagerank scores of all the nodes using PageRank algorithm implemented in problem 5
    x = pagerank(A, alpha)
    # compute the sorted list of node IDs, higher ranked nodes should have higher pagerank scores.
    sorted_ids = score2rank(x)
    #########################################
    return sorted_ids




#--------------------------------------------

''' TEST ALL functions in Problem 6:
        Now you can test the correctness of all the above functions by typing `nosetests -v test6.py' in the terminal.

        If your code passed all the tests, you will see the following message in the terminal:
            ---------- Problem 6 (20 points in total) ------------ ... ok
            (10 points) import_A ... ok
            (5 points) score2rank ... ok
            (5 points) node_ranking ... ok

            ----------------------------------------------------------------------
            Ran 4 tests in 1.758s

            OK

'''

#--------------------------------------------





#--------------------------------------------

''' FINAL TEST of your submission:
        Now you can test the correctness of all the problems in this homework by typing `nosetests -v' in the terminal.

        If your code passed all the tests, you will see the following message in the terminal:

            ---------- Problem 1 (10 points in total) ------------ ...ok

            (2 points) Install Python 3 and nosetests on your computer ... ok
            (3 points) swap() ... ok
            (5 points) sort_list() ... ok

            ---------- Problem 2 (10 points in total) ------------ ... ok

            (1 points) nd-array ... ok
            (1 points) float array ... ok
            (1 points) get_shape ... ok
            (1 points) all_one_matrix ... ok
            (1 points) mat sum ... ok
            (1 points) mat_scalar_multiplication ... ok
            (2 points) matrix_vector_multiplication ... ok
            (1 points) find_zeros ... ok
            (1 points) diag_mat ... ok

            ---------- Problem 3 (30 points in total) ------------ ... ok

            (10 points) compute_P ... ok
            (5 points) random_walk_one_step ... ok
            (10 points) random_walk ... ok
            (5 points) pagerank_v1 ... ok

            ---------- Problem 4 (10 points in total) ------------ ... ok

            (5 points) compute_S ... ok
            (5 points) pagerank_v2 ... ok

            ---------- Problem 5 (20 points in total) ------------ ... ok

            (10 points) compute_G() ... ok
            (10 points) pagerank ... ok

            ---------- Problem 6 (20 points in total) ------------ ... ok

            (10 points) import_A ... ok
            (5 points) score2rank ... ok
            (5 points) node_ranking ... ok

            ----------------------------------------------------------------------
            Ran 29 tests in 1.838s

            OK

'''

#--------------------------------------------
