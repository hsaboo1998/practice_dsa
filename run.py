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
if out==None and not captured:
    print("Result:", inp) # capture inplace changes for mutable objects
elif out is not None:
    print("Result: ", out) # capture output
else:
    print("Result:", captured) # capture stdout/print produced inside func