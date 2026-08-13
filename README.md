cat > README.md << 'EOF'
# ARGUS - Phone-wide File Scanner

ARGUS scans your entire Android storage (12k+ files) from Termux to find sensitive files, duplicates, and anomalies.

## Features
- **v4 Full Scan** - recursive scan of `/storage/emulated/0`
- Detects large files, APKs, hidden dirs,.env/secrets
- Works 100% offline in Termux
- Optimized for low RAM Android devices

## Files
- `argus_v4_full.py` - latest full scan engine (12k files)
- `argus_v2.py` - lightweight scan
- `argus_phone_v2.py` - phone-optimized version

## Install in Termux
```bash
pkg update && pkg install python git
git clone https://github.com/mungomajoseph0/ARGUS_Project.git
cd ARGUS_Project
python argus_v4_full.py
