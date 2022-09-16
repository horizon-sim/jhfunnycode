import os

# 별 찍기
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

# pypi 패키지 자료구조 생성함수
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

def tentobin(value):
    if type(value) is int:
        binvalue = bin(value)
        return int(binvalue[2:])
    
    elif type(value) is float:
        strvalue = (str(value))
        dotindex = strvalue.index(".")
        
        front_value = bin(int(strvalue[:dotindex]))
        back_basic_value = float("0."+strvalue[dotindex + 1:])
        
        back_value = ""
        
        while True:
            back_basic_value *= 2
            
            if back_basic_value > 1:
                back_value += "1"
                back_basic_value -= 1
            elif back_basic_value < 1:
                back_value += "0"
            elif back_basic_value == 1:
                back_value += "1"
                break
            
        complete_value = float((str(front_value))[2:]+"."+(back_value))
        return complete_value