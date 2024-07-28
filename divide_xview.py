import os
import shutil


path = "../autodl-tmp/nturgbd_videos"      # 文件夹目录，存放所有56880个样本的文件夹
files = os.listdir(path)    # 得到文件夹下的所有文件名称
train = ['C002', 'C003']
test = ['C001']

for file in files:  # 遍历文件夹
    for i in range(2):
        if train[i] in file:
            file = os.path.join(path, file)
            shutil.copy(file, '../autodl-tmp/Cross-View/Train')
    for i in range(1):
        if test[i] in file:
            file = os.path.join(path, file)
            shutil.copy(file, '../autodl-tmp/Cross-View/Test')
