#-------------------------------------------------------------------------
'''
    Problem 1: Elo ranking algorithm
    In this problem, you will implement the Elo rating algorithm.
'''

#--------------------------
def Terms_and_Conditions():
    '''
        By submitting this homework or changing this function, you agree with the following terms:
       (1) Not sharing your code/solution with any student before and after the homework due. For example, sending your code segment to another student, putting your solution online or lending your laptop (if your laptop contains your solution or your Dropbox automatically copied your solution from your desktop computer and your laptop) to another student to work on this homework will violate this term.
       (2) Not using anyone's code in this homework and building your own solution. For example, using some code segments from another student or online resources due to any reason (like too busy recently) will violate this term. Changing other's code as your solution (such as changing the variable names) will also violate this term.
       (3) When discussing with any other student about this homework, only discuss high-level ideas or use pseudo-code. Don't discuss about the solution at the code level. For example, two students discuss about the solution of a function (which needs 5 lines of code to solve) and they then work on the solution "independently", however the code of the two solutions are exactly the same, or only with minor differences (variable names are different). In this case, the two students violate this term.
      All violations of (1),(2) or (3) will be handled in accordance with the WPI Academic Honesty Policy.  For more details, please visit: https://www.wpi.edu/about/policies/academic-integrity/dishonesty
      Historical Data: in one year, we ended up finding 25% of the students in that class violating this term in their homework submissions and we handled ALL of these violations according to the WPI Academic Honesty Policy.
    '''
    #*******************************************
    # CHANGE HERE
    Read_and_Agree = True  #if you have read and agree with the term above, change "False" to "True".
    #*******************************************
    return Read_and_Agree

#--------------------------
def compute_EA(RA, RB):
    '''
        compute the expected probability of player A (with rating RA) to win in a game against a player B (with ratting RB).
        Input:
            RA: the rating of player A, a float scalar value
            RB: the rating of player B, a float scalar value
        Output:
            EA: the expected probability of A wins, a float scalar value between 0 and 1.
    '''
    #########################################
    ## INSERT YOUR CODE HERE
    diff = RB-RA
    fac = 10 ** (diff/400)
    EA = 1/(1+fac)
    #########################################
    return EA


    ''' TEST: Now you can test the correctness of your code above by typing `nosetests -v test1.py:test_compute_EA' in the terminal.  '''




#--------------------------
def update_RA(RA, SA, EA, K = 16.):
    '''
        compute the new rating of player A after playing a game.
        Input:
            RA: the current rating of player A, a float scalar value
            SA: the game result of player A, a float scalar value.
                if A wins in a game, SA = 1.; if A loses, SA =0.
            EA: the expected probability of player A to win in the game, a float scalar between 0 and 1.
             K: k-factor, a constant number which controls how fast to correct the ratings based upon the latest game result.
        Output:
            RA_new: the new rating of player A, a float scalar value
    '''
    #########################################
    ## INSERT YOUR CODE HERE
    RA_new = RA + K*(SA-EA)
    #########################################
    return RA_new

    ''' TEST: Now you can test the correctness of your code above by typing `nosetests -v test1.py:test_update_RA' in the terminal.  '''


#--------------------------
def elo_rating(W, n_player, K= 16.):
    '''
        An implementation of Elo rating algorithm, which was used in FaceMash.
        Given a collection of game results W, compute the Elo rating scores of all the players.
        Input:
                W: the game results, a numpy matrix of shape (n_game,2), dtype as integers.
                    n_game is the number of games in the datasets.
                    Each row of W, contains the result of one game: if player i wins player j in the k-th game, W[k][0] = i, W[k][1] = j.
                n_player: the total number of players in the dataset, an integer scalar.
                K: k-factor, a constant number which controls how fast to correct the ratings with the new game results.
        Output:
                R: the Elo rating scores,  a python array of float values, such as [1000., 200., 500.], of length num_players
    '''

    # initialize the ratings of all players with 400
    R = n_player * [400.]

    # for each game, update the ratings based upon the result
    for (A, B) in W:
        # the game result: player A wins, player B loses
        # A is the index of player A, B is the index of player B
        # For example,  A=0, B=2, which means that in this game, the first player (A=0) wins the game against the 3rd player (B=2).

        ##############################
        # INSERT YOUR CODE HERE

        # extract player A's current rating from R
        RA = R[A]
        # extract player B's current rating from R
        RB = R[B]

        # compute the expected winning probability of player A
        EA = compute_EA(RA, RB)

        # compute the expected winning probability of player B
        EB = compute_EA(RB, RA)

        # update player A's rating based upon the game result (Player A wins)
        SA=1
        RA_new = update_RA(RA, SA, EA, K)

        # update player A's rating based upon the game result (Player B loses)
        SB=0
        RB_new = update_RA(RB, SB, EB, K)

        R[A]=RA_new
        R[B]=RB_new
        ##############################
    return R



#--------------------------------------------

''' TEST ALL:
        Now you can test the correctness of all the above functions by typing `nosetests -v test1.py' in the terminal.

        If your code passed all the tests, you will see the following message in the terminal:

            ----------- Problem 1 (30 points in total)-------------- ... ok
            (10 points) compute_EA ... ok
            (10 points) compute_RA ... ok
            (10 points) elo_rating ... ok
            ----------------------------------------------------------------------
            Ran 5 tests in 0.004s

            OK
'''

#--------------------------------------------
