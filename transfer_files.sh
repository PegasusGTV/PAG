#!/bin/bash
# Script to help transfer MS MARCO data files from local machine to SSH server
# 
# Usage from your LOCAL machine (not on SSH server):
#   scp -r /home/necromancer/Downloads/gopalakt/required/* user@server:/data/kmirakho/Gopal/PAG/PAG/data/msmarco-full/
#
# Or use rsync (recommended):
#   rsync -avz --progress /home/necromancer/Downloads/gopalakt/required/ user@server:/data/kmirakho/Gopal/PAG/PAG/data/msmarco-full/

echo "To transfer files from your local machine to the SSH server, run one of these commands from YOUR LOCAL MACHINE:"
echo ""
echo "Option 1: Using scp (simple copy)"
echo "  scp -r /home/necromancer/Downloads/gopalakt/required/* kmirakho@gretel:/data/kmirakho/Gopal/PAG/PAG/data/msmarco-full/"
echo ""
echo "Option 2: Using rsync (recommended - shows progress and can resume)"
echo "  rsync -avz --progress /home/necromancer/Downloads/gopalakt/required/ kmirakho@gretel:/data/kmirakho/Gopal/PAG/PAG/data/msmarco-full/"
echo ""
echo "Option 3: If you have the files in a zip/tar archive:"
echo "  scp /home/necromancer/Downloads/gopalakt/required.zip kmirakho@gretel:/data/kmirakho/Gopal/PAG/PAG/data/msmarco-full/"
echo "  Then on the server, extract it:"
echo "  cd /data/kmirakho/Gopal/PAG/PAG/data/msmarco-full/ && unzip required.zip"
echo ""
echo "After transferring, the following should exist:"
echo "  - data/msmarco-full/full_collection/"
echo "  - data/msmarco-full/dev_qrel.json"
echo "  - data/msmarco-full/TREC_DL_2019/"
echo "  - data/msmarco-full/TREC_DL_2020/"
echo "  - data/msmarco-full/dev_queries/"

