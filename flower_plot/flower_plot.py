import matplotlib.pyplot as plt
import numpy as np
from matplotlib.axes._base import _AxesBase
from matplotlib.patches import Ellipse, Circle


def calc_point_on_circle(i: int, slice: float, radius: float, center: (float, float) = (0, 0)):
    """
    Return coordinates of the i-th point on a circle.

    :param i: i-th point
    :param slice: width of the slices [degrees]
    :param radius: radius of the circle
    :param center: (x, y) coordinates of the circle center
    :return:
    """
    angle = slice * i
    new_x = center[0] + radius * np.cos(angle)
    new_y = center[1] + radius * np.sin(angle)
    return new_x, new_y


calculate_angle = lambda i, n_slices: 360 / n_slices * i
autorotate_angle = lambda angle: angle - 180 if 90 < angle < 270 else angle
autoalign_text = lambda angle: 'right' if 90 < angle < 270 else 'left'


def validate_data(genome: str, data: dict) -> None:
    for key in ['color', 'shell', 'unique']:
        if key not in data:
            raise KeyError(f'Genome {genome} is missing attribute {key}!')


def flower_plot(
        genome_to_data: dict[str:dict],
        n_core: int,
        shell_color='lightgray',
        core_color='darkgrey',
        alpha: float = 0.3,
        rotate_shell: bool = True,
        rotate_unique: bool = True,
        rotate_genome: bool = True,
        default_fontsize: float = None,
        core_fontsize: float = 12,
        ax: _AxesBase = None
) -> _AxesBase:
    """
    Create a flower plot. Returns matplotlib axis object.

    :param genome_to_data: dictionary that maps genome names to associated data (color, number of unique and shell genes)
    :param n_core: number of core genes
    :param shell_color: color of the shell circle
    :param core_color: color of the core circle
    :param alpha: opacity of the ellipses
    :param rotate_shell: whether to rotate the number of shell genes text
    :param rotate_unique: whether to rotate the number of unique genes text
    :param rotate_genome: whether to rotate the genome name
    :param default_fontsize: font size for number of genes and genome name
    :param core_fontsize: font size for number of core genes
    :param ax: matplotlib axis
    :return: matplotlib axis
    """
    assert len(genome_to_data) > 0, f'No data was supplied. {len(genome_to_data)=}'

    if ax is None:
        fig, ax = plt.subplots(subplot_kw={'aspect': 'equal'}, figsize=(6, 6), dpi=300)

    n_genomes = len(genome_to_data)

    # scale plot according to the number of genomes
    factor = n_genomes / 16
    factor = max([1, factor])  # ensure factor is never less than 1

    # default text parameters
    if default_fontsize is None:
        default_fontsize = 3.5 / np.log10(factor + 1)  # empirical
    textparams = dict(va='center', fontsize=default_fontsize, bbox=dict(facecolor='white', alpha=1e-16))

    # calculate width of the slices [degrees]
    slice = 2 * np.pi / n_genomes

    # shell circle
    circle_shell = Circle(
        xy=(0, 0), radius=3 * factor, color=shell_color
    )
    ax.add_artist(circle_shell)

    for i, (genome, data) in enumerate(genome_to_data.items()):
        validate_data(genome, data)

        angle = calculate_angle(i, n_genomes)
        rotated_angle = autorotate_angle(angle)

        # unique genes: ellipses
        ax.add_artist(Ellipse(
            calc_point_on_circle(i, slice, 3 * factor),
            width=4, height=1.5, angle=angle, alpha=alpha, color=data['color']
        ))

        # unique genes: number
        text_unique = ax.text(
            *calc_point_on_circle(i, slice, 3 * factor + 1),
            s=data['unique'], ha='center',
            rotation=rotated_angle if rotate_unique else None,
            **textparams
        )
        text_unique.set_gid(f'flower-unique-{genome}')

        # shell genes: number
        text_shell = ax.text(
            *calc_point_on_circle(i, slice, 3 * factor - 1),
            s=data['shell'], ha='center',
            rotation=rotated_angle if rotate_shell else None,
            **textparams
        )
        text_shell.set_gid(f'flower-shell-{genome}')

        # genome name
        text_genome = ax.text(
            *calc_point_on_circle(i, slice, 3 * factor + 2.1),
            s=genome, ha=autoalign_text(angle),
            rotation=rotated_angle if rotate_genome else None, rotation_mode='anchor',
            **textparams
        )
        text_genome.set_gid(f'flower-genome-{genome}')

    # core circle
    circle_core = Circle(
        xy=(0, 0), radius=1 * factor, color=core_color
    )
    circle_core.set_gid('flower-core')
    ax.add_artist(circle_core)

    # core genes: number
    text_core = ax.text(
        0, 0, n_core,
        ha='center', va='center',
        fontsize=core_fontsize
    )
    text_core.set_gid('flower-core-text')

    # scale plot
    lim = 4 + 3 * factor
    ax.set_xlim(-lim, lim)
    ax.set_ylim(-lim, lim)
    ax.set_gid(f'flower-plot')

    # disable axis
    ax.set_axis_off()

    return ax
