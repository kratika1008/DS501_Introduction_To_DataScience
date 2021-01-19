
#-------------------------------------------------------------------------
# Note: please don't use any additional package except the following packages
import numpy as np
#-------------------------------------------------------------------------
'''
    Problem 1: TicTacToe and MiniMax AI player
    In this problem, you will implement two different AI players for the TicTacToe game.
'''
#--------------------------
def Terms_and_Conditions():
    '''
        By submitting this homework or changing this function, you agree with the following terms:
       (1) Not sharing your code/solution with any student before and after the homework due. For example, sending your code segment to another student, putting your solution online or lending your laptop (if your laptop contains your solution or your Dropbox automatically synchronize your solution between your home computer and your laptop) to another student to work on this homework will violate this term.
       (2) Not using anyone's code in this homework, build your own solution. For example, using some code segments from another student or online resources due to any reason (like too busy recently) will violate this term. Changing other people's code as your solution (such as changing the variable names) will also violate this term.
       (3) When discussing with any other student about this homework, only discuss high-level ideas or using pseudo-code. Don't discuss about the solution at the code level. For example, discussing with another student about the solution of a function (which needs 5 lines of code to solve), and then working on the solution "independently", however the code of the two solutions are exactly the same, or only with minor differences  (like changing variable names) will violate this term.
      All violations of (1),(2) or (3) will be handled in accordance with the WPI Academic Honesty Policy.  For more details, please visit: https://www.wpi.edu/about/policies/academic-integrity/dishonesty
      Historical Data: in one year, we ended up finding 25% of the students in the class violating the terms in their homework submissions and we handled ALL of these violations according to the WPI Academic Honesty Policy.
    '''
    #****************************************
    #* CHANGE CODE HERE
    Read_and_Agree = True  #if you have read and agree with the term above, change "False" to "True".
    #****************************************
    return Read_and_Agree


#-------------------------------------------------------
'''
    Utility Functions: Let's first implement some utility functions for Tic-Tac-Toe game.
    We will need to use them later.
'''
# ----------------------------------------------
def get_valid_moves(s):
    '''
       Get a list of available (valid) next moves from a game state of TicTacToe
        Input:
            s: the current state of the game, an integer matrix of shape 3 by 3.
                s[i,j] = 0 denotes that the i-th row and j-th column is empty
                s[i,j] = 1 denotes that the i-th row and j-th column is taken by "X".
                s[i,j] = -1 denotes that the i-th row and j-th column is taken by the "O".
                For example, the following game state
                 | X |   | O |
                 | O | X |   |
                 | X |   | O |
                is represented as the following numpy matrix in game state
                s= [[ 1 , 0 ,-1 ],
                    [-1 , 1 , 0 ],
                    [ 1 , 0 ,-1 ]]
        Outputs:
            m: a list of possible next moves, where each next move is a (r,c) tuple,
               r denotes the row number, c denotes the column number.
        For example, for the following game state,
                s= [[ 1 , 0 ,-1 ],
                    [-1 , 1 , 0 ],
                    [ 1 , 0 ,-1 ]]
        the valid moves are the empty grid cells:
            (r=0,c=1) --- the first row, second column
            (r=1,c=2) --- the second row, the third column
            (r=2,c=1) --- the third row , the second column
        So the list of valid moves is m = [(0,1),(1,2),(2,1)]
        Hint: you could use np.where() function to find the indices of the elements in an array, where a test condition is true.
        Hint: you could solve this problem using 2 lines of code.
    '''
    #########################################
    ## INSERT YOUR CODE HERE
    p = np.where(s==0)
    m = list(zip(p[0],p[1]))
    #########################################
    return m


    ''' TEST: Now you can test the correctness of your code above by typing `nosetests -v test1.py:test_get_valid_moves' in the terminal.  '''



# ----------------------------------------------
def check_game(s):
    '''
        check if the TicTacToe game has ended or not.
        If yes (game ended), return the game result (1: x_player win, -1: o_player win, 0: draw)
        If no (game not ended yet), return None

        Input:
            s: the current state of the game, an integer matrix of shape 3 by 3.
                s[i,j] = 0 denotes that the i-th row and j-th column is empty
                s[i,j] = 1 denotes that the i-th row and j-th column is taken by "X" player.
                s[i,j] = -1 denotes that the i-th row and j-th column is taken by "O" player.
        Outputs:
            e: the result, an integer scalar with value 0, 1 or -1.
                if e = None, the game has not ended yet.
                if e = 0, the game ended with a draw.
                if e = 1, X player won the game.
                if e = -1, O player won the game.
    '''
    #########################################
    ## INSERT YOUR CODE HERE
    n = s.shape[0]
    e = None
    gameEnded = False
    # check the 7 lines in the board to see if the game has ended.
    d = s.diagonal()
    rd = np.fliplr(s).diagonal()
    if(len(set(d))==1):
        e = d[0]
    elif(len(set(rd))==1):
        e = rd[0]
    if(e == 1 or e ==-1):
        gameEnded=True
    # if the game has ended, return the game result
    if gameEnded!=True:
        for i in range(n):
            if(len(set(s[i]))==1):
                e = s[i][0]
            elif(len(set(s[:,i]))==1):
                e = s[:,i][0]
            if(e == 1 or e ==-1):
                gameEnded=True
                break
    # if the game has not ended, return None
    if gameEnded!=True:
        p = np.argwhere(s==0)
        if(len(p)==0):
            e=0
        else:
            e=None

    #########################################
    return e

    ''' TEST: Now you can test the correctness of your code above by typing `nosetests -v test1.py:test_check_game' in the terminal.  '''



