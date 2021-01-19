from problem2 import *
from problem1 import PlayerMiniMax
import numpy as np
import sys

'''
    Unit test 2:
    This file includes unit tests for problem2.py.
'''

#-------------------------------------------------------------------------
def test_python_version():
    ''' ----------- Problem 2 (55 points in total)---------------------'''
    assert sys.version_info[0]==3 # require python 3 (instead of python 2)

#-------------------------------------------------------------------------
def test_sample():
    '''(10 points) sample'''
    #------------------------
    s=np.array([ [ 0, 1, 1],
                 [ 0,-1, 1],
                 [-1, 1,-1]])
    sc=np.array([[ 0, 1, 1],
                 [ 0,-1, 1],
                 [-1, 1,-1]])
    n = MCNode(s,x=-1) # "O" player's turn
    assert np.allclose(s,sc) # the game state should not change after simulation
    v=0
    for _ in range(100):
        e=sample(n)
        assert e==-1 or e==1
        v+=e
    assert np.abs(v)<25  # the two results should have roughly the same chance

    #------------------------
    s=np.array([[ 0, 1, 1],
                [-1,-1, 1],
                [-1, 1,-1]])
    n = MCNode(s,x=1) # X player's turn
    for _ in range(100):
        e=sample(n)
        assert e==1

    #------------------------
    s=np.array([[ 0, 1, 0],
                [-1,-1, 1],
                [-1, 1, 1]])
    n = MCNode(s,x=-1) # O player's turn
    for _ in range(100):
        e=sample(n)
        assert e==-1

    #------------------------
    s=np.array([[ 0, 1, 1],
                [ 0,-1, 1],
                [ 0,-1,-1]])

    n = MCNode(s,x=1) # X player's turn
    v=0
    for _ in range(100):
        e=sample(n)
        assert e==-1 or e==1
        v+=e
    assert np.abs(v)<25  # X player has 1/2 chance to win and 1/2 to lose

    #------------------------
    # Terminal node, the game has already ended, the simulation result should always be the same.
    s=np.array([[-1, 0, 0],
                [ 1,-1, 1],
                [ 0, 1,-1]]) # terminal node: O player won
    n = MCNode(s,x=1)
    for _ in range(100):
        assert sample(n)==-1
    
    s_=np.array([[-1, 0, 0],
                 [ 1,-1, 1],
                 [ 0, 1,-1]])
    assert np.allclose(n.s,s_) # the game state should not change after simulation


    s=np.array([[-1,-1, 1],
                [ 1, 1,-1],
                [-1, 1, 1]])
    n = MCNode(s)
    for _ in range(100):
        assert sample(n)==0

    #------------------------
    s=np.array([[ 0, 0, 0],
                [ 0, 1, 0],
                [ 0, 0, 0]])
    n = MCNode(s,x=-1)
    v = 0
    for _ in range(1000):
        e = sample(n)
        assert e==-1 or e==1 or e==0
        v += e 
    assert np.abs(v-500) <100

