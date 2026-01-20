#Current implementation to create filesystem storage
from pathlib import Path
from filesystem.file_des import FileType, Inode


def main():

    #Create a structure that represents a file system
    root_dir = Path('/home/bsgursta')
    for subdir in root_dir.iterdir():
        if subdir.is_dir():
            print(subdir)

    myInode = Inode(10,10, FileType.DIRECTORY)
    myInode1 = Inode(10,10, FileType.REG_FILE)
    myInode.print_inode()
    myInode1.print_inode()

if __name__ == '__main__':
    main()