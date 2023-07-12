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
            if self.only_files or (self.only_files is False and self.only_dirs is False):
                yield from (self.check_pattern(file) for file in files)

            if self.only_dirs or (self.only_files is False and self.only_dirs is False):
                yield from (self.check_pattern(directory) for directory in dirs)

    def check_pattern(self, object):
        if self.pattern is None or self.pattern in object:
            return os.path.join(self.root, object)
        else:
            return None