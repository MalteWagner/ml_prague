from os import listdir
import tarfile

def get_traffic(return_mode = "both", file_path = "data/gnnet-ch23-dataset-cbr-mb"):
    '''
        Returns path, flow for the whole train set
    '''
    
    infos_path   = []
    infos_flow   = []

    for folder in listdir(file_path):
        if "results" in folder:
            tar = tarfile.open(file_path + "/" + folder)
            for member in tar.getmembers():
                if "experimentResults.txt" in member.name:                        
                    f=tar.extractfile(member)
                    for line in f.readlines():
                        infos_path.append(line.decode('utf-8').strip("\n").split(";")[:-1])
                if "experimentResultsFlows.txt" in member.name:                        
                    f=tar.extractfile(member)
                    for line in f.readlines():
                        infos_flow.append(line.decode('utf-8').strip("\n").split(";")[:-1])
                    
    samples_path = []
    for i,info in enumerate(infos_path):
        data = []
        first_ele = info[0].split("|")
        data.append(first_ele[1])
        for ele in info:
            if "|" not in ele:
                data.append(ele)
        samples_path.append({
        "infos":first_ele[0],
        "data":data
    })
        
    for i,sample in enumerate(samples_path):
        for j,path in enumerate(sample["data"]):
            samples_path[i]['data'][j] = path.split(",")


    samples_flow = []
    for i,sample in enumerate(infos_flow):
        samples_flow.append([])
        for j,ele in enumerate(sample):
            samples_flow[i].append(1)
            if ":" in ele:
                samples_flow[i][j] = ele.split(":")

    for i, info in enumerate(samples_flow):
        for j, path in enumerate(info):
            if type(path) == str:
                samples_flow[i][j] = [path.split(",")]
            if type(path) == list:
                samples_flow[i][j] = [x.split(",") for x in path]
    if return_mode == "both":
        return samples_path,samples_flow
    elif return_mode == "path":
        return samples_path
    elif return_mode == "flow":
        return samples_flow
    else:
        print("Pass 'both', 'path' or 'flow' as return_mode")


if __name__ == "__main__":
    path, flow = get_traffic()

    # Acces a specific Router -> Router data via [src_router * N + dst_router] (index starts at 0, N is number of routers in Topology)
    # ADD PROPERTIES (list of 18 properties)
    src = 1
    dst = 3
    router = 5

    # 5 Router --> 25 Verbindungsmöglichkeiten
    # 0 -> 0  == 0
    # 0 -> 1  == 1 
    #  ....
    # 1 -> 0  == 5
    # path < N²


    # Get path property: samples_path[sample_nr]['data'][path][property]
    print(float(path[154]['data'][23][3]))

    # Get flow property: samples_flow[sample_nr][path][flow_id][property]
    print(float(flow[1200][1][0][3]))