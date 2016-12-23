from __future__ import print_function
from datetime import datetime
import time
import ssl
import re
import readline
import threading
import sys
#import requests
import json
import os
from pprint import pprint
import signal,random, getpass
import urlparse, argparse
import pkg_resources
#Counters and Toggles
import readline
import codecs
import unicodedata
import rlcompleter
import random, shlex, atexit
import platform, time, calendar
import words

arg_count = 0
no_auth = 0
database_count = 0
ddb_count = 0
hist_toggle = 0
prompt_r = 0



#For tab completion
COMMANDS = ['quit','clear','rhymes-relate','sounds-like',"rhymes-with",'related-to']
#For X number of arguements
ONE = ['boston']
TWO = ['sounds-like',"rhymes-with",'related-to']
THREE = ['rhymes-relate']
#For what class
WORDS = ['rhymes-relate','sounds-like',"rhymes-with",'related-to']
HELPER = ['hidden','?','help',"menus", 'quit', 'exit','clear','version' ]

for arg in sys.argv:
    arg_count += 1

#warnings are ignored because of unverified ssl warnings which could ruin output for scripting
import warnings
warnings.filterwarnings("ignore")



#These are lists of things that are persistent throughout the session
username=''
details = {}
def complete(text, state):
        for cmd in COMMANDS:
                if cmd.startswith(text):
                    if not state:
                        return cmd
                    else:
                        state -= 1



#os expand must be used foR
config_file = os.path.expanduser('~/.hhs')
hist_file = os.path.expanduser('~/.hhs_history')
buff = {}
hfile = open(hist_file, "a")
if os.path.isfile(config_file):
    config=open(config_file, 'r')
    config=json.load(config)
else:
    username = raw_input("Username:")
    password = getpass.getpass("Password:")
    config= {"default":[{"username":username,"password":password}]}

    config_file_new = open(config_file, "w")
    config_f = str(config)
    config_f = re.sub("'",'"',config_f)
    config_file_new.write(config_f)
    config_file_new.close

#Ending when intercepting a Keyboard, Interrupt
def Exit_gracefully(signal, frame):
    #hfile.write(buff)
    sys.exit(0)



#DUH
def get_sat_key(config):
    signal.signal(signal.SIGINT, Exit_gracefully)
    #global username
    username = config["default"][0]["username"]
    password = config["default"][0]["password"]
    key={}
    key['username']=username
    key['password']=password
    try:
        return(key)
    except KeyError:
        print("Bad Credentials!")
        os.unlink(config_file)
        bye()
    return(key)



hhs_p = 'hhs$ '

#main command line stuff
def cli():
    while True:
        valid = 0

        signal.signal(signal.SIGINT, Exit_gracefully)
        try:
            if 'libedit' in readline.__doc__:
                readline.parse_and_bind("bind ^I rl_complete")
            else:
                readline.parse_and_bind("tab: complete")

            readline.set_completer(complete)
            readline.set_completer_delims(' ')
            cli = str(raw_input(PROMPT))
        except EOFError:
            bye()
        if hist_toggle == 1:
            hfile.write(cli + '\n')
        if 'key' in locals():
            pass
        else:
            key = get_sat_key(config)

#This is not just a horrible way to take the commands and arguements, it's also shitty way to sanatize the input for one specific scenario

#I miss perl :(


        cli = re.sub('  ',' ', cli.rstrip())




##########################################################################################
# This starts the single trash commands
#######################################################################################
        buff = str({calendar.timegm(time.gmtime()) : cli})
        #api_key = get_sat_key(config)
        #Write try statement here for error catching
        command = cli.split(' ', 1)[0]

        if command in WORDS:
            l_class = 'words'
#       elif command in UCOMMANDS:
#            l_class = 'ucommands'
#        elif command in VMUTILS:
#            if key['si'] == None:
#                si = esxi_connect(key)

#                atexit.register(Disconnect, si)

#            key['si'] = si
#            l_class = 'vmutils'
        else:
            l_class = ''


        if len(cli.split(' ')) > 0:
            if len(cli.split(' ')) ==6:
                command,arg_one,arg_two,arg_three,arg_four,arg_five = cli.split()
                if command in SIX:
                    command = command.replace("-", "_")
                    l_class = eval(l_class)
                    result = getattr(l_class, command)(api_key, arg_one, arg_two,arg_three,arg_four,arg_five)
                    print(result)
                    valid = 1

            if len(cli.split(' ')) ==5:
                command,arg_one,arg_two,arg_three,arg_four = cli.split()
                if command in FIVE:
                    command = command.replace("-", "_")
                    l_class = eval(l_class)
                    result = getattr(l_class, command)(api_key, arg_one, arg_two,arg_three,arg_four)
                    print(result)
                    valid = 1

            if len(cli.split(' ')) ==4:
                command,arg_one,arg_two,arg_three = cli.split()
                if command in FOUR:
                    command = command.replace("-", "_")
                    l_class = eval(l_class)
                    result = getattr(l_class, command)(api_key, arg_one, arg_two,arg_three)
                    print(result)
                    valid = 1

            if len(shlex.split(cli)) ==3:
                command,arg_one,arg_two = shlex.split(cli)
                if command in THREE:
                    command = command.replace("-", "_")
                    l_class = eval(l_class)
                    result = getattr(l_class, command)(api_key, arg_one, arg_two)

                    pprint(result)
                    valid = 1

            elif len(shlex.split(cli)) ==2:
                command,arguement = shlex.split(cli)
                if command in TWO:
                    command = command.replace("-", "_")

                    l_class = eval(l_class)
                    result = getattr(l_class, command)(api_key, arguement)

                    pprint(result)
                    valid = 1

                else:
                    print("Invalid Arguements")

            else:
               if cli in ONE:
                    cli = cli.replace("-", "_")

               elif cli in HELPER:
                    if cli == "quit" or cli == "exit":
                        #hfile.write(buff)
                        hfile.close()
                        bye()
                    if cli == "version":
                        print(version())
                        valid = 1
                    if cli == "hidden":
                        print(hidden_menu())
                        valid = 1
                    if cli == "qotd":
                        print(qotd_menu())
                        valid = 1
                    if (cli == "help") or (cli == "?"):
                        print(help_menu())
                        valid = 1
                    if cli == "clear":
                       # if ucommands.os_platform() == 'windows':
                       #     print(os.system('cls'))
                       #     valid = 1
                        #if ucommands.os_platform() == 'nix':
                            #pprint(
                        os.system('clear')
                        valid = 1
               else:
                    print("Invalid Command")



        if valid == 0:
            print("Unrecoginized Command")


def help_menu():
####Why did I space the help like this, cause something something, then lazy
    help_var = """
No Help currently Available

"""
    return(help_var)


def hidden_menu():
    hidden_var = """
No Hidden Commands Currently Available
"""
    return(hidden_var)



def version():
    version = pkg_resources.require("trash")[0].version
    return version

def bye():
    exit()

if arg_count == 2:
    command = sys.argv[1]
#noauth is essentially for testing
    if command == "noauth":
        no_auth = 1
#history is to toggle writing a history file, there is currently no clean up so it is off by default
    if command == "history":
        hist_toggle = 1
    if command == "roulette":
        rando = random.randint(1, 3)
    if command == "extra":
        trash_p = config["default"][0]["prompt"]


PROMPT = hhs_p + '> '

if no_auth == 1:
    api_key =0
else:
    api_key = get_sat_key(config)


