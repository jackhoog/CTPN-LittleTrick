import os
from chardet import detect

fileSuffix = input("请输入文件后缀")
fns = []
filedir = os.path.join(os.path.abspath('.'), "")
file_name = os.listdir(os.path.join(os.path.abspath('.'), ""))
for fn in file_name:
    if fn.endswith(fileSuffix):  # 这里填文件后缀
        fns.append(os.path.join(filedir, fn))

for fn in fns:
    with open(fn, 'rb+') as fp:
        content = fp.read()
        codeType = detect(content)['encoding']
        content = content.decode(codeType, "ignore").encode("utf8")
        fp.seek(0)
        fp.write(content)
        print(fn, "：已修改为utf8编码")
