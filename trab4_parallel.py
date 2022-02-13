import os
import time
from matplotlib.axis import XAxis
import requests

import functools as ft
import multiprocessing as mp

import matplotlib.pyplot as plt

def download(link, file_dir):
    try:
        file_name = link.split("/")[-1]
        con = requests.get(link)
        open(file_name, 'wb').write(con.content)
        print(" {} baixou {}".format(mp.current_process().name  ,file_name))
    except Exception as e:
        print("ERRO: ", e)


if __name__ == "__main__":

    current_dir = os.path.abspath(__file__)
    file_dir = os.path.dirname(current_dir) #pega o diretorio atual para o download

    links = ["http://212.183.159.230/5MB.zip",
            "http://212.183.159.230/10MB.zip",
            "http://212.183.159.230/20MB.zip",
            "http://212.183.159.230/50MB.zip",
            "http://212.183.159.230/100MB.zip",
            "http://212.183.159.230/200MB.zip",
            "http://212.183.159.230/512MB.zip"
            ]
    
    threads = [2, 4, 8]
    t1 = 151.42115887533264
    x_axis = []
    y_axis = []
    for i in threads:
        time_ini = time.time()
        pool = mp.Pool(i) #numero de threads que serao criadas
        funct_part = ft.partial(download, file_dir = file_dir) 
        res = pool.map(funct_part, links)
        pool.close()
        pool.join()

        time_exec = (time.time() - time_ini)
        print("Tempo de execucao com {} threads: {} s\n".format(i, time_exec))
        x_axis.append(i)
        y_axis.append(t1/time_exec)

    plt.xlabel = "Threads"
    plt.ylabel = "Speedup"
    plt.plot(x_axis, y_axis)
    plt.show()