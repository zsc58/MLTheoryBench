#!/usr/bin/env python3
"""Unpack bounded text sources from a downloaded archive, without executing them."""
from __future__ import annotations
import argparse
import hashlib
import json
import stat
import tarfile
import zipfile
from pathlib import Path, PurePosixPath

TEXT_SUFFIXES = {'.lean', '.tex', '.bib', '.md', '.json', '.jsonl', '.yaml', '.yml', '.toml', '.txt', '.py'}
SPECIAL_NAMES = {'lean-toolchain', 'LICENSE', 'LICENSE.md', 'LICENSE.txt'}

def unpack(archive: Path, destination: Path):
    if destination.exists():
        raise ValueError('Refusing to overwrite an extracted snapshot')
    if zipfile.is_zipfile(archive):
        with zipfile.ZipFile(archive) as z:
            members = []
            for i in z.infolist():
                if i.is_dir(): continue
                if stat.S_ISLNK(i.external_attr >> 16): raise ValueError('Symlinks are not accepted')
                if i.file_size > 25_000_000: raise ValueError('Oversized member')
                members.append((i.filename, z.read(i)))
    else:
        with tarfile.open(archive) as t:
            members = []
            for i in t.getmembers():
                if i.isdir(): continue
                if not i.isfile(): raise ValueError('Only regular files are accepted')
                if i.size > 25_000_000: raise ValueError('Oversized member')
                members.append((i.name, t.extractfile(i).read()))
    if sum(len(b) for _,b in members) > 100_000_000: raise ValueError('Oversized archive')
    records = []
    for name, data in members:
        p = PurePosixPath(name)
        if p.is_absolute() or '..' in p.parts: raise ValueError('Unsafe member path')
        if p.suffix not in TEXT_SUFFIXES and p.name not in SPECIAL_NAMES: continue
        data.decode('utf-8')
        target = destination.joinpath(*p.parts)
        target.parent.mkdir(parents=True,exist_ok=True)
        target.write_bytes(data)
        records.append({'path': name,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()})
    destination.mkdir(parents=True,exist_ok=True)
    (destination/'extraction_manifest.json').write_text(json.dumps({
        'archive':str(archive),'archive_sha256':hashlib.sha256(archive.read_bytes()).hexdigest(),
        'executed':False,'files':records},ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'destination':str(destination),'text_files':len(records)}))

if __name__ == '__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('archive',type=Path);p.add_argument('destination',type=Path)
    a=p.parse_args();unpack(a.archive,a.destination)
