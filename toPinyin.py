#!/usr/bin/python3
# 张伟 to zhangwei
import os
import sys
import time
try:
    from pypinyin import Style, pinyin, load_phrases_dict
except:
    print('[-]Error Cannot import pinyin, please install it.\r\n\thttps://github.com/mozillazg/python-pinyin')

def clearChar(chars):
    restr = ['\n','\r','\t',' ']
    data = chars
    for s in restr:
        data = data.replace(s,'')

    return data


if __name__ == '__main__':
    if len(sys.argv)==2:
        target = sys.argv[1]
        tempfile = time.strftime("%Y%m%d%H%M%S_", time.localtime())+target
    else:
        print('python pinyin.py 张伟.txt')
        exit()
    if os.path.exists(target) == False:
        print('File \''+target+'\' is not found!')
        exit()
    li = []
    err = []

    t = open(target,'r+')

    w = open(tempfile,'w+')

    lines = t.readlines()

    for line in lines:
        line = clearChar(line)
        try:
            piny = pinyin(line,style=Style.NORMAL)
            strs = ''
            for p in piny:
                p = p[0]
                strs = strs+p
            
            if strs not in li:
                li.append(strs)
                print(strs)
                w.write(strs+'\r\n')
        except Exception as errs:
            print(errs)
            err.append(line)


    t.close()
    w.close()
    print('Error lines:')
    for i in err:
        print(i)