import requests as pla
import argparse,os

parser = argparse.ArgumentParser()
parser.add_argument('-u', '--url', help='url', required=True)
args = parser.parse_args()

file = 'Header.txt'
r = pla.get(args.url)
tt = str(r.headers)
if os.path.exists('Header.txt'):
    os.remove('Header.txt')
else:
    pass

with open('Header.txt', 'a') as f:
    f.write(tt)
    f.close()

    if os.path.exists(file):
        
        
        print('saved!')
    else:
        print('CHECK YOUR INTERNET CONNECTIOR OR THE URL YOU ENTER!')
