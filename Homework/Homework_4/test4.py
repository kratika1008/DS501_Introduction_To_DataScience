from problem3 import load_dataset 
from problem4 import * 
import sys
import numpy as np
import imageio

'''
    Unit test 4:
    This file includes unit tests for problem4.py.
'''

#-------------------------------------------------------------------------
def test_python_version():
    ''' ----------- Problem 4 (20 points in total)---------------------'''
    assert sys.version_info[0]==3 # require python 3 (instead of python 2)


#-------------------------------------------------------------------------
def test_compute_distance():
    '''(10 points) compute_distance'''
    #-------------------------------
    # an example matrix (two features, 3 instances)
    X = np.array([[0., 0.],
                  [1., 0.],
                  [1., 1.]])
    q = np.array([1., 1.])
    # call the function
    s = compute_distance(X,q)
    
    assert type(s) == np.ndarray
    assert s.shape == (3,)
    assert s.dtype == float
    assert np.allclose(s, [1.41421356,1,0],atol=1e-3)


    X = np.array([[1., 0., 0.],
                  [0., 1., 0.],
                  [1., 1., 1.]])
    q = np.array([1., 1.,1.])
    s = compute_distance(X,q)
    assert np.allclose(s, [1.41421356,1.41421356,0],atol=1e-3)



    X = np.array([[1., 0., 0.],
                  [0., 1., 0.],
                  [1., 1., 0.],
                  [1., 1., 1.]])
    q = np.array([1., 1.,1.])
    s = compute_distance(X,q)
    assert np.allclose(s, [1.41421356,1.41421356,1,0],atol=1e-3)


#-------------------------------------------------------------------------
def test_face_recognition():
    '''(10 points) face_recognition'''
    #-------------------------------
    # an example matrix: 2 features (k=2), 3 face images (n=3)
    Xp = np.array([[0., 1.],# the two dimensional features of the first face image (after PCA)
                   [1., .5],# the two dimensional features of the second face image (after PCA)
                   [0., 0.]])# the two dimensional features of the third face image (after PCA)
    q = np.array([1., 1.]) # the two dimensional features of the query face image
    # call the function
    ids = face_recognition(Xp,q)
    
    assert type(ids) == np.ndarray
    assert ids.shape == (3,)
    assert ids.dtype == int 

    assert ids.tolist() == [1,0,2]

    #-------------------------------
    qid = 7*10  # use one image as the query image

    Xp = np.load('face_pca.npy')
    q = Xp[qid,:]

    # call the function
    ids =face_recognition(Xp,q)
    
    assert type(ids) == np.ndarray
    assert ids.shape == (400,)
    assert ids.dtype == int 

    # the most similar image should be the query image itself
    assert ids[0] == qid 
    X, l, images = load_dataset()
    imageio.imwrite('query.jpg', images[qid])
    #scipy.misc.imsave('query.jpg', images[qid]) 

    # save the top 10 similar images to the query
    for i in range(10):
        x = images[ids[i]]
        imageio.imwrite('result_%d.jpg' % (i+1), x)
        #scipy.misc.imsave('result_%d.jpg' % (i+1), x) 
    
    assert ids[:4].tolist() ==[70, 71, 75, 74]


