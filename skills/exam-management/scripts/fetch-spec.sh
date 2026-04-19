#!/bin/bash
# fetch-spec.sh - Fetches the latest LinguoFlow Exam Specification

OUTPUT_FILE="${1:-E8-exam-spec.md}"
API_URL="http://localhost:3000/api/exam-spec.md"

echo "Fetching latest specification from $API_URL..."
curl -s -H "x-api-key: $LINGUOFLOW_API_KEY" "$API_URL" -o "$OUTPUT_FILE"

if [ $? -eq 0 ]; then
    echo "Specification saved to $OUTPUT_FILE"
else
    echo "Error fetching specification"
    exit 1
fi
