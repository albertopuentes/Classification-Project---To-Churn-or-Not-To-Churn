import pandas as pd
import numpy as np
import os
from env import host, username, password


# Get Connection
def get_connection(db, username=username, host=host, password=password):
    '''
    This function uses my info from my env file to
    create a connection url to access the Codeup SQL db.
    '''
    return f'mysql+pymysql://{username}:{password}@{host}/{db}'

# Get Telco Data
def telco_data():
    '''
    This function reads the telco_churn data from the Codeup db into a df
    '''
    
    # Create SQL query.
    sql_query = '''SELECT * FROM customers
                JOIN contract_types USING (contract_type_id)
                JOIN internet_service_types USING (internet_service_type_id)
                JOIN payment_types USING (payment_type_id)'''

    # Read in DataFrame from Codeup db.
    df = pd.read_sql(sql_query, get_connection('telco_churn'))

    return df