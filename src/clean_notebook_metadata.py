"""
Usage:
    python clean_notebook_metadata.py main.ipynb

This script removes the 'widgets' key from the notebook metadata to fix rendering issues.
"""
import sys
import nbformat

if len(sys.argv) != 2:
    print("Usage: python clean_notebook_metadata.py <notebook_file.ipynb>")
    sys.exit(1)

notebook_path = sys.argv[1]

with open(notebook_path, 'r', encoding='utf-8') as f:
    nb = nbformat.read(f, as_version=nbformat.NO_CONVERT)

if 'widgets' in nb.metadata:
    del nb.metadata['widgets']
    print("Removed 'widgets' metadata.")
else:
    print("No 'widgets' metadata found.")

with open(notebook_path, 'w', encoding='utf-8') as f:
    nbformat.write(nb, f)
    print(f"Cleaned notebook saved to {notebook_path}") 