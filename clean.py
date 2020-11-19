import os

def rmtree( directory):
    print ("remove tree: " + directory)
    for entry in os.ilistdir(directory):
        is_dir = entry[1] == 0x4000
        if is_dir:
            rmtree(directory + '/' + entry[0])
        else:
            print ("remove file: " + directory + '/' + entry[0])
            os.remove(directory + '/' + entry[0])
    if directory != '.':
        print ("remove dir " + directory)
        os.rmdir(directory)
rmtree('.')