#-------------------------------------------------------
'''
    Here is a Tic-Tac-Toe game engine.
    This can help you understand how the game works.
'''
#-------------------------------------------------------
class TicTacToe:
    '''
        TicTacToe game engine: the goal is to provide a platform for two AI players to play the game in turns and return the game result.
    '''
    # ----------------------------------------------
    def __init__(self):
        ''' Initialize the game state as all zeros (all empty board).  '''
        self.s = np.zeros((3,3))

    # ----------------------------------------------
    def game(self,x,o):
        '''
            run a tie-tac-toe game, letting X and O players to play in turns.  Here we assumes X player moves first in a game.
            Input:
                x: the "X" player (the first mover)
                o: the "O" player (the second mover)
            Outputs:
                e: the result of the game, an integer scalar with value 0, 1 or -1.
                    if e = 0, the game ends with a draw/tie.
                    if e = 1, X player won the game.
                    if e = -1, O player won the game.
        '''
        # repeat until the end of the game
        for _ in range(5):
            e = check_game(self.s) # check if the game has ended already
            if e is not None: # if the game has ended, stop the game and return the result
                break
            r,c = x.play(self.s) # "X" player choose a move
            assert self.s[r,c]== 0 # the move must be valid
            self.s[r,c]=1        # update the game state
            e = check_game(self.s) # check if the game has ended
            if e is not None: # if the game has ended, stop the game and return the result
                break
            r,c = o.play(self.s,-1) # "X" player choose a move
            assert self.s[r,c]== 0 # the move must be valid
            self.s[r,c]=-1  # update the game state
        return e



#-------------------------------------------------------
'''
    AI Player 1 (Random Player): Let's first implement the simplest player agent (Random Agent) to get familiar with TicTacToe AI.
'''
#-------------------------------------------------------
class PlayerRandom:
    '''
        Random player: it chooses a random valid move at each step of the game.
        This player is the simplest AI agent for the tic-tac-toe game.
        It is also the foundation of Monte-Carlo Sampling which we will need to use later.
    '''
    # ----------------------------------------------
    def play(self,s,x=1):
        '''
            The action function, which chooses one random valid move in each step of the game.
            This function will be called by the game at each game step.
            For example, suppose we have 2 random players (say A and B) in a game.
            The game will call the play() function of the two players in turns as follows:

            Repeat until game ends:
                (1) r,c = A.play(game_state, x=1 ) --- "X" player (A) choose a move
                (2) the game updates its game state
                (3) r,c = B.play(game_state, x=-1 ) --- "O" player (B) choose a move
                (4) the game updates its game state

            Input:
                s: the current state of the game, an integer matrix of shape 3 by 3.
                    s[i,j] = 0 denotes that the i-th row and j-th column is empty
                    s[i,j] = 1 denotes that the i-th row and j-th column is taken by "X".
                    s[i,j] = -1 denotes that the i-th row and j-th column is taken by the "O".
                    For example, the following game state
                     | X |   | O |
                     | O | X |   |
                     | X |   | O |
                    is represented as the following numpy matrix
                    s= [[ 1 , 0 ,-1 ],
                        [-1 , 1 , 0 ],
                        [ 1 , 0 ,-1 ]]
               x: the role of the player, x=1 if this agent is the "X" player in the game
                    x=-1 if this agent is the "O" player in the game.
           Outputs:
                r: the row number of the next move, an integer scalar with value 0, 1, or 2.
                c: the column number of the next move, an integer scalar with value 0, 1, or 2.
            For example, in the above game state example, the valid moves are the empty grid cells:
            (r=0,c=1) --- the first row, second column
            (r=1,c=2) --- the second row, the third column
            (r=2,c=1) --- the third row , the second column
            The random player should randomly choose one of the valid moves.
            Hint: you could solve this problem using 3 lines of code.
        '''
        #########################################
        ## INSERT YOUR CODE HERE

        # find all valid moves in the current game state
        m = get_valid_moves(s)
        # randomly choose one valid move
        r,c = m[np.random.choice(len(m))]
        #########################################
        return r,c


    ''' TEST: Now you can test the correctness of your code above by typing `nosetests -v test1.py:test_random_play' in the terminal.  '''



