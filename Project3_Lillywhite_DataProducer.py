# Project 3 - NCSU ST 554
# Author: Trevor Lillywhite
# Due Data: April 30, 2026

import pandas as pd
import time

def data_source(input_file_name: str):
    '''
    This function takes in a name to an input csv file (same directory level as the .py file and the .ipynb file invoking the .py file). It runs 20 iterations of a loop that randomly samples 5 rows from the input file and outputs those to a .csv file in the folder "stream_catcher". It does not write out indices but it does include column names because the code in the notebook can handle that. There is a 10 second pause between each loop iteration.
    '''
    
    df = pd.read_csv(input_file_name)
    
    for i in range(20):
        sample = df.sample(n = 5, random_state = (42 + i))
        sample.to_csv(f'stream_catcher/output{i}.csv', 
                      index = False,
                      header = True)
        print(f'iteration {i} complete')
        time.sleep(10)
    
    print('all iterations complete')
    return None