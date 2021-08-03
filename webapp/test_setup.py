"""Nasty hack because of pytest import behavior"""

import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))