#-----------------------------------------------
'''
    AI Player 2 (MinMax Player): Now let's implement the MinMax agent for the game.
    The goal of this agent is to find the optimal (best) move for the current game state.
    MinMax player will build a fully expanded search tree, where each tree node corresponds to a game state.
    The root of the tree is the current game state.
    Then we compute the score (value) of each node recursively using minmax algorithm.
    Finally, the MinMax agent will choose the child node with the largest value as the next move.

    For example, suppose the current game state is:
            s=[[ 0, 1, 1],
               [ 0,-1,-1],
               [ 1,-1, 1]]
    and it's "O" player's turn.
    Then the search tree will be:
   |-------------------
   |Root Node:
   |    s=[[ 0, 1, 1],
   |       [ 0,-1,-1],
   |       [ 1,-1, 1]]     -- the game state in the node
   |    x=-1               -- it's "O" player's turn at this step of the game
   |    p= None            -- The root node has no parent node
   |    m= None            -- the move it takes from parent node to this node (no parent node)
   |    c=[Child_Node_A, Child_Node_B] -- list of children nodes
   |    v=-1               -- The value of the game state:
   |                            assuming both players follows their optimal moves,
   |                            from this game state,  "O" player will win (-1).
   |----------------------------
      |Child Node A:  ---- If O player chooses the move (r=0,c=0)
      |    s=[[-1, 1, 1],
      |       [ 0,-1,-1],
      |       [ 1,-1, 1]] -- the game state in the node
      |    x= 1           -- it's "X" player's turn
      |    p= Root_Node   -- The parent node is the root node
      |    m= (0,0)       -- from parent node, took the move (r=0, c=0) to reach this node
      |    c=[Grand Child Node C] -- list of children nodes
      |    v= 1           -- The value of the game state:
      |                            assuming both players follows their optimal moves,
      |                            from this game state,  "X" player will win (1).
      |----------------------------
          |Grand Child Node A1: ---- If X player chooses the move (r=1, c=0)
          |    s=[[-1, 1, 1],
          |       [ 1,-1,-1],
          |       [ 1,-1, 1]]    -- the game state in the node
          |    x=-1              -- it's "O" player's turn
          |    p= Child_Node_B   -- The parent node is the child node B
          |    m= (1,0)          -- from parent node, took the move (r=1,c=0) to reach this node
          |    c=[] -- list of children nodes, no child node because the game has ended
          |    v= 0               -- The score of the game state:
          |                          Terminal node, the game ends with a Tie (0).
      |------------------------------
      |Child Node B:  ---- If O player chooses the move (r=1,c=0)
      |    s=[[ 0, 1, 1],
      |       [-1,-1,-1],
      |       [ 1,-1, 1]]     -- the game state in the node
      |    x= 1               -- it's "X" player's turn in this step of the game
      |    p= Root_Node       -- The parent node is the root node
      |    m= (1,0)           -- from parent node, took the move (r=1,c=0) to reach this node
      |    c=[] -- list of children nodes, no child node because the game has ended
      |    v=-1               -- The value of the game state:
      |                           Terminal node, the game ends: O player won (-1)
      |--------------------------


        The tree looks like this:

                          |--> Child Node A (v=0) |--> Grand Child Node A1 (v=0)
        Root Node(v=-1)-->|
                          |--> Child Node B (v=-1)

        In this example, the two children nodes have values as v=0 (child A) and v=-1 (child B).
        The "O" player will choose the child node with the smallest value as the next move.
        In this example, the smallest value is Child Node B (v=-1), so the optimal next move is (r=1, c=0)


------------------------------------------------------------
Now let's implement tree nodes first.
Then we can connect the nodes into a search tree.
------------------------------------------------------------
'''
class Node:
    '''
        Search Tree Node.

        List of Attributes:
            s: the current state of the game, an integer matrix of shape 3 by 3.
                s[i,j] = 0 denotes that the i-th row and j-th column is empty
                s[i,j] = 1 denotes that the i-th row and j-th column is taken by "X".
                s[i,j] = -1 denotes that the i-th row and j-th column is taken by the "O".
            x: who's turn in this step of the game (if X player: x=1, or if O player: x=-1)
            p: the parent node of this node
            m: the move that it takes from the parent node to reach this node.  m is a tuple (r,c), r:row of move, c:column of the move
            c: a python list of all the children nodes of this node
            v: the value of the node (-1, 0, or 1). We assume both players are choosing optimal moves, then this value v represents the best score that "X" player can achieve (1: win, 0:tie, -1: loss)
    '''
    def __init__(self,s,x=1,p=None,c=None,m=None,v=None):
        self.s = s # the current state of the game
        self.x=x # who's turn in this step of the game (X player:1, or O player:-1)
        self.p= p # the parent node of the current node
        self.m=m # the move that it takes from the parent node to reach this node.
                 # m is a tuple (r,c), r:row of move, c:column of the move
        self.c=[] # a list of children nodes
        self.v=v # the value of the node (X player will win:1, tie: 0, lose: -1)

    # ----------------------------------------------
    def expand(self):
        '''
            In order to build a search tree, we first need to implement an elementary operation:
            Expand the current tree node by adding one layer of children nodes.
            Add one child node for each valid next move.
        Input:
            self: the node to be expanded

        For example, if the current node (BEFORE expanding) is like:
       |-------------------
       |Current Node:
       |    s=[[ 0, 1,-1],
       |       [ 0,-1, 1],
       |       [ 0, 1,-1]]     -- the game state in the node
       |    x= 1               -- it's "X" player's turn in this step of the game
       |    p= None
       |    m= None
       |    c=[] -- no children node
       |    v= None
       |-------------------

        There are 3 valid next moves from the current game state.
        AFTER expanding this node, we add three children nodes to the current node.
        The tree looks like this after being expanded:

                            |--> Child Node A
           Current Node --> |--> Child Node B
                            |--> Child Node C

        Here are the details of the tree (attributes of each tree node):
       |-------------------
       |Current Node:
       |    s=[[ 0, 1,-1],
       |       [ 0,-1, 1],
       |       [ 0, 1,-1]]
       |    x= 1        -- it's "X" player's turn in this step of the game
       |    p= None
       |    m= None
       |    c=[Child_A, Child_B, Child_C] -- Three children nodes are created and added here
       |    v= None
       |-------------------------------
               |Child Node A:
               |    s=[[ 1, 1,-1],
               |       [ 0,-1, 1],
               |       [ 0, 1,-1]]
               |    x=-1            -- it's "O" player's turn in this step of the game
               |    p= Current_Node -- The parent node of this node is "Current_Node"
               |    m= (0,0)        -- The move it takes from parent node
               |                         to this node: first row (0), first column (0)
               |    c=[] -- this node has not been expanded yet
               |    v= None
               |-----------------------
               |Child Node B:
               |    s=[[ 0, 1,-1],
               |       [ 1,-1, 1],
               |       [ 0, 1,-1]]
               |    x=-1            -- it's "O" player's turn in this step of the game
               |    p= Current_Node -- The parent node of this node is "Current_Node"
               |    m= (1,0)        -- The move it takes from parent node
               |                        to this node: second row (1), first column (0)
               |    c=[] -- this node has not been expanded yet
               |    v= None
               |-----------------------
               |Child Node C:
               |    s=[[ 0, 1,-1],
               |       [ 0,-1, 1],
               |       [ 1, 1,-1]]
               |    x=-1            -- it's "O" player's turn in this step of the game
               |    p= Current_Node -- The parent node of this node is "Current_Node"
               |    m= (2,0)        -- The move it takes from parent node
               |                        to this node: third row (2), first column (0)
               |    c=[] -- this node has not been expanded yet
               |    v= None
               |-----------------------
            Hint: you could solve this problem using 6 lines of code.
        '''
        #########################################
        ## INSERT YOUR CODE HERE
        # get the list of valid next moves from the current game state
        m = get_valid_moves(self.s)
        if self.x==1:   xVal = -1
        elif self.x==-1: xVal = 1
        # expand the node with one level of children nodes
        for move in m:
            child_s = np.copy(self.s)
            child_s[move] = self.x
            self.c.append(Node(child_s,xVal,self,None,move,None))
        #########################################

    ''' TEST: Now you can test the correctness of your code above by typing `nosetests -v test1.py:test_expand' in the terminal.  '''



    # ----------------------------------------------
    def build_tree(self):
        '''
        Given a tree node (the current state of the game), build a fully-grown search tree, which includes all the possible future game states in the tree.

        For example, the current node is (BEFORE building tree)
        |-------------------
        |Current Node:
        |    s=[[ 0, 1,-1],
        |       [ 0,-1, 1],
        |       [ 0, 1,-1]]     -- the game state in the node
        |    x= 1               -- it's "X" player's turn in this step of the game
        |    p= None
        |    m= None
        |    c=[] -- list of children nodes
        |    v= None
        |-------------------

        AFTER expanding this node, we have a tree as follows:
        The tree looks like this after being expanded:

                                                 |--> Grand Child Node A1 |--> Great Grand Child A11
                            |--> Child Node A -->|
                            |                    |--> Grand Child Node A2
                            |
                            |                    |--> Grand Child Node B1
           Current Node --> |--> Child Node B -->|
                            |                    |--> Grand Child Node B2
                            |
                            |                    |--> Grand Child Node C1
                            |--> Child Node C -->|
                                                 |--> Grand Child Node C2 |--> Great Grand Child C21

       Each node of the tree represents a possible future game state.
       Here are the detailed attribute values of tree nodes:
       --------------------
       |Current Node:
       |    s=[[ 0, 1,-1],
       |       [ 0,-1, 1],
       |       [ 0, 1,-1]]
       |    x= 1        -- it's "X" player's turn in this step of the game
       |    p= None
       |    m= None
       |    c=[Child_A, Child_B, Child_C] -- Three children nodes are created and added here
       |    v= None
       |-------------------------------
           |Child Node A:
           |    s=[[ 1, 1,-1],
           |       [ 0,-1, 1],
           |       [ 0, 1,-1]]
           |    x=-1               -- it's "O" player's turn in this step of the game
           |    p= Current_Node    -- The parent node of this node is "Current_Node"
           |    m= (0,0)           -- The move it takes to from parent node
           |                           to this node is first row (0), first column (0)
           |    c=[Grand_Child_A, Grand_Child_B] -- Two children nodes
           |    v= None
           |-------------------------------
                   |Grand Child Node A1:
                   |    s=[[ 1, 1,-1],
                   |       [-1,-1, 1],
                   |       [ 0, 1,-1]]
                   |    x= 1            -- it's "X" player's turn in this step of the game
                   |    p= Child_Node_A -- The parent node of this node is "Child Node A"
                   |    m= (1,0)        -- The move it takes from parent node
                   |                         to this node: second row (1),first column (0)
                   |    c=[Great_Grand_Child_A11] -- one child node
                   |    v= None
                   |--------------------------------
                           |Great Grand Child Node A11:
                           |    s=[[ 1, 1,-1],
                           |       [-1,-1, 1],
                           |       [ 1, 1,-1]]
                           |    x=-1             -- it's "O" player's turn in this step of the game
                           |    p= Grand_Child_Node_A1  -- The parent node of this node
                           |    m= (2,0)         -- The move from parent node
                           |                        to this node is third row (2),first column (0)
                           |    c=[] -- Terminal node (no child)
                           |    v= None
                   -------------------------
                   |Grand Child Node A2:
                   |    s=[[ 1, 1,-1],
                   |       [ 0,-1, 1],
                   |       [-1, 1,-1]]
                   |    x= 1            -- it's "X" player's turn in this step of the game
                   |    p= Child_Node_A -- The parent node of this node is "Child Node A"
                   |    m= (2,0)        -- The move it takes from parent node
                   |                        to this node: third row (2),first column (0)
                   |    c=[] -- terminal node (game ends), no child node
                   |    v= None
           |-----------------------
           |Child Node B:
           |    s=[[ 0, 1,-1],
           |       [ 1,-1, 1],
           |       [ 0, 1,-1]]
           |    x=-1            -- it's "O" player's turn in this step of the game
           |    p= Current_Node -- The parent node of this node is "Current_Node"
           |    m= (1,0)        -- The move it takes from parent node to this node
           |    c=[] -- this node has not been expanded yet
           |    v= None
           |--------------------------------
                   |Grand Child Node B1:
                   |    s=[[-1, 1,-1],
                   |       [ 1,-1, 1],
                   |       [ 0, 1,-1]]
                   |    x= 1             -- it's "X" player's turn in this step of the game
                   |    p= Child_Node_B  -- The parent node of this node
                   |    m= (0,0)         -- The move it takes from parent node to this node
                   |    c=[]             -- Terminal node (no child)
                   |    v= None
                   -------------------------
                   |Grand Child Node B2:
                   |    s=[[ 0, 1,-1],
                   |       [ 1,-1, 1],
                   |       [-1, 1,-1]]
                   |    x= 1             -- it's "X" player's turn in this step of the game
                   |    p= Child_Node_B  -- The parent node of this node
                   |    m= (2,0)         -- The move it takes from parent node to this node
                   |    c=[] -- Terminal node (no child)
                   |    v= None
           |--------------------------------
           |Child Node C:
           |    s=[[ 0, 1,-1],
           |       [ 0,-1, 1],
           |       [ 1, 1,-1]]
           |    x=-1               -- it's "O" player's turn in this step of the game
           |    p= Current_Node    -- The parent node of this node is "Current_Node"
           |    m= (2,0)           -- The move it takes to from parent node to this node
           |    c=[] -- this node has not been expanded yet
           |    v= None
           |-------------------------------
                   |Grand Child Node C1:
                   |    s=[[-1, 1,-1],
                   |       [ 0,-1, 1],
                   |       [ 1, 1,-1]]
                   |    x= 1               -- it's "X" player's turn in this step of the game
                   |    p= Child_Node_A    -- The parent node of this node is "Child Node A"
                   |    m= (0,0)           -- The move it takes to from parent node to this node
                   |    c=[] -- game ends, no child
                   |    v= None
                   -------------------------
                   |Grand Child Node C2:
                   |    s=[[ 0, 1,-1],
                   |       [-1,-1, 1],
                   |       [ 1, 1,-1]]
                   |    x= 1             -- it's "X" player's turn in this step of the game
                   |    p= Child_Node_A  -- The parent node of this node is "Child Node A"
                   |    m= (1,0)         -- The move it takes from parent node to this node
                   |    c=[Great_Grand_Child_C21] -- one child node
                   |    v= None
                   |--------------------------------
                           |Great Grand Child Node C21:
                           |    s=[[ 1, 1,-1],
                           |       [-1,-1, 1],
                           |       [ 1, 1,-1]]
                           |    x=-1            -- it's "O" player's turn in this step of the game
                           |    p= Grand_Child_Node_C2  -- The parent node of this node
                           |    m= (0,0)        -- The move  from parent node to this node
                           |    c=[] -- Terminal node (no child)
                           |    v= None
                           |------------------------

        Hint: you could use recursion to build the tree and solve this problem using 5 lines of code.
        '''
        #########################################
        ## INSERT YOUR CODE HERE
        # if the game in the current state has not ended yet, expand the current node by one-level of children nodes
        if(check_game(self.s) == None):
            Node.expand(self)
            # recursion: for each child node, call build_tree() function to build a subtree rooted from each child node
            for childNode in self.c:
                Node.build_tree(childNode)
        #########################################


    ''' TEST: Now you can test the correctness of your code above by typing `nosetests -v test1.py:test_build_tree' in the terminal.  '''




    # ----------------------------------------------
    def compute_v(self):
        '''
            Given a fully-built tree, compute optimal values of the all the nodes in the tree using minimax algorithm
            Here we assume that the whole search-tree is fully grown, but no value on any node has been computed yet before calling this function.

            MinMax Algorithm:
            The optimal value of a tree node is defined as follows:
            (1) if the node is a terminal node, the value of the node is the game result (1, -1 or 0)
            (2) if the node is has children nodes,
                    (2.1) if it is X player's turn in the current node:
                            the value of the node is maximum value of all the children nodes' values.
                    (2.2) if it is O player's turn in the current node:
                            the value of the node is minimum value of all the children nodes' values.

            For example, the current game state is
            |-------------------
            |Current Node:
            |    s=[[ 1,-1, 1],
            |       [ 0, 0, 0],
            |       [ 0, 0,-1]]     -- the game state in the node
            |    x= 1               -- it's "X" player's turn in this step of the game
            |    p= None
            |    m= None
            |    c=[] -- list of children nodes
            |    v= None
            |-------------------

            The search tree will have 5 levels of children nodes.
            The first two levels of the tree looks like this:

                                |--> Child Node A -->|--> Grand Child Node A1
                                |     1,-1, 1        |--> Grand Child Node A2
                                |     1, 0, 0        |--> Grand Child Node A3
                                |     0, 0,-1        |--> Grand Child Node A4
                                |
                                |--> Child Node B -->|--> Grand Child Node B1
                                |     1,-1, 1        |--> Grand Child Node B2
                                |     0, 1, 0        |--> Grand Child Node B3
                                |     0, 0,-1        |--> Grand Child Node B4
                                |
              Current Node -->  |--> Child Node C -->|--> Grand Child Node C1
               1,-1, 1          |     1,-1, 1        |--> Grand Child Node C2
               0, 0, 0          |     0, 0, 1        |--> Grand Child Node C3
               0, 0,-1          |     0, 0,-1        |--> Grand Child Node C4
                                |
                                |--> Child Node D -->|--> Grand Child Node D1
                                |     1,-1, 1        |--> Grand Child Node D2
                                |     0, 0, 0        |--> Grand Child Node D3
                                |     1, 0,-1        |--> Grand Child Node D4
                                |
                                |--> Child Node E -->|--> Grand Child Node E1
                                      1,-1, 1        |--> Grand Child Node E2
                                      0, 0, 0        |--> Grand Child Node E3
                                      0, 1,-1        |--> Grand Child Node E4

            If we finish computing the values of all the Grand Children nodes, we have:

                                     (O's turn)
                                |--> Child Node A -->|--> Grand Child Node A1 (v=1)
                                |     1,-1, 1        |--> Grand Child Node A2 (v=1)
                                |     1, 0, 0        |--> Grand Child Node A3 (v=0)
                                |     0, 0,-1        |--> Grand Child Node A4 (v=1)
                                |
                                |--> Child Node B -->|--> Grand Child Node B1 (v=1)
                                |     1,-1, 1        |--> Grand Child Node B2 (v=1)
                                |     0, 1, 0        |--> Grand Child Node B3 (v=0)
                                |     0, 0,-1        |--> Grand Child Node B4 (v=1)
               (X's turn)       |
              Current Node -->  |--> Child Node C -->|--> Grand Child Node C1 (v=0)
               1,-1, 1          |     1,-1, 1        |--> Grand Child Node C2 (v=0)
               0, 0, 0          |     0, 0, 1        |--> Grand Child Node C3 (v=0)
               0, 0,-1          |     0, 0,-1        |--> Grand Child Node C4 (v=-1)
                                |
                                |--> Child Node D -->|--> Grand Child Node D1 (v=1)
                                |     1,-1, 1        |--> Grand Child Node D2 (v=1)
                                |     0, 0, 0        |--> Grand Child Node D3 (v=1)
                                |     1, 0,-1        |--> Grand Child Node D4 (v=1)
                                |
                                |--> Child Node E -->|--> Grand Child Node E1 (v=0)
                                      1,-1, 1        |--> Grand Child Node E2 (v=0)
                                      0, 0, 0        |--> Grand Child Node E3 (v=1)
                                      0, 1,-1        |--> Grand Child Node E4 (v=0)

            In Child Node A, it is "O" player's turn, so the value of Child Node A is the MINIMUM of all its children nodes' values: min(1,1,0,1) = 0
            Similarly, we can compute all the children nodes' (A,B,C,D).

                                     (O's turn)
                                |--> Child Node A -->|--> Grand Child Node A1 (v=1)
                                |     1,-1, 1 (v=0)  |--> Grand Child Node A2 (v=1)
                                |     1, 0, 0        |--> Grand Child Node A3 (v=0)
                                |     0, 0,-1        |--> Grand Child Node A4 (v=1)
                                |
                                |--> Child Node B -->|--> Grand Child Node B1 (v=1)
                                |     1,-1, 1 (v=0)  |--> Grand Child Node B2 (v=1)
                                |     0, 1, 0        |--> Grand Child Node B3 (v=0)
                                |     0, 0,-1        |--> Grand Child Node B4 (v=1)
               (X's turn)       |
              Current Node -->  |--> Child Node C -->|--> Grand Child Node C1 (v=0)
               1,-1, 1          |     1,-1, 1 (v=-1) |--> Grand Child Node C2 (v=0)
               0, 0, 0          |     0, 0, 1        |--> Grand Child Node C3 (v=0)
               0, 0,-1          |     0, 0,-1        |--> Grand Child Node C4 (v=-1)
                                |
                                |--> Child Node D -->|--> Grand Child Node D1 (v=1)
                                |     1,-1, 1 (v=1)  |--> Grand Child Node D2 (v=1)
                                |     0, 0, 0        |--> Grand Child Node D3 (v=1)
                                |     1, 0,-1        |--> Grand Child Node D4 (v=1)
                                |
                                |--> Child Node E -->|--> Grand Child Node E1 (v=0)
                                      1,-1, 1 (v=1)  |--> Grand Child Node E2 (v=0)
                                      0, 0, 0        |--> Grand Child Node E3 (v=1)
                                      0, 1,-1        |--> Grand Child Node E4 (v=0)

            Now the values of all the children nodes of the current node are ready, we can compute the value of the current node.
            In the current node, it is "X" player's turn, so the value of the current node is the MAXIMUM of all its children nodes' values: max(0,0,-1,1,0) = 1

                                     (O's turn)
                                |--> Child Node A -->|--> Grand Child Node A1 (v=1)
                                |     1,-1, 1 (v=0)  |--> Grand Child Node A2 (v=1)
                                |     1, 0, 0        |--> Grand Child Node A3 (v=0)
                                |     0, 0,-1        |--> Grand Child Node A4 (v=1)
                                |
                                |--> Child Node B -->|--> Grand Child Node B1 (v=1)
                                |     1,-1, 1 (v=0)  |--> Grand Child Node B2 (v=1)
                                |     0, 1, 0        |--> Grand Child Node B3 (v=0)
                                |     0, 0,-1        |--> Grand Child Node B4 (v=1)
               (X's turn)       |
              Current Node -->  |--> Child Node C -->|--> Grand Child Node C1 (v=0)
               1,-1, 1 (v=1)    |     1,-1, 1 (v=-1) |--> Grand Child Node C2 (v=0)
               0, 0, 0          |     0, 0, 1        |--> Grand Child Node C3 (v=0)
               0, 0,-1          |     0, 0,-1        |--> Grand Child Node C4 (v=-1)
                                |
                                |--> Child Node D -->|--> Grand Child Node D1 (v=1)
                                |     1,-1, 1 (v=1)  |--> Grand Child Node D2 (v=1)
                                |     0, 0, 0        |--> Grand Child Node D3 (v=1)
                                |     1, 0,-1        |--> Grand Child Node D4 (v=1)
                                |
                                |--> Child Node E -->|--> Grand Child Node E1 (v=0)
                                      1,-1, 1 (v=0)  |--> Grand Child Node E2 (v=0)
                                      0, 0, 0        |--> Grand Child Node E3 (v=1)
                                      0, 1,-1        |--> Grand Child Node E4 (v=0)
            Hint: you could use recursion to compute the values of the current node recursively.
                  you could use 12 lines of code to solve this problem.
        '''
        #########################################
        ## INSERT YOUR CODE HERE
        v = check_game(self.s)
        # (1) if the game has already ended, the value of the node is the game result
        if(v!= None): self.v = v
        # (2) if the game has not ended yet:
        else:
            #   (2.1)first compute values of all children nodes recursively by calling compute_v() in each child node
            for childNode in self.c:
                Node.compute_v(childNode)
        #   (2.2) now the values of all the children nodes are computed, let's compute the value of the current node:
        if(self.p != None and len(self.p.c)!=0):
            maxVal = -5
            minVal = 5
            for c in self.p.c:
                if(c.v == None):
                    continue
                else:
                    maxVal = max(c.v,maxVal)
                    minVal = min(c.v,minVal)
            #(2.2.1) if it is X player's turn, the value of the current node is the max of all children node's values
            if(self.p.x==1):
                self.p.v = maxVal
            #(2.2.2) if it is O player's turn, the value of the current node is the min of all children node's values
            elif(self.p.x==-1):
                self.p.v = minVal
            else:
                self.p.v = 0
        #########################################


    ''' TEST: Now you can test the correctness of your code above by typing `nosetests -v test1.py:test_compute_v' in the terminal.  '''

