import os
import pickle
path = "/home/wandors/Профоблік.dbs"
db ={}

with open(path, "rb") as f:
    text = pickle.load(f)
    f.close()

