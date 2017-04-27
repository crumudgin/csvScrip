# Program: CSV Script
# Description: generates a .csv file for the intelligent systems project 2
# author: Zac Chu
# usage: when prompted give the script the path to your first set of .stat files, then give it the path
#        to your seccond set of .stat files, continue with this for all .stat file locations


import csv
import os

class CVSScript:
    files = []
    train = []
    test = []



# generates an array of all files within a directory
# peramiters: path - the path to the folder
    def readFolderIntoArray(self, path):
        for (path, dirnames, filenames) in os.walk(path):
            self.files.extend(os.path.join(path, name) for name in filenames)


# adds the correctly classified value to an array of results
# peramiters: file - the file with the data
#             dataset - an integer representing a dataset
    def addFileContentToArrays(self, file, dataset):
        found = False
        with open(file, newline='') as inputfile:
            content = inputfile.readlines()
            content = [x.strip() for x in content]
            for i,item in enumerate(content):
                if item == 'Correctly classified:':
                    if found == False:
                        self.test[dataset].append(content[i+1])
                        found = True
                    else:
                        self.train[dataset].append(content[i+1])

# driver of the script
    def run(self):
        path = input('path to stat files: ')
        self.readFolderIntoArray(path)
        self.train = [[] for i in self.files]
        self.test = [[] for i in self.files]
        while path != '':
            self.files = []
            self.readFolderIntoArray(path)
            for i, data in enumerate(self.files):    
                self.addFileContentToArrays(data, i)
            print(self.train)
            path = input('path to stat files')
        with open("test.csv",'w') as resultFile:
            wr = csv.writer(resultFile, dialect='excel')
            wr.writerows(self.test)
        with open("train.csv", 'w') as resultFile:
            wr = csv.writer(resultFile, dialect='excel')
            wr.writerows(self.train)


def main():
    x = CVSScript()
    x.run()
                    

main()
