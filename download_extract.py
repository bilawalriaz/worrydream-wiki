#!/usr/bin/env python3
"""Download all PDFs from worrydream.com/refs/ and extract text."""
import os
import re
import subprocess
import sys
import time

WIKI = os.path.expanduser("~/repos/hyperflash-business/departments/engineering/research/worrydream-wiki")
RAW_DIR = os.path.join(WIKI, "raw", "papers")
LINKS_FILE = "/tmp/worrydream_links.txt"
BASE_URL = "https://worrydream.com/refs/"

def download_all():
    """Download all PDFs and extract text."""
    with open(LINKS_FILE) as f:
        links = [l.strip() for l in f if l.strip() and not l.startswith('#') and l.strip() != './']
    
    print(f"Found {len(links)} links")
    
    pdf_count = 0
    html_count = 0
    skip_count = 0
    fail_count = 0
    
    for i, link in enumerate(links):
        # Clean link
        if link.startswith('http'):
            url = link
            filename = link.split('/')[-1]
        else:
            url = BASE_URL + link
            filename = link
        
        if not filename or filename == './':
            continue
        
        dest = os.path.join(RAW_DIR, filename)
        
        # Skip if already downloaded
        if os.path.exists(dest) and os.path.getsize(dest) > 1000:
            skip_count += 1
            continue
        
        # Download
        try:
            result = subprocess.run(
                ['curl', '-sL', '-o', dest, url],
                capture_output=True, timeout=60
            )
            
            if result.returncode != 0 or not os.path.exists(dest):
                fail_count += 1
                continue
            
            size = os.path.getsize(dest)
            if size < 500:
                os.remove(dest)
                fail_count += 1
                continue
            
            if filename.endswith('.pdf'):
                pdf_count += 1
            else:
                html_count += 1
            
            if (i + 1) % 50 == 0:
                print(f"  Progress: {i+1}/{len(links)} downloaded ({pdf_count} PDFs, {html_count} HTML)")
            
            time.sleep(0.2)  # Be polite
            
        except Exception as e:
            fail_count += 1
            print(f"  FAIL: {filename}: {e}")
    
    print(f"\nDownload complete: {pdf_count} PDFs, {html_count} HTML, {skip_count} skipped, {fail_count} failed")


def extract_all():
    """Extract text from all PDFs."""
    try:
        import fitz
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pymupdf", "-q"])
        import fitz
    
    files = sorted(os.listdir(RAW_DIR))
    pdf_files = [f for f in files if f.endswith('.pdf')]
    
    print(f"\nExtracting text from {len(pdf_files)} PDFs...")
    
    success = 0
    scanned = 0
    fail = 0
    
    for i, filename in enumerate(pdf_files):
        txt_name = filename.replace('.pdf', '.txt')
        txt_path = os.path.join(RAW_DIR, txt_name)
        
        # Skip if already extracted
        if os.path.exists(txt_path) and os.path.getsize(txt_path) > 100:
            success += 1
            continue
        
        filepath = os.path.join(RAW_DIR, filename)
        try:
            doc = fitz.open(filepath)
            text = ""
            for page in doc:
                text += page.get_text()
            doc.close()
            
            if len(text.strip().split()) < 20:
                scanned += 1
                # Try web_extract fallback later
                with open(txt_path, 'w') as f:
                    f.write(f"[SCANNED PDF - text extraction failed, {len(text.split())} words extracted]\n")
            else:
                with open(txt_path, 'w') as f:
                    f.write(text)
                success += 1
            
            if (i + 1) % 50 == 0:
                print(f"  Progress: {i+1}/{len(pdf_files)} extracted ({success} ok, {scanned} scanned)")
                
        except Exception as e:
            fail += 1
            print(f"  FAIL: {filename}: {e}")
    
    print(f"\nExtraction complete: {success} text, {scanned} scanned, {fail} failed")
    return scanned  # number of scanned PDFs that need web_extract


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "both"
    
    if mode in ("download", "both"):
        download_all()
    
    if mode in ("extract", "both"):
        scanned = extract_all()
        if scanned > 0:
            print(f"\n{scanned} scanned PDFs need web_extract fallback")
