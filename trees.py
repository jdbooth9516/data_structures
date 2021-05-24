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


            
tree = Tree()

tree.add_node(20)
tree.add_node(25)
tree.add_node(15)
tree.add_node(17) 
tree.add_node(23)
tree.add_node(22)
tree.add_node(7)
tree.add_node(13)

tree.search_tree(22)