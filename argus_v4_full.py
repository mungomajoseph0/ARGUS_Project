import os
ROOT = "/storage/emulated/0"
SKIP = {'.thumbnails', '.cache', '.Trash', 'LOST.DIR'}

def search_all(query):
    q = query.lower()
    q2 = q.replace("-", " ").replace("_", " ")
    hits=[]
    total_scanned=0
    for dirpath, dirnames, files in os.walk(ROOT, topdown=True, onerror=None):
        # don't skip Android - try it
        dirnames[:] = [d for d in dirnames if d not in SKIP]
        # skip only super deep Android/data/data
        if dirpath.count('/') > 9:
            continue
        for f in files:
            total_scanned+=1
            try:
                full = os.path.join(dirpath, f)
                full_low = full.lower()
                # THIS IS THE FIX: search full path, not just name
                if q in full_low or q2 in full_low.replace("-", " ").replace("_", " "):
                    hits.append(full)
            except:
                continue
    return hits, total_scanned

print("ARGUS v4 - Full Path Search")
print("Now searches folder names too")
while True:
    q=input("\n[ARGUS v4] > ")
    if q in ['exit','quit']:
        break
    if not q.strip():
        continue
    h, scanned = search_all(q)
    print("Scanned " + str(scanned) + " files total")
    print("Found " + str(len(h)) + " matching '" + q + "':")
    for x in h[:100]:
        print(" - " + x)
    if len(h) > 100:
        print(" ... and " + str(len(h)-100) + " more (showing 100)")