import os
from argparse import ArgumentParser
from shutil import move


class FileParser:

    def __init__(self, path=None, searched=None, replacer=None):
        self.path = path
        self.searched = searched
        self.replacer = replacer
        self.temp = "temp.txt"

    def _validate_path(self):
        if os.path.isfile(self.path) and os.path.exists(self.path):
            return True
        else:
            raise ValueError("Path doesn't lead to file or not exists")

    def file_reader(self, function):
        self._validate_path()
        with open(self.path, 'r+') as file:
            return function(file)

    def _temp_file_init(self):
        with open(self.temp, 'w+'):
            pass

    def _file_writer(self, file):
        self._temp_file_init()
        with open(self.temp, 'a+') as writer:
            for line in file:
                writer.write(line.replace(self.searched, self.replacer))

    def count_substring_in_file(self, file):
        substring_inputs = 0
        for line in file:
            substring_inputs += line.count(self.searched)
        return substring_inputs

    def replace_words_in_file(self):
        self.file_reader(self._file_writer)
        move(self.temp, self.path)


def make_cli():
    cli = ArgumentParser()
    cli.add_argument('-m', type=int, choices=[1, 2], default=1)
    cli.add_argument('-p', type=str, required=True)
    cli.add_argument('-c', type=str, default=' ')
    cli.add_argument('--r', type=str, default=None)
    return cli


def main():
    cli = make_cli()
    args = cli.parse_args()
    mode = args.m
    if mode == 2 and not args.r:
        raise ValueError('Mode 2 needs --r flag to work')
    parser = FileParser(path=args.p, replacer=args.r, searched=args.c)
    if mode == 1:
        print(parser.file_reader(parser.count_substring_in_file))
    else:
        parser.replace_words_in_file()


if __name__ == '__main__':
    main()
