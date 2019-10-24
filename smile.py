import sys


from analyzer import Analyzer
from termcolor import colored


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: ./smile word")

    analyzer = Analyzer()

    score = analyzer.analyze(sys.argv[1])
    if score > 0.0:
        print(colored(":-)", "green"))
    elif score < 0.0:
        print(colored(":-(", "red"))
    else:
        print(colored(":-|", "yellow"))


if __name__ == "__main__":
    main()
