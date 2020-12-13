from algos_datastructures.trees.tree import Node


def main():
    parent = Node(1)
    parent.left = Node(2)
    parent.right = Node(3)
    print(parent)
    print(parent.left)
    print(parent.right)


if __name__ == "__main__":
    main()
