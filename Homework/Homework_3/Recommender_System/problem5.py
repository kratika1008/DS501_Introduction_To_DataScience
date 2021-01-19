import numpy as np
import math
#-------------------------------------------------------------------------
'''
    Problem 5: Collaborative Filtering by Matrix Decomposition
'''

#--------------------------
def compute_B(R):
    '''
        Compute the binary masking matrix B, where B is a m by n matrix.
        Here m is the number of movies, n is the number of users.
        if R[i,j] is not missing, B[i,j]= 1
        if R[i,j] is missing (None), B[i,j]= 0
        Input:
            R: the rating matrix, a float numpy matrix of shape m by n.
                If the rating is unknown, the number is None.
        Output:
            S: the binary masking matrix, a float numpy matrix of shape m by n.
                if R[i,j] is not missing, B[i,j]= 1
                if R[i,j] is missing (None), B[i,j]= 0
    '''

    #########################################
    ## INSERT YOUR CODE HERE
    B = np.where(R==None,0,1)
    #########################################
    return B

    ''' TEST: Now you can test the correctness of your code above by typing `nosetests -v test5.py:test_compute_B' in the terminal.  '''


#--------------------------
def compute_L(R,U,V):
    '''
        Compute the error/loss matrix L, where L is a m by n matrix.
        Here m is the number of movies, n is the number of users.
        if R[i,j] is not missing, L[i,j]= R[i,j] - np.dot(U[i,:],V[:,j] >
        if R[i,j] is missing (None), L[i,j]= 0
        Input:
            R: the rating matrix, a float numpy matrix of shape m by n.
                If the rating is unknown, the number is None.
        Output:
            L: the loss matrix, a float numpy matrix of shape m by n.
                if R[i,j] is not missing, L[i,j]= R[i,j] - np.dot(U[i,:],V[:,j] >
                if R[i,j] is missing (None), L[i,j]= 0
    '''

    #########################################
    ## INSERT YOUR CODE HERE

    # compute a binary matrix B
    B = compute_B(R)
    L = np.zeros((R.shape),dtype=float)
    # compute the loss matrix L
    X= np.matmul(U,V)
    for i in range(len(R)):
        for j in range(len(R.T)):
            if R[i,j]!=None:
                L[i,j] = (R[i,j]-X[i,j])*B[i,j]
            else:
                L[i,j] = 0
    #########################################
    return L

    ''' TEST: Now you can test the correctness of your code above by typing `nosetests -v test5.py:test_compute_L' in the terminal.  '''

#--------------------------
def compute_dU(L,U, V,mu=1.):
    '''
        Compute the gradient of matrix U, a matrix of shape m by k.
        Here m is the number of movies, k is the number of hidden factors.
        Input:
            R: the rating matrix, a float numpy matrix of shape m by n.
                If the rating is unknown, the number is None.
            mu: the parameter for regularization term, a float scalar
        Output:
            dU: the gradient of matrix U, a float numpy matrix of shape m by k.
    '''

    #########################################
    ## INSERT YOUR CODE HERE
    A = np.dot(L,V.T)
    dU = ((-2)*A) + (2*mu*U)
    #########################################
    return dU

    ''' TEST: Now you can test the correctness of your code above by typing `nosetests -v test5.py:test_compute_dU' in the terminal.  '''

#--------------------------
def compute_dV(L,U, V, mu=1.):
    '''
        Compute the gradient of matrix V, a matrix of shape k by n.
        Here m is the number of movies, n is the number of users.
        Input:
            R: the rating matrix, a float numpy matrix of shape m by n.
                If the rating is unknown, the number is None.
            mu: the parameter for regularization term, a float scalar
        Output:
            dV: the gradient of matrix V, a float numpy matrix of shape k by n.
    '''

    #########################################
    ## INSERT YOUR CODE HERE
    A = np.dot(U.T,L)
    dV = ((-2)*A) + (2*mu*V)
    #########################################
    return dV

    ''' TEST: Now you can test the correctness of your code above by typing `nosetests -v test5.py:test_compute_dV' in the terminal.  '''


#--------------------------
def update_U(U, dU, beta=.001):
    '''
        Update the matrix U (movie factors) using gradient descent.
        Input:
            U: the current item (movie) factor matrix, a numpy float matrix of shape m by k.
            dU: the gradient of matrix U, a float numpy matrix of shape m by k.
            beta: step-size parameter for gradient descent, a float scalar
        Output:
            U_new: the updated U matrix, a numpy float matrix of shape m X k. Here m is the number of movies (items).
    '''

    #########################################
    ## INSERT YOUR CODE HERE
    U_new = U - (beta*dU)
    #########################################
    return U_new

    ''' TEST: Now you can test the correctness of your code above by typing `nosetests -v test5.py:test_update_U' in the terminal.  '''

#--------------------------
def update_V(V, dV, beta=.001):
    '''
        Update the matrix V (user factors) using gradient descent.
        Input:
            V: the current user factor matrix, a numpy float matrix of shape k by n. Here n is the number of users.
            dV: the gradient of matrix V, a float numpy matrix of shape k by n.
            beta: step-size parameter for gradient descent, a float scalar
        Output:
            V_new: the updated V matrix, a numpy float matrix of shape  k by n.
    '''

    #########################################
    ## INSERT YOUR CODE HERE
    V_new = V - (beta*dV)
    #########################################
    return V_new

    ''' TEST: Now you can test the correctness of your code above by typing `nosetests -v test5.py:test_update_V' in the terminal.  '''