#-------------------------------------------------------------------------
def test_expand():
    '''(5 points) expand'''

    # Current Node (root)
    s=np.array([[0, 1,-1],
                [0,-1, 1],
                [0, 1,-1]])
    n = MCNode(s,x=1) #it's X player's turn
    # expand
    sc=expand(n)
    assert n.x==1
    assert len(n.c) ==3 

    assert type(sc)==MCNode
    assert sc.p == n
    assert sc.x==-1
    assert sc.p==n
    assert sc.c==[]
    assert sc.v==0
    assert sc.N==0

    s_=np.array([[0, 1,-1],
                 [0,-1, 1],
                 [0, 1,-1]])
    # the current game state should not change after expanding
    assert np.allclose(n.s,s_) 
    for c in n.c:
        assert c.x==-1
        assert c.p==n
        assert c.c==[]
        assert c.v==0
        assert c.N==0

    # child node A
    s=np.array([[ 1, 1,-1],
                [ 0,-1, 1],
                [ 0, 1,-1]])
    c = False
    for x in n.c:
        if np.allclose(x.s,s):
            c=True
            assert x.m==(0,0)
    assert c

    # child node B
    s=np.array([[ 0, 1,-1],
                [ 1,-1, 1],
                [ 0, 1,-1]])
    c = False
    for x in n.c:
        if np.allclose(x.s,s):
            c=True
            assert x.m==(1,0)
    assert c

    # child node C
    s=np.array([[ 0, 1,-1],
                [ 0,-1, 1],
                [ 1, 1,-1]])
    c = False
    for x in n.c:
        if np.allclose(x.s,s):
            c=True
            assert x.m==(2,0)
    assert c

    # the selected child node should be in the children list
    c = False
    for x in n.c:
        if sc==x:
            c=True
    assert c

    #--------------------------

    # Current Node (root)
    s=np.array([[ 1, 1,-1],
                [ 0,-1, 1],
                [ 0, 1,-1]])
    n = MCNode(s,-1) #it's O player's turn
    sc=expand(n)
    assert n.x==-1
    assert len(n.c) ==2
    assert type(sc)==MCNode
    assert sc.p == n
    assert sc.x==1
    assert sc.p==n
    assert sc.c==[]
    assert sc.v==0
    assert sc.N==0

    for c in n.c:
        assert c.x==1
        assert c.p==n
        assert c.c==[]
        assert c.v==0
        assert c.N==0

    # child node A
    s=np.array([[ 1, 1,-1],
                [-1,-1, 1],
                [ 0, 1,-1]])
    c = False
    for x in n.c:
        if np.allclose(x.s,s):
            c=True
            assert x.m==(1,0)
    assert c

    # child node B
    s=np.array([[ 1, 1,-1],
                [ 0,-1, 1],
                [-1, 1,-1]])
    c = False
    for x in n.c:
        if np.allclose(x.s,s):
            c=True
            assert x.m==(2,0)
    assert c

    # the selected child node should be in the children list
    c = False
    for x in n.c:
        if sc==x:
            c=True
    assert c

    #---------------------------
    n = MCNode(np.zeros((3,3)),1)
    sc=expand(n)
    assert n.x==1
    assert len(n.c) ==9
    a=False
    for c in n.c:
        assert c.x==-1
        assert c.p==n
        assert c.c==[]
        assert np.sum(c.s)==1
        assert c.v==0
        assert c.N==0
        if sc==c:
            a=True
    assert a # the selected child node should be in the children list



#-------------------------------------------------------------------------
def test_backprop():
    '''(5 points) backprop'''
    s=np.array([[ 0, 0, 0],
                [-1, 1, 1],
                [ 0, 0,-1]])
    r = MCNode(s,x=1) # X player's turn 
    expand(r) # expand the root node with one level of children nodes
    # simulation 1
    c1 = r.c[1] # suppose the second child node is selected 
    backprop(c1, e=1) # run a simulation on c, suppose the result is X player won
    assert c1.v ==1 # won one game in the simulation
    assert c1.N ==1 # number of simulations in the node 
    assert r.v ==1 
    assert r.N ==1


    # simulation 2
    c2 = r.c[2] # suppose the third child node is selected
    expand(c2) # expand the tree with one level of children nodes
    c2c0 = c2.c[0] # suppose the first grand child is selected
    backprop(c2c0,e=-1) # run a simulation, suppose the game result: O player won
    assert c2c0.v ==-1 
    assert c2c0.N ==1
    assert c2.v ==-1 
    assert c2.N ==1
    assert r.v ==0 
    assert r.N ==2
    assert c1.v ==1
    assert c1.N ==1
    c2c1 = c2.c[1] 
    assert c2c1.v ==0 
    assert c2c1.N ==0


    # simulation 3
    c2c1 = c2.c[1] # suppose the second child is selected
    backprop(c2c1,e=0) # run a simulation: a tie in the game
    assert c2c1.v ==0 
    assert c2c1.N ==1
    assert c2.v ==-1 
    assert c2.N ==2
    assert r.v ==0 
    assert r.N ==3
    assert c2c0.v ==-1 
    assert c2c0.N ==1
    assert c1.v ==1 # won one game in the simulation
    assert c1.N ==1 # number of simulations in the node 


