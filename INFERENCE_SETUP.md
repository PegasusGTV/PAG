# PAG Inference Setup Status

## ✅ Completed Setup

1. **Directory Structure**: Created `data/` directory with symlinks to:
   - `experiments-full-lexical-ripor/`
   - `experiments-splade/`
   - `msmarco-full/`

2. **Script Fixes**: Fixed `full_lexical_ripor_evaluate.sh` by removing undefined `docid_to_tokenids_path` parameter

3. **Model Checkpoint**: Verified at:
   - `experiments-full-lexical-ripor/lexical_ripor_direct_lng_knp_seq2seq_1/checkpoint/`

4. **DocID Files**: Verified:
   - Sequential: `experiments-full-lexical-ripor/t5-full-dense-1-5e-4-12l/aq_smtid/docid_to_tokenids.json`
   - Set-based: `experiments-splade/t5-splade-0-12l/top_bow/docid_to_tokenids.json`

5. **Dependencies**: All installed in `pag_env` conda environment:
   - PyTorch 1.10.0+cu111
   - Transformers 4.17.0
   - FAISS-GPU
   - All other requirements

## ⚠️ Missing Files

The following MS MARCO data files need to be downloaded from [PAG-data](https://drive.google.com/drive/folders/1q8FeHQ6nxPYpl1Thqw8mS-2ndzf7VZ9y?usp=sharing):

Required files/folders:
- `msmarco-full/full_collection/` (directory)
- `msmarco-full/dev_qrel.json`
- `msmarco-full/TREC_DL_2019/` (directory with queries_2019/ and qrel files)
- `msmarco-full/TREC_DL_2020/` (directory with queries_2020/ and qrel files)
- `msmarco-full/dev_queries/` (directory)

## 🚀 Running Inference

Once the MS MARCO data files are downloaded and placed in `data/msmarco-full/`, run:

```bash
cd /data/kmirakho/Gopal/PAG/PAG
source $(conda info --base)/etc/profile.d/conda.sh
conda activate pag_env
bash full_scripts/full_lexical_ripor_evaluate.sh
```

The script is already configured with `task=lexical_constrained_retrieve_and_rerank` on line 1.

## 📝 Notes

- The script uses a single GPU by default (nproc_per_node=1 for the main task)
- Inference requires an 80GB A100 according to the README, but other GPUs (like V100) will work, just slower
- Output will be saved in: `data/experiments-full-lexical-ripor/lexical_ripor_direct_lng_knp_seq2seq_1/all_lex_rets/lex_ret_1000/ltmp_smt_ret_10/` and similar directories

