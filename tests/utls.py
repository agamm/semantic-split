import os
FIXTURE_DIR = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    'test_files',
)


def test_path(file):
    return os.path.join(FIXTURE_DIR, file)


def load_testdata(file):
    with open(test_path(file), 'r') as f:
        return f.read()
