# to debug: run this file in the shell or put a breakpoint pdb in the file
import os
import pandas as pd
home = os.path.join(os.environ['HOME'], 'minicomp', 'raw-data')


def load_raw_data(home = home):
    raw_data = {}

    for fi in os.listdir(home):
        if 'csv' in fi:
            print(fi)
            raw_data[fi]=pd.read_csv(os.path.join(home,fi))
    return raw_data

# if running this script, run this
# if only importing: don't
if __name__=='__main__':
    raw = load_raw_data(100)
    
