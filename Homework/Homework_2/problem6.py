import pandas as pd
import numpy as np
from problem3 import filtering, sum_column
from problem5 import runs_created
#-------------------------------------------------------------------------
'''
    Problem 6: Player selection for Oakland A's Team (OAK)
    In this problem, you will choose baseball players for Oakland A's using different methods.
'''

#--------------------------
def sum_salaries(T, D):
    '''
        Given a team of players (T), compute the sum of salaries of all the players in the team.
        Input:
            T: a python list of playerID's, for example, ['zitoba01', 'hiljuer01', ...]
            D: a data frame loaded from 'Batting2001AJS.csv', which we processed in problem4.py.
        Output:
            S: an integer scalar, the sum of salaries of all the players in the team.
    '''
    #########################################
    ## INSERT YOUR CODE HERE
    Y = filtering(D,'playerID',T)
    S = sum_column(Y,'salary')

    #########################################
    return S

    ''' TEST: Now you can test the correctness of your code above by typing `nosetests -v test6.py:test_sum_salaries' in the terminal.  '''




#--------------------------
def sum_stat(T, D, key='H'):
    '''
        Given a team of players (T), compute the sum of game statistics of all the players in the team.
        For example, suppose we have a team with two players, the number of hits: 100, 200.
        Then the sum of hits in the team will be: 100+200 = 300
        Input:
            T: a python list of playerID's, for example, ['zitoba01', 'hiljuer01', ...]
            D: a data frame loaded from 'Batting2001AJS.csv', which we processed in problem4.py.
            key: the column to be summed, for example, 'H' represents the number of hits
        Output:
            S: an integer scalar, the sum of statistics of all the players in the team.
    '''
    #########################################
    ## INSERT YOUR CODE HERE
    Y = filtering(D,'playerID',T)
    S = sum_column(Y,key)

    #########################################
    return S

    ''' TEST: Now you can test the correctness of your code above by typing `nosetests -v test6.py:test_sum_stat' in the terminal.  '''



#--------------------------
def runs(T, D):
    '''
        compute the expected runs created by a team based upon Bill James' runs created formula.
        You need to first compute the total number of hits (H) in the team, and total number of second base (_2B) in the team, etc.
        Then you could use Bill James' runs created formula to compute the expected runs created by the team.
        Input:
            T: a python list of playerID's, for example, ['zitoba01', 'hiljuer01', ...]
            D: a data frame loaded from 'Batting2001AJS.csv', which we processed in problem4.py.
        Output:
            RC: the expected runs created/scored by a team, a float scalar.
    '''
    #########################################
    ## INSERT YOUR CODE HERE
    H = sum_stat(T, D, key='H')
    _2B = sum_stat(T, D, key='2B')
    _3B = sum_stat(T, D, key='3B')
    HR = sum_stat(T, D, key='HR')
    BB = sum_stat(T, D, key='BB')
    AB = sum_stat(T, D, key='AB')

    RC = runs_created(H, _2B, _3B, HR, BB, AB)
    #########################################
    return RC

    ''' TEST: Now you can test the correctness of your code above by typing `nosetests -v test6.py:test_runs' in the terminal.  '''


#-------------------------------------------------------------------------
# Team Building Methods
#-------------------------------------------------------------------------


#--------------------------
def scout():
    '''
        Hand-pick three players for OAK in 2002 to replace Jason Giambi, Johnny Damon and Jason Isringhausen.
        Please manually look through the player information in file "Batting2001AJS.csv" and build the OAK team by hand.
        (1) Please note that the overall budget for OAK team is $40,004,167.
        So the sum of salaries in your team should NOT exceed this budget.
        (2) the number of players in the team should be at least 20.
        (3) the expected number of runs created by the team should be at least 700
        (4) the new player chosen cannot be the members of OAK team in year 2001.
        Output:
            T: a python list of three playerID's, for example, ['zitoba01', 'hiljuer01', 'jonesan01']
    '''
    #########################################
    ## INSERT YOUR CODE HERE
    T = ['perryhe01','maynebr01','alicelu01']
    #########################################
    return T

    ''' TEST: Now you can test the correctness of your code above by typing `nosetests -v test6.py:test_scout' in the terminal.  '''




