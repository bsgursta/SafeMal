from enum import Enum

class FileType(Enum):
    DIRECTORY = 1
    REG_FILE = 2
    SYMBOLIC_LINK = 3


class Inode:
    #static member variable, Class Attribute
    curr_id = 0

    def __init__(self, user_id,group_id, file_type: FileType):
        self.inode_id =Inode. curr_id
        self.user_id = user_id
        self.group_id = group_id
        self.file_type = file_type

        #Implement the rest of the attributes here

        Inode.curr_id += 1


    #self just uses its own parameters
    def print_inode(self):
        print(f"Inode ID: {self.inode_id}\nUser ID: {self.user_id}\nGroup ID: {self.group_id}\n"
              f"File Type: {self.file_type}\n")

