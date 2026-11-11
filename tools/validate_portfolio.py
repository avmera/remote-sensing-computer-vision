"""Offline publication checks. Never runs notebook cells or loads model files."""
from pathlib import Path
import ast
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
failures = []
notebooks = list(ROOT.glob('*/*.ipynb'))
for path in notebooks:
    nb = json.loads(path.read_text(encoding='utf-8'))
    assert nb['nbformat'] == 4
    ids = [cell['id'] for cell in nb['cells']]
    assert len(ids) == len(set(ids))
    for cell in nb['cells']:
        if cell['cell_type'] != 'code':
            continue
        source = ''.join(cell['source'])
        # No shell / magic cells should remain in this publication copy.
        try:
            ast.parse(source)
        except SyntaxError as exc:
            failures.append(f'{path.name}/{cell["id"]}: {exc}')
for path in ROOT.rglob('*.md'):
    for link in re.findall(r'!?\[[^\]]*\]\(([^)]+)\)', path.read_text(encoding='utf-8')):
        if '://' not in link and not link.startswith('#'):
            if not (path.parent / link.split('#')[0]).exists():
                failures.append(f'Broken link in {path.name}: {link}')
excluded = {'.pt', '.pth', '.h5', '.pkl', '.npy', '.zip', '.pem', '.key'}
files = [p for p in ROOT.rglob('*') if p.is_file() and '.git' not in p.parts]
for path in files:
    if path.suffix in excluded or path.stat().st_size > 10_000_000:
        failures.append(f'Unexpected publication artifact: {path.relative_to(ROOT)}')
    if path.suffix in {'.md', '.ipynb', '.json', '.yaml', '.txt', '.csv'}:
        text = path.read_text(encoding='utf-8')
        if re.search(r'(?:gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|AKIA[A-Z0-9]{16}|-----BEGIN .*PRIVATE KEY|[A-Za-z]:\\\\?Users\\\\?)', text):
            failures.append(f'Potential sensitive content: {path.relative_to(ROOT)}')
print(f'Checked {len(notebooks)} notebooks and {len(files)} files without executing experiments.')
if failures:
    print('\n'.join(failures))
    sys.exit(1)
print('PASS: syntax, local documentation links, size limits, and sensitive-artifact checks.')
