import argparse
import importlib
from ast import literal_eval

parser = argparse.ArgumentParser()
parser.add_argument("-m")
parser.add_argument("-f")
parser.add_argument("-i")
args = parser.parse_args()

module = importlib.import_module(args.m)
func = getattr(module, args.f)
inp = literal_eval(args.i)
out = func(inp)
print("Result: ", out)