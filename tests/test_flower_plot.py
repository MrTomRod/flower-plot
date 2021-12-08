import os
from itertools import cycle
from unittest import TestCase
import matplotlib.pyplot as plt
from flower_plot import flower_plot

SAVE = False
OUTDIR = os.path.join(os.path.dirname(__file__), 'output')

CORE = 788
DATA = {
    'NIZO2256': {'color': (0.5, 0.0, 1.0), 'shell': 48, 'unique': 0},
    'NIZO2257': {'color': (0.45294117647058824, 0.07385252747487396, 0.9993170601430229), 'shell': 53, 'unique': 4},
    'NIZO2259': {'color': (0.39803921568627454, 0.1594757912099808, 0.9967953249171991), 'shell': 95, 'unique': 0},
    'NIZO2260': {'color': (0.3431372549019608, 0.24391372010837714, 0.9924205096719357), 'shell': 87, 'unique': 2},
    'NIZO2262a': {'color': (0.28823529411764703, 0.3265387128400833, 0.9862007473534026), 'shell': 98, 'unique': 0},
    'NIZO2264': {'color': (0.23333333333333334, 0.40673664307580015, 0.9781476007338057), 'shell': 90, 'unique': 1},
    'NIZO2457': {'color': (0.17843137254901964, 0.4839114241003015, 0.9682760409157589), 'shell': 88, 'unique': 0},
    'NIZO2484': {'color': (0.12352941176470589, 0.5574894393428855, 0.9566044195004408), 'shell': 102, 'unique': 0},
    'NIZO2494': {'color': (0.06862745098039214, 0.6269238058941065, 0.9431544344712774), 'shell': 88, 'unique': 0},
    'NIZO2535': {'color': (0.013725490196078438, 0.6916984393193699, 0.9279510898565747), 'shell': 92, 'unique': 0},
    'NIZO2741': {'color': (0.04117647058823526, 0.7513318895568732, 0.9110226492460883), 'shell': 83, 'unique': 0},
    'NIZO2776': {'color': (0.09607843137254901, 0.8053809193888326, 0.8924005832479478), 'shell': 45, 'unique': 0},
    'NIZO2801': {'color': (0.15098039215686276, 0.8534437988883159, 0.8721195109836108), 'shell': 69, 'unique': 1},
    'NIZO2806': {'color': (0.19803921568627447, 0.8896040127307095, 0.853443798888316), 'shell': 68, 'unique': 0},
    'NIZO2814': {'color': (0.2529411764705882, 0.9256376597815562, 0.8301840308155507), 'shell': 86, 'unique': 0},
    'NIZO2830': {'color': (0.307843137254902, 0.9547913248866443, 0.8053809193888326), 'shell': 92, 'unique': 0},
    'NIZO1836': {'color': (0.36274509803921573, 0.9768483177596007, 0.7790805745256704), 'shell': 106, 'unique': 7},
    'NIZO1838': {'color': (0.41764705882352937, 0.9916446955107427, 0.7513318895568734), 'shell': 55, 'unique': 0},
    'NIZO1839': {'color': (0.4725490196078431, 0.9990704811844932, 0.7221864503320093), 'shell': 55, 'unique': 1},
    'NIZO1840': {'color': (0.5274509803921568, 0.9990704811844932, 0.6916984393193701), 'shell': 61, 'unique': 0},
    'NIZO2766': {'color': (0.5823529411764705, 0.9916446955107427, 0.6599245348787227), 'shell': 82, 'unique': 0},
    'CIP104448': {'color': (0.6372549019607843, 0.9768483177596008, 0.6269238058941066), 'shell': 72, 'unique': 0},
    'NIZO1837a': {'color': (0.692156862745098, 0.9547913248866443, 0.5927576019625549), 'shell': 87, 'unique': 0},
    'NIZO2258': {'color': (0.7470588235294118, 0.9256376597815563, 0.5574894393428855), 'shell': 53, 'unique': 0},
    'NIZO2485': {'color': (0.8019607843137255, 0.8896040127307095, 0.5211848828765852), 'shell': 102, 'unique': 2},
    'NIZO2855': {'color': (0.8490196078431373, 0.8534437988883159, 0.4892929169339235), 'shell': 85, 'unique': 0},
    'NIZO2802': {'color': (0.9039215686274509, 0.8053809193888327, 0.45124405704532283), 'shell': 77, 'unique': 1},
    'NIZO2877': {'color': (0.9588235294117646, 0.7513318895568735, 0.41235631747390367), 'shell': 85, 'unique': 0},
    'NIZO2889': {'color': (1.0, 0.6916984393193701, 0.3727019919909141), 'shell': 84, 'unique': 0},
    'NIZO2891': {'color': (1.0, 0.6269238058941065, 0.3323547994796596), 'shell': 92, 'unique': 0},
    'NIZO2896': {'color': (1.0, 0.5574894393428858, 0.29138974688932473), 'shell': 85, 'unique': 0},
    'NIZO3400': {'color': (1.0, 0.4839114241003016, 0.24988298979423082), 'shell': 59, 'unique': 0},
    'NIZO2753': {'color': (1.0, 0.40673664307580004, 0.20791169081775923), 'shell': 52, 'unique': 0},
    'NIZO2757': {'color': (1.0, 0.3265387128400838, 0.1655538761841302), 'shell': 81, 'unique': 0},
    'NIZO2726a': {'color': (1.0, 0.24391372010837745, 0.12288829066471427), 'shell': 85, 'unique': 0},
    'NIZO2831': {'color': (1.0, 0.1594757912099809, 0.07999425118854168), 'shell': 92, 'unique': 0},
    'NIZO2263': {'color': (1.0, 0.07385252747487431, 0.03695149938914507), 'shell': 91, 'unique': 0},
    'NIZO2029': {'color': (1.0, 1.2246467991473532e-16, 6.123233995736766e-17), 'shell': 89, 'unique': 10}
}


def generate_data(n: int) -> dict[str:dict]:
    data_generator = cycle(DATA.values())
    return {f'FakeGenome{i}': next(data_generator) for i in range(n)}


def show_or_save(title: str):
    plt.tight_layout()
    if SAVE:
        plt.savefig(f'{OUTDIR}/{title}.svg')
    else:
        plt.show()


class Test(TestCase):
    def setUp(self) -> None:
        plt.close()

    def tearDown(self) -> None:
        plt.close()

    def test_flower_plot_no_data(self):
        with self.assertRaises(AssertionError):
            flower_plot(genome_to_data={}, n_core=CORE)

    def test_flower_plot_bad_data(self):
        with self.assertRaises(KeyError):
            flower_plot(genome_to_data={'genome1': [1]}, n_core=CORE)
        with self.assertRaises(KeyError):
            flower_plot(genome_to_data={'genome1': {'color': (0, 1, 1)}}, n_core=CORE)

    def test_flower_plot_rotate(self):
        flower_plot(genome_to_data=DATA, n_core=CORE)
        show_or_save('rotate')

    def test_flower_plot_no_rotate(self):
        flower_plot(
            genome_to_data=DATA, n_core=CORE,
            rotate_genome=False, rotate_shell=False, rotate_unique=False
        )
        show_or_save('no_rotate')

    def test_flower_plot_different_genomes(self):
        for n in [1, 2, 3, 4, 10, 15, 20, 50, 100, 200]:
            flower_plot(genome_to_data=generate_data(n), n_core=CORE)
            plt.suptitle(f'Generated {n} datapoints')
            show_or_save(f'generate_{n}')
