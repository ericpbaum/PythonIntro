Location =  input('Please provide your filePath of where we should save this file? ')
Namingconvention = input('Please provide your preferred naming convention: ')
Name = input('Please provide your name: ')
Address = input('Please provide your Address: ')
PhoneNumber = input('Please provide your phone number: ')

import os #import the OS library
filePath = Location
fileName = Namingconvention
completePath = filePath+fileName
if os.path.isfile(fileName): #check if file exists
 print('File Exists')
if os.path.isdir(filePath): #check if file path exists
 print('Directory Exists')
if os.path.exists(completePath): #check if complete path exists
 print('Complete path exists')
print('Complete Path',completePath)
with open(completePath, 'w') as fileHandle: #open file for writing
 fileHandle.write(Name) + fileHandle.write(',') #write data to file 
 fileHandle.write(Address) + fileHandle.write(',') 
 fileHandle.write(PhoneNumber)
with open(completePath, 'r') as fileHandle: #open same file for reading
 data = fileHandle.read() #read data from the file
 print(data)