from problem3 import * 
import numpy as np
import sys
import imageio

'''
    Unit test 3:
    This file includes unit tests for problem3.py.
'''

#-------------------------------------------------------------------------
def test_python_version():
    ''' ----------- Problem 3 (25 points in total)---------------------'''
    assert sys.version_info[0]==3 # require python 3 (instead of python 2)

#-------------------------------------------------------------------------
def test_vector_to_image():
    ''' (3 points) vector_to_image'''
    x = np.array([1.,2.,3.,4.])
    i = vector_to_image(x)
    assert type(i)==np.ndarray
    assert i.shape == (2,2)
    i_true = np.array([[1.,2.],
                       [3.,4.]])
    assert np.allclose(i,i_true)


    x = np.array([1.,2.,3.,4.,5.,6.,7.,8.,9.])
    i = vector_to_image(x)
    assert i.shape == (3,3)
    i_true = np.array([[1.,2.,3.],
                       [4.,5.,6.],
                       [7.,8.,9.]])
    assert np.allclose(i,i_true)

    x = np.random.random(4096)

    # call the function
    image = vector_to_image(x)
    
    assert type(image) == np.ndarray
    assert image.shape == (64,64)

    for _ in range(20):
        i = np.random.randint(64)
        j = np.random.randint(64)
        assert image[i,j] == x[i*64+j]
    

#-------------------------------------------------------------------------
def test_load_dataset():
    ''' (2 points) load_dataset'''
    # call the function
    X, y, images = load_dataset()
    assert type(X) == np.ndarray
    assert X.shape == (400,4096)
    assert type(y) == np.ndarray
    assert y.shape == (400,)
    assert type(images) == np.ndarray
    assert images.shape == (400,64,64)
    imageio.imwrite('face.jpg', images[70]) 


#-------------------------------------------------------------------------
def test_compute_mu_image():
    ''' (5 points) compute_mu_image'''
    

    # call the function
    X, _, _ = load_dataset()
    mu = compute_mu_image(X)
    
    assert type(mu) == np.ndarray
    assert mu.shape == (64,64)

    # write average face image to file 'mu.jpg'
    imageio.imwrite('mu.jpg', mu)
    
    # you could take a lot at the average face image in your folder
    
    assert np.allclose([0.40013435, 0.43423545, 0.4762809],mu[0,:3],atol=1e-2)
    assert np.allclose([0.36046496, 0.36678693, 0.37106389],mu[-1,:3],atol=1e-2)

#-------------------------------------------------------------------------
def test_compute_eigen_faces():
    ''' (15 points) compute_eigen_faces'''
    # load the face image dataset 
    X, _, _ = load_dataset()
    P_images, Xp = compute_eigen_faces(X,k= 20)
    assert type(P_images) == list
    assert len(P_images) == 20
    assert type(Xp) == np.ndarray
    assert type(P_images[0]) == np.ndarray
    assert P_images[0].shape == (64,64) 
    assert Xp.shape == (400,20) 

    for i,image in enumerate(P_images):
        imageio.imwrite('eigen_face_%d.jpg' % (i+1), image) 
    # If you are getting errors in the above line, the error is likely to be related to the `centering_X` function in problem2.
    # Note: in order to center X, you don't have to multiply mu with an all-one vector. Use the broadcasting method in numpy: Xc = X - mu

    c = P_images[0]
    assert np.allclose([-0.0041911,  -0.0071095,  -0.00933609],c[0,:3],atol=1e-3) or np.allclose([0.0041911,  0.0071095,  0.00933609],c[0,:3],atol=1e-3)
    assert np.allclose([0.01161627,  0.01290446,  0.01308161],c[-1,:3],atol=1e-3) or np.allclose([-0.01161627, -0.01290446, -0.01308161],c[-1,:3],atol=1e-3)

    # save the results into a file
    np.save('face_pca.npy',Xp)

