import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--cmd', required = True, help='order')
opt = parser.parse_args()

os.system(opt.cmd)