import json
from operator import itemgetter


def generate_diff(pathtofile1, pathtofile2):
    ans = []
    file1 = json.load(pathtofile1)
    file2 = json.load(pathtofile2)
    setfile1 = set(file1.keys())
    setfile2 = set(file2.keys())
    onlyfile1 = setfile1 - setfile2
    onlyfile2 = setfile2 - setfile1
    intersectionfiles = setfile1 & setfile2
    for item in onlyfile1:
        ans.append((item, '-', file1[item]))
    for item in onlyfile2:
        ans.append((item, '+', file2[item]))
    for item in intersectionfiles:
        if file1[item] == file2[item]:
            ans.append((item, ' ', file1[item]))
        else:
            ans.append((item, '-', file1[item]))
            ans.append((item, '+', file2[item]))
    ans.sort(key=itemgetter(1), reverse=True)
    ans.sort(key=itemgetter(0))
    print('{')
    for item in ans:
        print("  {} {}: {}".format(item[1], item[0], item[2]))
    print('}')
