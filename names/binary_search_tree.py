class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            
            if not self.left:
                
                self.left = BSTNode(value)
                
            else:
                
                self.left.insert(value)

        if value >= self.value:
            if not self.right:
                
                self.right = BSTNode(value)

            else:
                self.right.insert(value)
                

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target is self.value:
            return True
        
        elif target < self.value:
            if not self.left:
                
                return False
            else:
                
                return self.left.contains(target)

        if target >= self.value:
            if not self.right:
                
                return False
            else:
                return self.right.contains(target)
