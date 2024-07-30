import os
import sys

from rdoclient import RandomOrgClient


def main():
    api_key = open(os.path.join(sys.path[0], 'api.key')).readline()
    rand = RandomOrgClient(api_key)
    print(f'{rand.get_requests_left()} requests from random.org are left available today.')

    first_five = []
    first_two = []
    second_five = []
    second_two = []
    third_five = []
    third_two = []
    fourth_five = []
    fourth_two = []

    first_six = []
    second_six = []
    third_six = []
    fourth_six = []
    fifth_six = []

    ###########################################################
    #                       _            _                _
    #   ___ _   _ _ __ ___ (_) __ _  ___| | ___ __   ___ | |_
    #  / _ \ | | | '__/ _ \| |/ _` |/ __| |/ / '_ \ / _ \| __|
    # |  __/ |_| | | | (_) | | (_| | (__|   <| |_) | (_) | |_
    #  \___|\__,_|_|  \___// |\__,_|\___|_|\_\ .__/ \___/ \__|
    #                    |__/                |_|

    first_five = sorted(rand.generate_integers(n=5, min=1, max=50, replacement=False))
    first_two = sorted(rand.generate_integers(n=2, min=1, max=12, replacement=False))
    second_five = sorted(rand.generate_integers(n=5, min=1, max=50, replacement=False))
    second_two = sorted(rand.generate_integers(n=2, min=1, max=12, replacement=False))

    third_five = sorted(rand.generate_integers(n=5, min=1, max=50, replacement=False))
    third_two = sorted(rand.generate_integers(n=2, min=1, max=12, replacement=False))

    print(f'{first_five} {first_two}')
    print(f'{second_five} {second_two}')
    # print(f'{third_five} {third_two}\n')

    #########################
    #  _       _   _
    # | | ___ | |_| |_ ___
    # | |/ _ \| __| __/ _ \
    # | | (_) | |_| || (_) |
    # |_|\___/ \__|\__\___/
    #

    first_six = sorted(rand.generate_integers(n=6, min=1, max=49, replacement=False))
    second_six = sorted(rand.generate_integers(n=6, min=1, max=49, replacement=False))
    third_six = sorted(rand.generate_integers(n=6, min=1, max=49, replacement=False))
    fourth_six = sorted(rand.generate_integers(n=6, min=1, max=49, replacement=False))

    # fifth_six = sorted(rand.generate_integers(n=6, min=1, max=49, replacement=False))

    print(f'{first_six}\n{second_six}\n{third_six}\n{fourth_six}')

    # print(f'{fifth_six}')

    used = set()
    used.update(first_five)
    used.update(first_two)
    used.update(second_five)
    used.update(second_two)
    used.update(third_five)
    used.update(third_two)

    used.update(first_six)
    used.update(second_six)
    used.update(third_six)
    used.update(fourth_six)
    used.update(fifth_six)

    all_50 = set(range(1, 51))

    unused = list(set.difference(all_50, used))
    unused = set.difference(all_50, used)

    print(f'\n{sorted(unused)}\n')

    #############################################################
    #                     _ _                                  _
    #  _ __ ___ _ __ ___ | | |  _   _ _ __  _   _ ___  ___  __| |
    # | '__/ _ \ '__/ _ \| | | | | | | '_ \| | | / __|/ _ \/ _` |
    # | | |  __/ | | (_) | | | | |_| | | | | |_| \__ \  __/ (_| |
    # |_|  \___|_|  \___/|_|_|  \__,_|_| |_|\__,_|___/\___|\__,_|

    low = list(filter(lambda x: x <= 12, unused))

    if len(low) >= 2:
        i = rand.generate_integers(n=2, min=0, max=len(low)-1, replacement=False)
        fourth_two = sorted([low[i[0]], low[i[1]]])
        unused = list(set.difference(set(unused), set(fourth_two)))
    else:
        fourth_two = sorted(rand.generate_integers(n=2, min=1, max=12, replacement=False))

    i = rand.generate_integers(n=5, min=0, max=len(unused) - 1, replacement=False)
    fourth_five = list(sorted([unused[i[0]], unused[i[1]], unused[i[2]], unused[i[3]], unused[i[4]]]))

    print(f'{fourth_five} {fourth_two}\n')


if __name__ == "__main__":
    main()
