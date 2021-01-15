import pandas as pd
import numpy as np
import torch

data = pd.read_csv('data-stats-combs.csv', dtype=str)
XY = data.values[:,-3:-1].astype(float)
answers = pd.get_dummies(data[data.columns[:-3]])

answers = answers.values
answers = answers.astype(int)
XY = XY.astype(float)
dataset = torch.utils.data.DataLoader(list(zip(torch.from_numpy(answers), torch.from_numpy(XY))), batch_size=1)

all_weights = pd.read_csv('weights.csv', index_col=0)
x_weights = all_weights.loc['X']
y_weights = all_weights.loc['Y']
# see the diffs after rounding the weights
x_tensor = torch.from_numpy(x_weights.values).float()
y_tensor = torch.from_numpy(y_weights.values).float()
diffs = []
for ans, res in dataset:
    ans, res = ans.float(), res.float()
    pred_res = torch.from_numpy(np.array([[(ans@x_tensor.T).item(),(ans@y_tensor.T).item()]]))
    diff = res.detach().numpy().flatten()-pred_res.detach().numpy().flatten()
    diffs.append(diff)
diffs = np.array(diffs)
stat_corrections = pd.DataFrame(np.hstack((data[data.columns[-10:-3]], diffs)), 
                                columns=list(data.columns[-10:-3])+['difference_X', 'difference_Y'])
stat_corrections.to_csv('stat-corrections.csv', index=False)