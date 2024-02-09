"""Implementation of the function of loading a list of categories from a json file."""

from pathlib import Path

from utils.file_funcs import load_from_file

json_filename = str(Path(Path(__file__).parent.parent, 'data', 'products.json'))

print(load_from_file(json_filename))
