import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import networkx as nx
from os import listdir
import tarfile
import  tarfile
import pandas as pd
import io

def visualize_sample(sample_nr, dataset =  "data/gnnet-ch23-dataset-cbr-mb"):    
    for folder in listdir(dataset):
        if "results" in folder:
            upper = int(folder.split("-")[-1].split(".")[0])
            lower = int(folder.split("-")[1].split("_")[-1])
            if upper >= sample_nr >= lower :
                print(dataset + "/" + folder)
                tar = tarfile.open(dataset + "/" + folder)
                for member in tar.getmembers():
                    if "input" in member.name:                        
                        f=tar.extractfile(member)
                        content = f.read().decode('utf-8')
                        df = pd.read_csv(io.StringIO(content), delimiter=';', header = None)
                        df.columns = ["Sample","L3_graph","L3_routing","L2_graph","L2_routing","tg"]
                        df = df[df.Sample == sample_nr]

                        return df
                break

    return 0

if __name__ == "__main__":
    sample_info = visualize_sample(182)



