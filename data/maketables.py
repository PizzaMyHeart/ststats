#!/usr/bin/python3

import pandas as pd

year = ''
filename = ''

def read_txt(filename):
    with open(filename, 'r') as src:
        values = [line for line in src]
        return values


def build_dict(values):
    data = {'specialty': [],
            'level': [],
            'applications': [],
            'posts': [],
            'ratio': []}

    data['specialty'] = values[0::5]
    data['level'] = values[1::5]
    data['applications'] = values[2::5]
    data['posts'] = values[3::5]
    data['ratio'] = values[4::5]
    
    return data



data = build_dict(read_txt(filename))


df = pd.DataFrame.from_dict(data)
df['year'] = year
pd.DataFrame.to_csv(df, f'{year}.csv')
