import os

def starpix(star_index, updown="up"):
    
    if updown == "up":
        i = 0
        while i <= star_index:
            print("*"*i)
            i += 1
            
    elif updown == "down":
        i = 0
        miner_idx = star_index
        while i <= star_index:
            print("*"*miner_idx)
            miner_idx -= 1
            i += 1

def pypi(package_name):
    # main directory
    os.makedirs(f'./{package_name}/{package_name}')
    with open(f"./{package_name}/{package_name}/__init__.py", "w") as f:
        pass
    with open(f"./{package_name}/{package_name}/module_name.py", "w") as f:
        pass
    # setup.py
    with open(f"./{package_name}/setup.py", "w") as f:
        f.write("from setuptools import setup, find_packages\n\n\
setup(\n\
name ='',\n\
version = '1.0.0',\n\
description = 'description',\n\
author = 'author',\n\
author_email = None,\n\
url = None,\n\
install_requires = [],\n\
packages=find_packages(),\n\
)")
    # etc
    with open(f"./{package_name}/README.md", "w") as f:
        pass

