import datetime
from collections import defaultdict
from itertools import cycle

import matplotlib.pyplot as plt

dataset_1 = [1409.63, 5414.63, 17.60, 15.50, 25.00, 38.00, 21.48, 10.20, 10.00, 200.00, 72.00, 15.30, 30.60, 43.82,
             85.27, 9.09, 200.00, 300.00, 14.20, 41.90, 10.50, 15.11, 49.99, 108.99, 35.30, 60.68, 24.00, 18.85, 85.99,
             40.03, 25.00, 12.30, 37.89, 4.50, 52.40, 10.00, 12.35, 65.77, 12.00, 25.72, 158.28, 23.00, 45.00, 19.80,
             18.98, 6.49, 10.65, 25.00, 20.90, 20.20, 11.22, 23.13, 164.87, 28.90, 23.09, 37.40, 64.90, 13.77, 27.54,
             25.13, 25.00, 11.59, 7.99, 4.85, 29.98, 47.40, 19.74, ]

dataset_2 = [1409.63, 5414.63, 50.00, 17.60, 15.50, 25.00, 38.00, 21.48, 10.20, 10.00, 200.00, 72.00, 15.30, 30.60,
             25.00, 43.82, 85.27, 9.09, 200.00, 300.00, 14.60, 85.40, 19.00, 60.00, 1.00, 14.20, 40.00, 41.90, 40.00,
             45.00, 10.50, 15.11, 40.00, 49.99, 108.99, 13.00, 35.30, 60.68, 24.00, 21.00, 96.00, 18.85, 85.99, 40.03,
             25.00, 12.30, 37.89, 4.50, 52.40, 10.00, 12.35, 65.77, 12.00, 25.72, 158.28, 23.00, 45.00, 19.80, 18.98,
             6.49, 10.65, 25.00, 20.90, 20.20, 11.22, 23.13, 164.87, 28.90, 23.09, 37.40, 64.90, 13.77, 27.54, 25.13,
             25.00, 11.59, 7.99, 4.85, 29.98, 47.40, 19.74, ]

dataset_3 = [3732.86, 38.47, 16.97, 33.98, 15.00, 10.39, 1000.00, 25.00, 62.00, 27.00, 47.50, 20.00, 30.00, 135.00,
             30.89, 108.99, 100.00, 24.00, 20.00, 41.00, 10.12, 70.00, 60.00, 100.00, 19.64, 12.19, 19.99, 200.00,
             72.00, 27.36, 332.64, 2.00, 7.82, 37.08, 25.00, 14.00, 11.45, 8.79, 8.49, 23.75, 99.25, 19.51, 18.00,
             49.99, 23.00, 93.00, 12.00, 48.00, 13.00, 23.40, 20.00, 2.00, 25.90, 25.00, 13.74, 26.80, 21.48, 8.25,
             41.16, 27.00, 860.79, 49.99, 35.00, 20.90, 15.00, 20.00, 30.00, 8.00, 10.00, 13.00, 16.50, 42.39, 2.00,
             25.00, 15.50, 62.00, 7.00, 8.24, 7.19, 10.65, 15.29, 42.80, 20.97, ]

benford = {'1': 0.301, '2': 0.176, '3': 0.125, '4': 0.097, '5': 0.079, '6': 0.067, '7': 0.058, '8': 0.051, '9': 0.046, }


def crunch_dataset(dataset: list):
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


def draw_graph(dataset_list):
    width = 1500
    height = 600
    ppi = 72
    figure, subplot_1 = plt.subplots(1, 1, figsize=(width / ppi, height / ppi), dpi=ppi)

    colors = cycle([
        (0.40, 0.40, 0.40),  # grey
        (0.92, 0.30, 0.27),  # red 1
        (0.12, 0.75, 0.27),  # green 1
        (0.00, 0.27, 0.87),  # blue
    ])

    # set widths for multiple bars on one value
    bar_width = 1 / (len(dataset_list) + 1)
    current_width = -0.5

    for name, dataset in dataset_list.items():
        # offset the middle of bars to be on the middle of value
        current_width += bar_width
        range_with_width = [x + current_width for x in range(1, 10)]

        plt.bar(range_with_width, dataset.values(), bar_width, label=name, color=next(colors))

    # show all numbers on x-axis
    subplot_1.set_xticks(range(1, 10))

    #
    handles, labels = subplot_1.get_legend_handles_labels()
    labels, handles = zip(*sorted(zip(labels, handles), key=lambda t: t[0]))

    subplot_1.legend(handles=handles, labels=labels, loc="center left", bbox_to_anchor=(0.9, 0.85))

    filename = "plots/" + datetime.datetime.now().strftime("%Y-%m-%d") + ".png"
    plt.savefig(filename, dpi=ppi, bbox_inches="tight")


def main():
    output_1 = crunch_dataset(dataset_1)
    output_2 = crunch_dataset(dataset_2)
    output_3 = crunch_dataset(dataset_3)

    pretty_print_output(output_1, 'dataset_1')
    pretty_print_output(output_2, 'dataset_2')
    pretty_print_output(output_3, 'dataset_3')
    pretty_print_output(benford, "theoretical Benford's distribution:")

    draw_graph({
        "Benford's\ntheoretical\ndistribution": benford,
        "Dataset 1": output_1,
        "Dataset 2": output_2,
        "Dataset 3": output_3,
    })


if __name__ == '__main__':
    main()
