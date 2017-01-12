import os;
import shutil;
#from scipy import ndimage
#from scipy import misc
#import pylab as pl
#import matplotlib.pyplot as plt
from PIL import Image
import datetime;

def imcut(impath):
	os.chdir(impath);
	path=os.getcwd();
	if not os.path.isdir("part0"):#是否存在part目录
		os.mkdir("part0");#新建part目录
	if not os.path.isdir("part1"):#是否存在part目录
		os.mkdir("part1");#新建part目录
	if not os.path.isdir("part2"):#是否存在part目录
		os.mkdir("part2");#新建part目录	
	if not os.path.isdir("part3"):#是否存在part目录
		os.mkdir("part3");#新建part目录
	filename="cutlist";
	# f=open(filename,"a+");
	filelist=os.listdir(path)#该文件夹下所有的文件（包括文件夹）
	for files in filelist:#遍历所有文件
		NowDir=os.path.join(path,files);#当前遍历的文件路径
		addstr="";#补增0
		if os.path.isdir(NowDir):#如果是文件则跳过
			continue;
		print "in "+NowDir
		im=Image.open(files);
		imsize=im.size;		
		region = (0,0,imsize[0]/2,imsize[1]);#左半侧裁剪
		croped=im.crop(region);
		name=files.split(".");
		Newdir0=os.path.join(path+"\\part0",name[0]+"_cl"+".jpg");
		if not os.path.exists(Newdir0):
			croped.save(Newdir0);
			# f.write("part\\"+name[0]+"_cl"+".jpg"+" 0\n");
			
		region = (imsize[0]/2,0,imsize[0],imsize[1]);#右半侧裁剪
		croped=im.crop(region);
		Newdir0=os.path.join(path+"\\part1",name[0]+"_cr"+".jpg");
		if not os.path.exists(Newdir0):
			croped.save(Newdir0);
			
		region = (0,0,imsize[0],imsize[1]/2);#上半侧裁剪
		croped=im.crop(region);
		Newdir0=os.path.join(path+"\\part2",name[0]+"_cu"+".jpg");
		if not os.path.exists(Newdir0):
			croped.save(Newdir0);
			
		region = (0,imsize[1]/2,imsize[0],imsize[1]);#下半侧裁剪
		croped=im.crop(region);
		Newdir0=os.path.join(path+"\\part3",name[0]+"_cd"+".jpg");
		if not os.path.exists(Newdir0):
			croped.save(Newdir0);
		
imcut("/home/yzy/caffe/data/cardata/1_5add")