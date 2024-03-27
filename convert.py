from ftplib import FTP
from Naked.toolshed.shell import execute_js, muterun_js
from pathlib import Path
import re
import csv
import os
import json


def add_meta(image):
    with open(image, 'a+b') as f:
        f.write(json.dumps({'Description': 'Optimized'}).encode('utf-8'))


def read_meta(image):
    with open(image, 'rb') as f:
        data = str(f.read())
    meta = re.search(r'xff.*({.*})\'\Z', data)
    return meta


def download(f):
    match = re.search(temp, f)
    if match:
        with open(f'{f}', 'wb') as file:
            ftp.retrbinary('RETR ' + f, file.write)
    print(f'{f} downloaded')


def check_if_optimized(f):
    meta = read_meta(f)
    if not meta:
        muterun_js('webp-conv.js', arguments=f'q=4')
        print(f'{f} optimized')
        add_meta(f)


def upload(p, f, ext):
    for i in p.rglob(ext):
        with open(f'{f}', 'rb') as file:
            ftp.storbinary(f'STOR {f}', file)
        print(f'{f} uploaded')
        os.remove(f)


with open('config.csv') as f:
    reader = csv.reader(f)
    scan = list(reader)
    config = scan[1]

temp = r'(.+\.jpg)|(.+\.jpeg)|(.+\.png)|(.+\.JPG)|(.+\.JPEG)'

ftp = FTP(config[0])
ftp.login(user=config[1], passwd=config[2])
ftp.retrlines('LIST')
ftp.cwd(config[3])
ftp.retrlines('LIST')
a = ftp.nlst()

for i in a:
    download(i)
    check_if_optimized(i)

    p = Path("./")
    upload(p, i, '*.jpg')
    upload(p, i, '*.png')
    upload(p, i, '*.jpeg')
    upload(p, i, '*.webp')
