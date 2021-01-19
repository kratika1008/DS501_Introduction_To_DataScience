import numpy as np
import problem1 as p1
#-------------------------------------------------------------------------
'''
    Problem 5: Graph Clustering (Spectral Clustering)
    In this problem, you will implement a version of the spectral clustering method to cluster the nodes in a graph into two groups.

    Notations:
            ---------- input data ------------------------
            n: the number of nodes in the network, an integer scalar.
            A:  the adjacency matrix, a float numpy matrix of shape n by n.
                If there is a link between node i an node j, then A[i][j] = A[j][i] = 1.
            ---------- computed data ------------------------
            D:  the degree matrix, a numpy float matrix of shape n by n.
                All off-diagonal elements are 0. Each diagonal element represents the degree of the node (number of links).
            L:  the Laplacian matrix, a numpy float matrix of shape n by n.
                L = D-A
            e2:  the eigen vector corresponding to the smallest non-zero eigen value, a numpy float vector of length n.
            tol: the tolerance threshold for eigen values, a float scalar. A very small positive value. If an eigen value is smaller than tol, then we consider the eigen value as being 0.
            x:  the binary vector of length n, a numpy float vector of (0/1) values.
                It indicates a binary partition on the graph, such as [1.,1.,1., 0.,0.,0.].
            --------------------------------------------------
'''

#--------------------------
def compute_D(A):
    '''
        Compute the degree matrix D.
        Input:
            A:  the adjacency matrix, a float numpy matrix of shape n by n. Here n is the number of nodes in the network.
                If there is a link between node i an node j, then A[i][j] = A[j][i] = 1.
        Output:
            D:  the degree matrix, a numpy float matrix of shape n by n.
                All off-diagonal elements are 0. Each diagonal element represents the degree of the node (number of links).
        Hint: you could solve this problem using 2 lines of code.
    '''
    #########################################
    ## INSERT YOUR CODE HERE
    d = []
    # degree vector of the nodes
    for i in range(len(A)):
        d.append(np.sum(A[i]))
    # diagonal matrix
    D = np.diag(d)

    #########################################
    return D

    ''' TEST: Now you can test the correctness of your code above by typing `nosetests -v test5.py:test_compute_D' in the terminal.  '''


#--------------------------
def compute_L(D,A):
    '''
        Compute the Laplacian matrix L.
        Input:
            D:  the degree matrix, a numpy float matrix of shape n by n.
                All off-diagonal elements are 0. Each diagonal element represents the degree of the node (number of links).
            A:  the adjacency matrix, a float numpy matrix of shape n by n. Here n is the number of nodes in the network.
                If there is a link between node i an node j, then A[i][j] = A[j][i] = 1.
        Output:
            L:  the Laplacian matrix, a numpy float matrix of shape n by n.
        Hint: you could solve this problem using 1 line of code.
    '''

    #########################################
    ## INSERT YOUR CODE HERE
    L = D-A
    #########################################
    return L

    ''' TEST: Now you can test the correctness of your code above by typing `nosetests -v test5.py:test_compute_L' in the terminal.  '''



#--------------------------
def find_e2(L,tol= 1e-4):
    '''
        find the eigen vector that corresponds to the smallest non-zeros eigen values of the Laplacian matrix.

        Input:
            L:  the Laplacian matrix, a numpy float matrix of shape n by n.
            tol: the tolerance threshold for eigen values, a float scalar. A very small positive value. If an eigen value is smaller than tol, then we consider the eigen value as being 0.
        Output:
            e2:  the eigen vector corresponding to the smallest non-zero eigen value, a numpy float vector of length n.

        For example, if the eigen values are [0.5, 0.000000000001, 2.], the first eigen vector is the answer.
        Here we assume 0.00000001 is close enough to 0 because is smaller than the tolerance level (tol).
        For example, if the eigen values are [2., 0.0000000000001, 0.3], the last eigen vector is the answer.
        For example, if the eigen values are [0.00003, 0.000001, 0.3], the last eigen vector is the answer.
    '''

    #########################################
    ## INSERT YOUR CODE HERE
    Ep = p1.compute_eigen_pairs(L)
    Ep = p1.sort_eigen_pairs(Ep)
    for i in range(len(Ep)):
        v,e = Ep[i]
        if(v>tol):
            e2 = e
            break
    #########################################
    return e2

    ''' TEST: Now you can test the correctness of your code above by typing `nosetests -v test5.py:test_find_e2' in the terminal.  '''



