import os

WATCH = ["/storage/emulated/0/Download", "/storage/emulated/0/Documents"]

def search(q):
    q = q.lower()
    hits=[]
    for root in WATCH:
        if not os.path.exists(root):
            continue
        for d,_,files in os.walk(root):
            for f in files:
                if q in f.lower():
                    hits.append(os.path.join(d,f))
                    if len(hits) >= 20:
                        return hits
    return hits

print("ARGUS v2 - Offline")
while True:
    q=input("\n[ARGUS] > ")
    if q in ['exit','quit']:
        break
    h=search(q)
    print("Found " + str(len(h)) + ":")
    for x in h:
        print(" - " + x)
