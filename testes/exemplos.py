import classes as c

def inorder_example_tree():
    tree = c.ArvoreBinaria()
    n1 = c.Node('a')
    n2 = c.Node('+')
    n3 = c.Node('*')
    n4 = c.Node('b')
    n5 = c.Node('-')
    n6 = c.Node('/')
    n7 = c.Node('c')
    n8 = c.Node('d')
    n9 = c.Node('e')

    n6.left = n7
    n6.right = n8
    n5.left = n6
    n5.right = n9
    n3.left = n4
    n3.right = n5
    n2.left = n1
    n2.right = n3
    
    tree.raiz = n2
    return tree

def postorder_example_tree():
    tree = c.ArvoreBinaria()
    n1 = c.Node('I')
    n2 = c.Node('N')
    n3 = c.Node('S')
    n4 = c.Node('C')
    n5 = c.Node('R')
    n6 = c.Node('E')
    n7 = c.Node('V')
    n8 = c.Node('A')
    n9 = c.Node('5')
    n0 = c.Node('3')

    n0.left = n6
    n0.right = n9
    n6.left = n1
    n6.right = n5
    n5.left = n2
    n5.right = n4
    n4.right = n3
    n9.left = n8
    n8.right = n7

    tree.raiz = n0
    return tree