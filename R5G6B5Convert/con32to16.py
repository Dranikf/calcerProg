from PIL import Image;
import numpy as np
import ctypes

filename = input('Ender image name: '); 
#file opening
im = Image.open(filename);
#getting size
size = im.size;
# getting image as array
a = np.asarray(im);
result = [];

def conv32_16(r , g , b):
    """function get r, g , b as int and return appropriate 16int"""
    r = int(r / 8);# max 31
    g = int(g / 4);# max 63
    b = int(b / 8);# max 31
    # rrrrr gggggg bbbbb
    # (<<11)  (<<5)  (<<0)
    return ctypes.c_int16(b| g<<5 | r<<11);


filename = 'result.bin';
f_obj = open(filename, 'wb');


# writing to file
for i in list(range(0 , size[1])):
    for j in list(range(0 , size[0])):
        temp = a[i][j];
        f_obj.write(conv32_16(temp[0] , temp[1] , temp[2]));

f_obj.close();

print('saved as ' + filename);

im.show();
