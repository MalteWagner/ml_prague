from os import listdir, rename
#Brings testdata in correct format


path = "data\gnnet-ch23-test-dataset"

folders = listdir(path)

for folder in folders:
    if "results" in folder:
        rename(path + "\\" + folder, path + "\\" + folder.replace("ch23_","ch23-"))

