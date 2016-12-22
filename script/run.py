import rename_class;


starttime = datetime.datetime.now();
print("satrt at "+str(starttime));		
pathset("D:\mydatabase\haixin_test");
rename(0,6);#运行
#imcut("result.txt")
endtime = datetime.datetime.now();
print("end at "+str(endtime))
interval=(endtime - starttime).seconds
print("used "+str(interval)+"s");