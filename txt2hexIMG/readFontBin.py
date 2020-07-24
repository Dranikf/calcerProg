from bitstring import BitArray;
from pathlib import Path;

def printSymbol(symbol, height):
    for i in range(0, height):
        print(symbol[i]);

def getBytes(width, height, array):
    bitString= BitArray(array).bin;
    symbol = [];

    for j in range(0, height):
        tempStr = '';
        for i in range(j, width*height, height):
            tempStr += bitString[i];
        symbol.append(tempStr);
    return symbol;
        
file_name = input('Enter file name: ');

try:
    file_obj = open(file_name, 'rb');
except FileNotFoundError:
    print("can't find " + file_name);
    exit();
    
width  = int(input('Enter character width: '));
height = int(input('Enter charactet height: '));

charSize = int(width * (height/8));
fileSize = Path(file_name).stat().st_size;
charCount = int(fileSize/charSize);

symbols = [];
for i in range(0, charCount):
    symbols.append(getBytes(width, height,file_obj.read(charSize)));

file_obj.close();

while True:
    s = int(input('Enter symbol code you like to see, or -1 for exit: '));
    if s == -1:
        break;
    elif s < -1 or s > charCount:
        print('uncknown signal, try again');
    else:
        printSymbol(symbols[s], height);
