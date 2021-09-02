def swapFile():
    file1 = input('Enter name of first file: ')
    file2 = input('Enter name of second file: ')
    
    with open(file1, 'r') as f:
        Data1 = f.read()
    
    with open(file2, 'r') as f:
        Data2 = f.read()
    
    with open(file2, 'w') as f:
        f.write(Data1)
        
    with open(file1, 'w') as f:
        f.write(Data2)
        
swapFile()
    
    