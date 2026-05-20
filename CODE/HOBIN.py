import os
import os.path

# 目标文件夹的路径
filedir = 'C:/Users/USER/Desktop/OUTPUT/OUTPUT1'
# 获取当前文件夹中的文件名称列表
filelist = os.listdir(filedir)
# print(filelist)

# 合并文件，并将结果存储在 JoinData.TXT 文件中
with open('C:/Users/USER/Desktop/OUTPUT/OUTPUT1/all.csv', 'w', encoding='utf-8') as f:
    # 遍历文件名,构建文件路径
    for filename in filelist:
        filepath = filedir + '/' + filename
        # 遍历文件,按行写入
        for line in open(filepath):
            f.writelines(line)
        f.write('\n')
