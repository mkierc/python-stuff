import json
from collections import defaultdict
from itertools import cycle
from os import listdir
from os.path import isfile, join

import matplotlib.pyplot as plt

benford = {'1': 0.301, '2': 0.176, '3': 0.125, '4': 0.097, '5': 0.079, '6': 0.067, '7': 0.058, '8': 0.051, '9': 0.046, }


def calculate_distribution(dataset: list):
    count_map = defaultdict(int)
    total = len(dataset)
    for number in dataset:
        first_digit = str(number)[0]
        count_map[first_digit] += 1

    output_map = dict()
    for digit in range(1, 10):
        count = count_map[str(digit)]
        output_map[digit] = count / total

    return output_map


def pretty_print_output(dataset, name):
    print(f'\n{name}')
    for x, y in dataset.items():
        print(f'{x}: {str(round(y * 100, 1)).rjust(5)}%')


def draw_graph(distribution, name, filename):
    width = 1500
    height = 600
    ppi = 72
    figure, subplot_1 = plt.subplots(1, 1, figsize=(width / ppi, height / ppi), dpi=ppi)

    colors = cycle([
        (0.40, 0.40, 0.40),  # grey
        (0.12, 0.75, 0.27),  # green 1
        (0.00, 0.27, 0.87),  # blue
        (0.92, 0.30, 0.27),  # red 1
    ])

    # set widths for multiple bars on one value
    bar_width = 1 / 3
    bar_offset = bar_width * 0.5
    bar_1_range = [x - bar_offset for x in range(1, 10)]
    bar_2_range = [x + bar_offset for x in range(1, 10)]

    plt.bar(
        bar_1_range,
        benford.values(),
        bar_width,
        label="Benford's theoretical distribution",
        color=next(colors)
    )
    plt.bar(
        bar_2_range,
        distribution.values(),
        bar_width,
        label=name,
        color=next(colors)
    )

    # show all numbers on x-axis
    subplot_1.set_xticks(range(1, 10))
    subplot_1.set_ylim(0, 0.5)

    handles, labels = subplot_1.get_legend_handles_labels()
    labels, handles = zip(*sorted(zip(labels, handles), key=lambda t: t[0]))

    subplot_1.legend(handles=handles, labels=labels, bbox_to_anchor=(0.99, 0.98))

    filename = f'plots/{filename}.png'
    plt.savefig(filename, dpi=ppi, bbox_inches="tight")


def main():
    filenames = [f for f in listdir('datasets') if isfile(join('datasets', f))]

    datasets = dict()
    for filename in filenames:
        with open(join('datasets', filename)) as file:
            datasets[filename] = json.load(file)

    for filename, dataset in datasets.items():
        for name, data in dataset.items():
            distribution = calculate_distribution(data)
            pretty_print_output(distribution, name)
            draw_graph(distribution, name, filename.split('.')[0])


if __name__ == '__main__':
    main()
