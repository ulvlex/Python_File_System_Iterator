from file_iterator.FileSystemIterator import FileSystemIterator

if __name__ == '__main__':
    for item in FileSystemIterator("C:/root1", False, False, None):
        print(item)

    print("################################")

    print(next(FileSystemIterator("C:/root1", False, False, None)))