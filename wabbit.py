#######################
# WABBIT
# A PROJECT BY SETH
# I AM NOT RESPONSIBLE FOR YOUR USE OF THIS PROGRAM
#######################

#######################
# TODO
#######################

#Clean'hashid.py'
#OnlineBrute 

#######################
# IMPORTS
#######################

import os
import webbrowser
from platform import system
from time import sleep
import hashlib
import random
import socket
from builtins import input
from sys import argv, exit

#######################
# MODULE IMPORT
#######################

from modules import HashID
from modules import HashBrute
from modules import AntHashLib
from modules import WebBrute
#######################
# VARIABLES
#######################

user = socket.gethostname()
eyes = '-     -'
file = 'wabbit'
dir = '~/' + file

class Constant:
  Prompt = f'''\033[31m┌─[{user}\033[1;33m@\033[0;36m\033[31m]─[{dir}]\n└──╼ $\033[1;37m '''
  user = socket.gethostname()
  logo = '''\033[1;37m
   ***       
  ** **
 **   **
 **   **         **** 
 **   **       **   ****
 **  **       *   **   **
  **  *      *  **  ***  **
   **  *    *  **     **  *
    ** **  ** **        **
    **   **  **
   *           *
  *             *
 *    \033[1;31m-     -\033[1;37m    *
 *   /   @   \   *
 *   \__/ \__/   *
   *     W     *
     **     **   
       *****
       
  '''
  
c = Constant()

clear = lambda: os.system('cls' if os.name=='nt' else 'clear')

#######################
# FUNCTIONS
#######################

def main():
  print(c.logo)
  print(f'Welcome {c.user}\n')
  while True:
    cmdInput = input(c.Prompt)
    command = cmdInput.split(' ')
    mainCommand = command[0].lower()
    if mainCommand == 'hashid':
      try:
        if command[1]:
          hash = command[1]
          HashID.hashid(hash)
      except IndexError:
        print('Usage: hashid [hash*]')
    elif mainCommand == 'hash':
      try:
        string = command[1]
        hashType = command[2]
        hashType = hashType.lower()
        string = AntHashLib.String(string)
        print(f'\n\n-------------------------{string.hash(hashType)}\n-------------------------')
      except IndexError:
        print('Usage: hash [string*] [hashType*]')
    elif mainCommand == 'wizard':
      print('not finished yet')
    elif mainCommand == 'randombrute' or mainCommand == 'rbrute':
      try:
        hash = command[1]
        hashType = command[2]
        hashType = hashType.lower()
        len = command[3]
        len = int(len)
        HashBrute.Random(hash, hashType, False, len)
      except IndexError:
        print('Usage: randombrute [hash*] [hashType*] [length*] [Fixed*]')
    elif mainCommand == 'wordlistbrute' or mainCommand == 'wlbrute' or mainCommand == 'wbrute':
      try:
        hash = command[1]
        hashType = command[2]
        hashType = hashType.lower()
        wordlistDir = command[3]
        HashBrute.Wordlist(hash, hashType, wordlistDir)
      except IndexError:
        print('Usage: wordlistBrute [hash*] [hashType*] [wordlist*]')
    elif mainCommand == 'dirbrute' or mainCommand == 'dbrute':
      try:
        website = command[1]
        wordlist = command [2]
        WebBrute.dir(website, wordlist)
      except IndexError:
        print('Usage: dirbrute [website*] [wordlist*] [proxy]')
    elif mainCommand == 'clear' or mainCommand == 'cls':
      clear()
      print(c.logo)
      print(f'Welcome {c.user}\n')
    elif mainCommand == 'help':
      print('''
      hashid [hash*]                                     | Identifies possible hashes of a given hash
      hash [string*] [hashType*]                         | Hashes a given string with the given hash type
      randombrute [hash*] [hashType*] [length*] [Fixed?*]| Brutes a given hash by randomly generating a password
      wordlistbrute [hash*] [hashType*] [wordlist*]      | Brutes a given hash by uing each password in a wordlist
      dirbrute [website*] [wordlist*] [proxylist]        | Checks a given website for every directory in the wordlist
      proxy [protocol*] [IP address*] [user:pass]
      wizard                                             | Opens a more simple version of Wabbit
      clear                                              | Clears the console
      help                                               | take a guess
      ''')
    else:
      print('Command not found. Try running help.')



#######################
# RUN
#######################

if __name__ == '__main__': 
  try:
    main()
  except KeyboardInterrupt:
    print('\n\nThe wabbit sleeps...')
    exit()
  
