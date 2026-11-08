#!/usr/bin/env python3
"""Summarize fictitious incident records with Python's standard library."""
import argparse
import csv
import json
from collections import Counter
from pathlib import Path

DATA_FILE = Path(__file__).parent / 'data' / 'incidents.csv'
VALID = {'low', 'medium', 'high', 'critical'}

def analyze(path):
    with open(path, newline='', encoding='utf-8') as fh:
        rows = list(csv.DictReader(fh))
    by_status, by_priority, by_category = Counter(), Counter(), Counter()
    for row in rows:
        priority = row.get('priority', '').strip().lower()
        if priority not in VALID:
            raise ValueError('Invalid incident priority: ' + priority)
        by_priority[priority] += 1
        by_status[row.get('status', 'unknown').strip().lower()] += 1
        by_category[row.get('category', 'unknown').strip().lower()] += 1
    return {'total': len(rows), 'by_priority': dict(by_priority),
            'by_status': dict(by_status), 'by_category': dict(by_category)}

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', type=Path, default=DATA_FILE)
    args = parser.parse_args()
    print(json.dumps(analyze(args.input), ensure_ascii=False, indent=2))

if __name__ == '__main__':
    main()