#-------------------------------------------------------------------------
def test_compute_UCB():
    '''(5 points) compute_UCB'''

    # X player's turn, want to maximize the average score in vi/ni
    u = compute_UCB(1,1,1,x=1)
    assert u==1.

    # O player's turn, want to minimize the average score in vi/ni
    u = compute_UCB(-1,1,1,x=-1)
    assert u==1.

    # X player's turn, want to maximize the average score in vi/ni
    u = compute_UCB(1,2,2,x=1)
    assert np.allclose(u,1.172, atol=1e-3)

    # O player's turn, want to minimize the average score in vi/ni
    u = compute_UCB(-1,2,2,x=-1)
    assert np.allclose(u,1.172, atol=1e-3)

    # X player's turn, want to maximize the average score in vi/ni
    u = compute_UCB(6,50,100,x=1)
    assert np.allclose(u,0.4665, atol=1e-3)

    # O player's turn, want to minimize the average score in vi/ni
    u = compute_UCB(-6,50,100,x=-1)
    assert np.allclose(u,0.4665, atol=1e-3)

    # X player's turn, want to maximize the average score in vi/ni
    u = compute_UCB(6,50,100,x=1,c=2.)
    assert np.allclose(u,0.7269, atol=1e-3)

    # O player's turn, want to minimize the average score in vi/ni
    u = compute_UCB(-6,50,100,x=-1,c=2.)
    assert np.allclose(u,0.7269, atol=1e-3)

    u = compute_UCB(0,0,100,x=1, c=2.)
    assert np.allclose(u,float('inf'), atol=1e-3)

    u = compute_UCB(0,0,100,x=-1, c=2.)
    assert np.allclose(u,float('inf'), atol=1e-3)


#-------------------------------------------------------------------------
def test_select_a_child():
    '''(5 points) select_a_child'''

    # A parent node with two children nodes 
    s=np.array([[ 1, 1,-1],
                [ 0,-1,-1],
                [ 0, 1, 1]])
    p = MCNode(s,x=-1) # O player's turn
    expand(p) # expand the root node with one level of children nodes
    c1,c2=p.c

    # set the node statistics (this is only used for testing, in the real game, the statistics will be different from these numbers)
    p.v=-6
    p.N=12
    c1.v=-1
    c1.N=2
    c2.v=-5
    c2.N=10
    # select the child node with the highest UCB score
    c = select_a_child(p)
    assert c ==c1

    #----------------------
    p.v=-10
    p.N=20
    c1.v=-5
    c1.N=10
    c2.v=-5
    c2.N=10
    # select the child node with the highest UCB score
    c = select_a_child(p)
    assert c ==c1 # a tie in UCB score, use index as tie-breaker

    #----------------------
    p.v=-6
    p.N=20
    c1.v=-1
    c1.N=10
    c2.v=-5
    c2.N=10
    # select the child node with the highest UCB score
    c = select_a_child(p)
    assert c ==c2 

    #----------------------
    # A parent node with three children nodes 
    s=np.array([[ 0,-1,-1],
                [ 0, 1, 1],
                [ 0,-1, 1]])
    p = MCNode(s, x=1) # X player's turn
    expand(p) # expand the root node with one level of children nodes
    c1,c2,c3=p.c

    p.v=1
    p.N=1
    c1.v=1
    c1.N=1
    c = select_a_child(p)
    assert c ==c2

    #----------------------
    p.v=2
    p.N=2
    c2.v=1
    c2.N=1
    c = select_a_child(p)
    assert c ==c3

    #----------------------
    p.v=1
    p.N=3
    c3.v=-1
    c3.N=1
    c = select_a_child(p)
    assert c ==c1

    #----------------------
    p.v=2
    p.N=4
    c1.v=2
    c1.N=2
    c = select_a_child(p)
    assert c == c2


