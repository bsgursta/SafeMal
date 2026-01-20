#SuperBlock -> Inodes -> B-tree (hashed)

class Superblock:
# https://blogs.oracle.com/linux/understanding-ext4-disk-layout-part-1
    def __init__(self, inode_count,block_count, block_size):
        self.inode_count = inode_count
        self.block_count = block_count
        self.free_inodes = inode_count
        self.free_blocks = block_count
        self.block_size = block_size

    def print_block(self):
        print(f"Inode Count: {self.inode_count}\nBlock Count : {self.block_count}\n")