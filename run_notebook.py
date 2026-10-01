"""Execute analysis.ipynb with this interpreter in a fresh local kernel."""
from pathlib import Path
import json
import os
import sys
from tempfile import TemporaryDirectory

import nbformat
from nbclient import NotebookClient


def execute_fresh(notebook, project):
    """Use a temporary kernel specification; register nothing globally."""
    previous = os.environ.get('JUPYTER_PATH')
    try:
        with TemporaryDirectory(prefix='manga-kernel-') as directory:
            kernel = Path(directory) / 'kernels' / 'manga-local'
            kernel.mkdir(parents=True)
            (kernel / 'kernel.json').write_text(json.dumps({
                'argv': [sys.executable, '-m', 'ipykernel_launcher', '-f',
                         '{connection_file}', '--matplotlib=inline'],
                'display_name': 'MaNGA local Python', 'language': 'python',
            }), encoding='utf-8')
            os.environ['JUPYTER_PATH'] = directory
            client = NotebookClient(
                notebook, timeout=None, kernel_name='manga-local',
                allow_errors=False, resources={'metadata': {'path': str(project)}},
            )
            return client.execute()
    finally:
        if previous is None:
            os.environ.pop('JUPYTER_PATH', None)
        else:
            os.environ['JUPYTER_PATH'] = previous


def main():
    project = Path(__file__).resolve().parent
    cube = project / 'data' / 'manga-8244-12704-LOGCUBE.fits.gz'
    if not cube.is_file():
        raise FileNotFoundError('Download the input cube as described in data/README.md.')
    target = project / 'analysis.ipynb'
    notebook = nbformat.read(target, as_version=4)
    for cell in notebook.cells:
        if cell.cell_type == 'code':
            cell.outputs = []
            cell.execution_count = None
    execute_fresh(notebook, project)
    # An execution error raises before the saved notebook is overwritten.
    nbformat.write(notebook, target)
    print('Execution completed; analysis.ipynb saved.')


if __name__ == '__main__':
    main()
