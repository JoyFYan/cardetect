import random
from PIL import Image
import numpy as np
#import h5py
import os
import datetime
##根据文件夹下图片生成result.txt
#pathset(path):path为工作目录
#path中有若干个文件夹，每一个代表一类，下包含多个类内容图片
#输出为两个txt文件，一个为测试集一个为训练集
#search(HDF5=False,rate=0.9):
#im2lmdb是否自动转为lmdb格式
#rate为训练集占总数据比例，默认0.9

#HDF5_FILE = ['hdf5_train.h5', 'hdf5_test.h5']
#LIST_FILE = ['list_train.txt', 'list_test.txt']

def pathset(path):
	os.chdir(path)#更改工作目录

	
def search(rate=0.9):
	now = datetime.datetime.now()#当前时间
	path=os.getcwd();
	#f=open("result"+now.strftime('_%m_%d_%H_%M')+".txt","a+");#打开输出到的txt文件
	#f=open(,"w");#
	filelist=os.listdir(path)#该文件夹下所有的文件（包括文件夹）
	for files in filelist:#遍历所有文件
		NowDir=os.path.join(path,files);#当前遍历的文件路径
		addstr="";#补增0
		if os.path.isfile(NowDir):#如果是文件则跳过
			continue;
		print "in "+NowDir
		files_index=files.split('_')#分割后的多种标签;
		#index=tuple([int(i) for i in files_index])#转为int 型tuple
		create(NowDir,files,now,rate,files_index);#是文件夹进入并创建该目录下的list
		
	
	
def create(pathnow,dicname,now,rate,index):
	filelist=os.listdir(pathnow)#该文件夹下所有的文件（包括文件夹）
	
	result_train=open("train"+now.strftime('_%m_%d_%H_%M')+".txt","a+");#打开输出到的txt文件
	result_test=open("test"+now.strftime('_%m_%d_%H_%M')+".txt","a+");#打开输出到的txt文件
	classname=' ';
	classname=classname.join(index);
	for files in filelist:#遍历所有文件
		NowDir=os.path.join(pathnow,files);#当前遍历的文件路径
		#addstr="";#补增0
		
		if os.path.isdir(NowDir):#如果是文件夹则跳过
			continue;
		if random.uniform(0, 1)<rate:
			result_train.write("/"+dicname+"/"+files+' '+classname+'\n');
			
		else:
			#result=open("test"+now.strftime('_%m_%d_%H_%M')+".txt","a+");#打开输出到的txt文件
			result_test.write("/"+dicname+"/"+files+' '+classname+'\n');
			
		
	result_train.close;
	result_test.close;	
'''
def createHDF5(pathnow,dicname,rate,index):
	filelist=os.listdir(pathnow)#该文件夹下所有的文件（包括文件夹）
	random.shuffle(filelist);#乱序
	num_all=len(filelist);#该类总图片数
	num_train=num_all*rate;#训练图片数
	num_test=num_all-num_train;#测试图片数
	for num,files in enumerate(filelist):#遍历所有文件
		NowDir=os.path.join(pathnow,files);#当前遍历的文件路径
		#addstr="";#补增0
		datas = np.zeros((len(file_list), 3, 256, 256))
		if os.path.isdir(NowDir):#如果是文件夹则跳过
			continue;
		if random.uniform(0, 1)<rate:
			result_train.write("/"+dicname+"/"+files+' '+dicname+'\n');
			
		else:
			#result=open("test"+now.strftime('_%m_%d_%H_%M')+".txt","a+");#打开输出到的txt文件
			result_test.write("/"+dicname+"/"+files+' '+dicname+'\n');
			
		classname+=1;
	result_train.close;
	result_test.close;
	return 
'''
def read(filename):
	f=open(filename,"r");#打开文件
	lines=f.readlines();
	path=os.getcwd();
	
	allnum=len(lines);
	print allnum;
	datas = np.zeros((allnum, 3, 100, 100));#图片大小
	#labels = np.zeros((allnum, 2));
	labels0 = np.zeros((allnum, 1));
	labels1 = np.zeros((allnum, 1));
	h5name=filename.split('_')[0]+'.h5';
	for count,line in enumerate(lines):
		print "processing:"+str(count+1)+"/"+str(allnum);
		info=line.split(" ",1);#分割一次
		info[1]=info[1].replace('\n','');#删除换行符
		classname=info[1].split(' ');#类名分割
		label=tuple([int(i) for i in classname]);#改为tuple
		img=Image.open(path+info[0]);#打开图片
		img=img.resize((100,100),Image.ANTIALIAS);#修改大小
		datas[count, :, :, :] =  np.array(img).astype(np.float32).transpose(2,0,1) / 255;
		labels[count, :] = np.array(label).astype(np.int);
		# labels0[count, :] = np.array(classname[0]).astype(np.int);
		# labels1[count, :] = np.array(classname[1]).astype(np.int);
	with h5py.File(h5name, 'w') as f:
        	f['data'] = datas
        	f['labels'] = labels
			# f['labels1'] = labels1
        	f.close()
		
	with open(filename.split('_')[0]+"_h5list.txt", 'w') as f:
		f.write(os.path.abspath(h5name) + '\n')
		f.close()
		
	print str(allnum)+" files complete"
	
	
pathset('/home/yzy/caffe/data/cardata/1_3hdf5'); 
#F:\GITClone\cardetect\script D:\mydatabase\lb005-4w_out\cardata
search();
#read("test_12_28_15_11.txt")
#read("train_12_28_15_11.txt")
