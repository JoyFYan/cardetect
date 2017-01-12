import os;
import shutil;
#from scipy import ndimage
#from scipy import misc
#import pylab as pl
#import matplotlib.pyplot as plt
from PIL import Image
import datetime;

def pathset(path):
	#path="D:\mydatabase\haixin_test";#设置工作目录"D:\mydatabase\lb005-4w_out"
	os.chdir(path)#更改工作目录
	#f=open("result.txt","w");#打开输出到的txt文件
	if not os.path.isdir("full"):#是否存在full目录
		os.mkdir("full");#新建full目录
	if not os.path.isdir("part"):#是否存在part目录
		os.mkdir("part");#新建part目录
	if not os.path.isdir("part0"):#是否存在part目录
		os.mkdir("part");#新建part目录
	if not os.path.isdir("part1"):#是否存在part目录
		os.mkdir("part");#新建part目录
	if not os.path.isdir("part2"):#是否存在part目录
		os.mkdir("part");#新建part目录	
	if not os.path.isdir("part3"):#是否存在part目录
		os.mkdir("part");#新建part目录
		
def rename(begin,weishu):#批量重命名，begin：起始数。weishu：数字位数
	count=begin;
	path=os.getcwd();
	#f=open("result.txt","w");#打开输出到的txt文件
	filelist=os.listdir(path)#该文件夹下所有的文件（包括文件夹）
	for files in filelist:#遍历所有文件
		Olddir=os.path.join(path,files);#原来的文件路径
		addstr="";#补增0
		if os.path.isdir(Olddir):#如果是文件夹则跳过
			continue;
		addwei=weishu-len(str(count));#计算需要填多少0
		for i in range(addwei):
			addstr+="0";#增加到所需位数
		filename=os.path.splitext(files)[0];#文件名
		filetype=os.path.splitext(files)[1];#文件扩展名
		if filetype!=".jpg":#如果不为jpg文件则跳过
			continue;
		string=str(count);#将计数值转为字符
		newfilename=addstr+string+filetype;#合成最终文件名
		f.write(newfilename+" ");#输出文件名到文件
		Newdir=os.path.join(path,newfilename);#新的文件路径
		os.rename(Olddir,Newdir);#重命名
		classify(newfilename)#进行分类操作
		count+=1;#计数加一
		print(newfilename);#打印当前处理文件名	
	f.close();
		

def classify(filename):#分类函数，filename：所需分类文件名
	path=os.getcwd();
	img = Image.open(filename)#打开所要分类的图片
	imgsize=img.size;#图像大小
	full=1;#是否完整，1为完整
	w=imgsize[0];
	h=imgsize[1];
	rate=float(w)/float(h);#长宽比
	if rate<0.6 or rate>1.6 or w<200 or h<200:#判断条件
		full=0;
	if w*h>250000:#判断条件
		full=1;
	if full:
		Newdir0=os.path.join(path+"\\full",filename);
		shutil.copyfile(filename,Newdir0);#复制文件
		f.write("1"+"\n");#输出是否完整标记
	else:
		Newdir0=os.path.join(path+"\\part",filename);
		shutil.copyfile(filename,Newdir0);#复制文件
		f.write("0"+"\n");#输出是否完整标记
		
		
def imcut(filename):
	path=os.getcwd();
	f=open(filename,"r");
	lines=f.readlines();
	count=0;
	num=len(lines);
	f.close();
	f=open(filename,"a+");
	for line in lines:
		
		#line.strip('\n');
		#print(line);
		info=line.split(" ");
		#print(info)
		if info[1]=="1\n":
			#print(info[0]);
			im=Image.open(info[0]);
			imsize=im.size;		
			#print(imsize)
			region = (0,0,imsize[0]/2,imsize[1]);#左半侧裁剪
			croped=im.crop(region);
			name=info[0].split(".");
			Newdir0=os.path.join(path+"\\part0",name[0]+"_cl"+".jpg");
			if not os.path.exists(Newdir0):
				croped.save(Newdir0);
				f.write("part\\"+name[0]+"_cl"+".jpg"+" 0\n");
			
			region = (imsize[0]/2,0,imsize[0],imsize[1]);#右半侧裁剪
			#print(region);
			croped=im.crop(region);
			#name=info[0].split(".");
			Newdir0=os.path.join(path+"\\part1",name[0]+"_cr"+".jpg");
			if not os.path.exists(Newdir0):
				croped.save(Newdir0);
				f.write("part\\"+name[0]+"_cr"+".jpg"+" 0\n");
			
			region = (0,0,imsize[0],imsize[1]/2);#上半侧裁剪
			croped=im.crop(region);
			Newdir0=os.path.join(path+"\\part2",name[0]+"_cu"+".jpg");
			if not os.path.exists(Newdir0):
				croped.save(Newdir0);
				f.write("part\\"+name[0]+"_cu"+".jpg"+" 0\n");
			
			region = (0,imsize[1]/2,imsize[0],imsize[1]);#下半侧裁剪
			croped=im.crop(region);
			Newdir0=os.path.join(path+"\\part3",name[0]+"_cd"+".jpg");
			if not os.path.exists(Newdir0):
				croped.save(Newdir0);
				f.write("part\\"+name[0]+"_cd"+".jpg"+" 0\n");
		count+=1;
		print("process:"+str(count)+'/'+str(num));
	f.close();
			

starttime = datetime.datetime.now();
print("satrt at "+str(starttime));		
pathset("D:\mydatabase\haixin_test");
#f=open("result.txt","w");#打开输出到的txt文件
#rename(0,6);#运行
imcut("result.txt");
endtime = datetime.datetime.now();
print("end at "+str(endtime))
interval=(endtime - starttime).seconds
print("used "+str(interval)+"s");