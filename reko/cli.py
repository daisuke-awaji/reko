from argparse import ArgumentParser

parser = ArgumentParser(
    prog="reko",
    description="This is my console application.")

parser.add_argument(
    "message",
    action="store",
    help="The message string.")