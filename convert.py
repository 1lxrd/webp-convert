from ftplib import FTP
from Naked.toolshed.shell import muterun_js
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
    for _ in p.rglob(ext):
        with open(f'{f}', 'rb') as file:
            ftp.storbinary(f'STOR {f}', file)
        print(f'{f} uploaded')
        os.remove(f)


def read_config():
    with open('config.csv') as f:
        reader = csv.reader(f)
        scan = list(reader)
        del scan[0]
    return scan


temp = r'(.+\.jpg)|(.+\.jpeg)|(.+\.png)|(.+\.JPG)|(.+\.JPEG)'

conf = read_config()

for i in conf:

    ftp = FTP(i[0])
    ftp.login(user=i[1], passwd=i[2])
    ftp.retrlines('LIST')
    ftp.cwd(i[3])
    ftp.retrlines('LIST')
    a = ftp.nlst()

    for j in a:
        download(j)
        check_if_optimized(j)

        t = Path("./")
        upload(t, j, '*.jpg')
        upload(t, j, '*.png')
        upload(t, j, '*.jpeg')
        upload(t, j, '*.webp')
