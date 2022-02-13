import sys, os
import time
import string
from threading import Thread
from time import perf_counter
from pip._vendor import requests

def separaFinal(url):
    s = url
    parts = s.split(".")
    x = len(parts)
    return parts[x-1]

def baixaImagem(url, i):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36 Edg/98.0.1108.50'}
    formato = separaFinal(url)
    path = "K:/Unifesp_2021_2/Pcd/Trabalho4/python/imagens2/" + str(i) + "." + formato
    file = open(path, "wb")
    response = requests.get(url, headers=headers)
    file.write(response.content)
    file.close()
    print("Download da imagem " + str(i) + " finalizado")

def iniciaEexecutaThreads():
    urls = [
        "https://upload.wikimedia.org/wikipedia/commons/3/39/Rue_Danville_-_Paris_XIV_%28FR75%29_-_2021-08-01_-_1.jpg",
        "https://upload.wikimedia.org/wikipedia/commons/1/1a/Honda_Masanobu.jpg",
        "https://upload.wikimedia.org/wikipedia/commons/f/f2/Devi_Prasad_Bagrodia_at_his_office.jpg",
        "https://upload.wikimedia.org/wikipedia/commons/3/3b/Teguise_Guatiza_-_Jardin_06_ies.jpg",
        "https://upload.wikimedia.org/wikipedia/commons/0/05/Abilene_Semi-Weekly_Farm_Reporter_%28Abilene%2C_Tex.%29%2C_Vol._30%2C_No._44%2C_Ed._1_Tuesday%2C_May_10%2C_1910_-_DPLA_-_0e9da41ec13d69fb4c34a429e4696dfe_%28page_4%29.jpg",
        "https://upload.wikimedia.org/wikipedia/commons/5/5f/J_and_K3_Team_JKT48_Honda_GIIAS_2016_IMG_2916_%2828510305913%29.jpg",
        "https://upload.wikimedia.org/wikipedia/commons/7/79/Ceratotherium_germanoafricanum_mandible.jpg",
        "https://upload.wikimedia.org/wikipedia/commons/0/03/Hjortn%C3%A4s_brygga_May_2018_05.jpg",
        "https://upload.wikimedia.org/wikipedia/commons/1/16/USMC-091101-M-2786W-003.jpg",
        "https://upload.wikimedia.org/wikipedia/commons/3/34/Oleksa_Novakivsky_16.jpg",
        "https://upload.wikimedia.org/wikipedia/commons/4/45/NMCB-11_battlesight_zero_on_Camp_Leatherneck_120219-N-UH337-050.jpg",
        "https://upload.wikimedia.org/wikipedia/commons/6/68/Threeshockwavesfour.jpg",
        "https://upload.wikimedia.org/wikipedia/commons/1/1b/ISS062-E-119721_-_View_of_Earth.jpg",
        "https://upload.wikimedia.org/wikipedia/commons/3/36/De_Gesammelte_Werke_III_%28Schnitzler%29_219.jpg",
        "https://upload.wikimedia.org/wikipedia/commons/a/ac/ISS021-E-28570_-_View_of_Earth.jpg",
        "https://upload.wikimedia.org/wikipedia/commons/4/4c/National_Oceanographic_Centre%2C_Southampton_-_geograph.org.uk_-_14447.jpg",
        "https://upload.wikimedia.org/wikipedia/commons/4/45/PygoscelisChickGoodchild.jpg",
        "https://upload.wikimedia.org/wikipedia/commons/d/d7/%D0%A3%D0%BD%D0%B8%D0%B2%D0%B5%D1%80%D1%81%D0%B8%D1%82%D0%B5%D1%82%D1%81%D0%BA%D0%B0%D1%8F_%D0%BD%D0%B0%D0%B1%D0%B5%D1%80%D0%B5%D0%B6%D0%BD%D0%B0%D1%8F_%D0%A1%D1%84%D0%B8%D0%BD%D0%BA%D1%81%D1%8B_20.jpg",
        "https://upload.wikimedia.org/wikipedia/commons/8/8e/Festival_Kaafala_th%C3%A9atre_2016_%C3%A0_Ouak%C3%A9_19.jpg",
        "https://upload.wikimedia.org/wikipedia/commons/f/ff/SanJose%2CBatangasjf9770_09.jpg",
        "https://upload.wikimedia.org/wikipedia/commons/8/80/DE_CDB_1_21_087.jpg",
        "https://upload.wikimedia.org/wikipedia/commons/f/f0/Boerderij_ERVE_GROOT_KEVELAM_achtergevel_nr._F_24-31_-_Markelo_-_20482385_-_RCE.jpg",
        "https://upload.wikimedia.org/wikipedia/commons/a/a0/Acalypha_wilkesiana_%27Mooreana%27.jpg",
        "https://upload.wikimedia.org/wikipedia/commons/0/05/Suport_AGBS_Tremp.jpg",
        "https://upload.wikimedia.org/wikipedia/commons/6/61/Hakata_Station_sign_%28San%27yo_Shinkansen%29_20131219.jpg",
        "https://upload.wikimedia.org/wikipedia/commons/8/8a/Stift_Klosterneuburg_8900.jpg",
        "https://upload.wikimedia.org/wikipedia/commons/a/af/Mobeye-%C3%89t%C3%A9DesVilles-M%C3%A9ricourt-534.jpg",
    ]

    threads = [Thread(target=baixaImagem, args=(url, urls.index(url)+1))
            for url in urls]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    time_ini = time.time()
    iniciaEexecutaThreads()

    time_exec = (time.time() - time_ini)
    print("Tempo de execucao: ", time_exec, "ms")