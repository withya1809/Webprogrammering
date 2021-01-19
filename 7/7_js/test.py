
def __load_albums(albums_file):
    # open file, read, split for hver tab (artist, album, bilde)
    file = open(albums_file,"r")

    for line in file.readlines():
        print(line)


if __name__ == '__main__':
    __load_albums("albums.txt")
