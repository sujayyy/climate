# src/surrogate.py
import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader
import numpy as np

class EmissionsToTempDataset(Dataset):
    def __init__(self, X, y):
        self.X = torch.tensor(X, dtype=torch.float32)
        self.y = torch.tensor(y, dtype=torch.float32)
    def __len__(self):
        return len(self.X)
    def __getitem__(self, idx):
        return self.X[idx], self.y[idx]

class SmallMLP(nn.Module):
    def __init__(self, in_dim, out_dim):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(in_dim, 128),
            nn.ReLU(),
            nn.Linear(128, 64),
            nn.ReLU(),
            nn.Linear(64, out_dim)
        )
    def forward(self, x):
        return self.net(x)

def train_surrogate(X, y, epochs=5):
    ds = EmissionsToTempDataset(X,y)
    dl = DataLoader(ds, batch_size=32, shuffle=True)
    model = SmallMLP(X.shape[1], y.shape[1])
    opt = torch.optim.Adam(model.parameters(), lr=1e-3)
    loss_fn = nn.MSELoss()
    for ep in range(epochs):
        tot=0
        for xb, yb in dl:
            pred = model(xb)
            loss = loss_fn(pred, yb)
            opt.zero_grad(); loss.backward(); opt.step()
            tot += loss.item()
        print(f'Epoch {ep} loss {tot/len(dl):.6f}')
    return model

if __name__ == '__main__':
    # toy data: X = emissions summary (e.g., cumulative), y = delta temp
    X = np.random.rand(200, 10)
    y = np.random.rand(200, 1) * 2.0
    model = train_surrogate(X,y, epochs=3)
    print('Trained toy surrogate')
