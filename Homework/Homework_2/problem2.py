from problem1 import elo_rating
import numpy as np
#-------------------------------------------------------------------------
'''
    Problem 2:
    In this problem, you will use the Elo rating algorithm in problem 1 to rank the NCAA teams, based upon a dataset of game results.
'''

#--------------------------
def import_team_names(filename ='ncaa_teams.txt'):
    '''
        import a list of team names from a txt file.
        Each line of the file contains one team name. The ordering of the names indicates the indices of the teams.
        For example, the first line contains the name of the 0-th (index) team: "Liberty"
                     the second line contains the name of the 1-th (index) team: "Randolph Col"
        These indices will be used later in the game results:
        For example, if team 0 wins and team 1 loses in a game, the result file "ncaa_results.csv" will contain a line: "0, 1".
        Input:
                filename: the name of txt file, a string
        Output:
                team_names: the list of for team names, a python list of string values, such as ['team a', 'team b','team c'].
        Hint: NumPy has a function, called loadtxt(), to load an array from text file.
        To load strings into the array, you could set the dtype parameter in the function.
    '''
    #########################################
    ## INSERT YOUR CODE HERE
    team_names = list(np.loadtxt(filename,delimiter='\n',dtype='str'))
    #########################################
    return team_names

    ''' TEST: Now you can test the correctness of your code above by typing `nosetests -v test2.py:test_import_team_names' in the terminal.  '''



#--------------------------
def import_W(filename ='ncaa_results.csv'):
    '''
        import the matrix W of game results from a CSV file.
        In the CSV file, each line contains the result of one game. For example, (i,j) in the line represents the i-th team won, the j-th team lost in the game.
        Input:
                filename: the name of csv file, a string
        Output:
                W: the game result matrix, a numpy integer array of shape (n by 2)
        Hint: NumPy has a function, called loadtxt(), to load an array from text file.
        To load integers into the array, you could set the dtype parameter in the function.
    '''
    #########################################
    ## INSERT YOUR CODE HERE
    W = np.loadtxt(filename,delimiter=',',dtype='int')
    #########################################
    return W

    ''' TEST: Now you can test the correctness of your code above by typing `nosetests -v test2.py:test_import_W' in the terminal.  '''



#--------------------------
def team_rating(resultfile = 'ncaa_results.csv',
                teamfile='ncaa_teams.txt',
                K=16.):
    '''
        Rate the teams based upon the game results imported from a CSV file.
        (1) import the W matrix from `resultfile` file.
        (2) compute Elo ratings of all the teams
        (3) return a list of team names sorted by descending order of Elo ratings

        Input:
                resultfile: the csv filename for the game result matrix, a string.
                teamfile: the text filename for the team names, a string.
                K: a float scalar value, which is the k-factor of Elo rating system

        Output:
                top_teams: the list of team names in descending order of their Elo ratings, a python list of string values, such as ['Randolph Col', 'Liberty', ... ].
                top_ratings: the list of elo ratings in descending order, a python list of float values, such as ['600.', '500.','300.'].

    '''
    #########################################
    ## INSERT YOUR CODE HERE

    # load team names from 'teamfile'
    team_names = import_team_names(teamfile)

    # load game results from 'resultfile'
    W = import_W(resultfile)
    n = len(team_names)
    # compute Elo rating of all the teams
    R_new = elo_rating(W,n,K)
    # sort team names according to their Elo ratings
    for i in range(len(R_new)):
        for j in range(len(R_new)-i-1):
            if(R_new[j]<R_new[j+1]):
                R_new[j],R_new[j+1]=R_new[j+1],R_new[j]
                team_names[j],team_names[j+1]=team_names[j+1],team_names[j]
    top_teams = team_names
    top_ratings = R_new
    #########################################
    return top_teams, top_ratings




#--------------------------------------------

''' TEST ALL:
        Now you can test the correctness of all the above functions by typing `nosetests -v test2.py' in the terminal.

        If your code passed all the tests, you will see the following message in the terminal:
            ----------- Problem 2 (20 points in total)-------------- ... ok
            (5 points) import_team_names ... ok
            (5 points) import_W ... ok
            (10 points) team_rating ... ok

            ----------------------------------------------------------------------
            Ran 4 tests in 0.220s

            OK
'''

#--------------------------------------------
