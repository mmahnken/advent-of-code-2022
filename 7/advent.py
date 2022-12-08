

class Node:
    def __init__(self, name, size=None, parent=None):
        self.name = name
        self.size = size
        self.children = []
        self.parent = parent
        self.children_map = {}


    def add_child(self, child_node):
        self.children.append(child_node)
        self.children_map[child_node.name] = child_node

    def is_dir(self):
        return not self.size

    def is_file(self):
        return self.size != None


    def total_size(self):
        to_visit = [c for c in self.children]
        total_size = 0
        while to_visit:
            current = to_visit.pop()
            if current.is_file():
                total_size += current.size
            if current.children: 
                to_visit.extend(current.children)

        return total_size

    def __repr__(self):
        if self.is_dir():
            return f"<DirNode {self.name}>"
        else:
            return f"<Node {self.name}>"

    def __gt__(self, other):
        if self.is_dir():
            return self.total_size() > other
        else:
            return self.size > other


    def __lt__(self, other):
        if self.is_dir():
            return self.total_size() < other
        else:
            return self.size < other

def process(filename):
    f = open(filename)

    root = Node('/', parent=None)
    current_directory = root
    directories = [root]

    next(f)

    for line in f:
        line = line.strip()

        if line[0] != '$':
            tokens = line.split()
            if tokens[0] == 'dir':
                node = Node(tokens[1], parent=current_directory)
                directories.append(node)
            else:
                node = Node(tokens[1], size=int(tokens[0]), parent=current_directory)
            
            current_directory.add_child(node)


        # command
        if line[0] == '$':
            tokens = line.split()
            if tokens[1] == 'cd':
                # update current directory
                if tokens[2] == '..':
                    current_directory = current_directory.parent
                else:
                    current_directory = current_directory.children_map.get(tokens[2])
                        
            elif tokens[1] == 'ls':
                continue

    return directories, root


def find_small_directories(d):
    total = 0
    for direc in d:
        d_size = direc.total_size()
        if d_size < 100000:
            total += d_size
    print(total)


def get_space_needed(root):

    FILE_SYSTEM = 70000000
    UPDATE = 30000000
    USED = root.total_size()
    CURRENT_AVAILABLE = FILE_SYSTEM - USED

    return UPDATE - CURRENT_AVAILABLE


def find_directory_to_delete(d, space_needed):
    d = sorted(d, reverse=True)
    previous = d[0]

    for directory in d[1:]:
        if directory.total_size() < space_needed and previous > space_needed:
            return previous.total_size()

        previous = directory


if __name__ == "__main__":
    d, root = process("input.txt")
    
    # Part 1
    find_small_directories(d)


    # Part 2
    space = get_space_needed(root)
    print("SPACE NEEDED", space)
    print(find_directory_to_delete(d, space))











