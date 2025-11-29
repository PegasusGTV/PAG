# MS MARCO Data Download Issue

## Problem

The automated download using `gdown` is encountering Google Drive permission/access issues when trying to download the MS MARCO data files. The error message indicates:

```
Cannot retrieve the public link of the file. You may need to change
the permission to 'Anyone with the link', or have had many accesses.
```

## What Was Successfully Downloaded

✅ **Model checkpoint and DocID files** (already present):
- Model: `experiments-full-lexical-ripor/lexical_ripor_direct_lng_knp_seq2seq_1/checkpoint/`
- Sequential DocIDs: `experiments-full-lexical-ripor/t5-full-dense-1-5e-4-12l/aq_smtid/docid_to_tokenids.json`
- Set-based DocIDs: `experiments-splade/t5-splade-0-12l/top_bow/docid_to_tokenids.json`

## What's Still Missing

❌ **MS MARCO data files** (required for inference):
- `data/msmarco-full/full_collection/` (directory)
- `data/msmarco-full/dev_qrel.json`
- `data/msmarco-full/TREC_DL_2019/` (directory)
- `data/msmarco-full/TREC_DL_2020/` (directory)
- `data/msmarco-full/dev_queries/` (directory)

## Solutions

### Option 1: Manual Download (Recommended)

1. Go to the [PAG-data Google Drive](https://drive.google.com/drive/folders/1q8FeHQ6nxPYpl1Thqw8mS-2ndzf7VZ9y?usp=sharing)
2. Navigate to the `msmarco-full` folder
3. Download the following files/folders:
   - `full_collection` folder
   - `dev_qrel.json`
   - `TREC_DL_2019` folder
   - `TREC_DL_2020` folder
   - `dev_queries` folder
4. Extract and place them directly in `data/msmarco-full/`

### Option 2: Use Google Drive API with Authentication

If you have access to Google Drive API credentials, you could use authenticated access to download the files.

### Option 3: Wait and Retry

Sometimes Google Drive has temporary rate limits. You could try again later.

### Option 4: Contact Repository Maintainers

The repository maintainers may need to adjust the Google Drive folder permissions to allow public downloads.

## Current Status

The download script is working for most files, but Google Drive is blocking access to the MS MARCO data files specifically. This appears to be a Google Drive limitation rather than an issue with the download script.