#--------------------------
def rank_BA(D, t=300,max_salary=1200000):
    '''
        Rank the players based upon Batting Average (BA).
        The players with the highest BA will be ranked to the top.
        Note, we want to exclude small samples, like 1/1 (H/AB) = 100% (BA).
        So if the number of AB for a player is smaller than a threshold (t), we will simply set the BA = 0 for that player.
        If a player's salary is higher than the max_salary, we will also set his BA =0, to ignore expensive players.
        Input:
            D: a data frame loaded from 'Batting2001AJS.csv', which we processed in problem4.py.
            t: an integer scalar, the threshold on AB (at-Bat).
            max_salary: an integer scalar, the maximum salary that we can afford for a player.
        Output:
            R: a python list of playerID's, for example, ['zitoba01', 'hiljuer01', ...], with descending order of BA scores.
    '''
    #########################################
    ## INSERT YOUR CODE HERE
    X = D.copy()
    X['BA']=X['H']/X['AB']
    X.to_csv('kratika.csv', index=False)
    X.loc[(X.salary>max_salary) | (X.AB<t), 'BA'] = 0.0
    X = X.sort_values('BA',ascending=False)
    R = X.playerID.tolist()
    #########################################
    return R


    ''' TEST: Now you can test the correctness of your code above by typing `nosetests -v test6.py:test_rank_BA' in the terminal.  '''


#--------------------------
def rank_OBP(D,t=300,max_salary=1200000):
    '''
        Rank the players based upon On Base Percentage(OBP)
        The players with the highest OBP will be ranked to the top.
        Note, we want to exclude small samples, like 1/1 (H/AB) = 100% (BA).
        So if the number of AB is smaller than a threshold t, we will simply set the OBP = 0
        If a player's salary is higher than the max_salary, we will also set his OBP =0, to ignore expensive players.
        Input:
            D: a data frame loaded from 'Batting2001AJS.csv', which we processed in problem4.py.
            t: an integer scalar, the threshold on AB (at-Bat).
            max_salary: an integer scalar, the maximum salary that we can afford for a player.
        Output:
            R: a python list of playerID's, for example, ['zitoba01', 'hiljuer01', ...], with descending order of OBP scores.
    '''
    #########################################
    ## INSERT YOUR CODE HERE
    X = D.copy()
    X['OBP']=(X['H']+X['BB']+X['HBP'])/(X['AB']+X['BB']+X['HBP']+X['SF'])
    X.loc[(X.salary>max_salary) | (X.AB<t), 'OBP'] = 0.0
    X = X.sort_values('OBP',ascending=False)
    R = X.playerID.tolist()
    #########################################
    return R


    ''' TEST: Now you can test the correctness of your code above by typing `nosetests -v test6.py:test_rank_OBP' in the terminal.  '''







#--------------------------------------------

''' TEST ALL functions in Problem 6:
        Now you can test the correctness of all the above functions by typing `nosetests -v test6.py' in the terminal.

        If your code passed all the tests, you will see the following message in the terminal:
            ----------- Problem 5 (15 points in total)-------------- ... ok
            (2 points) sum_salaries ... ok
            (2 points) sum_stat ... ok
            (2 points) runs ... ok
            (3 points) scout ... ok
            (3 points) rank_BA ... ok
            (3 points) rank_OBP ... ok

            ----------------------------------------------------------------------
            Ran 7 tests in 0.758s

            OK

'''

#--------------------------------------------





#--------------------------------------------

''' FINAL TEST of your submission:
        Now you can test the correctness of all the problems in this homework by typing `nosetests -v' in the terminal.

        If your code passed all the tests, you will see the following message in the terminal:

            ----------- Problem 1 (30 points in total)-------------- ... ok
            (10 points) compute_EA ... ok
            (10 points) compute_RA ... ok
            (10 points) elo_rating ... ok
            ----------- Problem 2 (20 points in total)-------------- ... ok
            (5 points) import_team_names ... ok
            (5 points) import_W ... ok
            (10 points) team_rating ... ok
            ---------- Problem 3 (10 points in total) ------------ ... ok
            (1 points) dataframe ... ok
            (1 points) load_csv ... ok
            (1 points) search_height ... ok
            (1 points) save_csv ... ok
            (1 points) sum_column ... ok
            (2 points) aggregate ... ok
            (2 points) join ... ok
            (1 points) filtering ... ok
            ---------- Problem 4 (15 points in total) ------------ ... ok
            (2 points) load_batting ... ok
            (2 points) search_batting ... ok
            (3 points) aggregate_batting ... ok
            (3 points) join_batting ... ok
            (2 points) search_salary ... ok
            (3 points) join_salary ... ok
            ----------- Problem 5 (10 points in total)-------------- ... ok
            (2 points) batting_average ... ok
            (2 points) on_base_percentage ... ok
            (2 points) slugging_percentage ... ok
            (2 points) runs_created ... ok
            (2 points) win_ratio ... ok
            ----------- Problem 5 (15 points in total)-------------- ... ok
            (2 points) sum_salaries ... ok
            (2 points) sum_stat ... ok
            (2 points) runs ... ok
            (3 points) scout ... ok
            (3 points) rank_BA ... ok
            (3 points) rank_OBP ... ok
            ----------------------------------------------------------------------
            Ran 38 tests in 2.838s

            OK

'''

#--------------------------------------------