#-------------------------------------------------------------------------
def test_selection():
    '''(5 points) selection'''
    #----------------------
    # The root node is a leaf node
    s=np.array([[ 0,-1, 1],
                [ 0, 0, 1],
                [ 0,-1, 1]])
    p = MCNode(s, x=-1) # O player's turn
    c = selection(p)
    assert c == p

    #----------------------
    # tree with one level of children nodes
    s=np.array([[ 1, 1,-1],
                [ 0,-1,-1],
                [ 0, 1, 1]])
    p = MCNode(s,x=-1) # O player's turn
    expand(p) # expand the root node with one level of children nodes
    c1,c2=p.c

    p.v=-6
    p.N=12
    c1.v=-1
    c1.N=2
    c2.v=-5
    c2.N=10

    c = selection(p)
    assert c ==c1


    p.v=-10
    p.N=20
    c1.v=-5
    c1.N=10
    c2.v=-5
    c2.N=10
    # select the child node with the highest UCB score
    c = selection(p)
    assert c ==c1 # a tie in UCB score, use index as tie-breaker

    # A parent node with three children nodes 
    s=np.array([[ 0,-1,-1],
                [ 0, 1, 1],
                [ 0,-1, 1]])
    p = MCNode(s, x=1) # X player's turn
    expand(p) # expand the root node with one level of children nodes
    c1,c2,c3=p.c

    p.v=1
    p.N=1
    c1.v=1
    c1.N=1
    c = selection(p)
    assert c ==c2

    #----------------------
    p.v=2
    p.N=2
    c2.v=1
    c2.N=1
    c = selection(p)
    assert c ==c3

    #----------------------
    p.v=1
    p.N=3
    c3.v=-1
    c3.N=1
    c = selection(p)
    assert c ==c1

    #----------------------
    p.v=2
    p.N=4
    c1.v=2
    c1.N=2
    c = selection(p)
    assert c == c2


    #----------------------
    # tree with two levels of children nodes
    s=np.array([[ 0, 0,-1],
                [-1, 1, 1],
                [ 0, 0, 0]])
    p = MCNode(s,x=1) # X player's turn
    expand(p) # expand the root node with one level of children nodes
    p.v=0
    p.N=5
    for c in p.c:
        c.v=0
        c.N=1
        expand(c) # expand the second level children nodes

    for j in range(4): 
        for i in range(5): 
            l = selection(p)
            assert l==p.c[i].c[j]
            p.c[i].c[j].N=1
            p.c[i].N+=1
            p.N+=1

    p.c[1].v=1
    p.c[1].c[2].v=-1
    l = selection(p)
    assert l == p.c[1].c[2]
    

#-------------------------------------------------------------------------
def test_build_tree():
    '''(5 points) build_tree'''
    #--------------------------
    s=np.array([[ 0, 1, 1],
                [-1, 1,-1],
                [ 0,-1, 1]])

    n = MCNode(s,x=-1) # O player's turn
    # run one iteration 
    build_tree(n,1)
    assert len(n.c)==2 
    assert n.N == 1
    assert n.v == 1

    for c in n.c:
        assert c.x==1
        assert c.p==n
        assert c.c==[]

    c = 0 
    for x in n.c:
        if x.N>0:
            c+=1
            assert x.v==1
            assert x.N==1
    assert c==1

    # run another iteration 
    build_tree(n,1)
    assert len(n.c)==2 
    assert n.N == 2
    assert n.v == 2

    for c in n.c:
        assert c.x==1
        assert c.p==n

    c = 0 
    for x in n.c:
        assert x.v==1
        assert x.N==1
        if len(x.c)==1:
            c+=1
    assert c==1

    # run two more iterations
    build_tree(n,2)
    assert n.N == 4
    assert n.v == 4

    for c in n.c:
        assert c.x==1
        assert c.p==n

    count=0
    for x in n.c:
        assert len(x.c)==1
        assert x.v==2
        assert x.N==2
        c=x.c[0]
        assert c.x==-1
        assert c.p==x
        assert c.N==c.v 
        assert c.N==1 or c.N==2
        if c.N==2:
            count+=1
    assert count ==1

    #--------------------------

    s=np.array([[ 0, 1, 1],
                [ 0,-1, 0],
                [ 0, 0, 0]])
    n = MCNode(s,x=-1)
    build_tree(n,1000)
    assert n.x ==-1
    assert n.N == 1000

    s1=np.array([[-1, 1, 1],
                 [ 0,-1, 0],
                 [ 0, 0, 0]])

    for x in n.c:
        if np.allclose(x.s,s1):
            assert x.x == 1
            assert x.p == n
            assert x.N > 900
            assert np.abs(x.v) < 50
            c1=x
   
    s2=np.array([[-1, 1, 1],
                 [ 0,-1, 0],
                 [ 0, 0, 1]]) 
    for x in c1.c:
        if np.allclose(x.s,s2):
            assert x.x ==-1
            assert x.p == c1
            assert x.N > 800
            assert np.abs(x.v) < 50
            c2=x

    s3=np.array([[-1, 1, 1],
                 [ 0,-1,-1],
                 [ 0, 0, 1]]) 
    for x in c2.c:
        if np.allclose(x.s,s3):
            assert x.x == 1
            assert x.p == c2
            assert x.N > 700
            assert np.abs(x.v) < 50
            c3=x

    s4=np.array([[-1, 1, 1],
                 [ 1,-1,-1],
                 [ 0, 0, 1]]) 
    for x in c3.c:
        if np.allclose(x.s,s4):
            assert x.x == -1
            assert x.p == c3
            assert x.N > 600
            assert np.abs(x.v) < 50


