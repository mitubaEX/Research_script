import glob
import sys
import os

files = glob.glob("./data/search_result/" + sys.argv[1] + "/*")

for i in files:
    f = open(i).read().split("\n")
    frequnce_file = open("./data/frequence_search_result/" + sys.argv[1] + "/" + os.path.basename(i))
    f075 = open("./data/parsed_search_result/075/" + sys.argv[1] + "/" + os.path.basename(i), 'w')
    f05 = open("./data/parsed_search_result/05/" + sys.argv[1] + "/" + os.path.basename(i), 'w')
    f025 = open("./data/parsed_search_result/025/" + sys.argv[1] + "/" + os.path.basename(i), 'w')
    for index, l in enumerate(f):
        if index <= int(f[1]):
            f075.write(l + "\n")
        if index <= int(f[2]):
            f05.write(l + "\n")
        if index <= int(f[3]):
            f025.write(l + "\n")
    f075.close()
    f05.close()
    f025.close()
