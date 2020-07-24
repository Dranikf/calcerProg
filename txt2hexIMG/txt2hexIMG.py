import getch;

def byteArrayBitsRev(array):
    """function for revercing bits in bytes of byteArray"""
    result = bytearray();
    for item in array:
        b = '{:0{width}b}'.format(item, width=8);
        result.append(int(b[::-1], 2));

    return result;


def line2bytesArr(line, reverce):
    """gets the line with hex for every chat and returns bytesArr for save
    if reverce = true, bits will be reverced"""

    line = line[14:len(line)];# drop extra spaces and first number
    c = 0;# counter
    resultArr = '';

    while True:

        num = line[c+2:c+4];
        c += 6;

        if '/' in num:
            break;
        resultArr = resultArr + num;
        
    byteResult = bytearray.fromhex(resultArr);

    if reverce:
        byteResult = byteArrayBitsRev(byteResult);

    return byteResult;


#MAIN+++++++++++++++++++++++++++++++++++++++++++++++
readingMode = 0; #0 - reading header; 1 - reading data

txtFilename = input('Enter file name: ');
try:    
    read_obj = open(txtFilename, 'r');
except FileNotFoundError:
    print("can't find " + txtFilename);
    exit();


print('need reverece bits? (y/n)');
while True:
    temp = getch.getch();
    if temp == 'y':
        revFlag = True;
        break;
    elif temp == 'n':
        revFlag = False;
        break;


save_obj = open('result.bin', 'wb');
tempCounter = 0;

while(True):
    line = read_obj.readline();

    if line == '' or '};' in line:
        break;

    if readingMode == 0:
        if '{' in line:
            readingMode = 1;# in the next line will be data
    elif readingMode == 1:
        save_obj.write(line2bytesArr(line, revFlag));

read_obj.close();
save_obj.close();
print('saved as result.bin');
#MAIN+++++++++++++++++++++++++++++++++++++++++++++++
