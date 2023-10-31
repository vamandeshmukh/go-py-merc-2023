print('start')

with open('sample.txt', 'r') as file:
    fileData = file.read()
    print(fileData)

with open('sample.txt', 'a') as file:
    fileDataToWrite = '\nsome more text'
    file.write(fileDataToWrite)

with open('sample.txt', 'r') as file:
    fileData = file.read()
    print(fileData)

print('end')
