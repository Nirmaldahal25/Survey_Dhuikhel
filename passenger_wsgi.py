import os
import sys


sys.path.insert(0, os.path.dirname(__file__))
from survey.wsgi import application
