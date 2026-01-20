#Current implementation to create filesystem storage
from pathlib import Path

def main():

    #Create a structure that represents a file system
    root_dir = Path('/home/bryan')
    for subdir in root_dir.iterdir():
        if subdir.is_dir():
            print(subdir)



if __name__ == '__main__':
    main()