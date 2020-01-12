import pkg_resources
try:
    __version__ = pkg_resources.get_distribution(__name__).version
except pkg_resources.DistributionNotFound:
    pass

__all__ = [
    "arty_a7",
    "atlys",
    "blackice_ii",
    "blackice",
    "de0_cv",
    "de0",
    "de10_nano",
    "fomu_hacker",
    "ice40_hx1k_blink_evn",
    "ice40_hx8k_b_evn",
    "icebreaker",
    "icestick",
    "kc705",
    "kcu105",
    "mercury",
    "mister",
    "numato_mimas",
    "sk_xc6slx9",
    "tinyfpga_ax1",
    "tinyfpga_ax2",
    "tinyfpga_bx",
    "versa_ecp5_5g",
    "versa_ecp5",
    "zturn_lite_z007s",
    "zturn_lite_z010",
]

def list_boards():
    " get a dictionary of board names and classes"
    import importlib
    name_dict = {}
    for i in __all__:
        board = importlib.import_module('nmigen_boards.'+i)
        platforms = board.__all__
        for j in platforms:
            b = board.__dict__[j]
            name_dict[i] = b
        
    return name_dict


def all_resources():
    boards = list_boards()
    counts = {}
    for i in boards.values():
        # collate resources
        inst = i()
        res = inst.resources
        for j  in res:
            name = j[0]
            if name not in counts:
                val = set()
                counts[name] = val
                val.add(i)
            else:
                counts[name].add(i)
    return counts


class BoardFinder:
    " Collect all the boards into a super class"
    def __init__(self):
        # add all the boards
        self.boards = list_boards()
        self._res = all_resources()
        for i in self._res:
            setattr(self,i,self._res[i])

    def __call__(self):
        for i,j in enumerate(self.boards):
            print(i," : ",j)

    def resources(self):
        return list(self._res.keys())

    def connector(self):
        for i,j in self.boards.items():
            inst = j()
            print(i," : ",list(inst.connectors.keys()))

    def family(self):
        fma = {}
        for i,j in self.boards.items():
            inst = j()
            if hasattr(inst,'family'):
                print(inst.family,i)
            else:
                print('No Family ',i)
