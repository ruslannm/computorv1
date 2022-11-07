from argparse import ArgumentParser
from . import Parser
    
if __name__ == "__main__":    
    parser = ArgumentParser()
    parser.add_argument("polynom", action="store", type=str, help="polynomial equations")
    parser.add_argument("-v", "--verbose", action="store_true", default=False, help="show the intermediate steps")
    args = parser.parse_args()
    try:
        parser = Parser(args.polynom)
    except (Exception, BaseException) as e:
        print(e)
        exit(1)