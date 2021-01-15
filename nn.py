import torch
import torch.nn as nn
import torch.optim as optim
import pandas as pd
import numpy as np

class SingleLayerNeuralNetwork(nn.Module):
    def __init__(self, input_dim, output_dim):
        super().__init__()
        self.input_dim = input_dim
        self.output_dim = output_dim
        self.layer = nn.Linear(self.input_dim, self.output_dim, bias=False)
    
    def forward(self, data):
        out = self.layer(data)
        return out

data = pd.read_csv('data-m111111-ignore-stats.csv', dtype=str)
XY = data.values[:,-2:].astype(float)
answers = pd.get_dummies(data[data.columns[:-2]])

answers = answers.values
answers = answers.astype(int)
XY = XY.astype(float)
# reserve 20 trials as testing data
CUTOFF = answers.shape[0]-20
train_ans, train_res = answers[:CUTOFF], XY[:CUTOFF]
test_ans, test_res = answers[CUTOFF:], XY[CUTOFF:]
# load the data as answers-results tuples
train_dataset = list(zip(torch.from_numpy(train_ans), torch.from_numpy(train_res)))
test_dataset = list(zip(torch.from_numpy(test_ans), torch.from_numpy(test_res)))
train_loader = torch.utils.data.DataLoader(train_dataset, batch_size=1)
test_loader = torch.utils.data.DataLoader(test_dataset, batch_size=1)

# fix random seed
torch.manual_seed(0)

model = SingleLayerNeuralNetwork(answers.shape[1], XY.shape[1])
optimizer = optim.SGD(model.parameters(), lr=1e-4, momentum=0.1)
criterion = nn.L1Loss()
losses = []
EPOCHS = 10000
for epoch in range(EPOCHS):
    loss = 0
    for ans, res in train_loader:
        ans, res = ans.float(), res.float()
        optimizer.zero_grad()
        pred_res = model(ans)
        train_loss = criterion(pred_res, res)
        train_loss.backward()
        optimizer.step()
        loss += train_loss.item()
    losses.append(loss)
    if (epoch+1)%100==0:
        print(f'epoch: {epoch+1}/{EPOCHS}, loss: {loss}')
    if loss <= 0.5:
        break

params = list(model.parameters())

x_weights = params[0][0].detach()
columns = pd.get_dummies(data[data.columns[:-2]]).columns
x_weights = pd.DataFrame(np.array([x_weights.numpy()]), columns=columns)
# observe from the .csv files that X is always in increments of 0.5
x_weights = x_weights.applymap(lambda val: round(val*2)/2)

y_weights = params[0][1].detach()
y_weights = pd.DataFrame(np.array([y_weights.numpy()]), columns=columns)
# observe from the .csv files that Y is always in increments of 0.25
y_weights = y_weights.applymap(lambda val: round(val*4)/4)

all_weights = pd.concat([x_weights, y_weights], ignore_index=True)
all_weights.index = ['X','Y']
all_weights.to_csv('weights.csv')