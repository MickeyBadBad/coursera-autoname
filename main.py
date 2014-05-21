__author__ = 'ILYG'
import os
import re

filelist = os.listdir(os.getcwd())
srtlist = []
mp4list = []
def name(srtlist=srtlist,mp4list=mp4list):
	for i in filelist:
		x = re.match(r'.*[.]srt',i)
		if x != None:
			srtlist.append(x.group())
		else:
			pass
	for i in filelist:
		x = re.match(r'.*[.]mp4',i)
		if x != None:
			mp4list.append(x.group())
		else:
			pass
	return srtlist,mp4list

def rmsame(filelist=filelist):
	for i in mp4list:
		for j in srtlist:
			if i[:-4] == j[:-4]:
				mp4list.remove(i)
				srtlist.remove(j)
			else:
				pass

	return mp4list,srtlist

def rename(filelist=filelist,srtlit=srtlist,mp4list=mp4list):
	if len(srtlist) == 0:
		print 'No file name is change !'
	else:
		mp4list.sort(key=lambda x:int(x[9:-4]))
		srtlist.sort(key=lambda x:int(x[:2]))
		for i in range(len(mp4list)):
			os.rename('./'+mp4list[i],'./'+srtlist[i].strip('.srt')+'.mp4')

if __name__ == '__main__':
	name()
	for i in range(10):
		rmsame()
	rename()
	if raw_input('press any key to continue:'):
		pass