#-------------------------------------------------------------------------
def test_choose_optimal_move():
    '''(5 points) choose_optimal_move()'''
    #-------------------------
    s=np.array([[ 1,-1, 1],
                [ 0, 0,-1],
                [ 0, 1,-1]])
    n = MCNode(s, x=1)
    build_tree(n,100)
    r,c=choose_optimal_move(n)
    assert r == 2
    assert c == 0

    #-------------------------
    s=np.array([[ 1,-1, 1],
                [ 0, 1,-1],
                [ 0, 1,-1]])
    n = MCNode(s, x=-1)
    build_tree(n,100)
    r,c=choose_optimal_move(n)
    assert r == 2
    assert c == 0

    #-------------------------
    s=np.array([[ 1,-1, 1],
                [ 0, 0, 0],
                [ 0, 0, 0]])
    n = MCNode(s, x=-1)
    build_tree(n,200)
    r,c=choose_optimal_move(n)
    assert r == 1
    assert c == 1


#-------------------------------------------------------------------------
def test_MCTS_play():
    '''(10 points) MCTS play'''
    p =PlayerMCTS()
    s=np.array([[ 0,-1,-1],
                [ 0, 1, 0],
                [ 0, 0, 0]])
     
    r,c=p.play(s)
    assert r ==0
    assert c ==0

    s=np.array([[ 0, 0,-1],
                [ 0, 1,-1],
                [ 0, 0, 0]])
     
    r,c=p.play(s)
    assert r ==2
    assert c ==2


    s=np.array([[ 0, 0, 1],
                [ 0,-1, 1],
                [ 0, 0, 0]])
     
    r,c=p.play(s,x=-1)
    assert r ==2
    assert c ==2


    '''random vs MCTS'''

    p1 = PlayerMCTS()
    p2 = PlayerRandom()
    w=0
    for i in range(10):
        g = TicTacToe()
        g.s=np.array([[ 0,-1, 1],
                      [-1, 1,-1],
                      [ 0,-1,-1]])
        e = g.game(p1,p2)
        w += e
    assert w==10

    w=0
    for i in range(10):
        g = TicTacToe()
        g.s=np.array([[ 0,-1, 1],
                      [-1, 1,-1],
                      [-1, 1, 0]])
        e = g.game(p1,p2)
        w += e
    assert w==0

    ''' Minimax vs MCTS '''

    p1 = PlayerMCTS()
    p2 = PlayerMiniMax()
    w=0
    for i in range(10):
        g = TicTacToe()
        g.s=np.array([[ 0, 0, 1],
                      [ 0,-1, 0],
                      [ 1,-1, 0]])
        e = g.game(p1,p2)
        w += e
    assert w==0


    w=0
    for i in range(10):
        g = TicTacToe()
        g.s=np.array([[ 0, 0, 0],
                      [ 0, 0, 0],
                      [ 1,-1, 0]])
        e = g.game(p1,p2)
        w += e
    print(w)
    assert w>5
