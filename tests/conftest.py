# -*- coding: utf-8 -*-

# standard imports
import os
import sys

# lib imports
import pytest

# add Contents directory to the system path
pytest.root_dir = root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
pytest.contents_dir = contents_dir = os.path.join(root_dir, 'Contents')
if os.path.isdir(contents_dir):
    sys.path.append(contents_dir)
else:
    raise Exception('Contents directory not found')
