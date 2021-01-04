from torch.utils.data import Dataset
import numpy as np
from PIL import Image
from torchvision import transforms

class DataHandler_Points(Dataset):
    def __init__(self, X, Y=None, select=True):
        
        self.select = select
        if not self.select:
        	self.X = X.astype(np.float32)
        	self.Y = Y
        else:
        	self.X = X.astype(np.float32)  #For unlabeled Data

    def __getitem__(self, index):
    	if not self.select:
    		x, y = self.X[index], self.Y[index]
    		return x, y, index
    	else:
        	x = self.X[index]              #For unlabeled Data
        	return x, index

    def __len__(self):
        return len(self.X)

class DataHandler_MNIST(Dataset):

    def __init__(self, X, Y=None, select=True):
        self.select = select
        transform = transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.1307,), (0.3081,))])
        if not self.select:
            self.X = X
            self.Y = Y
            self.transform = transform
        else:
            self.X = X
            self.transform = transform

    def __getitem__(self, index):
        if not self.select:
            x, y = self.X[index], self.Y[index]
            x = Image.fromarray(x)
            x = self.transform(x)
            return x, y, index

        else:
            x = self.X[index]
            x = Image.fromarray(x)
            x = self.transform(x)
            return x, index

    def __len__(self):
        return len(self.X)