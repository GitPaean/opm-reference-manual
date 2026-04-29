"""Local conftest for the fodt2md test suite.

We don't import gitpython here (unlike the parent ``conftest.py``) so the
fodt2md tests can run with a minimal dependency set:
``pip install lxml pyyaml click pytest``.
"""