#--------------------------
def compute_x(e2):
    '''
        Compute the partition on the graph from the thresholding an eigen vector with 0 threshold.
        Input:
            e2:  the eigen vector corresponding to the smallest non-zero eigen value, a numpy float vector of length n.
        Output:
            x:  the binary vector of length n, a numpy float vector of (0/1) values.
                It indicates a binary partition on the graph, such as [1.,1.,1., 0.,0.,0.].
    '''

    #########################################
    ## INSERT YOUR CODE HERE
    x = np.empty((len(e2)),dtype=np.int)
    for i in range(len(e2)):
        if e2[i]>0:
            x[i]=1
        else:
            x[i]=0
    #########################################
    return x

    ''' TEST: Now you can test the correctness of your code above by typing `nosetests -v test5.py:test_compute_x' in the terminal.  '''




#--------------------------
def spectral_clustering(A):
    '''
        Spectral clustering of a graph.
        Input:
            A:  the adjacency matrix, a float numpy matrix of shape n by n. Here n is the number of nodes in the network.
                If there is a link between node i an node j, then A[i][j] = A[j][i] = 1.
        Output:
            x:  the binary vector of length n, a numpy float vector of (0/1) values.
                It indicates a binary partition on the graph, such as [1.,1.,1., 0.,0.,0.].
        Note: you cannot use any existing python package for spectral clustering, such as scikit-learn.
        Hint: x is related to the eigen vector of L with the smallest positive eigen values.
              For example, if the eigen vector is [0.2,-0.1, -0.2], the values larger than zero will be 1, so x=[1,0,0] in this example.
              Note: if the eigen value is small enough (say smaller than 0.000001), we can treat it as being zero.
    (5 points)
    '''

    #########################################
    ## INSERT YOUR CODE HERE
    # compute degree matrix
    D = compute_D(A)

    # compute laplacian matrix
    L = compute_L(D,A)

    # find the eigen vector with the smallest non-zero eigen value
    e2 = find_e2(L,1e-6)

    # compute the graph partition
    x = compute_x(e2)

    #########################################
    return x


    ''' TEST: Now you can test the correctness of your code above by typing `nosetests -v test5.py:test_spectral_clustering' in the terminal.  '''


#--------------------------------------------

''' TEST Problem 5:
        Now you can test the correctness of all the above functions by typing `nosetests -v test5.py' in the terminal.

        If your code passed all the tests, you will see the following message in the terminal:
            ----------- Problem 5 (20 points in total)--------------------- ... ok
            (4 points) compute_D ... ok
            (4 points) compute_L ... ok
            (4 points) find_e2 ... ok
            (4 points) compute_x ... ok
            (4 points) spectral clustering ... ok

            ----------------------------------------------------------------------
            Ran 6 tests in 0.021s
            OK
'''



#--------------------------------------------

''' FINAL TEST of your submission:
        Now you can test the correctness of all the problems in this homework by typing `nosetests -v' in the terminal.

        If your code passed all the tests, you will see the following message in the terminal:
            ----------- Problem 1 (10 points in total)--------------------- ... ok
            (5 points) compute_eigen_pairs ... ok
            (5 points) sort_eigen_pairs ... ok
            ----------- Problem 2 (25 points in total)--------------------- ... ok
            (3 points) centering_X ... ok
            (2 points) compute_C ... ok
            (5 points) compute_P ... ok
            (5 points) compute_Xp ... ok
            (10 points) PCA ... ok
            ----------- Problem 3 (25 points in total)--------------------- ... ok
            (3 points) vector_to_image ... ok
            (2 points) load_dataset ... ok
            (5 points) compute_mu_image ... ok
            (15 points) compute_eigen_faces ... ok
            ----------- Problem 4 (20 points in total)--------------------- ... ok
            (10 points) compute_distance ... ok
            (10 points) face_recognition ... ok
            ----------- Problem 5 (20 points in total)--------------------- ... ok
            (4 points) compute_D ... ok
            (4 points) compute_L ... ok
            (4 points) find_e2 ... ok
            (4 points) compute_x ... ok
            (4 points) spectral clustering ... ok
            ----------------------------------------------------------------------
            Ran 23 tests in 17.602s

'''

#--------------------------------------------
