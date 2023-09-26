class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None
        "Передаем в иницилизатор данные"
 
 
class Tree:
    "Создаем класс Tree"
    def __init__(self):
        self.root = None
 
    def __find(self, node, parent, value):
        if node is None:
            return None, parent, False
        """
        Создаем рекурсивный метод поиска значений
        Делаем проверку текущего значения  относительно текущего значения, который хранится в узле, если текущее значение меньше, то
        идем по левой ветке, иначе идем по правой ветку

        """
 
        if value == node.data:
            return node, parent, True
 
        if value < node.data:
            if node.left:
                return self.__find(node.left, node, value)
 
        if value > node.data:
            if node.right:
                return self.__find(node.right, node, value)
 
        return node, parent, False
 
    def append(self, obj):
        """
        Создаем метод добавления эллементов
        """
        if self.root is None:
            self.root = obj
            return obj
 
        s, p, fl_find = self.__find(self.root, None, obj.data)
 
        if not fl_find and s:
            if obj.data < s.data:
                s.left = obj
            else:
                s.right = obj
 
        return obj
 
    def show_tree(self, node):
        """рекурсивный метод, который отображает бинарное дерево

        """
        if node is None:
            return
 
        self.show_tree(node.right)
        print(node.data)
        self.show_tree(node.left)
        # Вызываем рекурсивный метод
 
    def show_wide_tree(self, node):
        #Отоброжение бинарного дерева в ширину 
        if node is None:
            return
 
        v = [node]
        while v:
            vn = []
            for x in v:
                print(x.data, end=" ")
                if x.left:
                    vn += [x.left]
                if x.right:
                    vn += [x.right]
            print()
            v = vn
 
    def __del_leaf(self, s, p):
        if p.left == s:
            p.left = None
        elif p.right == s:
            p.right = None
 
    def __del_one_child(self, s, p):
        """ Создаем метод удаления вершины, у которого один потомок  
        Делаем проверку на пренадлежность эллемента  к правой или левой ветке и переопределяем эллемент"""
        if p.left == s:
            if s.left is None:
                p.left = s.right
            elif s.right is None:
                p.left = s.left
        elif p.right == s:
            if s.left is None:
                p.right = s.right
            elif s.right is None:
                p.right = s.left
 
    def __find_min(self, node, parent):
        if node.left:
            return self.__find_min(node.left, node)
 
        return node, parent
 
    def del_node(self, key):
        """
        Удаление вершины бинарного дерева
        Находим вершину которую хотим удалить
        Если листовая вершина s.left и s.right принимает значение none ,то вызываем метод удаления del_leaf(s,p) - удаление листа
        s - удаляемая вершина, p - родительская
        Если отсутствует левый или правый потомок, то вершина s имеет одного потомка
        Находим минимальное и родителя минимального значения
        Удаляем вершину sr"""
        
        s, p, fl_find = self.__find(self.root, None, key)
 
        if not fl_find:
            return None
 
        if s.left is None and s.right is None:
            self.__del_leaf(s, p)
        elif s.left is None or s.right is None:
            self.__del_one_child(s, p)
        else:
            sr, pr = self.__find_min(s.right, s)
            s.data = sr.data
            self.__del_one_child(sr, pr)
 
 
v = [10, 5, 7, 16, 13, 2, 20]
#v = [20, 5, 24, 2, 16, 11, 18]
# Cписок из добавляемых значений
 
t = Tree()
# Объект бинарного дерева
for x in v:
    t.append(Node(x))
    # Перебираем значения
 
t.del_node(5)
#Удаление эллемента
t.show_wide_tree(t.root)
# Отоброжения бинарного дерева в ширину