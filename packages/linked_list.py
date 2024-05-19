"""
* Implemententation of a linked list
------------------------------------

"""

class Node:
    """
    * An object for storing a single node of a linked list.
    * models two attributes--- data and the link to the next node in the list
    """

    data = None
    next_node= None

    def __init__(self,data):
        self.data= data

    def __repr__(self) -> str:
        return "<Node data: %s>" % self.data
    
class LinkedList:
    """ Singly Linked  List"""
    def __init__(self):
        self.head = None
    
    def isEmpty(self):
        return self.head == None
    
    def size(self):
        """ 
        * Returns the number of nodes in the list and 
        * Takes O(n) time
        """

        current = self.head
        counter = 0

        while current:
            counter +=1

            current = current.next_node
        return counter 
    
    def add(self,data):
        #prepend
        """
        * Adds new Node containing data at the head of the list
        """
        new_node= Node(data)
        new_node.next_node = self.head
        self.head = new_node
    
    def insert(self,pred_data,data):
        """
        * Inserts a new node after the node with the specified predecessor value.
        """
        pred = self.head

        while pred is not None and pred.data != pred_data:
            pred = pred.next_node
        if pred is not None:
            # the predecessor node is found
            node = Node(data)
            node.next_node = pred.next_node

    def append(self,data):
        """
        * Inserts a new node with the specified value at the end of this List.
        """
        if self.isEmpty():
            self.head = Node(data)
            return
        pred = self.head
        while pred.next_node is not None:
            pred=pred.next_node
        pred.next_node = Node(data)

    def delete_first(self):
        """
        * Deletes and returns the first node from this list
        """
        if self.isEmpty():
            return None
        temp = self.head
        self.head = self.head.next_node
        return temp
    
    def delete(self,value):
        """
        * Deletes and returns the first found node with the specified value 
        """
        if self.isEmpty():
            return None
        if self.head.data == value:
            #Delete the head
            temp = self.head
            self.head = self.head.next_node
            return temp
        pred = self.head
        temp = self.head.next_node
        while temp is not None and temp.data != value:
            pred = pred.next_node
            temp = temp.next_node
        if temp is not None:
            """
            * The node to be deleted is found.
            * Delete it by changing the references.
            """
            pred.next_node = temp.next_node
        return temp
    
    def pop(self):
        """
        * Deletes and returns the last node from this list
        """
        if self.isEmpty():
            return None
        if self.head.next_node is None:
            temp = self.head
            self.head = None
            return temp
        pred = self.head
        temp = self.head.next_node
        while temp.next_node is not None:
            pred = pred.next_node
            temp = temp.next_node
        pred.next_node = None
        return temp
    
    def search(self,key):
        """
        * Searches first node containing data that matches the key
        * Return None if value not found
        * Takes O(n)
        """
        current = self.head

        while current:
            if current.data == key:
                return current
            else:
                current = current.next_node
        return None

    def __repr__(self) -> str:
        """
        * Return a string reprensentation of the list 
        * Take O(n) time"""
 
        nodes = []
        current = self.head

        while current:
            if current is self.head:
                nodes.append("[Head: %s]" % current.data)
            elif current.next_node is None:
                nodes.append("[Tail: %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)

            current = current.next_node

        return '->'.join(nodes)
