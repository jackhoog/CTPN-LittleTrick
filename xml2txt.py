#coding=utf-8
import os
import sys
import xml.etree.ElementTree as ET
import glob

def xml_to_txt(indir,outdir):

    os.chdir(indir)
    annotations = os.listdir('.')
    annotations = glob.glob(str(annotations)+'*.xml')

    for i, file in enumerate(annotations):

        file_save = file.split('.')[0]+'.txt'
        file_txt=os.path.join(outdir,file_save)
        f_w = open(file_txt,'w')

        # actual parsing
        in_file = open(file,encoding='UTF-8')
        tree=ET.parse(in_file)
        root = tree.getroot()

        for obj in root.iter('object'):
                current = list()
                name = obj.find('name').text

                xmlbox = obj.find('bndbox')
                xmin = xmlbox.find('xmin').text
                xmax = xmlbox.find('xmax').text
                ymin = xmlbox.find('ymin').text
                ymax = xmlbox.find('ymax').text

                f_w.write(xmin+','+ymin+','+xmax+','+ymin+','+xmax+','+ymax+','+xmin+','+ymax+'\n')


indir = 'E:\dataset\Scan_CTPN/xml'   #xml目录
outdir ='E:\dataset\Scan_CTPN/txt'  #txt目录

xml_to_txt(indir, outdir)
