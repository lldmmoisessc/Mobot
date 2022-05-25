import os

def generateConfiguration(extension, newfile, Token, seanToken):
    if os.path.exists('config.py') and newfile == True:
        print("Config File Exists")
    else:
        with open('config.py', 'w') as files:
            files.write('Token = \'' + Token + '\'\n')
            files.write('extension = \'' + extension + '\'\n')
            files.write(('seanToken = \'' + seanToken + '\'\n'))