#-----------------------------------------------
'''
    AI Player 2 (MinMax Player): Now let's implement the MinMax agent for the game.
    The goal of this agent is to find the optimal (best) move for the current game state.
    (1) Build Tree: we will first build a fully-grown search tree, where the root of the tree is the current game state.
    (2) Compute Node Values: Then we compute the value of each node recursively using MinMax algorithm.
    (3) Choose Optimal Next Move: the agent will choose the child node with the largest/smallest value as the next move.
            if the MinMax player is the "X" player in the game, it will choose the largest value among children nodes.
            if the MinMax player is the "O" player in the game, it will choose the smallest value among children nodes.
'''


# ----------------------------------------------
# Let's first implement step (3): choose optimal next move
def choose_optimal_move(n,x=1):
    '''
        Assume we have a fully-grown search tree, and the values of all nodes are already computed.

        (3) Choose Next Move: the agent will choose the child node with the largest/smallest value as the next move.
            if the MinMax player is the "X" player in the game, it will choose the largest value among children nodes.
            if the MinMax player is the "O" player in the game, it will choose the smallest value among children nodes.

       Inputs:
            n: the current node of the search tree, assuming the values in all nodes are already computed.
            x: the role of the player, 1 if you are the "X" player in the game
                    -1 if you are the "O" player in the game.
       Outputs:
            r: the row number of the optimal next move, an integer scalar with value 0, 1, or 2.
            c: the column number of the optimal next move, an integer scalar with value 0, 1, or 2.

        For example, suppose we have the following search tree (X player's turn):
                                |--> Child Node A
                                |    |1,-1, 1|(v=0)
                                |    |1, 0, 0|(m=(1,0))
                                |    |0, 0,-1|
                                |
                                |--> Child Node B
                                |    |1,-1, 1|(v=0)
                                |    |0, 1, 0|(m=(1,1))
                                |    |0, 0,-1|
               (X's turn)       |
              Current Node -->  |--> Child Node C
              |1,-1, 1|(v=1)    |    |1,-1, 1|(v=-1)
              |0, 0, 0|         |    |0, 0, 1|(m=(1,2))
              |0, 0,-1|         |    |0, 0,-1|
                                |
                                |--> Child Node D
                                |    |1,-1, 1|(v=1)
                                |    |0, 0, 0|(m=(2,0))
                                |    |1, 0,-1|
                                |
                                |--> Child Node E
                                     |1,-1, 1|(v=0)
                                     |0, 0, 0|(m=(2,1))
                                     |0, 1,-1|
        The optimal next move will be child node with the largest value (Child Node D).
        So in this example, the next move should be (r=2, c=0)
        Hint: you could solve this problem using 5 lines of code.
    '''
    #########################################
    ## INSERT YOUR CODE HERE
    val = []
    optimalVal = 0
    for c in n.c:
        val.append(c.v)
    if(x==1):
        optimalVal = max(val)
    if(x==-1):
        optimalVal = min(val)
    index = val.index(optimalVal)
    r,c = n.c[index].m
    #########################################
    return r,c

    ''' TEST: Now you can test the correctness of your code above by typing `nosetests -v test1.py:test_choose_optimal_move' in the terminal.  '''


