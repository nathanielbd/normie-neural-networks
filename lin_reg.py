import torch
import pandas as pd
import numpy as np

data = pd.read_csv('data-m111111-ignore-stats.csv', dtype=str)
XY = data.values[:,-2:].astype(float)

# one-hot encode the categorical data
answers = pd.get_dummies(data[data.columns[:-2]])

from sklearn.linear_model import LinearRegression
reg = LinearRegression(fit_intercept=False).fit(answers, XY)
vals = pd.DataFrame([[round(val*2)/2 for val in reg.coef_[0]], 
    [round(val*4)/4 for val in reg.coef_[1]]], columns=pd.get_dummies(data[data.columns[:-2]]).columns)
vals.index = ['X', 'Y']
vals.to_csv('weights.csv')

answers = answers.values
answers = answers.astype(int)
XY = XY.astype(float)
# load the data as answers-results tuples
dataset = list(zip(torch.from_numpy(answers), torch.from_numpy(XY)))
loader = torch.utils.data.DataLoader(dataset, batch_size=1)

all_weights = pd.read_csv('weights.csv', index_col=0)
x_weights = all_weights.loc['X']
y_weights = all_weights.loc['Y']
# see the diffs after rounding the weights
x_tensor = torch.from_numpy(x_weights.values).float()
y_tensor = torch.from_numpy(y_weights.values).float()
for ans, res in loader:
    ans, res = ans.float(), res.float()
    pred_res = torch.from_numpy(np.array([[(ans@x_tensor.T).item(),(ans@y_tensor.T).item()]]))
    diff = res.detach().numpy().flatten()-pred_res.detach().numpy().flatten()
    print(f'diff: {diff}')

# NOTE: stat correction for M111111 is [-2, -0.25]