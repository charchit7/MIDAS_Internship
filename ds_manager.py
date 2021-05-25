import os
import pathlib as Path
from collections import defaultdict
import csv

# os.walk() returns the generator which is of type path, directory, filename

#to check for the unique files in a csv
# from more_itertools import unique_everseen
# with open('1.csv','r') as f, open('2.csv','w') as out_file:
#     out_file.writelines(unique_everseen(f))

path = '/Users/mac_admin/Desktop/MIDAS/testing'

def create_list_for_csv(path):
    """
    takes path and returns the list containing 
    the list mapping of parent directory of image : image file name
    """
    mapping_dir_img = []
    for directory in os.listdir(path):
        if directory == '.DS_Store':
            continue
        else:
            newp = path+'/'+directory
            for images in os.listdir(newp):
                mapping_dir_img.append([directory,images])
    
    return mapping_dir_img

def create_csv(images_list, csv_name):
    
    """
    creates csv file and stores the data..
    """
    
    print('the csv is created in path:', os.getcwd())
    with open(csv_name, 'w') as csvfile:
        ff = ['labels','images']
        writer = csv.writer(csvfile)
        writer.writerow(ff)
        for images in images_list:
            writer.writerow(images)
    print('csv file create!')


def checkdirfordir(path,name):
    obj = os.scandir(path)
    for files in obj:
        if files.name == name and files.is_dir:
            print('directory is present in the given path..')
            print('printing the path to the directory...')
            temp = path+str(files.name)
            print('Path is::',temp)
            print('files/directories in that path:')
            print('.....')
            print(os.listdir(temp))


temp = create_list_for_csv(path)
create_csv(temp,'mark2.csv')



[('img001-005.png', 'small_o', tensor(0.7097)), ('img001-015.png', 'O', tensor(0.6159)), ('img001-041.png', 'O', tensor(0.5871)), ('img001-028.png', '00', tensor(0.5985)), ('img001-040.png', '00', tensor(0.8653)), ('img001-031.png', 'O', tensor(0.5443)), ('img001-006.png', 'small_o', tensor(0.4994)), ('img001-039.png', '00', tensor(0.5399)), ('img001-048.png', 'O', tensor(0.6689)), ('img001-035.png', 'small_o', tensor(0.6379)), ('img001-032.png', '00', tensor(0.6969)), ('img001-038.png', 'O', tensor(0.8594)), ('img001-020.png', '00', tensor(0.7054)), ('img001-023.png', 'O', tensor(0.7565)), ('img001-022.png', '00', tensor(0.6484))]

[('img002-033.png', '01', tensor(0.9472)), ('img002-022.png', '01', tensor(0.9492)), ('img002-014.png', '01', tensor(0.9988)), ('img002-016.png', 'I', tensor(0.4381)), ('img002-015.png', '01', tensor(0.9963)), ('img002-027.png', 'I', tensor(0.3958)), ('img002-039.png', '01', tensor(0.9915)), ('img002-005.png', '01', tensor(0.5947)), ('img002-051.png', '01', tensor(0.4819)), ('img002-023.png', '01', tensor(0.9996)), ('img002-044.png', 'I', tensor(0.5023)), ('img002-054.png', '01', tensor(0.7846)), ('img002-036.png', 'I', tensor(0.5451)), ('img002-029.png', '01', tensor(0.9852)), ('img002-030.png', '01', tensor(0.8619))]

[('img003-001.png', '02', tensor(1.0000)), ('img003-035.png', '02', tensor(0.9243)), ('img003-014.png', '02', tensor(0.8923)), ('img003-029.png', '02', tensor(0.9993)), ('img003-013.png', '02', tensor(0.9885)), ('img003-038.png', '02', tensor(1.0000)), ('img003-052.png', '02', tensor(0.9948)), ('img003-018.png', '02', tensor(0.9973)), ('img003-051.png', '02', tensor(1.0000)), ('img003-021.png', '02', tensor(0.9946)), ('img003-043.png', '02', tensor(1.0000)), ('img003-046.png', 'small_x', tensor(0.5150)), ('img003-034.png', '02', tensor(0.9897)), ('img003-024.png', '02', tensor(0.9999)), ('img003-007.png', '02', tensor(0.9998))]

