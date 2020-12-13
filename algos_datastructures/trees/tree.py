class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

    def __str__(self):
        lv = None
        if self.left is not None:
            lv = self.left.val

        rv = None
        if self.right is not None:
            rv = self.right.val

        return "Node(left=%s, right=%s, val=%s)" \
            % (lv, rv, self.val)
