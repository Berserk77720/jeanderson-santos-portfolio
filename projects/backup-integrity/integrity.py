#!/usr/bin/env python3
"""Generate and verify SHA-256 manifest for a local file (no file copies)."""
import argparse
import hashlib
import json
from pathlib import Path

def sha256_file(path):
    digest = hashlib.sha256()
    with open(path, 'rb') as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b''):
            digest.update(chunk)
    return digest.hexdigest()

def manifest(path):
    f = Path(path)
    return {'name': f.name, 'size_bytes': f.stat().st_size, 'sha256': sha256_file(f)}

def verify(path, expected):
    return manifest(path)['sha256'] == expected['sha256'] and Path(path).stat().st_size == expected['size_bytes']

def main():
    parser = argparse.ArgumentParser(description='Local file hash integrity check')
    parser.add_argument('command', choices=['create', 'verify'])
    parser.add_argument('file', type=Path)
    parser.add_argument('--manifest', type=Path, default=Path('manifest.json'))
    args = parser.parse_args()
    if args.command == 'create':
        args.manifest.write_text(json.dumps(manifest(args.file), indent=2), encoding='utf-8')
        print('Manifest written to', args.manifest)
    else:
        data = json.loads(args.manifest.read_text(encoding='utf-8'))
        good = verify(args.file, data)
        print('MATCH' if good else 'MISMATCH')
        if not good:
            raise SystemExit(1)

if __name__ == '__main__':
    main()
