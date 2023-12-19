import requests as pla
import argparse,os

parser = argparse.ArgumentParser()
parser.add_argument('-u', '--url', help='url example is https://site.com/', required=True)
args = parser.parse_args()

def kill():
    file = 'Header.json'
r = pla.get(args.url)
tt = str(r.headers)
if os.path.exists('Header.json'):
    os.remove('Header.json')
    print('Server :',r.headers['Server'])
    if not r.headers['Server'] == r.headers['Server']:
        pass
    else:
        print('Server :',r.headers['Server'])
    if not r.headers.get('X-XSS-Protection') == r.headers.get('X-XSS-Protection'):
        pass
    else:
        print('XSS-Protection :',r.headers.get('X-XSS-Protection'))
    if not r.headers['Cache-Control'] == r.headers['Cache-Control']:
        pass
    else:
        print('Cache Control :', r.headers['Cache-Control'])
    if not r.headers.get('Set-Cookie') == r.headers.get('Set-Cookie'):
        pass
    else:
        print('Cookies :', r.headers.get('Set-Cookie'))
    if not r.headers.get('User-Agent') == r.headers.get('User-Agent'):
       pass
    else:
        print('User-Agent :',r.headers.get('User-Agent'))
   
else:
    with open('Header.json', 'a') as f:
        f.write(tt)
        f.close()

with open('Header.json', 'a') as f:
    f.write(tt.replace(" ", '||\n||')) 
    f.close()

    if not r.headers['Server'] == r.headers['Server']:
        pass
    else:
        print('Server :',r.headers['Server'])
    if not r.headers.get('X-XSS-Protection') == r.headers.get('X-XSS-Protection'):
        pass
    else:
        print('XSS-Protection :',r.headers.get('X-XSS-Protection'))
    if not r.headers['Cache-Control'] == r.headers['Cache-Control']:
        pass
    else:
        print('Cache Control :', r.headers['Cache-Control'])
    if not r.headers.get('Set-Cookie') == r.headers.get('Set-Cookie'):
        pass
    else:
        print('Cookies :', r.headers.get('Set-Cookie'))
    if not r.headers.get('User-Agent') == r.headers.get('User-Agent'):
       pass
    else:
        print('User-Agent :',r.headers.get('User-Agent'))
