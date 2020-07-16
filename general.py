import os


def create_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


def write_file(path, data):
    f = open(path, 'w', encoding="utf-8")
    f.write(data)
    f.close()
