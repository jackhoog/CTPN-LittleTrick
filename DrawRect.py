import os
import cv2

def drawRect(inPath,txtPath,outPath,vis=False):
    inImgFs = os.listdir(inPath)
    for inImgF in inImgFs:
        im = cv2.imread(inPath+os.sep+inImgF)
        with open(txtPath+os.sep+inImgF.strip('.jpg')+'.txt', 'r') as f:
            lines = f.readlines()
            while '\n' in lines:
                lines.remove('\n')

            for line in lines:
                line = list(map(int,line.split(',')))
                x1 = line[0]
                y1 = line[1]
                x2 = line[2]
                y2 = line[5]
                cv2.rectangle(im, (x1,y1), (x2,y2), (0,255,0), 4)
            if vis == True:
                cv2.imshow('im',im)
                cv2.waitKey(0)
            cv2.imwrite(outPath+os.sep+inImgF,im)
            print(outPath+os.sep+inImgF,'done')
inPath = r'E:\CTPN\data\demo'
txtPath = r'E:\CTPN\data\resTXT'
outPath = r'E:\CTPN\data\resIMG'
drawRect(inPath,txtPath,outPath,True)
