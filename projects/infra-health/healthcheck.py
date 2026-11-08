#!/usr/bin/env python3
"""Safe, read-only example: disk usage and DNS resolution."""
import argparse
import json
import shutil
import socket
from pathlib import Path


def disk_status(path='.', warning_percent=85):
    total, used, free = shutil.disk_usage(path)
    percent = round(100 * used / total, 1) if total else 0.0
    return {'path': str(Path(path).resolve()), 'used_percent': percent,
            'available_gb': round(free / 1024**3, 2),
            'status': 'warning' if percent >= warning_percent else 'ok'}

def dns_status(hostname):
    try:
        addresses = sorted({r[4][0] for r in socket.getaddrinfo(hostname, None)})
        return {'hostname': hostname, 'status': 'ok', 'addresses': addresses}
    except socket.gaierror:
        return {'hostname': hostname, 'status': 'unresolved', 'addresses': []}

def main():
    parser = argparse.ArgumentParser(description='Read-only local infrastructure check')
    parser.add_argument('--host', default='example.com', help='Only resolve hosts you are allowed to query')
    parser.add_argument('--path', default='.')
    parser.add_argument('--warning', type=int, default=85)
    args = parser.parse_args()
    if not 1 <= args.warning <= 100:
        parser.error('--warning must be between 1 and 100')
    print(json.dumps({'disk': disk_status(args.path, args.warning), 'dns': dns_status(args.host)},
                     indent=2, ensure_ascii=False))

if __name__ == '__main__':
    main()
