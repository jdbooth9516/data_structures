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


    def in_order_traverse(self):
        #to traverse a tree of unknown size 

        current = self.root
        previous = None
        end = False

        while not end:
            if current.left is not None:
                previous = current
                current = current.left

            elif current == self.root and self.root.left == None and self.root.right != None and self.root.data != None:
                print( self.root.data)
                self.root.data = None

                previous = current
                current = current.right


            elif self.root.left == None and self.root.right == None:
                end = True

            else: 
                print(current.data)
                if previous.left != None and previous.left.data == current.data:
                    previous.left = None
                    current = self.root
                elif previous.right != None and previous.right.data == current.data:
                    previous.right = None
                    current = self.root


tree = Tree()
tree_traverse = tree

tree.add_node(20)
tree.add_node(25)
tree.add_node(15)
tree.add_node(17) 

tree.add_node(7)


tree.search_tree(17)

tree_traverse.in_order_traverse()
print(tree)