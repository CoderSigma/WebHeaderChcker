import requests as pla
import argparse,os

parser = argparse.ArgumentParser()
parser.add_argument('-u', '--url', help='url example is https://site.com/', required=True)
args = parser.parse_args()

file = 'Header.json'
r = pla.get(args.url)
tt = str(r.headers)
if os.path.exists('Header.json'):
    os.remove('Header.json')
else:
    pass

with open('Header.json', 'a') as f:
    f.write(tt.replace(" ", '||\n||'))
    f.close()

    if os.path.exists(file):
        
        
        print('saved!')
    else:
        print('CHECK YOUR INTERNET CONNECTIOR OR THE URL YOU ENTER!')
