import os;
import shutil;
from scipy import ndimage
from scipy import misc
import pylab as pl
import matplotlib.pyplot as plt
from PIL import Image

def rename(begin,weishu):#批量重命名，begin：起始数。weishu：数字位数
	count=begin;
	path="D:\mydatabase\lb005-4w_out";#文件夹路径
	filelist=os.listdir(path)#该文件夹下所有的文件（包括文件夹）
	for files in filelist:#遍历所有文件
		Olddir=os.path.join(path,files);#原来的文件路径
		addstr="";
		if os.path.isdir(Olddir):#如果是文件夹则跳过
			continue;
		addwei=weishu-len(str(count));#计算需要填多少0
		for i in range(addwei):
			addstr+="0";
		filename=os.path.splitext(files)[0];#文件名
		filetype=os.path.splitext(files)[1];#文件扩展名
		if filetype!="jpg":#如果不为jpg文件则跳过
			continue;
		string=str(count);
		Newdir=os.path.join(path,addstr+string+filetype);#新的文件路径
		os.rename(Olddir,Newdir);#重命名
		count+=1;
		



#rename(0,6);
path="F:\GITClone\cardetect\script";
os.chdir(path)
filename="car1.jpg";
img = Image.open(filename)
plt.figure("beauty")
plt.subplot(1,2,1), plt.title('origin')
plt.imshow(img),plt.axis('off')
imgsize=img.size;
full=1;
w=imgsize[0];
h=imgsize[1];
rate=float(w)/float(h);
print(rate)
if rate<0.67 or rate>1.5 or w<200 or h<200:
	full=0;
if full:
	if not os.path.isdir("full"):
		os.mkdir("full");
	Newdir=os.path.join(path+"\\full",filename);
	print(Newdir)
	Olddir=os.path.join(path,filename);
	print(Olddir)
	shutil.copyfile(Olddir,Newdir);
else:
	if not os.path.isdir("part"):
		os.mkdir("part");
	Newdir=os.path.join(path+"\\part",filename);
	print(Newdir)
	Olddir=os.path.join(path,filename);
	print(Olddir)
	shutil.copyfile(Olddir,Newdir);

print(full)
box=(80,100,260,300)
roi=img.crop(box)
plt.subplot(1,2,2), plt.title('roi')
plt.imshow(roi),plt.axis('off')
plt.show()