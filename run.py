# Command line tool
import argparse
import importlib
from ast import literal_eval
from io import StringIO
from contextlib import redirect_stdout

parser = argparse.ArgumentParser()
parser.add_argument("-m")
parser.add_argument("-f")
parser.add_argument("-i")
args = parser.parse_args()

module = importlib.import_module(args.m)
func = getattr(module, args.f)
inp = literal_eval(args.i)
f = StringIO()
with redirect_stdout(f):
    out = func(*inp)
captured = f.getvalue()
if captured !='':
    print("captured: ", captured) # capture stdout/print produced inside func
if out is not None:
    print("Result: ", out) # capture output
if out is None and captured is None:
    print("Result: ", inp)