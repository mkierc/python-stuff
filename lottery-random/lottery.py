import os
import sys

from rdoclient_py3 import RandomOrgClient


def main():
    api_key = open(os.path.join(sys.path[0], 'api.key')).readline()
    rand = RandomOrgClient(api_key)
    print(f'{rand.get_requests_left()} requests from random.org are left available today.')

    if len(sys.argv) > 1 and sys.argv[1].lower() == 'lotto':
        first_six = sorted(rand.generate_integers(n=6, min=1, max=49, replacement=False))
        second_six = sorted(rand.generate_integers(n=6, min=1, max=49, replacement=False))

        print(f'{first_six}\n{second_six}')

    else:
        first_five = sorted(rand.generate_integers(n=5, min=1, max=50, replacement=False))
        first_two = sorted(rand.generate_integers(n=2, min=1, max=10, replacement=False))
        second_five = sorted(rand.generate_integers(n=5, min=1, max=50, replacement=False))
        second_two = sorted(rand.generate_integers(n=2, min=1, max=10, replacement=False))

        print(f'{first_five} {first_two}\n{second_five} {second_two}')


if __name__ == "__main__":
    main()
