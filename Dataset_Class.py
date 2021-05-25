import os
from torch.utils.data import Dataset
import pandas as pd
import numpy as np

path = '/Users/mac_admin/Desktop/MIDAS/mark1.csv'

mnist_images = pd.read_csv(path)
mnist_images.head