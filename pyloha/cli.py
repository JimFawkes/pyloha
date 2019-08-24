import argparse
from loader import ReqresLoader


help_text = """
Project PyLoHa

"""

epilog = """

Written as first draft by Moritz Eilfort.

"""

parser = argparse.ArgumentParser(
    prog="pyloha",
    formatter_class=argparse.RawDescriptionHelpFormatter,
    description=help_text,
    epilog=epilog,
)

parser.add_argument(
    "--base_url", "-b", help="Base URL", type=str, required=True
)

parser.add_argument(
    "--count",
    "-c",
    help="Number of elements to load per request",
    type=int,
    default=1,
)


def load_data(base_url, count=None):
    loader = ReqresLoader(base_url=base_url, per_page=count)
    for data in loader:
        print(data)


def main():
    args = parser.parse_args()
    load_data(args.base_url, args.count)


if __name__ == "__main__":
    main()
