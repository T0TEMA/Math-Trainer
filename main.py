import argparse
import modes


def main(mode):
    if mode == "m":
        print(modes.multiply())


if '__main__' == __name__:
    parser = argparse.ArgumentParser(usage="python3 main.py -u <Username>")
    parser.add_argument('-u', '--user', type=str, required=True, help="Is used to save user statistics.")
    parser.add_argument('-m', '--mode', type=str, required=False, help="")
    args = parser.parse_args()
    main(args.mode)
