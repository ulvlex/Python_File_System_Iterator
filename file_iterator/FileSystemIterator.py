import os

class FileSystemIterator:
    def __init__(self, root, only_files, only_dirs, pattern):
        self.root = root
        self.only_files = only_files
        self.only_dirs = only_dirs
        self.pattern = pattern
        self.generator = self.generate()

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.generator)

    def generate(self):
        for path, dirs, files in os.walk(self.root):
            if self.only_files and not self.only_dirs:
                for file in files:
                    cur_path = self.check_pattern(file)
                    yield cur_path
            elif self.only_dirs and not self.only_files:
                for directory in dirs:
                    cur_path = self.check_pattern(directory)
                    yield cur_path
            else:
                for file in files:
                    cur_path = self.check_pattern(file)
                    yield cur_path
                for directory in dirs:
                    cur_path = self.check_pattern(directory)
                    yield cur_path

    def check_pattern(self, object):
        if self.pattern is None or self.pattern in object:
            return os.path.join(self.root, object)
        else:
            print(f"There is no such {object}")