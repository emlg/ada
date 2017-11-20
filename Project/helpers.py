import pandas as pd
import px_reader as px
import matplotlib.pyplot as plt

def read_file(file):
    px_obj = px.Px('data/' + file)
    return px_obj.pd_dataframe()


def string_to_float(s):
    res = []
    val = -1
    for v in s:
        if v == '-':
            val = 0
        else:
            val = float(v.replace(';', ''))
        res.append(val)
    return res

def parse_df(df, nb_to_discard):
    for c in df.columns[nb_to_discard:]:
        #print(c)
        df[c] = string_to_float(df[c])
    return df
