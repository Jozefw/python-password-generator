from pathlib import Path;

p = Path('.')
p.relative_to(p.parent)