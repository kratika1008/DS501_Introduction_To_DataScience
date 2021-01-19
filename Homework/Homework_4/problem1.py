#-------------------------------------------------------------------------
# Note: please don't use any additional package except the following packages
import numpy as np
#-------------------------------------------------------------------------
'''
    Problem 1:
    In this problem, you will get familiar with matrix eigen vectors and eigen values.

'''

#--------------------------
def Terms_and_Conditions():
    '''
        By submitting this homework or changing this function, you agree with the following terms:
       (1) Not sharing your code/solution with any student before and after the homework due. For example, sending your code segment to another student, putting your solution online or lending your laptop (if your laptop contains your solution or your Dropbox automatically synchronize your solution between your home computer and your laptop) to another student to work on this homework will violate this term.
       (2) Not using anyone's code in this homework, build your own solution. For example, using some code segments from another student or online resources due to any reason (like too busy recently) will violate this term. Changing other people's code as your solution (such as changing the variable names) will also violate this term.
       (3) When discussing with any other student about this homework, only discuss high-level ideas or using pseudo-code. Don't discuss about the solution at the code level. For example, discussing with another student about the solution of a function (which needs 5 lines of code to solve), and then working on the solution "independently", however the code of the two solutions are exactly the same, or only with minor differences  (like changing variable names) will violate this term.
      All violations of (1),(2) or (3) will be handled in accordance with the WPI Academic Honesty Policy.  For more details, please visit: https://www.wpi.edu/about/policies/academic-integrity/dishonesty
      Historical Data: in one year, we ended up finding 25% of the students in the class violating this term in their homework submissions and we handled ALL of these violations according to the WPI Academic Honesty Policy.
    '''
    #########################################
    ## CHANGE CODE HERE
    Read_and_Agree = True
    #########################################
    return Read_and_Agree


#--------------------------
def compute_eigen_pairs(X):
    '''
        Compute the eigen vectors and eigen values of matrix X.
        Input:
            X:  a numpy float matrix of shape p by p, Note, X should be a symmetric matrix.
        Output:
            Ep:  the eigen pairs of matrix X, a python list of length p.
                Ep is a list as [(v1,e1), (v2, e2), ... ]
                Each element of Ep corresponds to one eigen pair (v,e), here v is an eigen value of matrix X, e is its eigen vector.
                Here v is a float scalar, and e is a numpy vector of length p.

        For example, suppose we have a 3x3 matrix:
            X =  1, 0, 0
                 0, 2, 0
                 0, 0, 3
        This matrix has three eigen pairs:
        v1= 1, e1 = [1,0,0]
        v2= 2, e2 = [0,1,0]
        v3= 3, e3 = [0,0,1]
        So in this example, the eigen pairs of matrix X should be
        Ep =[(1, [1,0,0]),
             (2, [0,1,0]),
             (3, [0,0,1])]
        Here P[0] represents the first eigen pair (1,[1,0,0]), where the eigen value is 1, and the eigen vector is [1,0,0]
        Hint: you could use np.linalg.eigh() to compute the eigen pairs of a matrix.
    '''

    #########################################
    ## INSERT YOUR CODE HERE
    v,e = np.linalg.eigh(X)
    Ep=list(zip(v,e.T))
    #########################################
    return Ep


    ''' TEST: Now you can test the correctness of your code above by typing `nosetests -v test1.py:test_compute_eigen_pairs' in the terminal.  '''



#--------------------------
def sort_eigen_pairs(Ep, order = 'ascending'):
    '''
        Sort the eigen pairs in descending/ascending order of the eigen values.
        Input:
            Ep:  the eigen pairs of matrix X, a python list of length p.
                Ep is a list as [(v1,e1), (v2, e2), ... ]
                Each element of Ep corresponds to one eigen pair (v,e), here v is an eigen value of matrix C, e is its eigen vector.
                Here v is a float scalar, and e is a numpy vector of length p.
            order: a string of either 'ascending' or 'descending', whether to sort the eigen pairs in ascending or descending order of the eigen values.
        Output:
            Ep: the sorted list of eigen pairs, a python list of length p.

        For example, suppose we have a 3x3 matrix:
            X =  2, 0, 0
                 0, 1, 0
                 0, 0, 3
        This matrix has three eigen pairs:
        v1= 2, e1 = [1,0,0]
        v2= 1, e2 = [0,1,0]
        v3= 3, e3 = [0,0,1]
        So in this example, the eigen pairs of matrix X should be
        Ep =[(2, [1,0,0]),
             (1, [0,1,0]),
             (3, [0,0,1])]
        If we sort P in ascending order:
        Ep= [(1, [0,1,0]),
             (2, [1,0,0]),
             (3, [0,0,1])]
        If we sort P in descending order:
        Ep= [(3, [0,0,1]),
             (2, [1,0,0]),
             (1, [0,1,0])]
        Hint: you could use np.linalg.eigh() to compute the eigen pairs of a matrix.
    '''

    #########################################
    ## INSERT YOUR CODE HERE
    n=len(Ep)
    for i in range(n):
        for j in range(n-i-1):
            if order == 'descending':
                if(Ep[j][0]<Ep[j+1][0]):
                    Ep[j],Ep[j+1]=Ep[j+1],Ep[j]
            else:
                if(Ep[j][0]>Ep[j+1][0]):
                    Ep[j],Ep[j+1]=Ep[j+1],Ep[j]
    
    #########################################
    return Ep

    ''' TEST: Now you can test the correctness of your code above by typing `nosetests -v test1.py:test_sort_eigen_pairs' in the terminal.  '''




#--------------------------------------------

''' TEST Problem 1:
        Now you can test the correctness of all the above functions by typing `nosetests -v test1.py' in the terminal.

        If your code passed all the tests, you will see the following message in the terminal:
            ----------- Problem 1 (10 points in total)--------------------- ... ok
            (5 points) compute_eigen_pairs ... ok
            (5 points) sort_eigen_pairs ... ok

            ----------------------------------------------------------------------
            Ran 3 tests in 0.002s
            OK
'''

#--------------------------------------------
