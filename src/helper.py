'''
A module containing some helper functions to help with QC
'''

__author__ = 'Simon Lee (slee@celsiustx.com)'

import numpy as np
import project_configs as project_configs
import pandas as pd
import rpy2.robjects as robjects
from rpy2.robjects import pandas2ri
pandas2ri.activate()

def gene_intersection(df1, df2):
    '''
    Takes two dataframes (usually bulk samples and gene signature set), 
    finds the intersection of the two and returns two dataframes with matching gene sets. Required for SVR'

    Parameters:
        df1 (pd.Dataframe): numpy array of predicted values
        df2 (pd.Dataframe): numpy array of true values
    
    Returms: 
        The dataframes filtered with the gene intersections
    '''
    set1 = set(df1.index)
    set2 = set(df2.index)
    intersection = set1.intersection(set2)
    inter = list(intersection)

    signature = df1.filter(items=inter,axis=0)
    bulk = df2.filter(items=inter,axis=0)

    assert signature.shape[0] == bulk.shape[0], "Shapes of the two dataframes don't match"
    return signature, bulk

def flatten(predicted_values, true_values):
    '''
    Uses np.ravel() to flatten a matrix into a 1D array

    Parameters:
        predicted_values (nd.array): numpy array of predicted values
        true_values (nd.array): numpy array of true values

    '''
    ind_names = predicted_values.index.intersection(true_values.index)
    print(ind_names)
    col_names = predicted_values.columns.intersection(true_values.columns)
    print(col_names)

def rds_to_df(file_path):
    '''
    pass in a .rds R data file with relative path and get a pandas df in return

    Parameters:
        file_path: the file with relative path to .rds data file (e.g. preds matrix)
    
    Returns:
        df: a pandas dataframe object of the rds file
    '''
    readRDS = robjects.r['readRDS']
    file = readRDS(file_path)
    df = pandas2ri.ri2py(file)
    return df

