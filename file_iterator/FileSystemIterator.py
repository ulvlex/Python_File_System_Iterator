import os

class FileSystemIterator:
    def __init__(self, root, only_files, only_dirs, pattern):
        self.root = root
        self.only_files = only_files
        self.only_dirs = only_dirs
        self.pattern = pattern

        if not os.path.exists(self.root):
            raise FileNotFoundError("The root path does not exist.")

        if self.only_files and self.only_dirs:
            raise ValueError("Both 'only_files' and 'only_dirs' cannot be True")

        self.generator = self.generate()

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.generator)

    def generate(self):
        for path, dirs, files in os.walk(self.root):
            if self.only_files is False:
                yield from (os.path.join(path, directory).replace(os.sep, '/') for directory in dirs if self.check_pattern(directory))

            if self.only_dirs is False:
                yield from (os.path.join(path, file).replace(os.sep, '/') for file in files if self.check_pattern(file))

    def check_pattern(self, object):
        if self.pattern is None or self.pattern in object:
            return True
        else:
            return False