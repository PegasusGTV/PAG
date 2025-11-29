#!/bin/bash
# Script to verify MS MARCO data files are in the correct location

echo "Verifying MS MARCO data files..."
echo "=================================="

TARGET_DIR="/data/kmirakho/Gopal/PAG/PAG/data/msmarco-full"
ALL_GOOD=true

check_file() {
    if [ -e "$1" ]; then
        if [ -d "$1" ]; then
            size=$(du -sh "$1" 2>/dev/null | cut -f1)
            echo "✓ $1 (directory, $size)"
        else
            size=$(du -h "$1" 2>/dev/null | cut -f1)
            echo "✓ $1 ($size)"
        fi
        return 0
    else
        echo "✗ $1 (MISSING)"
        ALL_GOOD=false
        return 1
    fi
}

echo ""
echo "Required files:"
echo "---------------"

check_file "$TARGET_DIR/full_collection"
check_file "$TARGET_DIR/dev_qrel.json"
check_file "$TARGET_DIR/TREC_DL_2019"
check_file "$TARGET_DIR/TREC_DL_2020"
check_file "$TARGET_DIR/dev_queries"

echo ""
if [ "$ALL_GOOD" = true ]; then
    echo "=================================="
    echo "✓ All required files are present!"
    echo "=================================="
    echo ""
    echo "You can now run inference with:"
    echo "  bash full_scripts/full_lexical_ripor_evaluate.sh"
    exit 0
else
    echo "=================================="
    echo "✗ Some files are missing"
    echo "=================================="
    echo ""
    echo "Please transfer the missing files from your local machine."
    echo "See TRANSFER_INSTRUCTIONS.md for details."
    exit 1
fi

