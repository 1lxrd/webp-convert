from ftplib import FTP
from Naked.toolshed.shell import execute_js, muterun_js
from pathlib import Path
import re


temp = r'(.+\.jpg)|(.+\.jpeg)|(.+\.png)|(.+\.JPG)|(.+\.JPEG)'

ftp = FTP('ftp.intel.com')
ftp.login()
a = ftp.retrlines('LIST')
print(a)
ftp.cwd('images')
ftp.retrlines('LIST')
a = ftp.nlst()
for i in a:
    match = re.search(temp, i)
    if match:
        with open(f'{i}', 'wb') as file:
            ftp.retrbinary('RETR ' + i, file.write)

response = muterun_js('webp-conv.js')
print(response.stdout)

p = Path("./result")
for i in p.rglob('*.webp'):
    print(i)
    # with open(f'{i}', 'rb') as file:
    #     ftp.storbinary(f'STOR {i}', file)




