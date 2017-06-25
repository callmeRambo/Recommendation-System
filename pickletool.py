import pickle
import itembasedsimilarity
import os
root = os.getcwd() + '//sets/'

def dumpPickle(item, dirPath):
    output = open(root + dirPath, 'wb')
    pickle.dump(item, output)
    output.close()


def loadPickle(dirPath):
    pkl_file = open(root + dirPath, 'rb')
    data = pickle.load(pkl_file)
    pkl_file.close()
    return data
