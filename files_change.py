import os
# import cv2
# import pathlib as Path
#this prints the path of the current locations
# print(os.getcwd())
#this prints the directory of the current folders 
#print(os.lisdir(os.getcwd()))
#converter for numbers 

def number_conv():
    for i in range(1,10):
        path = '/Users/mac_admin/Desktop/MIDAS/train/'
        replace_with = str(0) + str(i-1)
        to_replace = 'Sample0' + str(0) + str(i)
        os.replace(path+to_replace,path+replace_with)
        if i==10:
            os.replace(path+'Sample0'+str(i), path+replace_with)
        # print(path+to_replace, path+replace_with)
        

#converter for capital alphabets, use ord() function in python which prints ASCII values.

def alphabet_conv():
    convert_to = '`'
    counter = 1
    path = '/Users/mac_admin/Desktop/MIDAS/train/'
    for i in range(37,63):
        a = 'small_'+chr(ord(convert_to)+counter)
        to_convert = path + 'Sample' + '0' + str(i)
        os.replace(to_convert, a)
        counter += 1


# number_conv()
# alphabet_conv()


