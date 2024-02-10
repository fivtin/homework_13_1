from pathlib import Path

from utils.file_funcs import load_from_file

json_filename = str(Path(Path(__file__).parent.parent, 'data', 'products.json'))


def test_load_from_file():
    assert len(load_from_file(json_filename)) == 2
