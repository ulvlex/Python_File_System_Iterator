from file_iterator.FileSystemIterator import FileSystemIterator

if __name__ == '__main__':
    for item in FileSystemIterator("C:/Users/ASUS/Desktop/Занятия", False, False, None):
        print(item)

    print("################################")

    print(next(FileSystemIterator("C:/Users/ASUS/Desktop/Занятия", False, False, None)))