#--------------------------
def matrix_decoposition(R, k=5, max_steps=1000000, beta=.01, mu=.01):
    '''
        Compute the matrix decomposition for optimization-based recommender system.
        Input:
            R: the rating matrix, a float numpy matrix of shape m by n. Here m is the number of movies, n is the number of users.
                If the rating is unknown, the number is 0.
            k: the number of latent factors for users and items.
            max_steps: the maximum number of steps for gradient descent.
            beta: step parameter for gradient descent, a float scalar
        Output:
            U: the item (movie) factor matrix, a numpy float matrix of shape m X k. Here m is the number of movies (items).
            V: the user factor matrix, a numpy float matrix of shape k X n. Here n is the number of users.
    '''

    # initialize U and V with random values
    n_movies, n_users = R.shape
    U = np.random.rand(n_movies, k)
    V = np.random.rand(k, n_users)

    # repeat iteration until convergence or max_steps reached
    for _ in range(max_steps):
        #########################################
        ## INSERT YOUR CODE HERE

        # compute L matrix
        L = compute_L(R,U,V)

        # ------ (update U while fixing V) ------
        # compute gradient of U
        dU = compute_dU(L,U, V,mu)
        # update U using gradient descent
        U_new = update_U(U, dU, beta)
        # if U is not changed much in values, stop iteration
        if np.allclose(U,U_new):
            break
        else:
            U=U_new




        # ------ (update V while fixing U) ------
        # compute gradient of V
        dV = compute_dV(L,U, V, mu)
        # update V using gradient descent
        V_new = update_V(V, dV, beta)
        # if V is not changed much in values, stop iteration
        if np.allclose(V,V_new):
            break
        else:
            V=V_new




        #########################################
    return U, V


    ''' TEST: Now you can test the correctness of your code above by typing `nosetests -v test5.py:test_matrix_decoposition' in the terminal.  '''

#--------------------------
def predict(U, V, i, j):
    '''
        Compute a prediction of the rating of the j-th user on the i-th movie using user-based approach.

        Input:
            U: the item (movie) factor matrix, a numpy float matrix of shape m X k. Here m is the number of movies (items).
            V: the user factor matrix, a numpy float matrix of shape k X n. Here n is the number of users.
            i: the index of the movie (item) to be predicted
            j: the index of the user to be predicted
        Output:
            p: the predicted rating of user j on movie i, a float scalar value between 1. and 5.
        Hint: this problem can be solved using one line of code.
    '''
    #########################################
    ## INSERT YOUR CODE HERE
    p = (np.dot(U,V))[i,j]
    #########################################
    return p

    ''' TEST: Now you can test the correctness of your code above by typing `nosetests -v test5.py:test_predict' in the terminal.  '''



#--------------------------------------------

''' TEST Problem 5:
        Now you can test the correctness of all the above functions by typing `nosetests -v test5.py' in the terminal.

        If your code passed all the tests, you will see the following message in the terminal:
            ----------- Problem 5 (35 points in total)-------------- ... ok
            (3 points) compute_B ... ok
            (3 points) compute_L ... ok
            (5 points) compute_dU ... ok
            (5 points) compute_dV ... ok
            (2 points) update_U ... ok
            (2 points) update_V ... ok
            (10 points) matrix decomposition ... ok
            (5 points) predict ... ok
            ----------------------------------------------------------------------
            Ran 8 tests in 1.090s
            OK
'''



#--------------------------------------------

''' FINAL TEST of your submission:
        Now you can test the correctness of all the problems in this homework by typing `nosetests -v' in the terminal.

        If your code passed all the tests, you will see the following message in the terminal:
            ----------- Problem 1 (15 points in total)-------------- ... ok
            (5 points) SuitCount ... ok
            (5 points) SuitSum ... ok
            (5 points) NumberCount ... ok
            ----------- Problem 2 (15 points in total)-------------- ... ok
            (3 points) MatMul1x1 ... ok
            (3 points) MatMul1x2 ... ok
            (3 points) MatMul2x1 ... ok
            (3 points) MatMul2x2 ... ok
            (3 points) MatMul random ... ok
            ----------- Problem 3 (25 points in total)-------------- ... ok
            (5 points) cosine_similarity ... ok
            (5 points) pairwise_item_sim ... ok
            (5 points) weighted_average ... ok
            (10 points) predict ... ok
            ----------- Problem 4 (10 points in total)-------------- ... ok
            (5 points) pairwise_user_sim ... ok
            (5 points) predict ... ok
            ----------- Problem 5 (35 points in total)-------------- ... ok
            (3 points) compute_B ... ok
            (3 points) compute_L ... ok
            (5 points) compute_dU ... ok
            (5 points) compute_dV ... ok
            (2 points) update_U ... ok
            (2 points) update_V ... ok
            (10 points) matrix decomposition ... ok
            (5 points) predict ... ok
            ----------------------------------------------------------------------
            Ran 27 tests in 3.333s

'''

#--------------------------------------------
