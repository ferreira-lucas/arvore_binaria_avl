def height(node):
    if node is None:
        return -1
    else:
        return node.height 

def left_rotation(r):
    y = r.right
    f = y.left

    y.left = r
    r.right = f

    r.height = max(height(r.left), height(r.right)) + 1
    y.height = max(height(y.left), height(y.right)) + 1

    return y
        
def right_rotation(r):
    y = r.left
    f = y.right

    y.right = r
    r.left = f

    r.height = max(height(r.left), height(r.right)) + 1
    y.height = max(height(y.left), height(y.right)) + 1

    return y

def double_left_rotation(r):
    r.right = right_rotation(r.right)
    return left_rotation(r)

def double_right_rotation(r):
    r.left = left_rotation(r.left)
    return right_rotation(r)