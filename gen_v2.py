import os
import random
import os.path as osp
import fnmatch
from glob import glob

img_sets = ['train', 'val', 'test', 'trainval']
#base_dir = os.getcwd()
base_dir = 'dataset'
ftrain = open(osp.join(base_dir, 'train.txt'), 'w')
fval = open(osp.join(base_dir, 'val.txt'), 'w')
ftest = open(osp.join(base_dir, 'test.txt'), 'w')
ftrainval = open(osp.join(base_dir, 'trainval.txt'), 'w')

trainval_percent = 0.9
train_percent = 0.9


img_dir = osp.join(base_dir, 'images')
print('Processing folder: {}'.format(img_dir))
txt_dir = osp.join(base_dir, 'labels')
#total_txt = os.listdir(txt_dir)
total_txt = []
for x in glob(osp.join(txt_dir,'*.txt')):
    total_txt.append(x)
num = len(total_txt)
print(num)
list = range(num)

tv = int(num * trainval_percent)
tr = int(tv * train_percent)
trainval = random.sample(list, tv)
train = random.sample(trainval, tr)
for i in list:
    print("Processing:{:.2f} %".format(i/len(list) * 100))
    img_name = total_txt[i][:-4]+'.jpg' + '\n'
    img_name  = img_name.replace('labels', 'images')
    txt_name = total_txt[i][:-4]+'.txt' + '\n'
    img_name = img_name.replace('\\', '/')
    print(img_name)
    if i in trainval:
        ftrainval.write(img_name)
        if i in train:
            ftrain.write(img_name)
        else:
            fval.write(img_name)
    else:
        ftest.write(img_name)

print("Successfully")
ftrain.close()
fval.close()
ftest.close()
ftrainval.close()
