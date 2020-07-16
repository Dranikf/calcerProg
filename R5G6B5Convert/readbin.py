import ctypes;
import numpy;
from PIL import Image;

width = int(input('enter width: '));
height = int(input('enter height: '));

filename = input('enter filename: ');

def read565(a):
    """consert 16 bit color to 32"""
    result = [];
    
    result.append((a & 63488)>>11);# 63488 = 11111 000000 00000
    result.append((a & 2016)>>5);# 2016 = 00000 1111111 00000
    result.append(a & 31);#00000 000000 11111

    return result;

f_obj = open('result.bin' , 'rb');

im = Image.new('RGB', (width , height));

for i in list(range(0,height)):
    for j in list(range(0,width)):

        # reading 2 bytes
        col16 = f_obj.read(2);
        # convert to int 'little' means that bytes will follow inconsistently 
        col16 = int.from_bytes(col16 ,'little');

        temp = read565(col16);

        temp[0] = temp[0]*8;temp[2] = temp[2]*8;
        temp[1] = temp[1]*4;

        # adding getted pixel to image
        im.putpixel((j , i) , tuple(temp));


im.show();

f_obj.close();
