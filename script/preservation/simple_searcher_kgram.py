
# input -> search_birthmark, birthmark, obfuscation
import sys
import commands
import time
import requests
import json

f = open(sys.argv[1]).read().split("\n")

def get_hex_row(row_birthmark):
    if row_birthmark == "data" or row_birthmark == "":
        return row_birthmark
    hex_row = ""
    for j in row_birthmark.split(','):
        for i in j.split(' '):
            try:
                hex_row += hex(int(i)).replace('0x', '')
            except:
                return row_birthmark
        hex_row += ','
    return hex_row

if not os.path.exists("./data/search_result/" + sys.argv[3] + "/" + sys.argv[2]):
    os.makedirs("./data/search_result/" + sys.argv[3] + "/" + sys.argv[2])

for i in f:
    f = open("./data/search_result/" + sys.argv[3]] + "/" + sys.argv[2] + "/" + i.split(",")[0] + "-" + sys.argv[2] + ".csv", 'w')
    f.write(i+"\n")
    row = i.split(",", 3)
    if len(row) >= 4:
        encode_row = get_hex_row(row[3].replace("&quot;", ""))
        # encode_row = row[3].replace("&quot;", "")
        start = time.time()
        tmp = requests.post('http://localhost:8983/solr/'+sys.argv[2]+'/query?fl=filename,score,place,birthmark,data&rows=500000&sort=score%20desc&wt=csv',
                json.dumps({'query':'encode_data:' + encode_row}),
                headers={'Content-Type': 'application/json'})

        f.write(tmp.text + "\n")
        f.write("searchTime:" + str(time.time() - start))
        f.close()
