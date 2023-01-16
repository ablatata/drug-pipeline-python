# coding: utf-8
# coding: utf-8
import os
import pandas as pd

R = os.path.abspath('../..')
if R not in os.sys.path : 
    S = os.sys.path.insert(0, R)
    
#from drugs_link_graph.data_cleaning.cleaner import Cleaner


def test():
    data = {'id': ["1", "2"], 
            'title': ["Use of Diphenhydramine as an Adjunctive Sedative", "Feasibility of a Randomized Controlled Clinical Trial"], 
            'date': ["1 January 2020", "25/05/2020"],
            'journal': ["Journal of emergency nursing", "Journal of emergency nursing"]
           }
    
    df = pd.DataFrame(data=data)
    
    clean = Cleaner(df)
    cleaned_date = clean.clean_date_column('date')
    cleaned_title = clean.clean_words_column('title')
    cleaned_journal = clean.clean_words_column('journal')
    cleaned_data = clean.deal_with_nan()

    assert len(cleaned_data) == 2
    
    return cleaned_data
    
if __name__ == '__main__':
    cleaned_data = test()
