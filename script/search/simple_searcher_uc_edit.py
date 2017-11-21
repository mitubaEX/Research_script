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

for i in f:
    f = open("./data/search_result/" + sys.argv[2] + "/" + i.split(",")[0] + "-" + sys.argv[2] + ".csv", 'w')
    f.write(i+"\n")
    row = i.split(",", 3)
    if len(row) >= 4:
        encode_row = row[3].replace("&quot;", "")
        start = time.time()

        tmp = requests.post('http://localhost:8983/solr/'+sys.argv[2]+'/query?fl=filename,lev:strdist(data, "'+encode_row+'", edit),place,birthmark,data&rows=500000&sort=strdist(data, "'+encode_row+'", edit)%20desc&wt=csv',
                # json.dumps({'query':'data:' + encode_row}),
                json.dumps({'query':'*:*'}),
                headers={'Content-Type': 'application/json'})

        f.write(tmp.text.encode('utf-8') + "\n")
        f.write("searchTime:" + str(time.time() - start))
        f.close()
