import glob
import sys

# argv[1] threshold argv[2] birthmark

files = glob.glob("./data/parsed_search_result/" + sys.argv[1]+ "/" + sys.argv[2] + "*")

for i in files:
    count = 0
    f = open(i).read().split("\n")
    for l in f:
        sim = l.split(",")[2]
        if float(sim) >= float("0.75"):
            count += 1
    print str(count) + "," + str(len(f))
