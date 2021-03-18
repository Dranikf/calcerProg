from PIL import Image;
import numpy as np
import ctypes

filename = input('Ender image name: ');
filename += ".png";

#file opening
try:
    im = Image.open(filename);
except FileNotFoundError:
    print('file not found, please try again');
    input();
    exit();
#getting size
size = im.size;
# getting image as array
a = np.asarray(im);
result = [];

def conv32_16(r , g , b):
    """function get r, g , b as int and return appropriate 16int"""
    b = int( b / 8 ); # >> 3
    b = b << 11;
    g = int( g / 4 ); # >> 2
    g =  g << 5;
    r = int( r / 8 ); # >> 3
    temp1 = b + g + r;
    
    # swap bytes order
    temp2 = temp1 >> 8;
    tenp3 = temp1 << 8;
    temp1 = temp2 + tenp3;
    # rrrrr gggggg bbbbb
    # (<<11)  (<<5)  (<<0)
    return ctypes.c_int16( temp1 );

OutFile = filename.split(".");

OutFile[1] = "bin";

filename1 = ".".join(OutFile);


f_obj = open(filename1, 'wb');

# writing to file
for i in list(range(0 , size[1])):
    for j in list(range(0 , size[0])):
        temp = a[i][j];
        f_obj.write(conv32_16(temp[2] , temp[1] , temp[0]));

f_obj.close();

print('saved as ' + filename1);
input();
