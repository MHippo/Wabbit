import os
import requests
#session = requests.Session()

def dir(website, wordlist):
  try: 
    os.chdir('Wordlist/')
    foundDirs = []
    with open(wordlist, 'r') as f:
      dirs = str(f.read()).split()
    for dir in dirs:
      try:
        web = requests.get(f'https://{website}/{dir}')
        if web.status_code == 200:
          foundDirs.append(dir)
          print(f'Found: https://{website}/{dir}')
        else:
          print(f'Trying: https://{website}/{dir}')
      except KeyboardInterrupt:
        print('Ending...')
        break
    print()
    print('Found Directories:')
    for dir in foundDirs:
      print(f'{website}/{dir}')
  except FileNotFoundError:
    print('file isnt found, did you put it in wabbit/wordlist?')