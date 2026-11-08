#!/usr/bin/env python3
"""Offline audit of HTTP response header names against a short checklist."""
import json
import argparse
from pathlib import Path

RECOMMENDED = {
    'strict-transport-security': 'HSTS: enable only after reviewing HTTPS policy',
    'content-security-policy': 'CSP: consider least-privilege directives',
    'x-content-type-options': 'Set to nosniff where applicable',
    'referrer-policy': 'Consider a privacy-preserving value',
}

def review(headers):
    normalized = {k.lower() for k in headers}
    return {'present': sorted(normalized & RECOMMENDED.keys()),
            'missing': {key: msg for key, msg in RECOMMENDED.items() if key not in normalized},
            'note': 'Presence alone does not establish a secure configuration.'}

def main():
    parser = argparse.ArgumentParser(description='Review sample headers without network traffic')
    parser.add_argument('--input', type=Path, default=Path(__file__).parent / 'data' / 'response_headers.json')
    args = parser.parse_args()
    headers = json.loads(args.input.read_text(encoding='utf-8'))
    if not isinstance(headers, dict):
        parser.error('JSON must be an object of header keys and values')
    print(json.dumps(review(headers), ensure_ascii=False, indent=2))

if __name__ == '__main__':
    main()
