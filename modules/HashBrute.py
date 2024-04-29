import random
from modules import AntHashLib
from sys import argv, exit
import os

def Random(hash, hashType, Fixed, len):
  cracked = False
  if Fixed == True:
      strLen = len
  while cracked == False:
    try:
      text = ''
      if Fixed == False:
        strLen = random.randint(1, len)
      for i in range(0, strLen):
        text += random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()[]\;,./{}|:>?-_=+`~")
      text = AntHashLib.String(text)
      if hash == text.hash(hashType):
        print("Found: " + text.string)
        cracked = True
      else:
        print(f'Trying: {text.string} || {text.hash(hashType)}')
    except KeyboardInterrupt:
        print("Ending...")
        break

def Wordlist(hash, hashType, wordlistDir):
  os.chdir('Wordlist/')
  with open(wordlistDir, 'r') as f:
    passwords = str(f.read()).split()
    for password in passwords:
      try:
        password = AntHashLib.String(password)
        if password.hash(hashType) == hash:
          print(f'Found: {password.string}')
          break
        else:
          print(f'Trying: {password.string} || {password.hash(hashType)}')
      except KeyboardInterrupt:
        print('Ending...')
        break
  