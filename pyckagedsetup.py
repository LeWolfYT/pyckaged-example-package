#this is the pyckagedsetup.py file
#it is used to install a package using pyckaged

import os
import colorama as clr
red = clr.Fore.RED
lime = clr.Fore.LIGHTGREEN_EX
cyan = clr.Fore.LIGHTCYAN_EX
print(lime + "Installing pyckaged example package...")
print(lime + "This will take a few seconds...")

#get the home directory
homedir = os.path.expanduser("~")
#install the package (./main.py)
os.system("cd ~/")
#now we can install the package
#the github repository is:
#LeWolfYT/pyckaged-example-package
os.system("git clone https://github.com/LeWolfYT/pyckaged-example-package.git " + homedir + "/.pyckaged-packages/pyckaged-example-package")