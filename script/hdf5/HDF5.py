import random
from PIL import Image
import numpy as np
#import h5py
import os

def read_file(dir):
	path=os.getcwd();
	im_dir=os.path.join(path,dir);
	filelist=os.listdir(im_dir)#不能包含文件夹
	return filelist
	
def create_index(flie_list):
	index=[];
	for i in file_list:
		index.append(i.split("_")[1].strip(".jpg"));#以_为分隔符，删除'.jpg'
	return index
	


IMAGE_DIR = ['image_train', 'image_test']
HDF5_FILE = ['hdf5_train.h5', 'hdf5_test.h5']
LIST_FILE = ['list_train.txt', 'list_test.txt']

LABELS = dict(
    # (kind_1, kind_2)
    A0 = (0, 0),
    B0 = (1, 0),
    A1 = (0, 1),
    B1 = (1, 1),
    A2 = (0, 2),
    B2 = (1, 2),
)

print '\nplease wait...'

for kk, image_dir in enumerate(IMAGE_DIR):
    # 读取文件列表于file_list
    file_list = read_file(image_dir)
    # 文件列表乱序
    random.shuffle(file_list)

    # 标签类别
    kind_index = create_index(file_list);

    # 图片大小为96*32，单通道
    datas = np.zeros((len(file_list), 3, 100, 100))
    # label大小为1*2
    labels = np.zeros((len(file_list), 2))

    for ii, _file in enumerate(file_list):
        # hdf5文件要求数据是float或者double格式
        # 同时caffe中Hdf5DataLayer不允许使用transform_param，
        # 所以要手动除以255
	#
	img=Image.open(os.path.join(image_dir,_file));
	img=img.resize((100,100),Image.ANTIALIAS);
	datas[ii, :, :, :] =  np.array(img).astype(np.float32).transpose(2,0,1) / 255;
        #datas[ii, :, :, :] = \
        #np.array(Image.open(os.path.join(image_dir,_file)).resize(100,100),NEAREST).astype(np.float32) / 255
        labels[ii, :] = np.array(LABELS[kind_index[ii] ]).astype(np.int)

    # 写入hdf5文件
    #with h5py.File(HDF5_FILE[kk], 'w') as f:
    #    f['data'] = datas
    #    f['labels'] = labels
    #    f.close()

    # 写入列表文件，可以有多个hdf5文件
    with open(LIST_FILE[kk], 'w') as f:
        f.write(os.path.abspath(HDF5_FILE[kk]) + '\n')
        f.close()

print '\ndone...'
