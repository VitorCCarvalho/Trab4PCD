import os
import time
import requests


if __name__ == "__main__":

    current_dir = os.path.abspath(__file__)
    file_dir = os.path.dirname(current_dir) #pega o diretorio atual para o download

    links = ["http://212.183.159.230/5MB.zip",
            "http://212.183.159.230/10MB.zip",
            "http://212.183.159.230/20MB.zip",
            "http://212.183.159.230/50MB.zip",
            "http://212.183.159.230/100MB.zip",
            "http://212.183.159.230/200MB.zip",
            "http://212.183.159.230/512MB.zip"]
    
    time_ini = time.time()

    for link in links:
        try:
            file_name = link.split("/")[-1]
            con = requests.get(link)
            open(file_name, 'wb').write(con.content)
            print("Download de {} completo".format(file_name))
        except Exception as e:
            print(e)

    time_exec = (time.time() - time_ini)
    print("Tempo de execucao: ", time_exec, " s\n")