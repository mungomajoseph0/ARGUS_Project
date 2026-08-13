import os
ROOT = "/storage/emulated/0"
SKIP = {'.thumbnails', 'cache', '.cache', '.Trash', 'LOST.DIR'}
def search_all(query):
    q = query.lower()
    q2 = q.replace("-", " ").replace("_", " ")
    hits=[]
    print("Scanning " + ROOT + " for " + query + " ...")
    for dirpath, dirnames, files in os.walk(ROOT, topdown=True):
        dirnames[:] = [d for d in dirnames if d not in SKIP and not d.startswith('.')]
        if 'Android' in dirpath and 'data' in dirpath:
            if len(dirpath.split('/')) > 6:
                continue
        for f in files:
            try:
                low = f.lower()
                if q in low or q2 in low.replace("-", " ").replace("_", " "):
                    hits.append(os.path.join(dirpath, f))
                    if len(hits) >= 50:
                        return hits
            except:
                continue
    return hits

print("ARGUS v3 - Sees ALL 128GB")
while True:
    q=input("\n[ARGUS ALL] > ")
    if q in ['exit','quit']:
        break
    if not q.strip():
        continue
    h=search_all(q)
    print("Found " + str(len(h)) + " across WHOLE PHONE:")
    for x in h[:20]:
        print(" - " + x)