[('img004-010.png', '03', tensor(1.0000)), ('img004-032.png', '03', tensor(0.9968)), ('img004-015.png', '03', tensor(0.9982)), ('img004-005.png', '03', tensor(0.9952)), ('img004-053.png', '03', tensor(0.9999)), ('img004-052.png', '03', tensor(0.9986)), ('img004-004.png', '03', tensor(0.6506)), ('img004-051.png', '03', tensor(0.9994)), ('img004-054.png', '03', tensor(0.9998)), ('img004-017.png', '03', tensor(0.9999)), ('img004-019.png', '03', tensor(0.9994)), ('img004-043.png', '03', tensor(0.9991)), ('img004-037.png', '03', tensor(0.9999)), ('img004-046.png', '03', tensor(0.9961)), ('img004-045.png', '03', tensor(0.9996))]



for image 1
[('img001-005.png', 'small_o', tensor(0.7097)), ('img001-015.png', 'O', tensor(0.6159)), ('img001-041.png', 'O', tensor(0.5871)), ('img001-028.png', '00', tensor(0.5985)), ('img001-040.png', '00', tensor(0.8653)), ('img001-031.png', 'O', tensor(0.5443)), ('img001-006.png', 'small_o', tensor(0.4994)), ('img001-039.png', '00', tensor(0.5399)), ('img001-048.png', 'O', tensor(0.6689)), ('img001-035.png', 'small_o', tensor(0.6379)), ('img001-032.png', '00', tensor(0.6969)), ('img001-038.png', 'O', tensor(0.8594)), ('img001-020.png', '00', tensor(0.7054)), ('img001-023.png', 'O', tensor(0.7565)), ('img001-022.png', '00', tensor(0.6484))]
for image 2
[('img002-033.png', '01', tensor(0.9472)), ('img002-022.png', '01', tensor(0.9492)), ('img002-014.png', '01', tensor(0.9988)), ('img002-016.png', 'I', tensor(0.4381)), ('img002-015.png', '01', tensor(0.9963)), ('img002-027.png', 'I', tensor(0.3958)), ('img002-039.png', '01', tensor(0.9915)), ('img002-005.png', '01', tensor(0.5947)), ('img002-051.png', '01', tensor(0.4819)), ('img002-023.png', '01', tensor(0.9996)), ('img002-044.png', 'I', tensor(0.5023)), ('img002-054.png', '01', tensor(0.7846)), ('img002-036.png', 'I', tensor(0.5451)), ('img002-029.png', '01', tensor(0.9852)), ('img002-030.png', '01', tensor(0.8619))]
for image 3
[('img003-001.png', '02', tensor(1.0000)), ('img003-035.png', '02', tensor(0.9243)), ('img003-014.png', '02', tensor(0.8923)), ('img003-029.png', '02', tensor(0.9993)), ('img003-013.png', '02', tensor(0.9885)), ('img003-038.png', '02', tensor(1.0000)), ('img003-052.png', '02', tensor(0.9948)), ('img003-018.png', '02', tensor(0.9973)), ('img003-051.png', '02', tensor(1.0000)), ('img003-021.png', '02', tensor(0.9946)), ('img003-043.png', '02', tensor(1.0000)), ('img003-046.png', 'small_x', tensor(0.5150)), ('img003-034.png', '02', tensor(0.9897)), ('img003-024.png', '02', tensor(0.9999)), ('img003-007.png', '02', tensor(0.9998))]
for image 4
[('img004-010.png', '03', tensor(1.0000)), ('img004-032.png', '03', tensor(0.9968)), ('img004-015.png', '03', tensor(0.9982)), ('img004-005.png', '03', tensor(0.9952)), ('img004-053.png', '03', tensor(0.9999)), ('img004-052.png', '03', tensor(0.9986)), ('img004-004.png', '03', tensor(0.6506)), ('img004-051.png', '03', tensor(0.9994)), ('img004-054.png', '03', tensor(0.9998)), ('img004-017.png', '03', tensor(0.9999)), ('img004-019.png', '03', tensor(0.9994)), ('img004-043.png', '03', tensor(0.9991)), ('img004-037.png', '03', tensor(0.9999)), ('img004-046.png', '03', tensor(0.9961)), ('img004-045.png', '03', tensor(0.9996))]
for image 5
[('img005-015.png', '04', tensor(0.9999)), ('img005-026.png', '04', tensor(0.9996)), ('img005-030.png', '04', tensor(0.6328)), ('img005-053.png', '04', tensor(0.9999)), ('img005-041.png', '04', tensor(0.9996)), ('img005-035.png', '04', tensor(0.9999)), ('img005-010.png', '04', tensor(1.0000)), ('img005-003.png', '04', tensor(0.9999)), ('img005-006.png', '04', tensor(0.9991)), ('img005-028.png', '04', tensor(0.9990)), ('img005-018.png', '04', tensor(0.9997)), ('img005-040.png', '04', tensor(0.9998)), ('img005-019.png', '04', tensor(0.9998)), ('img005-043.png', '04', tensor(0.9999)), ('img005-039.png', '04', tensor(0.9998))]
for image 6
[('img006-040.png', '05', tensor(1.0000)), ('img006-013.png', '05', tensor(1.0000)), ('img006-031.png', '05', tensor(0.9999)), ('img006-037.png', '05', tensor(0.9999)), ('img006-046.png', '05', tensor(0.8876)), ('img006-054.png', '05', tensor(0.9553)), ('img006-019.png', '05', tensor(0.9987)), ('img006-044.png', '05', tensor(1.0000)), ('img006-033.png', '05', tensor(0.7419)), ('img006-047.png', '05', tensor(1.0000)), ('img006-016.png', 'S', tensor(0.8867)), ('img006-028.png', '05', tensor(1.0000)), ('img006-002.png', '05', tensor(1.0000)), ('img006-048.png', '05', tensor(0.9999)), ('img006-034.png', '05', tensor(0.9848))]
for image 7
[('img007-055.png', '06', tensor(0.9991)), ('img007-007.png', '06', tensor(0.9974)), ('img007-053.png', '06', tensor(0.9764)), ('img007-020.png', '06', tensor(1.0000)), ('img007-006.png', '06', tensor(0.5244)), ('img007-030.png', '06', tensor(0.5524)), ('img007-021.png', '06', tensor(0.9677)), ('img007-009.png', '06', tensor(0.9749)), ('img007-037.png', '06', tensor(0.9997)), ('img007-016.png', '06', tensor(0.9999)), ('img007-051.png', '06', tensor(0.9999)), ('img007-048.png', '06', tensor(0.9997)), ('img007-043.png', '06', tensor(0.9993)), ('img007-028.png', '06', tensor(0.9999)), ('img007-035.png', '06', tensor(0.9543))]
for image 8
[('img008-054.png', 'small_f', tensor(0.9589)), ('img008-048.png', '07', tensor(0.9984)), ('img008-025.png', '07', tensor(0.9981)), ('img008-001.png', '07', tensor(0.9275)), ('img008-036.png', '07', tensor(0.9996)), ('img008-022.png', '07', tensor(0.9995)), ('img008-037.png', '07', tensor(0.9999)), ('img008-030.png', '07', tensor(1.0000)), ('img008-043.png', '07', tensor(0.9994)), ('img008-006.png', '07', tensor(0.9894)), ('img008-020.png', '07', tensor(0.9997)), ('img008-004.png', '07', tensor(0.6930)), ('img008-050.png', '07', tensor(0.9996)), ('img008-051.png', '07', tensor(0.9989)), ('img008-045.png', '07', tensor(0.9917))]
for image 9
[('img009-027.png', '08', tensor(1.0000)), ('img009-050.png', '08', tensor(1.0000)), ('img009-014.png', '08', tensor(1.0000)), ('img009-043.png', '08', tensor(0.9999)), ('img009-055.png', '08', tensor(0.9999)), ('img009-053.png', '08', tensor(0.9994)), ('img009-025.png', '08', tensor(1.0000)), ('img009-033.png', '08', tensor(0.4942)), ('img009-019.png', '08', tensor(1.0000)), ('img009-004.png', '08', tensor(0.9977)), ('img009-044.png', '08', tensor(1.0000)), ('img009-048.png', '08', tensor(0.9999)), ('img009-031.png', '08', tensor(1.0000)), ('img009-021.png', '08', tensor(0.9936)), ('img009-002.png', '08', tensor(0.9999))]

















image_path = '/content/drive/MyDrive/test/Sample004'
sp004 = os.listdir(image_path)
sp004

image_path = '/content/drive/MyDrive/test/Sample004'
res = []
for i in sp004:
  image_path = os.path.join(image_path,i)
  pred,pred_idx,probs = inference.predict(image_path)
  image_path = '/content/drive/MyDrive/test/Sample004'
  res.append((i,pred, probs[pred_idx]))
print(res)


for i in range(1,10):
image_path = '/content/drive/MyDrive/test/Sample/00'+'i'


def automate(path):
    for i in range(62):
        arr = os.listdir(path)
        res = []
        for j in arr:
            image_path = os.path.join(path,j)
            pred,pred_idx,probs = inference.predict(image_path)
            image_path = path
            res.append(j,pred,probs[pred_idx])
        print('for image',i)
        print(res)
