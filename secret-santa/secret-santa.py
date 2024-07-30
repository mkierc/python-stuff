import random
from datetime import datetime

forced = {
    'Zuzia': 'Kasia'
}

givers = [
    'Marcin',
    'Zuzia',
    'Ola',
    'Tomek',
    'Michał',
    'Kasia',
    'Wojtek',
    'Ania',
    'Stasiu',
]

excludes = {
    'Kasia': 'Wojtek',
    'Wojtek': 'Kasia',
    'Ania': 'Stasiu',
    'Stasiu': 'Ania',
    'Ola': 'Tomek',
    'Tomek': 'Ola',
    'Zuzia': 'Marcin',
    'Marcin': 'Zuzia',
}


def generate_secret_santa():
    result = []
    restart = True

    while restart:
        restart = False
        receivers = givers[:]

        # For when we know some people already have presents ;)
        for k, v in forced.items():
            receivers.remove(v)
            givers.remove(k)
            result.append([k, v])

        for i in range(len(givers)):
            giver = givers[i]
            # Pick a random receiver
            receiver = random.choice(receivers)

            # If we've got to the last giver, and it's the same as the receiver, restart the generation
            if giver == receiver and i == (len(givers) - 1):
                restart = True
                break
            else:
                # Ensure the giver and receiver are not the same, and they are not in the excludes list
                while (receiver == giver) or (receiver in excludes and giver == excludes[receiver]):
                    receiver = random.choice(receivers)
                result.append([giver, receiver])
                receivers.remove(receiver)

    current_time = datetime.now().strftime("%Y.%m.%d %H:%M:%S")
    print("Wygenerowano w dniu", current_time)
    print("=======================================")
    for g, r in result:
        print(g + ' kupuje prezent dla ' + r)


def main():
    generate_secret_santa()


if __name__ == '__main__':
    main()
