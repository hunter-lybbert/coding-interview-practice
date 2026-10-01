"""
Problem #3:

Post Completion Reflections:
    - My first instinct was to use a silly python syntax short cut 'eval()' and to format the serialized string as the object creation function.
    - This is somehow both clever and super silly/dumb
    - My solution exposed us to possible injections in the eval() call
    - Overly complex cases, think about how your cases are repeating yourself
    - Great practice thinking through how a list/string can encode the values of nodes in a binary tree.
    - I need more practice thinking about "What is this testing?" not "how do I get just any random version of this function working?"
    - I have a decent logic working for getting through the Node left right value objects.

This is your coding interview problem for today.

This problem was asked by Google.

Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
We will be sending the solution tomorrow, along with tomorrow's question. As always, feel free to shoot us an email if there's anything we can help with.

Have a great day!
"""

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# =========================== Your Solution Below ========================== #

def serialize_v1(node: Node) -> str:
    """
    Take in a Node object (the root Node) and serialize the whole tree into a string.
    
    case 1: the current node has no children
        return f"Node({node.val!r})"
    case 2: the current node has only left child
        return f"Node({node.val!r}, {serialize(node.left)})"
    case 3: the current node has only right child
        return f"Node({node.val!r}, None, {serialize(node.right)})"
    case 3: the current node has both a left and a
        right child return f"Node({node.val!r}, {serialize(node.left)}, {serialize(node.right)})"
    """
    if not node.left and not node.right:
        return f"Node({node.val!r})"
    elif node.left and not node.right:
        return f"Node({node.val!r}, {serialize_v1(node.left)})"
    elif not node.left and node.right:
        return f"Node({node.val!r}, None, {serialize_v1(node.right)})"
    elif node.left and node.right:
        return f"Node({node.val!r}, {serialize_v1(node.left)}, {serialize_v1(node.right)})"
    else:
        raise ValueError("Something went wrong, our exhaustive cases didn't catch something")


def serialize_v2(node: Node) -> str:
    """
    Take in a Node object (the root Node) and serialize the whole tree into a string.
    
    case 1: the current node has no children
        return f"Node({node.val!r})"
    case 2: the current node has only left child
        return f"Node({node.val!r}, {serialize(node.left)})"
    case 3: the current node has only right child
        return f"Node({node.val!r}, None, {serialize(node.right)})"
    case 3: the current node has both a left and a
        right child return f"Node({node.val!r}, {serialize(node.left)}, {serialize(node.right)})"
    """
    if not node:
        return None
    return f"Node({node.val!r}, {serialize_v2(node.left)}, {serialize_v2(node.right)})"


def serialize(node: Node) -> str:
    """
    Take in a Node object (the root Node) and serialize the whole tree into a string.
    
    case 1: the current node has no children
        return f"Node({node.val!r})"
    case 2: the current node has only left child
        return f"Node({node.val!r}, {serialize(node.left)})"
    case 3: the current node has only right child
        return f"Node({node.val!r}, None, {serialize(node.right)})"
    case 3: the current node has both a left and a
        right child return f"Node({node.val!r}, {serialize(node.left)}, {serialize(node.right)})"
    """
    if not node:
        return '#'
    return f"{node.val} {serialize(node.left)} {serialize(node.right)}"


def deserialize(s: str) -> Node:
    """
    Take in a string of the Node and deserialize it back into the Node object.
    """
    values = iter(s.split())
    def helper():
        val = next(values)
        if val == '#':
            return None
        return Node(int(val), helper(), helper())
    return helper()
    # return eval(s)


# =========================== Your Solution Above ========================== #

def test_case():
    """
    This test case looks like this:
              root
            /      \
        left        right
        /
    left.left
    """
    tree_1 = Node('root', Node('left', Node('left.left')), Node('right'))
    assert deserialize(serialize(tree_1)).left.left.val == 'left.left'

    tree_2 = Node('blah')
    assert deserialize(serialize(tree_2)).val == 'blah'

    tree_3 = Node('blah', Node('foo', None, Node('BaR')))
    assert deserialize(serialize(tree_3)).left.right.val == 'BaR'

    tree_4 = Node('blah', None, Node('foo', None, Node('BaR', None, Node('root', Node('fizz')))))
    assert deserialize(serialize(tree_4)).right.right.right.left.val == 'fizz'

    print("Your tests passed!")

def alt_test_case():
    """
    Encoding would look like

    1 2 4 8 # # # 5 # # 3 6 # # 7 # #

    """
    tree = Node(1, Node(2, Node(4, Node(8, None, None), None), Node(5, None, None)), Node(3, Node(6, None, None), Node(7, None, None)))
    assert deserialize(serialize(tree)).left.right.val == 5

if __name__ == "__main__":
    # test_case()
    alt_test_case()

"""
Their Solution:

def serialize(root):
    if root is None:
        return '#'
    return '{} {} {}'.format(root.val, serialize(root.left), serialize(root.right))

def deserialize(data):
    def helper():
        val = next(vals)
        if val == '#':
            return None
        node = Node(int(val))
        node.left = helper()
        node.right = helper()
        return node
    vals = iter(data.split())
    return helper()

"""