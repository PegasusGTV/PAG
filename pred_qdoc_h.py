import json
import csv
import random
from argparse import ArgumentParser
import sys
from pathlib import Path

# Add parent directory to path
sys.path.append(str(Path(__file__).parent.parent))

from t5_pretrainer.utils.metrics import evaluate 

def load_json(path):
    with open(path, "r") as f:
        return json.load(f)

def load_tsv(path):
    mapping = {}
    row_idx = 0
    with open(path, "r") as f:
        reader = csv.reader(f, delimiter="\t")
        for row in reader:
            if len(row) >= 2:
                key = row[0].strip()
                value = row[1].strip()
                mapping[key] = value
            row_idx += 1
    return mapping

def invert_dict(xty):
    ytx = dict()

    for x, y in xty.items():
        ytx[y] = x
    
    return ytx

parser = ArgumentParser()
parser.add_argument(
    "--gr_preds",
    type=str,
    required=False,
    default="data/msmarco-full/experiments-full-lexical-ripor/lexical_ripor_direct_lng_knp_seq2seq_1/all_lex_rets/lex_ret_1000/TREC_DL_2019",
)
parser.add_argument("--qmap_file", type=str, default="data/msmarco-full/dev_queries/raw.tsv")
parser.add_argument("--dmap_file", type=str, default="data/msmarco-full/full_collection/raw.tsv")
parser.add_argument("--gt_map_file", default="data/msmarco-full/TREC_DL_2019/qrel_binary.json")
parser.add_argument("--output_csv", type=str, default="predicted_docs.csv")
parser.add_argument("--topk", type=int, default=100, help="Number of predictions to dump per query.")
parser.add_argument("--max_queries", type=int, default=200, help="Maximum number of queries to export.")

args = parser.parse_args()

genret_file = args.gr_preds
query_map_file = args.qmap_file
doc_map_file = args.dmap_file
gt_map_file = args.gt_map_file

query_map = load_tsv(query_map_file)  # QID -> Question
print("Loaded Query Map.")

gt_map = load_json(gt_map_file)  # QID -> {DocID: Score}
gt_data = {
    str(q): sorted(
        [(float(score), str(d)) for d, score in v.items() if score != 0],
        key=lambda score_doc: score_doc[0],
        reverse=True,
    )
    for q, v in gt_map.items()
}
print("Loaded Ground Truth Data.")

genret_data = load_json(genret_file)  # QID -> {DocID: score}
genret_data = {str(k): {str(d): float(score) for d, score in v.items()} for k, v in genret_data.items()}
print("Loaded Generative Retriever Predictions.")

doc_map = load_tsv(doc_map_file)  # DocID -> Doc Content
print("Loaded Doc Map.")
print("Data Loaded.")

out_csv = args.output_csv
with open(out_csv, "w") as out:
    query_ids = list(gt_data.keys())
    random.shuffle(query_ids)
    writer = csv.writer(out)
    writer.writerow(
        [
            "Query ID",
            "Query",
            "Min GT Rank",
            "GT Doc ID",
            "GT Doc",
            "nDCG@10",
            "nDCG@100",
            "Recall@10",
            "Recall@100",
            "Pred Rank",
            "Pred Doc ID",
            "Pred Score",
            "Pred Doc",
            "GT Grade",
        ]
    )

    queries_written = 0

    for qid in query_ids:
        if qid not in genret_data:
            continue
        if queries_written >= args.max_queries:
            break
        query_text = query_map.get(qid, "[MISSING QUERY]")
        print(qid, ":", query_text)
        retrieved_docs = genret_data[qid]
        sorted_docs = sorted(retrieved_docs.items(), key=lambda x: x[1], reverse=True)

        gt_docs = gt_data.get(qid)
        if not gt_docs:
            continue  # Need ground-truth docs for context
        gt_grades, gt_doc_ids = zip(*gt_docs)

        position = None
        gt_doc_id = None
        gt_doc_content = None
        for i, (doc_id, score) in enumerate(sorted_docs, 1):
            if doc_id in gt_doc_ids:
                position = i
                gt_doc_id = doc_id
                gt_doc_content = doc_map.get(doc_id, "[MISSING GT DOC CONTENT]")
                break
        if gt_doc_id is None:
            gt_doc_id = gt_doc_ids[0]
            gt_doc_content = doc_map.get(gt_doc_id, "[MISSING GT DOC CONTENT]")

        ndcg = evaluate({qid: genret_data[qid]}, {qid: gt_map[qid]}, metric="ndcg_cut")
        ndcg_10 = ndcg.get("ndcg_cut_10")
        ndcg_100 = ndcg.get("ndcg_cut_100")
        recall = evaluate({qid: genret_data[qid]}, {qid: gt_map[qid]}, metric="recall")
        recall_10 = recall.get("recall_10")
        recall_100 = recall.get("recall_100")

        for rank, (doc_id, score) in enumerate(sorted_docs[: args.topk], 1):
            doc_content = doc_map.get(doc_id, "[MISSING DOC CONTENT]")
            gt_grade = gt_map[qid].get(doc_id, 0)
            writer.writerow(
                [
                    qid,
                    query_text,
                    position,
                    gt_doc_id,
                    gt_doc_content,
                    ndcg_10,
                    ndcg_100,
                    recall_10,
                    recall_100,
                    rank,
                    doc_id,
                    float(score),
                    doc_content,
                    gt_grade,
                ]
            )

        queries_written += 1

    print(f"Queries Written: {queries_written}")
    print(f"Saved CSV to: {out_csv}")