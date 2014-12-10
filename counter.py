import os
import argparse

#fucking awesome docs - https://mkaz.com/2014/07/26/python-argparse-cookbook/

def file_len(fname):
    i = 0
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    if i != 0:
        return i + 1
    else:
        return i


parser = argparse.ArgumentParser()
parser.add_argument('extension',nargs=1)
parser.add_argument('roots',nargs='*')
args = parser.parse_args()
extension = args.extension[0]
roots = args.roots


total_len = 0
for root in roots:
    for rootdir,dir,files in os.walk(root):
        for file in files:
            if file.endswith(extension):
                file = os.path.join(rootdir,file)
                print file
                total_len += file_len(file)
    
    print total_len
                
        
                
