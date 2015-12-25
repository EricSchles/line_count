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

class month_total:
    def __init__(self,total_len=0,ave_hour=0,num_files=0):
        self.total_len = total_len
        self.ave_hour = ave_hour
        self.num_files = num_files


def main(extension,roots=[],show_dirs=False):

    month_totals = {
        "01":month_total(),
        "02":month_total(),
        "03":month_total(),
        "04":month_total(),
        "05":month_total(),
        "06":month_total(),
        "07":month_total(),
        "08":month_total(),
        "09":month_total(),
        "10":month_total(),
        "11":month_total(),
        "12":month_total()
    }

    if roots == []:
        roots.append("~")

    total_len = 0
    ave_hour = 0
    num_files = 0

    for root in roots:
        for rootdir,dir,files in os.walk(root):
            for file in files:
                if show_dirs:
                    print dir
                    if file.endswith(extension) and not file.startswith("."):
                        print file
                if file.endswith(extension) and not file.startswith("."):
                    file = os.path.join(rootdir,file)
                    month = datetime.datetime.fromtimestamp(os.stat(file).st_ctime).strftime("%m")
                    hour = int(datetime.datetime.fromtimestamp(os.stat(file).st_ctime).strftime("%H"))

                    month_totals[month].num_files += 1 #per month
                    num_files += 1 #total

                    month_totals[month].ave_hour += hour #per month
                    ave_hour += hour #total

                    month_totals[month].total_len += file_len(file) #per month
                    total_len += file_len(file) #total

    print "You worked best between %s and %s so far" % (str(ave_hour/num_files),str((ave_hour/num_files) + 1))
    print "You've written %d lines so far." % total_len
    print 

    month_translate = {
        "01":"january",
        "02":"february",
        "03":"march",
        "04":"april",
        "05":"may",
        "06":"june",
        "07":"july",
        "08":"august",
        "09":"september",
        "10":"october",
        "11":"november",
        "12":"december"
    }


    for month in month_totals:
        print "For",month_translate[month]
        if month_totals[month].num_files != 0:
            month_totals[month].ave_hour = month_totals[month].ave_hour/month_totals[month].num_files
        else:
            month_totals[month].ave_hour = 0
        print "You worked best between %s and %s so far" % (str(month_totals[month].ave_hour),str(month_totals[month].ave_hour + 1))
        print "You've written %d lines so far." % (month_totals[month].total_len)
        print 
                
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('extension',nargs=1)
    parser.add_argument('roots',nargs='*')
    parser.add_argument('--show-dirs',bool=False)
    args = parser.parse_args()
    extension = args.extension[0]
    roots = args.roots
    show_dirs = args.show_dirs
    main(extension,roots=roots,show_dirs=show_dirs)
