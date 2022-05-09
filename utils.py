'''
Utility functions.
------
Author: Muhammad Alrabeiah
Date: May, 2022
'''
import numpy as np
import scipy.io as sio


def cal_stats(imgs):
    """
    It calculates the RGB image mean and standard deviation
    :param imgs: a dataset of images with dimensions (# of images, color, height, width)
    :return: dictionary with mean and std vectors
    """
    m = np.zeros((3,))
    for idx in range(imgs.shape[0]):
        x = imgs[idx,:] # normalize to range [0,1]
        m[0] += x[0,:].sum()
        m[1] += x[1,:].sum()
        m[2] += x[2,:].sum()
    num_pix = x.shape[1]*x.shape[2] # Number of pixels in a color channel
    m = m/(num_pix*(idx+1)) # Compute mean of each color
    print('Mean {0:}, {1:}, and {2:}'.format(m[0], m[1], m[2]))

    std = np.zeros((3,))
    for idx in range(imgs.shape[0]):
        x = imgs[idx,:] # normalize to range [0,1]
        std[0] += ((x[0,:]-m[0])**2).sum()
        std[1] += ((x[1,:]-m[1])**2).sum()
        std[2] += ((x[2,:]-m[2])**2).sum()
    std = np.sqrt( std/(num_pix*(idx+1)) )
    print('Std {0:}, {1:}, and {2:}'.format(std[0], std[1], std[2]))

    stats = {'mean':m, 'std':std}

    return stats



if __name__ == '__main__':
    imgs = sio.loadmat('training.mat')['img']/255
    imgs = imgs.reshape(-1,3,32,32)
    stats = cal_stats(imgs)
    # Test stats:
    img_c = imgs - stats['mean'].reshape(1,3,1,1)
    m = np.mean(img_c[:,1,:])
    print(m)
    # Save stats
    sio.savemat('image_stats.mat',stats)