#-------------------------------------------------------
class PlayerMiniMax:
    '''
        Minimax player, who choose optimal moves by searching the tree with min-max.
    '''
    # ----------------------------------------------
    def play(self,s,x=1):
        '''
            The action function of the minimax player, which chooses next move in the game.
            The goal of this agent is to find the optimal (best) move for the current game state.
            (1) Build Tree: we will first build a fully-grown search tree, where the root of the tree is the current game state.
            (2) Compute Node Values: Then we compute the value of each node recursively using MinMax algorithm.
            (3) Choose Next Move: the agent will choose the child node with the largest/smallest value as the next move.
                    if the MinMax player is the "X" player in the game, it will choose the largest value among children nodes.
                    if the MinMax player is the "O" player in the game, it will choose the smallest value among children nodes.
           Inputs:
                s: the current state of the game, an integer matrix of shape 3 by 3.
                    s[i,j] = 0 denotes that the i-th row and j-th column is empty
                    s[i,j] = 1 denotes that the i-th row and j-th column is taken by "X".
                    s[i,j] = -1 denotes that the i-th row and j-th column is taken by the "O".
                x: the role of the player, 1 if you are the "X" player in the game
                    -1 if you are the "O" player in the game.
           Outputs:
                r: the row number of the next move, an integer scalar with value 0, 1, or 2.
                c: the column number of the next move, an integer scalar with value 0, 1, or 2.
          Hint: you could solve this problem using 4 lines of code.
        '''
        #########################################
        ## INSERT YOUR CODE HERE
        n = Node(s, x)
        # (1) build a search tree with the current state as the root node
        n.build_tree()


        # (2) compute values of all tree nodes
        n.compute_v()

        # (3) choose the optimal next move
        r,c = choose_optimal_move(n,x)
        #########################################
        return r,c

    ''' TEST: Now you can test the correctness of your code above by typing `nosetests -v test1.py:test_minmax_play' in the terminal.  '''



#--------------------------------------------

''' TEST Problem 1:
        Now you can test the correctness of all the above functions by typing `nosetests -v test1.py' in the terminal.

        If your code passed all the tests, you will see the following message in the terminal:
            ----------- Problem 1 (45 points in total)--------------------- ... ok
            (5 points) get_valid_moves() ... ok
            (5 points) check_game() ... ok
            (5 points) random play() ... ok
            (5 points) expand ... ok
            (5 points) build_tree ... ok
            (5 points) compute_v() ... ok
            (5 points) choose_optimal_move() ... ok
            (10 points) minmax play() ... ok
            ----------------------------------------------------------------------
            Ran 10 tests in 2.939s
            OK
'''

#--------------------------------------------
