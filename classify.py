import pandas as pd
import numpy as np
import torch

# only X,Y,result
cls_data = pd.read_csv('data-stats-combs.csv').iloc[:,-3:]

classes = list(pd.unique(cls_data['result']))

for cls in classes:
    subset = cls_data[cls_data['result']==cls]
    print(f"{cls}:\nX: [{subset['X'].min()}, {subset['X'].max()}]\nY: [{subset['Y'].min()}, {subset['Y'].max()}]")

def classify(x, y):
    if y > 6:
        if x < -5:
            return 'Social outcast'
        elif x < 1:
            return 'Simp'
        # not enough data to know for sure
        elif x <= 6:
            return 'Party dude'
        else:
            return 'Chad'
    elif y > 1:
        if x < -3:
            return 'Failed normie'
        elif x < 1:
            return 'Niche normie'
        elif x < 5:
            return 'Normie'
        else:
            return 'Turbo normie'
    elif y > -6:
        if x <= -4:
            return 'Sperg'
        elif x < 0:
            return 'Lame normie'
        elif x < 6:
            return 'Cool normie'
        else:
            return 'Based normie'
    else:
        if x < -6:
            return 'Wizard'
        elif x < 1:
            return 'Edge Lord'
        elif x < 6:
            return 'Sadboy'
        else:
            return 'Sociopath'

mistakes = 0
for idx, row in cls_data.iterrows():
    pred = classify(row['X'], row['Y'])
    actual = row['result']
    if pred != actual:
        print(f"XY: ({row['X']}, {row['Y']}), predicted: {pred}, actual: {actual}")
        mistakes += 1

print(f'mistakes: {mistakes}')