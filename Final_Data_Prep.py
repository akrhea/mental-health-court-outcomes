#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 16:08:54 2020

@author: kelseymarkey
"""

'''
Split Data into Train / Validate / Test Sets
Returns a static validation set with divisions based on timeline to reduce 
leakage and ensure that we only ever predict forward in time. Potential danger 
of bias because training set will have higher proportion of "finalized" rows.

'''    
def get_train_val_test (df, train_size, test_size, val_size): 
  #takes in df (assumes target variable = 'MHI') and 
  #train, test, and val sizes (fractions of 1)
  #returns xtrain, xval, xtest, ytrain, yval, ytest

    #check that specificed sizes sum to 1
    if train_size + test_size + val_size != 1:
      print('error: train_size + test_size + val_size must sum to 1')
      return 

    #sort ascending by received date
    sorted_df = df.sort_values(axis = 0, by=['received_date'])
    sorted_df = sorted_df.drop(columns = 'received_date')

    #set x and y
    x = sorted_df.drop('MHI', axis=1)
    y = sorted_df['MHI']

    total_size = len(x)

    #first train_size % indices in train
    xtrain = x.iloc[:int(round(train_size*total_size))]
    ytrain = y.iloc[:int(round(train_size*total_size))]

    #next val_size % indices in val
    xval = x.iloc[int(round(train_size*total_size)):int(round((train_size+val_size)*total_size))]
    yval = y.iloc[int(round(train_size*total_size)):int(round((train_size+val_size)*total_size))]

    #final test_size % indices in test
    xtest = x.iloc[int(round((train_size+val_size)*total_size)):-1]
    ytest = y.iloc[int(round((train_size+val_size)*total_size)):-1]

    return xtrain, xval, xtest, ytrain, yval, ytest