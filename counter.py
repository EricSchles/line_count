import os
import argparse
import datetime
#fucking awesome docs - https://mkaz.com/2014/07/26/python-argparse-cookbook/
#very good things - http://stackoverflow.com/questions/3682748/converting-unix-timestamp-string-to-readable-date-in-python

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
parser.add_argument('duration',nargs=1)
parser.add_argument('roots',nargs='*')
args = parser.parse_args()
extension = args.extension[0]
roots = args.roots
duration = args.duration

if duration == 'year':
    total_len = 0
    ave_hour = 0
    num_files = 0

if duration == 'month':
    month_totals = {
        "1":[],
        "2":[],
        "3":[],
        "4":[],
        "5":[],
        "6":[],
        "7":[],
        "8":[],
        "9":[],
        "10":[],
        "11":[],
        "12":[]
    }
    

for root in roots:
    for rootdir,dir,files in os.walk(root):
        for file in files:
            if file.endswith(extension):
                num_files += 1
                file = os.path.join(rootdir,file)
                if duration == 'month':
                    month = datetime.datetime.fromtimestamp(os.stat(file).st_ctime).strftime("%m")
                    hour = int(datetime.datetime.fromtimestamp(os.stat(file).st_ctime).strftime("%H"))
                    
                total_len += file_len(file)
    
    print total_len
                
        
                
