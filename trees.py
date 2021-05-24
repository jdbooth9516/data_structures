class Node: 
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None 


class Tree:
    def __init__(self):
        self.root = None
        
        
    def add_node(self, data):
        node = Node(data)
        end = False
        if self.root == None: 
            self.root = node 
            print(node.data)
            return


        current = self.root

        while not end: 
            if current.data > node.data:
                if current.left == None:
                    current.left = node
                    end = True
                    print(node.data)
                else:
                    temp = current.left
                    current = temp
            if current.data < node.data: 
                if current.right == None: 
                    current.right = node
                    end = True
                    print(node.data)
                else:
                    temp = current.right
                    current = temp

    def search_tree(self, search):
        end = False
        current = self.root

        while not end: 
            if current.data == search:
                print("data has been found")
                end = True
            else:
                if current.left != None:
                    if current.data > search:
                        current = current.left
                        continue
                if current.right != None:
                    if current.data < search:
                        current = current.right
                        continue
                elif current.right is None and current.left is None:
                    end = True
                    return print("data was not found")

        
        
        

    def in_order_traverse(self, start):
        #to traverse a tree of unknown size
       if start:
           self.in_order_traverse(start.left)
           print(start.data)
           self.in_order_traverse(start.right)

    def pre_order(self, start):

        if start: 
            print(start.data),
            self.pre_order(start.left)
            self.pre_order(start.right)




tree = Tree()
tree_traverse = tree

tree.add_node(20)
tree.add_node(25)
tree.add_node(15)
tree.add_node(17) 

tree.add_node(7)

print()
tree.search_tree(17)
print()

tree_traverse.in_order_traverse(tree.root)

print()
tree.pre_order(tree.root)