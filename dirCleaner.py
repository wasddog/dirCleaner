import os, argparse
from datetime import datetime, date


cwd = os.getcwd()
fileList = os.listdir(cwd)
today = int(date.today().strftime('%j'))
files = []
oldFiles = []

parser = argparse.ArgumentParser(description='Quick script to delete large amount of files with specific starting/ending name also with option to specify the oldeness of the files you want to delete')
parser.add_argument('-s', '--start', type=str, metavar='', help='Specify the starting of the files name')
parser.add_argument('-e', '--end', type=str, metavar='', help='Specify the ending of the files (mp3, pdf, html, txt, etc...)')
parser.add_argument('-d', '--days', type=int, metavar='', help='Specify how old the files should be to get cleaned (by days)')
args = parser.parse_args()


def convert_date(timestamp):
    d = datetime.utcfromtimestamp(timestamp)
    formated_date = d.strftime('%j')
    return formated_date

def fileCheck():
    for file in fileList:
        if args.start is not None and args.end is not None:
            if file[len(args.end):].lower() == args.end.lower() and file[0:len(args.start)].lower() == args.start.lower():
                files.append(file)
        elif args.start is not None and args.end is None:
            if file[0:len(args.start)].lower() == args.start.lower():
                files.append(file)
        elif args.end is not None and args.start is None:
            if file[-len(args.end):].lower() == args.end.lower(): # pooooo abeya
                files.append(file)
        else:
            files.append(file)

def getData(dd):
    res = []
    for file in dd:
        info = os.stat(file)
        res.append([file, int(convert_date(info.st_mtime))])
    return res

def findOlds():

    for file in getData(files):
        if args.days is None:
            oldFiles.append(file)
        elif file[1] + args.days <= today:
            oldFiles.append(file)

def removeOlds():
    for file in oldFiles:
        os.remove(file[0])
        print(f'{file[0]} was removed, was {today - file[1]} days old...')


if __name__ == '__main__':
    fileCheck()
    findOlds()
    if len(oldFiles) == 0:
        print('There is no old files found...')
    else: removeOlds()
