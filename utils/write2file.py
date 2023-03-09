# Translate data
# 将CSV文件转换为TXT文件 便于进行标注
import tqdm
def write2file(content, dir, add=False):
    if add:
        f = open(dir,'a')
    else:
        f = open(dir,'w')
    for i in content:
        f.write(i+"\n")
    f.close()

import  csv
with open('../data/data2.csv','r',encoding='utf-8') as cvfile:
    reader = csv.DictReader(cvfile)
    write_content = []
    for row in tqdm.tqdm(reader):
        content = row['content'].replace("\n",'')
        if len(content) < 10 : continue
        author = row['poetry_author'].replace("\n",'')
        name = row['poetry_name'].replace("\n",'')
        write_content.append(content+" "+author+" "+name)
    write2file(write_content,'../data/data.txt',add=True)