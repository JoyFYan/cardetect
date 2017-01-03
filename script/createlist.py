import os;
import shutil;
from PIL import Image
import datetime
import random
##根据文件夹下图片生成result.txt
#pathset(path):path为工作目录
#path中有若干个文件夹，每一个代表一类，下包含多个类内容图片
#输出为两个txt文件，一个为测试集一个为训练集
#search(HDF5=False,rate=0.9):
#im2lmdb是否自动转为lmdb格式
#rate为训练集占总数据比例，默认0.9


def pathset(path):
	#path="D:\mydatabase\haixin_test";#设置工作目录"D:\mydatabase\lb005-4w_out"
	os.chdir(path)#更改工作目录
	#f=open("result.txt","w");#打开输出到的txt文件
	#if not os.path.isdir("train"):#是否存在train目录
	#	os.mkdir("train");#新建train目录
	#if not os.path.isdir("test"):#是否存在train目录
	#	os.mkdir("test");#新建test目录
		
def search(HDF5=False,rate=0.9):
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
		create(NowDir,files,now,rate);#是文件夹进入并创建该目录下的list
	if HDF5:
		pass
	
	
def create(pathnow,dicname,now,rate):
	filelist=os.listdir(pathnow)#该文件夹下所有的文件（包括文件夹）
	classname=0;
	result_train=open("train"+now.strftime('_%m_%d_%H_%M')+".txt","a+");#打开输出到的txt文件
	result_test=open("test"+now.strftime('_%m_%d_%H_%M')+".txt","a+");#打开输出到的txt文件
	for files in filelist:#遍历所有文件
		NowDir=os.path.join(pathnow,files);#当前遍历的文件路径
		#addstr="";#补增0
		
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
	
def read(filename):
	f=open(filename,"r");#打开文件
	lines=f.readlines();
	path=os.getcwd();
	count=1;
	allnum=len(lines);
	miss=[];
	for line in lines:
		print "processing:"+str(count)+"/"+str(allnum);
		info=line.split(" ");
		info[1]=info[1].replace('\n','');
		if not os.path.isdir(info[1]):#是否存在目录
			os.mkdir(info[1]);#新建目录
		filepath=os.path.join(path,info[0]);#原图像目录
		if os.path.exists(filepath):
			newpath=os.path.join(path,info[1],info[0]);#新目录
			#os.system ("copy %s %s" % (filename, newpath))
			shutil.copyfile(filepath,newpath);#复制文件
		else:
			print "miss file:"+info[0];
			miss.append(info[0]);
		count+=1;
	print str(allnum)+" files complete"
	print str(len(miss))+" files miss"
	for i in range(len(miss)):
		print miss[i];
	
pathset('D:\mydatabase\lb005-4w_out\cardata'); #F:\GITClone\cardetect\script D:\mydatabase\lb005-4w_out\cardata
search();
#read("result.txt")