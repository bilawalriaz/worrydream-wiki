#!/usr/bin/env python3
"""Handle HTML text extraction and web_extract fallback for scanned PDFs."""
import os
import re
import html
import subprocess
import sys
import json
import time

WIKI = os.path.expanduser("~/repos/hyperflash-business/departments/engineering/research/worrydream-wiki")
RAW_DIR = os.path.join(WIKI, "raw", "papers")
BASE_URL = "https://worrydream.com/refs/"

try:
    import requests
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "requests", "-q"])
    import requests

def load_env(env_path):
    env = {}
    with open(env_path) as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#') and '=' in line:
                key, _, val = line.partition('=')
                env[key.strip()] = val.strip().strip('"').strip("'")
    return env

env = load_env(os.path.expanduser("~/.hermes/profiles/atlas/.env"))
API_KEY = env.get("OPENCODE_GO_API_KEY")
BASE_URL_API = env.get("OPENCODE_GO_BASE_URL", "https://opencode.ai/zen/go/v1")

def extract_html_files():
    """Extract text from HTML files."""
    files = sorted(os.listdir(RAW_DIR))
    html_files = [f for f in files if f.endswith('.html')]
    
    print(f"Extracting {len(html_files)} HTML files...")
    
    for filename in html_files:
        txt_name = filename.replace('.html', '.txt')
        txt_path = os.path.join(RAW_DIR, txt_name)
        
        if os.path.exists(txt_path) and os.path.getsize(txt_path) > 100:
            print(f"  SKIP: {filename}")
            continue
        
        filepath = os.path.join(RAW_DIR, filename)
        try:
            with open(filepath, 'r', errors='replace') as f:
                content = f.read()
            
            # Strip HTML tags
            content = re.sub(r'<script[^>]*>.*?</script>', '', content, flags=re.DOTALL)
            content = re.sub(r'<style[^>]*>.*?</style>', '', content, flags=re.DOTALL)
            content = re.sub(r'<[^>]+>', ' ', content)
            content = html.unescape(content)
            content = re.sub(r'\s+', ' ', content).strip()
            
            if len(content.split()) > 50:
                with open(txt_path, 'w') as f:
                    f.write(content)
                print(f"  OK: {filename} ({len(content.split())} words)")
            else:
                print(f"  SKIP (too short): {filename}")
        except Exception as e:
            print(f"  FAIL: {filename}: {e}")


def find_scanned_pdfs():
    """Find all scanned PDFs that need fallback."""
    scanned = []
    for f in sorted(os.listdir(RAW_DIR)):
        if f.endswith('.txt'):
            filepath = os.path.join(RAW_DIR, f)
            with open(filepath) as fh:
                first_line = fh.readline()
            if '[SCANNED PDF' in first_line:
                scanned.append(f.replace('.txt', '.pdf'))
    return scanned


def try_web_extract(url):
    """Try to extract text via web_extract (uses Hermes backend)."""
    try:
        # Use curl to hit a simple extraction endpoint
        # We'll use the requests library to call web_extract-like service
        # Actually, let's try downloading alternate versions from known sources
        return None
    except:
        return None


def find_alternate_source(filename):
    """Search for alternate text versions of scanned papers."""
    # Map known scanned papers to alternate sources
    alternates = {
        "Anderson_1972_-_More_is_Different.pdf": "https://www.tkm.kit.edu/downloads/TKM1_2011_more_is_different_PWA.pdf",
        "Feynman_1974_-_Cargo_Cult_Science.pdf": "https://calteches.library.caltech.edu/51/2/CargoCult.htm",
    }
    return alternates.get(filename)


def handle_scanned():
    """Try to get text for scanned PDFs from alternate sources."""
    scanned = find_scanned_pdfs()
    print(f"\n{len(scanned)} scanned PDFs need fallback")
    
    # For now, just report them - we can still analyze them via mimo-v2.5
    # if we provide enough context from the filename
    for pdf in scanned:
        alt = find_alternate_source(pdf)
        if alt:
            print(f"  HAS ALT: {pdf} -> {alt}")
        else:
            print(f"  NO ALT:  {pdf}")
    
    return scanned


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "all"
    
    if mode in ("html", "all"):
        extract_html_files()
    
    if mode in ("scanned", "all"):
        scanned = handle_scanned()
        print(f"\n{len(scanned)} scanned PDFs will need filename-based analysis")
