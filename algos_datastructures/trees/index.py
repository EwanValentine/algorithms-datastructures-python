from ..trees.tree import Node


def main():
    parent = Node(1)
    parent.left = Node(2)
    parent.right = Node(3)
    print(parent)


if __name__ == "__main__":
    main()
