#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd

"""
Created on Sat Jan 25 16:08:54 2020

@author: kelseymarkey
edited by akrhea
"""

def remove_final_dummy(df):
    '''
    Remove final dummy variable of each categorical feature.
    Changes df in-place.

    Assumes df has been 'exploded' by one-hot encoding.
    '''

    #read in pre-exploded non-OHE df, with data still in categorical format
    cat_df = pd.read_pickle('init_clean.pckl.gz', compression = 'gzip')

    #list of all categorical columns to get dummies for
    #excluding ID numbers, numerical features, datetime features, binary features
    cat_cols = ['offense_category', 'charge_offense_title', 'chapter', 'act', 
                'section', 'class', 'aoic', 'event', 'gender', 'race', 
                'law_enforcement_agency', 'unit', 'incident_city', 'updated_offense_category']
    for col in cat_cols:
        final_value = col+"_"+cat_df[col].unique()[-1]
        df.drop(columns=final_value, inplace=True)
    return
 

def get_train_val_test (df, train_size, test_size, val_size): 
    '''
    Split Data into Train / Validate / Test Sets
    Returns a static validation set with divisions based on timeline to reduce 
    leakage and ensure that we only ever predict forward in time. Potential danger 
    of bias because training set will have higher proportion of "finalized" rows.
    '''   

    #uses "timeline" method

    #takes in df (assumes target variable = 'MHI') and 
    #train, test, and val sizes (fractions of 1)
    #returns xtrain, xval, xtest, ytrain, yval, ytest
    #check that specificed sizes sum to 1
    assert train_size + test_size + val_size == 1, 'train_size + test_size + val_size must sum to 1'

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


def get_train_test (df, train_size, test_size): 
    #used for getting train/test split for training final model
    #no validation set

    #uses "timeline" method

    #takes in df (assumes 'MHI' is target variable)
    #takes in train and test sizes (fractions of 1)
    #returns training df and test df

    #check that specificed sizes sum to 1
    assert train_size + test_size == 1, 'train_size + test_size must sum to 1'
        
    #sort ascending by received date
    sorted_df = df.sort_values(by=['received_date'])
    sorted_df = sorted_df.drop('received_date', axis=1)

    total_size = len(sorted_df)

    #first train_size % indices in train
    train = sorted_df.iloc[:int(round(train_size*total_size))]

    #final test_size % indices in test
    test = sorted_df.iloc[int(round(train_size*total_size)):-1]

    return train, test



'''
Downsampling the training set
'''

def downsample(df, pct_MHI1): 
  #takes in percentage from 1 to 50
  #samples all MHI==1 cases
  #samples from MHI==0 cases such that downsampled_df has pct_MHI1 % positive cases

  #split into MHI 1 and MHI 0 
  MHI1 = df[df['MHI'] == 1]
  MHI0 = df[df['MHI'] == 0]

  #count number of MHIs
  count_MHI1 = len(MHI1)

  #compute number of negative cases to sample
  num_MHI0 = count_MHI1 * int(round((100-pct_MHI1)/pct_MHI1))

  #sample from negative cases
  MHI0_sample = MHI0.sample(n=num_MHI0, random_state=42)

  #append sampled negative cases to all positive cases
  downsampled_df = MHI1.append(MHI0_sample)

  return downsampled_df
