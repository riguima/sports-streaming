from pathlib import Path

import toml

config = toml.load(Path(__file__).parent.parent / '.config.toml')
