import os

WATCH = ["/storage/emulated/0/Download", "/storage/emulated/0/Documents"]

def search_v2(query):
    q = query.lower()
    # Make "executive being" match "Executive-Being"
    q_norm = q.replace("-"," ").replace("_"," ")
    hits=[]
    for root in WATCH:
        if not os.path.exists(root): continue
        for d,_,files in os.walk(root):
            if d.count('/')>12: continue
            for f in files:
                fp = os.path.join(d,f)
                f_norm = f.lower().replace("-"," ").replace("_"," ")
                # 1. Check filename with hyphen fix
                if q_norm in f_norm or q in f.lower():
                    hits.append(fp)
                    continue
                # 2. NEW: Check INSIDE txt/html files
                if fp.endswith(('.txt','.html','.md')):
                    try:
                        with open(fp,'r', errors='ignore') as file:
                            content = file.read(8000).lower().replace("-"," ")
                            if q_norm in content:
                                hits.append(fp + " [inside content]")
                    except:
                        pass
                if len(hits)>=25:
                    return hits
    return hits

print("ARGUS v0.2 - Sees INSIDE files")
while True:
    q=input("\n[ARGUS] > ")
    if q in ['exit','quit']: break
    if not q.strip(): continue
    h=search_v2(q)
    print(f"\nFound {len(h)} offline:")
    for x in h[:15]:
        print(f" - {x}")