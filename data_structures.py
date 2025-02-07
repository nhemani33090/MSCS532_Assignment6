# -------------------------------------------
# 1. Array Implementation
# -------------------------------------------
class Array:
    """Array implementation with methods for adding, removing, and accessing elements."""
    
    def __init__(self, capacity):
        """Initialize an array with a fixed size."""
        self.size = capacity
        self.container = [None] * capacity  

    def insert(self, index, value):
        """Insert a value at the specified index."""
        if 0 <= index < self.size:
            self.container[index] = value
        else:
            raise IndexError("Index out of range.")

    def delete(self, index):
        """Remove a value from a given index."""
        if 0 <= index < self.size:
            self.container[index] = None
        else:
            raise IndexError("Index out of range.")

    def access(self, index):
        """Retrieve an item at a specified index."""
        if 0 <= index < self.size:
            return self.container[index]
        else:
            raise IndexError("Index out of range.")

    def display(self):
        """Display array contents."""
        print(self.container)


# -------------------------------------------
# 2. Matrix Implementation
# -------------------------------------------
class Matrix:
    """Matrix with basic operations like modifying and accessing values."""
    
    def __init__(self, rows, cols):
        """Create a matrix with given dimensions, initialized with zeroes."""
        self.row_count = rows
        self.col_count = cols
        self.elements = [[0] * cols for _ in range(rows)]

    def insert(self, row, col, data):
        """Modify a specific position in the matrix."""
        if 0 <= row < self.row_count and 0 <= col < self.col_count:
            self.elements[row][col] = data
        else:
            raise IndexError("Invalid position.")

    def access(self, row, col):
        """Fetch an element from the matrix."""
        if 0 <= row < self.row_count and 0 <= col < self.col_count:
            return self.elements[row][col]
        else:
            raise IndexError("Invalid position.")

    def display(self):
        """Print the matrix."""
        for row in self.elements:
            print(row)


# -------------------------------------------
# 3. Stack Implementation (LIFO)
# -------------------------------------------
class Stack:
    """Stack implementation using a dynamic list."""
    
    def __init__(self):
        """Initialize an empty stack."""
        self.stack_data = []

    def push(self, value):
        """Add an item onto the stack."""
        self.stack_data.append(value)

    def pop(self):
        """Remove and return the last added item."""
        if self.is_empty():
            raise IndexError("Stack is empty.")
        return self.stack_data.pop()

    def peek(self):
        """View the top item without removing it."""
        if self.is_empty():
            raise IndexError("Stack is empty.")
        return self.stack_data[-1]

    def is_empty(self):
        """Check if the stack is empty."""
        return len(self.stack_data) == 0

    def display(self):
        """Print the stack contents."""
        print(self.stack_data)


# -------------------------------------------
# 4. Queue Implementation (FIFO)
# -------------------------------------------
class Queue:
    """Queue implementation with enqueue and dequeue operations."""
    
    def __init__(self):
        """Initialize an empty queue."""
        self.queue_items = []

    def enqueue(self, value):
        """Add an element to the queue."""
        self.queue_items.append(value)

    def dequeue(self):
        """Remove and return the front element."""
        if self.is_empty():
            raise IndexError("Queue is empty.")
        return self.queue_items.pop(0)

    def peek(self):
        """View the front element without removing it."""
        if self.is_empty():
            raise IndexError("Queue is empty.")
        return self.queue_items[0]

    def is_empty(self):
        """Check if the queue is empty."""
        return len(self.queue_items) == 0

    def display(self):
        """Show queue contents."""
        print(self.queue_items)


# -------------------------------------------
# 5. Singly Linked List
# -------------------------------------------
class Node:
    """A node representation for a singly linked list."""
    
    def __init__(self, value):
        """Initialize a node with value and a next pointer."""
        self.data = value
        self.next_node = None


class SinglyLinkedList:
    """Singly linked list supporting insertion, deletion, and traversal."""
    
    def __init__(self):
        """Initialize an empty linked list."""
        self.head_node = None

    def insert(self, value):
        """Add a new node at the end of the list."""
        new_entry = Node(value)
        if not self.head_node:
            self.head_node = new_entry
        else:
            temp = self.head_node
            while temp.next_node:
                temp = temp.next_node
            temp.next_node = new_entry

    def delete(self, value):
        """Remove a node containing the given value."""
        temp = self.head_node
        if temp and temp.data == value:
            self.head_node = temp.next_node
            return
        while temp and temp.next_node:
            if temp.next_node.data == value:
                temp.next_node = temp.next_node.next_node
                return
            temp = temp.next_node

    def display(self):
        """Print the linked list."""
        temp = self.head_node
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next_node
        print("None")


# -------------------------------------------
# 6. Rooted Tree
# -------------------------------------------
class TreeNode:
    """Tree node representation for hierarchical structures."""
    
    def __init__(self, value):
        """Initialize a tree node with a value and a child list."""
        self.node_value = value
        self.children_list = []

    def add_child(self, child_node):
        """Attach a child node to this tree node."""
        self.children_list.append(child_node)

    def display_tree(self, level=0):
        """Recursively display the tree structure."""
        print(" " * (level * 3) + str(self.node_value))
        for child in self.children_list:
            child.display_tree(level + 1)


# -------------------------------------------
# Example Usage of All Data Structures
# -------------------------------------------
if __name__ == "__main__":
    print("\n--- Array Example ---")
    arr = Array(5)
    arr.insert(0, 11)
    arr.insert(2, 22)
    arr.display()
    arr.delete(2)
    arr.display()

    print("\n--- Matrix Example ---")
    mat = Matrix(3, 3)
    mat.insert(1, 1, 7)
    mat.display()

    print("\n--- Stack Example ---")
    stk = Stack()
    stk.push(8)
    stk.push(18)
    stk.display()
    stk.pop()
    stk.display()

    print("\n--- Queue Example ---")
    q = Queue()
    q.enqueue(27)
    q.enqueue(47)
    q.display()
    q.dequeue()
    q.display()

    print("\n--- Linked List Example ---")
    ll = SinglyLinkedList()
    ll.insert(5)
    ll.insert(10)
    ll.display()
    ll.delete(5)
    ll.display()

    print("\n--- Tree Example ---")
    root = TreeNode("Root")
    nodeA = TreeNode("A")
    nodeB = TreeNode("B")

    root.add_child(nodeA)
    root.add_child(nodeB)

    nodeA.add_child(TreeNode("C"))
    nodeB.add_child(TreeNode("D"))

    root.display_tree()
