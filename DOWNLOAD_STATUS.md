# PAG Data Download Status

## ✅ Successfully Downloaded

The following files/folders were successfully downloaded from the PAG-data Google Drive:

1. **Model Checkpoint**: 
   - `data/msmarco-full/experiments-full-lexical-ripor/lexical_ripor_direct_lng_knp_seq2seq_1/checkpoint/` (942 MB)
   - Contains: pytorch_model.bin, config.json, tokenizer files, etc.

2. **DocID Files**:
   - `data/msmarco-full/experiments-full-lexical-ripor/t5-full-dense-1-5e-4-12l/aq_smtid/docid_to_tokenids.json` (529 MB)
   - `data/msmarco-full/experiments-splade/t5-splade-0-12l/top_bow/docid_to_tokenids.json` (2.97 GB)

3. **Other Files**:
   - Some evaluation results and intermediate files

## ⚠️ Missing Files

The following MS MARCO data files are still missing and need to be downloaded:

- `data/msmarco-full/full_collection/` (directory with document collection)
- `data/msmarco-full/dev_qrel.json` (relevance judgments for dev set)
- `data/msmarco-full/TREC_DL_2019/` (directory with queries and qrels)
- `data/msmarco-full/TREC_DL_2020/` (directory with queries and qrels)
- `data/msmarco-full/dev_queries/` (directory with dev queries)

## 📝 Next Steps

The MS MARCO data files need to be downloaded manually from the [PAG-data Google Drive](https://drive.google.com/drive/folders/1q8FeHQ6nxPYpl1Thqw8mS-2ndzf7VZ9y?usp=sharing).

1. Navigate to the `msmarco-full` folder in the Google Drive
2. Download the following:
   - `full_collection` folder
   - `dev_qrel.json`
   - `TREC_DL_2019` folder
   - `TREC_DL_2020` folder  
   - `dev_queries` folder
3. Place them in `data/msmarco-full/` directory

Alternatively, you can try running the download script again:
```bash
cd /data/kmirakho/Gopal/PAG/PAG
source $(conda info --base)/etc/profile.d/conda.sh
conda activate pag_env
python download_msmarco_data.py
```

## 📊 Current Directory Structure

```
data/msmarco-full/
├── experiments-full-lexical-ripor/  (1.6 GB) ✓
├── experiments-splade/              (2.8 GB) ✓
└── msmarco/                         (3.0 GB) ✓
```

The MS MARCO data files should be directly in `data/msmarco-full/` but are currently missing.

