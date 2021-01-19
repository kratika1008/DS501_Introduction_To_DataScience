#-------------------------------------------------------------------------
'''
    Problem 1: getting familiar with python and unit tests.
    In this problem, please install python version 3 and the following package:
        * nose   (for unit tests)

    To install python packages, you can use any python package management software, such as pip, conda. For example, in pip, you could type `pip3 install nose` in the terminal to install the package.

    Then start implementing function swap().
    '''

#--------------------------
def Terms_and_Conditions():
    '''
        By submitting this homework or changing this function, you agree with the following terms:
       (1) Not sharing your code/solution with any student before and after the homework due. For example, sending your code segment to another student, putting your solution online or lending your laptop (if your laptop contains your solution or your Dropbox automatically copied your solution from your desktop computer and your laptop) to another student to work on this homework will violate this term.
       (2) Not using anyone's code in this homework and building your own solution. For example, using some code segments from another student or online resources due to any reason (like too busy recently) will violate this term. Changing other's code as your solution (such as changing the variable names) will also violate this term.
       (3) When discussing with any other student about this homework, only discuss high-level ideas or use pseudo-code. Don't discuss about the solution at the code level. For example, two students discuss about the solution of a function (which needs 5 lines of code to solve) and they then work on the solution "independently", however the code of the two solutions are exactly the same, or only with minor differences (variable names are different). In this case, the two students violate this term.
      All violations of (1),(2) or (3) will be handled in accordance with the WPI Academic Honesty Policy.  For more details, please visit: https://www.wpi.edu/about/policies/academic-integrity/dishonesty
      Note: we will use the Stanford Moss system to check your code for code similarity. https://theory.stanford.edu/~aiken/moss/
      Historical Data: in one year, we ended up finding 25% of the students in that class violating this term in their homework submissions and we handled ALL of these violations according to the WPI Academic Honesty Policy.
      To avoid this from happening again, just in case if anyone is interested:), here is an article you could read: https://github.com/genchang1234/How-to-cheat-in-computer-science-101
    '''
    #*******************************************
    # CHANGE HERE
    Read_and_Agree = True #if you have read and agree with the term above, change "False" to "True".
    #*******************************************
    return Read_and_Agree




#--------------------------
def swap( A, i, j ):
    '''
        Swap the i-th element and j-th element in list A.
        Inputs:
            A:  a list, such as  [2,6,1,4]
            i:  an index integer for list A, such as  3
            j:  an index integer for list A, such as  0
    '''
    #########################################
    ## INSERT YOUR CODE HERE
    size = len(A)
    if (i>=0 and j>=0 and i<size and j<size):
        A[i],A[j]=A[j],A[i]
        return A

A=[2,6,1,4]
print(swap(A,1,2))

    #########################################


#--------------------------
def sort_list( A ):
    '''
        Given a disordered list of integers, rearrange the integers in natural order using bubble sort algorithm.
        Input: A:  a list, such as  [2,6,1,4]
        Output: A should be sorted, such as [1,2,4,6]
    '''
    #########################################
    ## INSERT YOUR CODE HERE
    n=len(A)

    for i in range(n):
        for j in range(n-i-1):
            if(A[j]>A[j+1]):
                A[j],A[j+1]=A[j+1],A[j]

    return A

A=[2,6,1,4,3,9,-4]
print(sort_list(A))

    #########################################


#--------------------------------------------

'''
    TEST Your Code:
        Now you can test the correctness of all the above functions by typing `nosetests -v test1.py' in the terminal.
        If your code passed the tests, you will see the following message in the terminal:

            ---------- Problem 1 (10 points in total) ------------ ... ok
            (2 points) Install Python 3 and nosetests on your computer ... ok
            (3 points) swap() ... ok
            (5 points) sort_list() ... ok
            ----------------------------------------------------------------------
            Ran 4 tests in 0.001s

    ERROR Message:
        If your code has an error, you will see an error message with the line number of the error:
        For example:

            ======================================================================
            FAIL: (3points) swap()
            ----------------------------------------------------------------------
            Traceback (most recent call last):
              File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/nose/case.py", line 198, in runTest
                self.test(*self.arg)
              File "test1.py", line 32, in test_swap
                assert A[0]==3
              AssertionError

        This error message means:
            (1) You are using python 3.6,
                    See: "... Versions/3.6/lib/python3.6/ ... "
            (2) Your code failed in Line 32, the test_swap function in test1.py file
                    See: " ...  File "test1.py", line 32, in test_swap "
            (3) The specific test that failed is that A[0] should equals to 3, but in your code, a different result is returned.
                    See: "  assert A[0]==3
                            AssertionError "

    Debug:

        To debug your code, you could insert a print statement before Line 32 of test1.py file:
            print(A[0])
        Then run the test again.

        Now after the error message, the value of A[0] will be printed like this:

            -------------------- >> begin captured stdout << ---------------------
            4

            --------------------- >> end captured stdout << ----------------------

        Then we know that the value of A[0] output by your current code.

'''
