from argparse import ArgumentParser
from Parser import Parser
from Solver import Solver

    
if __name__ == "__main__":    
    parser = ArgumentParser()
    parser.add_argument("polynom", action="store", type=str, help="polynomial equations")
    parser.add_argument("-v", "--verbose", action="store_true", default=False, help="show the intermediate steps")
    parser.add_argument("-s", "--simple", action="store_true", default=False, help="reduce to simple form")    
    args = parser.parse_args()
    try:
        parser = Parser(args.polynom, args.simple)
        solver = Solver(parser, args.verbose)
    except (Exception, BaseException) as e:
        print(e)
        exit(1)