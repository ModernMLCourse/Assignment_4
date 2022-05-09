'''
Construct neural network
--------------------------
Author: Muhammad Alrabeiah
Date: May, 2022
'''
import torch.nn as nn


class CNN(nn.Module): # Read about class inheritance
    def __init__(self,
                 inp_dim, # Number of color channels
                 out_dim, # Number of classes
                 ):
        super().__init__() # Read about super in Python classes. Useful reference: https://www.educative.io/edpresso/what-is-super-in-python

        # Conv blocks
        self.conv_b_1 = ConvBlock(
            #TODO build first conv stack
        )
        self.conv_b_2 = ConvBlock(
            #TODO build second conv stack
        )

        # Fully-Connected blocks
        self.dense_b_1 = DenseBlock(
            #TODO build first dense stack
        )
        self.dense_b_2 = DenseBlock(
            #TODO build output dense stack
        )

    def forward(self,x):
        x = self.conv_b_1(x)
        x = self.conv_b_2(x)
        x = #TODO convert tensor from shape (batch, channel, height, width) to (batch, channel*heigh*width)
        x = self.dense_b_1(x)
        x = self.dense_b_2(x)
        return x


class ConvBlock(nn.Module):
    def __init__(self,
                 kernel, # kernel size
                 inp_ch, # number of input channels
                 out_ch # number of output channels
                 ):
        super().__init__()

        self.conv_1 = #TODO implement 2D convolution with padding (output has same size a input)
        self.relu_1 = #TODO implement relu activation
        self.conv_2 = #TODO implement 2D convolution with padding (output has same size a input)
        self.relu_2 = #TODO implement relu activation
        self.max_pool = # TODO implement max-pooling with 2 by 2 kernel such that the output has 1/2 input size at each spatial dimension (i.e., 1/2 width, 1/2 height)

    def forward(self,x):
        #TODO define the forward pass
        return x


class DenseBlock(nn.Module):
    def __init__(self,
                 inp, # Input dimensions (not including batch size)
                 out, # Output dimensions (not including batch size)
                 act_type='relu'):
        super().__init__()

        self.fc = #TODO implement a linear combiner
        if act_type == 'relu': # Think carefully why if statement is needed here!!
            self.relu = #TODO implement a relu activation
        else:
            self.relu = None

    def forward(self,x):
        #TODO define forward pass
        return x

