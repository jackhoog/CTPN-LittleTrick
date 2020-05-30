import cv2
import os

def cut_IMG(inPath,outPath):
    im_files = os.listdir(inPath)
    for im_file in im_files:
        orgin_name = im_file.split('.jpg')[0].split(os.sep)[-1]
        im = cv2.imread(inPath+os.sep+im_file)
        #cv2.imshow('im',im)
        #cv2.waitKey(0)
        im_1 = im[:, 0:1200]
        im_2 = im[:, 1200:2400]
        im_3 = im[:, 2400:-1]

        cv2.imwrite(outPath+os.sep+orgin_name + '_1.jpg', im_1)
        cv2.imwrite(outPath+os.sep+orgin_name + '_2.jpg', im_2)
        cv2.imwrite(outPath+os.sep+orgin_name + '_3.jpg', im_3)


def split_TXT(inTXTpath, outTXTpath):

    for txtFile in os.listdir(inTXTpath):
        linesList = []
        with open(inTXTpath+os.sep+txtFile,'r') as iT:
            lines = iT.readlines()
            for line in lines:
                linesList.append(line)

        List1 = []
        List2 = []
        List3 = []
        for line in linesList:
            line = line.split()
            line = line[0].split(',')
            x1 = int(line[0])
            x2 = int(line[2])
            y1 = int(line[1])
            y2 = int(line[5])
            if x2<1200:
                p1 = [x1, y1, x2, y1, x2, y2, x1, y2]
                List1.append(p1)
            elif x1 >= 1200 and x2 <= 2400:
                p2 = [x1-1200, y1, x2-1200, y1, x2-1200, y2, x1-1200, y2]
                List2.append(p2)
            elif (x1 < 1200) and (x2 > 1200):
                p1 = [x1, y1, 1199, y1, 1199, y2, x1, y2]
                p2 = [0, y1, x2 - 1200, y1, x2 - 1200, y2, 0, y2]
                List1.append(p1)
                List2.append(p2)
            elif (x1 < 2400) and (x2 > 2400):
                p1 = [x1-1200, y1, 1199, y1, 1199, y2, x1-1200, y2]
                p2 = [0, y1, x2-2400, y1, x2-2400, y2, 0, y2]
                List2.append(p1)
                List3.append(p2)
            elif (x2 > 2400) and (x1 > 2400):
                p3 = [x1-2400, y1, x2-2400, y1, x2-2400, y2, x1-2400, y2]
                List3.append(p3)
        T1 = outTXTpath + os.sep + txtFile.split('.txt')[0] + '_1.txt'
        T2 = outTXTpath + os.sep + txtFile.split('.txt')[0] + '_2.txt'
        T3 = outTXTpath + os.sep + txtFile.split('.txt')[0] + '_3.txt'
        with open(T1,'w') as f1:
            for line in List1:
                f1.write(str(line).strip('[').strip(']').replace(' ','')+'\n')
        with open(T2,'w') as f2:
            for line in List2:
                f2.write(str(line).strip('[').strip(']').replace(' ','')+'\n')
        with open(T3,'w') as f3:
            for line in List3:
                f3.write(str(line).strip('[').strip(']').replace(' ','')+'\n')



inPath = r'E:\dataset\Wind_Circle\test\image'
outPath = r'E:\dataset\Wind_Circle\test\cutIMG'
inTXTpath = r'E:\dataset\Wind_Circle\test\label'
outTXTpath = r'E:\dataset\Wind_Circle\test\cutLab'
cut_IMG(inPath,outPath)
split_TXT(inTXTpath, outTXTpath)
