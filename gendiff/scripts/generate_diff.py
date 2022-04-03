import json
from operator import itemgetter
import yaml
import os


def openfile(filewrapper):
    if os.path.splitext(filewrapper.name)[1] in ['.yml','.yaml']:
        file = yaml.load(filewrapper, Loader=yaml.Loader)
    if os.path.splitext(filewrapper.name)[1] in ['.json']:
        file = json.load(filewrapper)
    return file 


def generate_diff(pathtofile1, pathtofile2):
    ans = []
    file1 = openfile(pathtofile1)
    file2 = openfile(pathtofile2)
    setfile1 = set(file1.keys())
    setfile2 = set(file2.keys())
    for item in setfile1 - setfile2:
        ans.append((item, '-', file1[item]))
    for item in setfile2 - setfile1:
        ans.append((item, '+', file2[item]))
    for item in setfile1 & setfile2:
        if file1[item] == file2[item]:
            ans.append((item, ' ', file1[item]))
        else:
            ans.append((item, '-', file1[item]))
            ans.append((item, '+', file2[item]))
    ans.sort(key=itemgetter(1), reverse=True)
    ans.sort(key=itemgetter(0))
    ansstring = '{\n'
    for item in ans:
        ansstring = ansstring + "  {} {}: {}\n".format(item[1], item[0], item[2]) # noqa E501
    ansstring = ansstring + '}'
    return ansstring
