from os import listdir
import string
import csv
import matplotlib.pyplot as plt
from os.path import isfile, join
onlyfiles = [f for f in listdir("C:/Users/Harsh/Desktop/Brown-Corpus/corpusCheck") if
             isfile(join("C:/Users/Harsh/Desktop/Brown-Corpus/corpusCheck", f))]

file_not_toRead = ["main.py", ".DS_Store", "mycsvfile.csv", "bible.txt"]



class corpusCheck:
    def __init__(self):
        self.wordDict = {}
        for files in onlyfiles:
            if files in file_not_toRead:
                continue
            read = open(files, "r+")
            for lines in read:
                lines = lines.split()
                for words in lines:
                    words = words.split("/")
                    for word in words:
                        word = word.translate(str.maketrans('', '', string.punctuation))
                        
                        if word == '' or word == ' ':
                            continue
                        if checkKey(self.wordDict, word):
                            self.wordDict[word] += 1
                        else:
                            self.wordDict[word] = 1
        self.wordDict = sorted(self.wordDict.items(), key=lambda x: x[1])
        self.wordDict = dict(self.wordDict)
        

        def checkKey(dic, key):
            if key in dic.keys(): 
                return True
            else: 
                return False
        
        def putinCSV():
            with open("mycsvfile.csv", "w", newline="") as f:
                w = csv.writer(f)
                for words in self.wordDict:
                    w.writerow([words, self.wordDict[words]])




# x = []
# y = []
# with open("mycsvfile.csv", 'r', newline="") as f:
#     plot = csv.reader(f, delimiter=',')
#     for row in plot:
#         x.append(row[0])
#         y.append(int(row[1]))
# plt.bar(x, y, color='g', width=0.72, label="Word Frequency")
# plt.xlabel("Word")
# plt.ylabel("Frequency")
# plt.title("Brown Corpus")
# plt.legend()
# plt.show()
