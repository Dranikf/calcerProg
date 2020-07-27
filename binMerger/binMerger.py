from getch import getch;
import os;

def readBinFileName(filename):
    """function for reading some bin file, returns [bytes , (int)filesize]"""
    while True:
        try:
            binFile = open(filename, 'rb');
        except FileNotFoundError:
            print("Cant find:" + filename);
            print('s - for skip file');
            print('e - for leave program');
            print('other - for try again');

            temp = getch();
            if temp == 's':
                return None;
            elif temp == 'e':
                exit();
            else:
                continue;

        break;
    
    file_size = os.path.getsize(filename);
    
    result = [binFile.read(file_size), file_size];
    binFile.close();

    return result;

# MAIN -----------------------------------------

descFileName = input('Enter discription file name: ');

try:
    descFile = open(descFileName);
except FileNotFoundError:
    print("Can't find " + descFileName);
    print('Finishing progaram!');
    input();

res_file = open('result.bin', 'wb');
sizes_file = open('sfile' , 'w');

while True:
    binName = descFile.readline();

    if binName == '':
        break;

    file_data = readBinFileName(binName.strip()); 
    if file_data == None:
        continue;
    else:
        res_file.write(file_data[0]);
        sizes_file.writelines(hex(file_data[1]) + '\n');


descFile.close();
res_file.close();
# MAIN -----------------------------------------
