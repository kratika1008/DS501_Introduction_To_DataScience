import pandas as pd
#-------------------------------------------------------------------------
'''
    Problem 5: Sabermetrics
    In this problem, you will implement different evaluation metrics for baseball players.
'''


#--------------------------
def batting_average(H, AB):
    '''
        compute the batting average of a player.
        Input:
            H: the number of hits, an integer scalar.
            AB: the number of "at bats",  an integer scalar
        Output:
            BA: the batting average of a player, a float scalar.
    '''
    #########################################
    ## INSERT YOUR CODE HERE
    BA = H / AB
    #########################################
    return BA


    ''' TEST: Now you can test the correctness of your code above by typing `nosetests -v test5.py:test_batting_average' in the terminal.  '''




#--------------------------
def on_base_percentage(H, AB, BB, HBP, SF):
    '''
        compute the on base percentage of a player.
        Input:
            H: the number of hits, an integer scalar.
            AB: the number of "at bats",  an integer scalar
            BB: the number of bases on balls (walks),  an integer scalar
            HBP: the number of hit by pitch,  an integer scalar
            SF: the number of sacrifice fly,  an integer scalar
        Output:
            OBP: the on base percentage of a player, a float scalar.
    '''
    #########################################
    ## INSERT YOUR CODE HERE
    Num = H+BB+HBP
    Deno = AB+BB+HBP+SF
    OBP = Num/Deno
    #########################################
    return OBP

    ''' TEST: Now you can test the correctness of your code above by typing `nosetests -v test5.py:test_on_base_percentage' in the terminal.  '''



#--------------------------
def slugging_percentage(H, _2B, _3B, HR, AB):
    '''
        compute the slugging percentage of a player.
        Input:
            H: the number of hits, an integer scalar.
            _2B: the number of 2nd base,  an integer scalar (note: python variable names cannot start with a number, so _ is added)
            _3B: the number of 3rd base,  an integer scalar
            HR: the number of home runs,  an integer scalar
            AB: the number of at bats,  an integer scalar
        Output:
            SLG: the slugging percentage of a player, a float scalar.
    '''
    #########################################
    ## INSERT YOUR CODE HERE

    # compute the total bases
    totalB = H + _2B + (2*_3B) + (3*HR)
    # compute SLG
    SLG = totalB/AB

    #########################################
    return SLG

    ''' TEST: Now you can test the correctness of your code above by typing `nosetests -v test5.py:test_slugging_percentage' in the terminal.  '''




#--------------------------
def runs_created(H, _2B, _3B, HR, BB, AB):
    '''
        compute the expected runs created by a team based upon Bill James' runs created formula.
        Input:
            H: the number of hits in the team, an integer scalar.
            _2B: the number of 2nd base,  an integer scalar (note: python variable names cannot start with a number, so _ is added)
            _3B: the number of 3rd base,  an integer scalar
            HR: the number of home runs,  an integer scalar
            BB: the number of bases on balls (walks),  an integer scalar
            AB: the number of at bats,  an integer scalar
        Output:
            RC: the expected runs created/scored by a team, a float scalar.
    '''
    #########################################
    ## INSERT YOUR CODE HERE

    # compute the total bases
    totalB = (H+BB)*(H+_2B+(2*_3B)+(3*HR))
    Deno = AB+BB
    # compute runs created
    RC = totalB/Deno
    #########################################
    return RC

    ''' TEST: Now you can test the correctness of your code above by typing `nosetests -v test5.py:test_runs_created' in the terminal.  '''




#--------------------------
def win_ratio(RC, RA):
    '''
        compute the expected wining ratio of a team based upon Bill James' Pythagorean expectation.
        Input:
            RC: the number of runs created/scored by a team, an integer scalar.
            RA: the number of runs allowed,  an integer scalar
        Output:
            WR: the projected winning ratio of a team, a float scalar.
    '''
    #########################################
    ## INSERT YOUR CODE HERE
    num = RC**2
    deno = (RC**2)+(RA**2)
    WR = num/deno

    #########################################
    return WR


    ''' TEST: Now you can test the correctness of your code above by typing `nosetests -v test5.py:test_win_ratio' in the terminal.  '''




#--------------------------------------------

''' TEST ALL functions in Problem 5:
        Now you can test the correctness of all the above functions by typing `nosetests -v test5.py' in the terminal.

        If your code passed all the tests, you will see the following message in the terminal:
            ----------- Problem 5 (10 points in total)-------------- ... ok
            (2 points) batting_average ... ok
            (2 points) on_base_percentage ... ok
            (2 points) slugging_percentage ... ok
            (2 points) runs_created ... ok
            (2 points) win_ratio ... ok
            ----------------------------------------------------------------------
            Ran 6 tests in 0.758s

            OK

'''

#--------------------------------------------
