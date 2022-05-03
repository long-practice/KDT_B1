import os
import argparse

argparse.ArgumentParser()
parser.add_argument('--cmd', required = True, help='order')
opt = parser.parse_args()

os.system(opt.cmd)