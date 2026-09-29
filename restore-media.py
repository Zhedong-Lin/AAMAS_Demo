"""Reassemble large MP4s before Pages publishes the static site (lossless)."""
from pathlib import Path
import hashlib
import json

root = Path(__file__).resolve().parent
manifest = json.loads((root / 'media-parts' / 'manifest.json').read_text())
for item in manifest:
    target = root / 'site' / item['path']
    assert (root / 'site').resolve() in target.resolve().parents
    target.parent.mkdir(parents=True, exist_ok=True)
    digest = hashlib.sha256()
    with target.open('wb') as output:
        for name in item['parts']:
            source = root / 'media-parts' / name
            assert (root / 'media-parts').resolve() in source.resolve().parents
            with source.open('rb') as part:
                while block := part.read(1024 * 1024):
                    digest.update(block)
                    output.write(block)
    assert digest.hexdigest() == item['sha256'], f'Checksum mismatch: {target.name}'
    assert target.stat().st_size == item['bytes']
    print(f'Restored and verified {item["path"]}')
