from argparse import ArgumentParser
from cowsay import cowsay, list_cows

presets = "bdgpstwy"

parser = ArgumentParser(description='Cowsay')
parser.add_argument('message', nargs="?")
parser.add_argument('-e', '--eyes', default='oo')
parser.add_argument('-f', '--cowfile', default=None)
parser.add_argument('-l', '--list', action='store_true')
parser.add_argument('-n', '--no-wrap')
parser.add_argument('-T', '--tongue', default='__')
parser.add_argument('-W', '--width', type=int, default=40)
parser.add_argument('-b', '--borg', dest='b')
parser.add_argument('-d', '--dead', dest='d')
parser.add_argument('-g', '--greedy', dest='g')
parser.add_argument('-p', '--paranoid', dest='p')
parser.add_argument('-s', '--stoned', dest='s')
parser.add_argument('-t', '--tired', dest='t')
parser.add_argument('-w', '--wired', dest='w')
parser.add_argument('-y', '--youthful', dest='y')

args = parser.parse_args()
print(args.__dict__)
if args.list:
    print(list_cows())
else:
    eyes = args.eyes if (args.eyes and len(args.eyes) == 2) else 'oo'
    tongue = args.tongue if (args.tongue and len(args.tongue) == 2) else '__'
    preset = ''.join([i for i in args.__dict__ if i in presets])
    print(cowsay(message=args.message, eyes=args.eyes, tongue=args.tongue, width=args.width, wrap_text=args.width,
                 cowfile=args.cowfile, preset=preset))
