#!/usr/bin/env python
"""
Script to download MS MARCO data files from PAG-data Google Drive folder.
Usage: python download_msmarco_data.py
"""

import os
import gdown
from pathlib import Path

# Google Drive folder ID from the PAG-data link
FOLDER_ID = "1q8FeHQ6nxPYpl1Thqw8mS-2ndzf7VZ9y"
BASE_URL = f"https://drive.google.com/drive/folders/{FOLDER_ID}"

# Target directory
TARGET_DIR = Path("./data/msmarco-full")
TARGET_DIR.mkdir(parents=True, exist_ok=True)

# Required files/folders according to README
REQUIRED_ITEMS = [
    "full_collection",
    "TREC_DL_2019",
    "TREC_DL_2020",
    "dev_qrel.json",
    "dev_queries"
]

def download_folder_from_google_drive(folder_id, output_dir):
    """Download a folder from Google Drive using gdown."""
    print(f"Downloading from Google Drive folder: {folder_id}")
    print(f"Output directory: {output_dir}")
    
    # Method 1: Use gdown download_folder with id parameter
    try:
        print(f"Attempting to download folder using gdown with id parameter...")
        result = gdown.download_folder(id=folder_id, output=str(output_dir), quiet=False, use_cookies=True)
        
        # Check if anything was downloaded
        items = list(output_dir.iterdir())
        if len(items) > 0:
            print("✓ Download completed successfully!")
            return True
        else:
            print("⚠ Download reported success but no files found. Trying alternative...")
            raise Exception("No files downloaded")
    except Exception as e:
        print(f"✗ Method 1 failed: {e}")
        print("\nTrying alternative method (using URL format)...")
        
        # Method 2: Try with URL format
        try:
            url = f"https://drive.google.com/drive/folders/{folder_id}"
            result = gdown.download_folder(url=url, output=str(output_dir), quiet=False, use_cookies=True)
            items = list(output_dir.iterdir())
            if len(items) > 0:
                print("✓ Download completed successfully!")
                return True
            else:
                raise Exception("No files downloaded")
        except Exception as e2:
            print(f"✗ Method 2 failed: {e2}")
            print("\nNote: Google Drive folder downloads may require authentication.")
            print("You may need to download manually from the Google Drive link.")
            return False

def verify_downloaded_files(target_dir):
    """Verify that required files/folders exist."""
    print("\nVerifying downloaded files...")
    missing = []
    
    for item in REQUIRED_ITEMS:
        item_path = target_dir / item
        if item_path.exists():
            if item_path.is_dir():
                size = sum(f.stat().st_size for f in item_path.rglob('*') if f.is_file())
                print(f"  ✓ {item}/ (directory, {size / (1024**3):.2f} GB)")
            else:
                size = item_path.stat().st_size / (1024**2)
                print(f"  ✓ {item} ({size:.2f} MB)")
        else:
            print(f"  ✗ {item} (MISSING)")
            missing.append(item)
    
    if missing:
        print(f"\n⚠ Warning: {len(missing)} required item(s) are missing: {', '.join(missing)}")
        return False
    else:
        print("\n✓ All required files/folders are present!")
        return True

def main():
    print("=" * 60)
    print("PAG MS MARCO Data Downloader")
    print("=" * 60)
    print(f"\nSource: {BASE_URL}")
    print(f"Target: {TARGET_DIR.absolute()}")
    print(f"\nRequired items:")
    for item in REQUIRED_ITEMS:
        print(f"  - {item}")
    
    print("\n" + "=" * 60)
    print("Starting download...")
    print("=" * 60)
    
    # Download the folder
    success = download_folder_from_google_drive(FOLDER_ID, TARGET_DIR)
    
    if success:
        # Verify downloaded files
        verify_downloaded_files(TARGET_DIR)
        print("\n" + "=" * 60)
        print("Download process completed!")
        print("=" * 60)
        print(f"\nData is available at: {TARGET_DIR.absolute()}")
        print("\nYou can now run inference with:")
        print("  bash full_scripts/full_lexical_ripor_evaluate.sh")
    else:
        print("\n" + "=" * 60)
        print("Download failed!")
        print("=" * 60)
        print("\nPlease try one of the following:")
        print("1. Download manually from:", BASE_URL)
        print("2. Use gdown command line:")
        print(f"   gdown --folder {BASE_URL} -O {TARGET_DIR}")
        print("3. Check your internet connection and try again")

if __name__ == "__main__":
    main()

