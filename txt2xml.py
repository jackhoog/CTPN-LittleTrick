# -*- coding:UTF-8 -*-
import os, sys
import glob
from PIL import Image

# 图像存储位置
src_img_dir = r"E:\dataset\CTPNSample\JPEGImages"
# 图像的 ground truth 的 txt 文件存放位置
src_txt_dir = r"E:\dataset\CTPNSample\label"
# 生成xml文件存放位置
src_xml_dir = r"E:\dataset\CTPNSample\xmlLabel"

img_Lists = glob.glob(src_img_dir + '/*.jpg')
img_basenames = []  # e.g. 100.jpg
for item in img_Lists:
    img_basenames.append(os.path.basename(item))
img_names = []  # e.g. 100
for item in img_basenames:
    temp1, temp2 = os.path.splitext(item)
    img_names.append(temp1)

print(img_names)
for img in img_names:
    im = Image.open((src_img_dir + '/' + img + '.jpg'))
    width, height = im.size  # xml文件中需要width和height信息，这里通过Image库计算出来
    # open the corresponding txt file，由于图片数量和txt数量不一致，所以对于有些图片，没有对应的txt文件，所以这边要用try
    try:
        gt = open(src_txt_dir + '/' + img + '.txt').read().splitlines()  # 把txt文件里每一行提取出来，我的txt有两行
        # print(gt)
        # print(gt[0],tpye(gt[0]))
    except:
        continue  # 跳过这次循环，进入下一张图片循环

    # write in xml file
    # os.mknod(src_xml_dir + '/' + img + '.xml')
    xml_file = open((src_xml_dir + '/' + img + '.xml'), 'w')
    xml_file.write('<annotation>\n')
    xml_file.write('    <folder>VOC2007</folder>\n')
    xml_file.write('    <filename>' + str(img) + '.jpg' + '</filename>\n')
    xml_file.write('    <size>\n')
    xml_file.write('        <width>' + str(width) + '</width>\n')
    xml_file.write('        <height>' + str(height) + '</height>\n')
    xml_file.write('        <depth>3</depth>\n')
    xml_file.write('    </size>\n')

    # write the region of image on xml file
    num_obj = len(gt)#int(gt[0])
    print('num_obj: ', num_obj)
    # assert 0
    for i in range(num_obj):

        print(gt[i],type(gt[i]))
        spt = gt[i].split(',')  # 这里如果txt里面是以逗号‘，’隔开的，那么就改为spt = img_each_label.split(',')。

        xml_file.write('    <object>\n')
        xml_file.write('        <name>' + str('txt') + '</name>\n')  # 类别名称,可以固定下来
        xml_file.write('        <pose>Unspecified</pose>\n')
        xml_file.write('        <truncated>0</truncated>\n')
        xml_file.write('        <difficult>0</difficult>\n')
        xml_file.write('        <bndbox>\n')
        xml_file.write('            <xmin>' + str(spt[0]) + '</xmin>\n')
        xml_file.write('            <ymin>' + str(spt[1]) + '</ymin>\n')
        xml_file.write('            <xmax>' + str(spt[2]) + '</xmax>\n')
        xml_file.write('            <ymax>' + str(spt[-1]) + '</ymax>\n')
        xml_file.write('        </bndbox>\n')
        xml_file.write('    </object>\n')


    xml_file.write('</annotation>')
    print('finish {}'.format(img))
