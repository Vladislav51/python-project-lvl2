import json
from operator import itemgetter
import yaml
import os


def openfile(filewrapper):
    if os.path.splitext(filewrapper.name)[1] in ['.yml', '.yaml']:
        file = yaml.load(filewrapper, Loader=yaml.Loader)
    if os.path.splitext(filewrapper.name)[1] in ['.json']:
        file = json.load(filewrapper)
    return file


def element_to_ans_list(key, sign, value, deep):
    if isinstance(value, dict):
        return (key, sign, diff_dict(value, value, deep + 1))
    if isinstance(value, bool):
        return (key, sign, str(value).lower())
    if value is None:
        return (key, sign, 'null')
    return (key, sign, value)


def element_to_plain_list(key, sign, value, path):
    if len(path) > 0 :
        tmp = path + '.' + key
    else:
        tmp = key
    if sign in ['-','+',' ']:
        return (tmp, sign, value)


def formate_items(value):
    if isinstance(value, dict):
        return '[complex value]'
    if isinstance(value, str):
        return "'{}'".format(value)
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    return value
    
                

def generate_diff(pathtofile1, pathtofile2, format_name='complex'):
    if format_name == "'plain'":
        ans = diff_dict_plain(openfile(pathtofile1), openfile(pathtofile2)) 
        #print(ans)
        ansstring=''
        for item in ans:
            if item[1] == '+':
               ansstring+="Property '{}' was added with value: {}\n".format(item[0],formate_items(item[2]))
            if item[1] == '-':
                ansstring+="Property '{}' was removed\n".format(item[0])
            if item[1] == ' ':
                ansstring+="Property '{}' was updated. From {} to {}\n".format(item[0],formate_items(item[2][0]),formate_items(item[2][1]))
                
        return ansstring
    return diff_dict(openfile(pathtofile1), openfile(pathtofile2))


def diff_dict_plain(dict1,dict2, path=''):   
    ans = []
    setdict1 = set(dict1.keys())
    setdict2 = set(dict2.keys())
    for item in setdict1 - setdict2:
        ans.append(element_to_plain_list(item, '-', dict1[item], path))
    for item in setdict2 - setdict1:
        ans.append(element_to_plain_list(item, '+', dict2[item], path))
    for item in setdict1 & setdict2:
        if dict1[item] == dict2[item]:
            pass
            #ans.append(element_to_ans_list(item, ' ', dict1[item], deep))
        else:
            if isinstance(dict1[item], dict) and isinstance(dict2[item], dict):
                if len(path) > 0 :
                    tmp = path + '.' + item
                else:
                    tmp = item
                ans.extend(diff_dict_plain(dict1[item], dict2[item], tmp)) # noqa E501
            else:
                ans.append(element_to_plain_list(item, ' ', (dict1[item],dict2[item]), path))
    ans.sort(key=itemgetter(1), reverse=True)
    ans.sort(key=itemgetter(0))

    return ans


def diff_dict(dict1, dict2, deep=0):
    ans = []
    setdict1 = set(dict1.keys())
    setdict2 = set(dict2.keys())
    for item in setdict1 - setdict2:
        ans.append(element_to_ans_list(item, '-', dict1[item], deep))
    for item in setdict2 - setdict1:
        ans.append(element_to_ans_list(item, '+', dict2[item], deep))
    for item in setdict1 & setdict2:
        if dict1[item] == dict2[item]:
            ans.append(element_to_ans_list(item, ' ', dict1[item], deep))
        else:
            if isinstance(dict1[item], dict) and isinstance(dict2[item], dict):
                ans.append((item, ' ', diff_dict(dict1[item], dict2[item], deep + 1))) # noqa E501
            else:
                ans.append(element_to_ans_list(item, '-', dict1[item], deep))
                ans.append(element_to_ans_list(item, '+', dict2[item], deep))
    ans.sort(key=itemgetter(1), reverse=True)
    ans.sort(key=itemgetter(0))
    ansstring = '{\n'
    for item in ans:
        ansstring = ansstring + " "*((deep*4)+2) + "{} {}: {}\n".format(item[1], item[0], item[2]) # noqa E501
    ansstring = ansstring + " " * deep * 4 + '}'
    return ansstring
