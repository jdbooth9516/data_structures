class Node:
    def __init__(self, data):
        self.next = None
        self.data = data

    
class linked_list:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def append_node(self, data):
        node = Node(data)

        if self.head is None: 
            self.head = node
            self.tail = node
            return

        else: 
            self.tail.next = node
            self.tail = self.tail.next


    def append_to_beginning(self,data):
        node = Node(data)

        if self.head is None: 
            self.head = node
            self.tail = node
            return
        else:
            temp = self.head
            self.head = node
            self.head.next = temp

    def contains_node(self, search):
        current = self.head

        while current is not None:
            if current.data == search: 
                print (f"Database contains Node {current.data}")
                return
            else: 
                temp = current.next
                current = temp

        if current is None: 
            print ("Node with that data was not found")
            return
                

linked = linked_list()
        

linked.append_node(20)
print(linked.head.data, linked.tail.data)
linked.append_node(45)
print(linked.head.data, linked.tail.data)

linked.append_node(60)
print(linked.head.data, linked.head.next.data,linked.tail.data)

linked.append_to_beginning(10) 
print(linked.head.data, linked.head.next.data)

linked.contains_node(70)
