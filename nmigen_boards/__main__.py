import argparse 
from jinja2 import Template 
import time

# boards
boards = {
    "ice40_hx8k_b_evn": "ICE40HX8KBEVNPlatform",
    "mercury": "MercuryPlatform",
    "ice40_hx1k_blink_evn": "ICE40HX1KBlinkEVNPlatform",
    "versa_ecp5": "VersaECP5Platform",
    "blackice": "BlackIcePlatform",
    "versa_ecp5_5g": "VersaECP55GPlatform",
    "atlys": "AtlysPlatform",
    "blackice_ii": "BlackIceIIPlatform",
    "arty_a7": "ArtyA7Platform",
    "kc705": "KC705Platform",
    "tinyfpga_bx": "TinyFPGABXPlatform",
    "icestick": "ICEStickPlatform",
    "icebreaker": "ICEBreakerPlatform",
}
# endboards

template = """
# Auto generated board file
# https://github.com/m-labs/nimgien-boards/
# {{time}}
from nmigen import *
from nmigen_boards.{{board}} import {{cls}}

class {{name}}({{cls}}):
    pass

if __name__ == "__main__":
    plat = {{name}}()
    
"""


def list():
    print("\nAvailable Boards:\n")
    for i in boards.keys():
        print(" ",i)
    print()

def build(board,cls,name):
    t = Template(template)
    r = t.render({'board':board,'cls':cls,'name':name})
    print(r)

if __name__ == "__main__":
    p = argparse.ArgumentParser()

    p.add_argument("-b",help="board name")
    p.add_argument("-o",action="store",help="output file",default="board.py")
    p.add_argument("-n",help="class name for board",default="MyBoard")
    p.add_argument("-f",help="force overwrite")

    args = p.parse_args()
    if args.b == None:
        p.print_help()
        list()
    else:
        if args.b in boards:
            build(args.b,boards[args.b],args.n)
        else:
            print('Board Not Found: ',args.b)
            list()
