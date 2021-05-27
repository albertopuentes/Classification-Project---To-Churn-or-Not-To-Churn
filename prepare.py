# import splitting and imputing functions
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer


# This function takes in the telco_df generated via acquire.telco_data() function and prepares the data to be split into train, validate & test dataframes 

def prep_df(telco_df):
    # Drop redundant data column 
    prep_df = telco_df.drop(columns=['customer_id'])
    
    # convert the total_charges spaces to zeros  
    prep_df['total_charges'] = prep_df['total_charges'].replace(' ', 0)
    
    # Convert total_charges from a str to a float
    prep_df['total_charges'] = prep_df['total_charges'].astype(float)
    
    # Drop columns with reference data
    prep_df = prep_df.drop(columns=['contract_type', 'internet_service_type', 'payment_type'])
    
    # Replace Yes/No entries with 1/0 across entire df
    prep_df = prep_df.replace({'Yes':1, 'No':0})
    
    # Assumptive Manipulation: conversion of non-service to a 'No'
    prep_df = prep_df.replace({'No internet service':0, 'No phone service':0})
    
    # convert the gender column to is_male and male/female strings to 1/0 values
    prep_df = prep_df.rename(columns={'gender': 'is_male'})

    # replace male/female with 1/0
    prep_df = prep_df.replace({'Male':1, 'Female':0})
    
    return prep_df   

# Train, Validate, Test data split

def telco_split(df):
    '''
    take in a prepped Telco dataframe and return train, validate, and test DataFrames; stratify on churn.
    return train, validate, test DataFrames.
    '''
    train_validate, test = train_test_split(df, test_size=.2, random_state=123, stratify=df.churn)
    train, validate = train_test_split(train_validate, 
                                       test_size=.3, 
                                       random_state=123, 
                                       stratify=train_validate.churn)
    return train, validate, test