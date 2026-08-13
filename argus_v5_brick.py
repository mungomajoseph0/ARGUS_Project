import os, csv
from pathlib import Path
from collections import defaultdict

SCAN_PATH = "/storage/emulated/0"
LARGE_MB = 100
SECRETS = [".env","id_rsa","private","seed","wallet",".pem","password",".key"]

print(f"[ARGUS v5] Scanning {SCAN_PATH}...")

files = []
dup_map = defaultdict(list)
secrets_found = []
whatsapp_trash = []
large_files = []
count = 0

for root, dirs, filenames in os.walk(SCAN_PATH, onerror=lambda e: None):
    # skip heavy system junk to keep phone alive
    dirs[:] = [d for d in dirs if d not in [".cache","cache",".thumbnails","Android"]]
    if "Android/data" in root or "Android/obb" in root:
        continue
    for f in filenames:
        try:
            fp = os.path.join(root, f)
            size = os.path.getsize(fp)
            files.append((fp, size))
            dup_map[f].append(fp)
            low = f.lower()
            if any(s in low for s in SECRETS):
                secrets_found.append(fp)
            if "WhatsApp" in root and f.startswith("."):
                whatsapp_trash.append(fp)
            if size > LARGE_MB*1024*1024:
                large_files.append((fp, size))
            count += 1
            if count % 2000 == 0:
                print(f" scanned {count}...")
        except:
            pass

# reports
files_sorted = sorted(files, key=lambda x: x[1], reverse=True)[:20]
dups = {k:v for k,v in dup_map.items() if len(v)>1}

with open("report.csv","w",newline="",encoding="utf-8") as csvf:
    w = csv.writer(csvf)
    w.writerow(["path","size_mb","type"])
    for p,s in files_sorted:
        w.writerow([p, round(s/1024/1024,2), "LARGE"])
    for name, paths in dups.items():
        for p in paths:
            w.writerow([p, "", f"DUP:{name}"])

with open("report.txt","w",encoding="utf-8") as out:
    out.write(f"ARGUS v5 REPORT - {count} files scanned\n")
    out.write(f"Large >{LARGE_MB}MB: {len(large_files)}\n")
    out.write(f"Duplicates: {len(dups)}\n")
    out.write(f"Secrets: {len(secrets_found)}\n")
    out.write(f"WhatsApp trash: {len(whatsapp_trash)}\n\n")
    out.write("TOP 20 LARGEST:\n")
    for p,s in files_sorted:
        out.write(f"{round(s/1024/1024,1)}MB - {p}\n")

print(f"\nDONE. {count} files")
print(f"TOP large: {len(large_files)} | Dups: {len(dups)} | Secrets: {len(secrets_found)}")
print("Files created: report.txt + report.csv")
