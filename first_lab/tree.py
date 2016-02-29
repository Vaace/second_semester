import argparse
from os import path, listdir

parser = argparse.ArgumentParser(
    description='Аналог утилиты tree, которая отображает древовидную структуру каталогов и файлов.'
)

parser.add_argument(
    'paths',
    metavar='FOLDERS',
    type=str,
    nargs='+',
    help='входные данные - пути к папкам'
)

parser.add_argument(
    '-f',
    '--folders-only',
    action="store_true",
    help='показывать только папки'
)

parser.add_argument(
    '-i',
    '--include',
    action="store",
    help='отображать только те элементы, в названии которых встречается текст'
)

parser.add_argument(
    '-e',
    '--exclude',
    action="store",
    help='не отображать те элементы, в названии которых встречается текст'
)

args = parser.parse_args()

names = args.paths
if args.include:
    names = [name for name in args.paths if args.include in name]
if args.exclude:
    names = [name for name in names if not (args.exclude in name)]

for name in names:
    if not path.isdir(name):
        print("Указанный путь не существует или не является папкой - " + name)
        exit()

for name in names:
    def tree(pth):
        res = []
        files = listdir(pth)
        if args.include:
            files = [file for file in files if args.include in file]
        if args.exclude:
            files = [file for file in files if not (args.exclude in file)]
        for file in files:
            if path.isdir(pth + "\\" + file):
                res.append(file + '\n'+ '\n'.join(['   ' + i for i in tree(pth + '/' + file).split('\n')]))
            elif not args.folders_only:
                res.append(file)
        return '\n'.join(res)
    print(tree(name))
