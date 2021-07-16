"""
@author: jun
@file: download_ava_actions.py
@time: 2021/7/16 13:55
@desc:
"""
import argparse
import os
import urllib.request
from tqdm import tqdm

def getFile(url, savedir):
    print("\ndownloading %s" % url)
    file_name = url.split('/')[-1]
    u = urllib.request.urlopen(url)
    f = open(os.path.join(savedir, file_name), 'wb')
    block_sz = 8192
    while True:
        buffer = u.read(block_sz)
        if not buffer:
            break
        f.write(buffer)
    f.close()


parser = argparse.ArgumentParser(prog='download for AVA-Avtions')
parser.add_argument("-i", "--url_txt", help="url_txt", default="test_url.txt", type=str)
parser.add_argument("-o", "--output_dir", help="ouput dir", default="test/", type=str)
opt = parser.parse_args()

os.makedirs(opt.output, exist_ok=True)
f = open(opt.url_txt)
url_list = f.readlines()
url_lst = []
for line in tqdm(url_list):
    line = line.rstrip("\n")
    getFile(line, opt.output)
