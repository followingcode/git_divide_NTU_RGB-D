import os
import shutil

path = "../autodl-tmp/nturgbd_videos"      # 文件夹目录，存放所有56880个样本的文件夹
files = os.listdir(path)    # 得到文件夹下的所有文件名称
train = ['P001', 'P002', 'P004', 'P005', 'P008', 'P009', 'P013', 'P014', 'P015', 'P016', 'P017', 'P018', 'P019',
         'P025', 'P027', 'P028', 'P031', 'P034', 'P035', 'P038']
test = ['P003', 'P006', 'P007', 'P010', 'P011', 'P012', 'P020', 'P021', 'P022', 'P023', 'P024', 'P026', 'P029',
        'P030', 'P032', 'P033', 'P036', 'P037', 'P039', 'P040']

for file in files:  # 遍历文件夹
    for i in range(20):
        if train[i] in file:
            file = os.path.join(path, file)
            shutil.copy(file, '../autodl-tmp/Cross-Subject/Train')
    for i in range(20):
        if test[i] in file:
            file = os.path.join(path, file)
            shutil.copy(file, '../autodl-tmp/Cross-Subject/Test')