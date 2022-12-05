with open('index.html', 'rb') as file:
    filedata = file.read()

filedata = filedata.replace('alt="BBC Learning English"'.encode(), 'alt="BBC Learning English" width=200'.encode())
filedata = filedata.replace('alt="Cambly"'.encode(), 'alt="Cambly" width=200'.encode())
filedata = filedata.replace('alt="Unknown website"'.encode(), 'alt="Unknown website" width=50'.encode())
filedata = filedata.replace('alt="Cambridge"'.encode(), 'alt="Cambridge" width=200'.encode())

with open('index.html', 'wb') as file:
    file.write(filedata)