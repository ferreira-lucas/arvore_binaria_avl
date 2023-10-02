import rotations as r

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 0

class ArvoreBinaria:
    def __init__(self, data=None, node=None):
        if node:
            self.raiz = node
        elif data:
            node = Node(data)
            self.raiz = node
        else:
            self.raiz = None
        
class ArvoreBinariaBusca(ArvoreBinaria):
    def height(self, node):
        if node is None:
            return -1
        else:
            return node.height 

    #INSERIR UM VALOR NA ÁRVORE
    def inserir(self, valor, node=0):
        """pai = None
        x = self.raiz

        while(x):
            pai = x
            if valor < x.data:
                x = x.left
            else:
                x = x.right
            
        if pai is None:
            self.raiz = Node(valor)
            pai = self.raiz
        elif valor < pai.data:
            pai.left = Node(valor)
        else:
            pai.right = Node(valor)
        
        pai.height = max(self.height(pai.left), self.height(pai.right)) + 1

        self.raiz = self.balancear(pai)"""
        if self.raiz is None:
            self.raiz = Node(valor)
            self.raiz.height = max(self.height(self.raiz.left), self.height(self.raiz.right)) + 1
            #self.raiz = self.balancear(self.raiz)
        else:
            if node == 0:
                node = self.raiz
        
            if node is None:
                node = Node(valor)
                return node
            else:
                if valor < node.data:
                    node.left = self.inserir(valor, node.left)
                elif valor > node.data:
                    node.right = self.inserir(valor, node.right)
                else:
                    print("Inserção não realizada")
        
            node.height = max(self.height(node.left), self.height(node.right)) + 1

            node = self.balancear(node)

            print(node)

        return node
    
    #PESQUISAR UM VALOR NA ÁRVORE
    def pesquisar(self, valor, node=0):
        if node == 0:
            node = self.raiz
        elif node is None:
            return None
        
        if node.data == valor:
            return ArvoreBinariaBusca(node)
        
        if valor < node.data:
            return self.pesquisar(valor, node.left)
        else:
            return self.pesquisar(valor, node.right)
        
    #REMOVER UM VALOR DA ÁRVORE
    def remover(self, valor, node=0):
        if node == 0:
            node = self.raiz
        elif node is None:
            return None
        
        if valor < node.data:
            node.left = self.remover(valor, node.left)
        elif valor > node.data:
            node.right = self.remover(valor, node.right)
        else:
            if node.left is None:
                return node.right #Remove elemento e sobe a subárvore da direita (se node.right for None, retorna None, ou seja, remove a folha)
            elif node.right is None:
                return node.left #Remove elemento e sobe a subárvore da esquerda
            else:
                subs = self.min(node.right)
                node.data = subs
                node.right = self.remover(subs, node.right)

        return node
    
    def imprimir(self, nivel, node=0):
        if node == 0:
            node = self.raiz

        if node:
            self.imprimir(nivel + 1, node.right)
            print('\n')

            for i in range(nivel):
                print('\t', end='')

            print(node.data)
            self.imprimir(nivel + 1, node.left)

    def fator(self, node):
        if node:
            print(self.height(node.left) - self.height(node.right))
            return self.height(node.left) - self.height(node.right)
        else:
            return 0        

    def balancear(self, node):
        fator_ = self.fator(node)

        if fator_ < -1 and self.fator(node.right) <= 0:
            node = r.left_rotation(node)

        elif fator_ > 1 and self.fator(node.left) >= 0:
            node = r.right_rotation(node)

        elif fator_ > 1 and self.fator(node.left) < 0:
            node = r.double_left_rotation(node)

        elif fator_ < -1 and self.fator(node.right) > 0:
            node = r.double_right_rotation(node)

        return node
            