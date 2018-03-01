class SinglyLinkedNode():
    """Implements a singly-linked node.
    """

    def __init__(self, value, nextNode=None):
        self._value = value
        self._nextNode = nextNode

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    @property
    def nextNode(self):
        return self._nextNode

    @nextNode.setter
    def nextNode(self, nextNode):
        self._nextNode = nextNode


#######################################################################
## Unit tests

def testNode():
    """Test a singly-linked node.
    """

    node = SinglyLinkedNode(0)

    result = node.value
    assert (result == 0)

    result = node.nextNode
    assert (result == None)

def testList():
    """Test the iteration of a singly-linked list.
    """

    # Create head node
    headNode = SinglyLinkedNode(0)
    # Create second node
    node = SinglyLinkedNode(1)
    # Connect second node to head node
    headNode.nextNode = node

    # Create second node
    node2 = SinglyLinkedNode(2)
    # Connect second node to head node
    node.nextNode = node2

    # Create third node
    node = SinglyLinkedNode(3)
    # Connect third node to second node
    node2.nextNode = node

    # Iterate the list
    node = headNode
    assert (node.value == 0)
    node = node.nextNode
    assert (node.value == 1)
    node = node.nextNode
    assert (node.value == 2)
    node = node.nextNode
    assert (node.value == 3)
    
    node = node.nextNode
    assert (node == None)