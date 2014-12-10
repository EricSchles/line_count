import os
import argparse

#fucking awesome docs - https://mkaz.com/2014/07/26/python-argparse-cookbook/

parser = argparse.ArgumentParser()
parser.add_argument('extension',nargs=1)
parser.add_argument('roots',nargs='*')
args = parser.parse_args()
extension = args.extension
roots = args.roots


# for root in roots:
#     for rootdir,dir,files in os.walk(root):
#         print files
        
