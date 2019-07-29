import pandas as pd
import glob2
import os
def convert2hdf(source_dir, desti_dir=os.getcwd()):
    temp = []
    for path_name in glob2.iglob(source_dir+'**/*.txt', recursive=True):
        _, file_name = os.path.split(path_name)
        file_name = file_name.split(".")[0]
        file_name = ''.join([i for i in file_name if not i.isdigit()])
        file_name = file_name.replace("_","")
        data = open(path_name, "r").read()
        temp.append([file_name,data])
    df = pd.DataFrame(temp, columns=["file_name", "data"])
    # print(df)
    df.to_hdf("data.h5", key="df")
    
if __name__ == '__main__':
	txtDir = "./data/"
	convert2hdf(txtDir)
	df = pd.read_hdf('data.h5', 'df')
	print(df)
