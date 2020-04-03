#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 11:48:54 2020

@author: kelseymarkey
"""

def is_binary(series, allow_na=False):
    '''
    Helper function for check_allcols_are_binary
    '''

    if allow_na:
        series.dropna(inplace=True)
    return sorted(series.unique()) == [0, 1]


def check_allcols_are_binary(df, start_string):
    ''' 
    Takes a OHE df and a string and checks if all columns starting with 
    that string are binary. If all columns are binary it returns the list of
    all column names, otherwise it returns a list of non_binary_cols.
    
    df: dataframe containing the OHE columns and data
    start_string: string that the OHE columns starts with (i.e. 'gender') 
    would return OHE columns ['gender_female', 'gender_male', 'gender_unknown']
    '''
    
    col_selection = [i for i in list(df.columns) if i.startswith(start_string)]
    non_binary_cols = []
    for column in col_selection:
        if is_binary(df[column]) != True:
            non_binary_cols.append(column)
    if non_binary_cols == []:
        print('All columns binary, returning complete column list')
        return col_selection
    else:
        print('Some columns not binary, returning list of non-binary columns')
        return non_binary_cols
    
    
def undo_ohe_cols(df, col_subset):
    ''' 
    Takes a OHE df and a list of BINARY columns and undoes the OHE of those
    columns, returning a single series with original values in it.
    
    df: dataframe containing the OHE columns and data 
    col_subset: list of binary OHE columns on which you want to undo OHE
    '''

    df_subset = df[df.columns & col_subset]
    def undo_binary(row):
        for c in df_subset.columns:
            if row[c]==1:
                return c
    single_col = df_subset.apply(undo_binary, axis=1)
    return single_col


''' 
Some code to test the above functions:

import pandas as pd
import numpy as np
import pickle
import os

os.chdir("..")
total_df = pd.read_pickle('total_df.pckl.gz', compression = 'gzip')

race_cols = check_allcols_are_binary(total_df, 'race')

single_race_col = undo_ohe_cols(total_df, race_cols)
'''