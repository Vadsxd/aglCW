import graphviz
import time

time_pause = 0.4


class Node:
    def __init__(self, value=None):
        self.red = False
        self.parent = None
        self.value = value
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.nil = Node()
        self.nil.red = False
        self.nil.left = None
        self.nil.right = None
        self.root = self.nil
        self.graph = graphviz.Digraph()

    def insert(self, value):
        new_node = Node(value)
        parent = self.nil
        current = self.root
        while current != self.nil:
            parent = current
            if new_node.value < current.value:
                current = current.left
            else:
                current = current.right

        new_node.parent = parent
        if parent == self.nil:
            self.root = new_node
        elif new_node.value < parent.value:
            parent.left = new_node
        else:
            parent.right = new_node

        new_node.left = self.nil
        new_node.right = self.nil
        new_node.red = True
        self.fix_insert(new_node)

    def rotate_left(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.nil:
            y.left.parent = x

        y.parent = x.parent
        if x.parent == self.nil:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def rotate_right(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.nil:
            y.right.parent = x

        y.parent = x.parent
        if x.parent == self.nil:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def transplant(self, u, v):
        if u.parent == self.nil:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def fix_insert(self, new_node):
        while new_node.parent.red:
            if new_node.parent == new_node.parent.parent.left:
                uncle = new_node.parent.parent.right
                if uncle.red:
                    uncle.red = False
                    new_node.parent.red = False
                    new_node.parent.parent.red = True
                    new_node = new_node.parent.parent
                else:
                    if new_node == new_node.parent.right:
                        new_node = new_node.parent
                        self.rotate_left(new_node)
                    new_node.parent.red = False
                    new_node.parent.parent.red = True
                    self.rotate_right(new_node.parent.parent)
            else:
                uncle = new_node.parent.parent.left
                if uncle.red:
                    uncle.red = False
                    new_node.parent.red = False
                    new_node.parent.parent.red = True
                    new_node = new_node.parent.parent
                else:
                    if new_node == new_node.parent.left:
                        new_node = new_node.parent
                        self.rotate_right(new_node)
                    new_node.parent.red = False
                    new_node.parent.parent.red = True
                    self.rotate_left(new_node.parent.parent)
        self.root.red = False

    def find(self, value):
        return self._find(self.root, value)

    def _find(self, node, value):
        if node == self.nil:
            return node
        if node.value == value:
            return node
        if value > node.value:
            return self._find(node.right, value)
        else:
            return self._find(node.left, value)

    def delete(self, val):
        node = self.find(val)
        if node != self.nil:
            self._delete(node)

    def _delete(self, node):
        y = node
        y_original_color = y.red
        if node.left == self.nil:
            x = node.right
            self.transplant(node, node.right)
        elif node.right == self.nil:
            x = node.left
            self.transplant(node, node.left)
        else:
            y = self.find_minumum(node.right)
            y_original_color = y.red
            x = y.right
            if y.parent == node:
                x.parent = y
            else:
                self.transplant(y, y.right)
                y.right = node.right
                y.right.parent = y

            self.transplant(node, y)
            y.left = node.left
            y.left.parent = y
            y.red = node.red
        if y_original_color is False:
            self.delete_fix(x)

    def delete_fix(self, x):
        while x != self.root and x.red is False:
            if x == x.parent.left:
                s = x.parent.right
                if s.red is True:
                    s.red = False
                    x.parent.red = True
                    self.rotate_left(x.parent)
                    s = x.parent.right

                if s.left.red is False and s.right.red is False:
                    s.red = True
                    x = x.parent
                else:
                    if s.right.red is False:
                        s.left.red = False
                        s.red = True
                        self.rotate_right(s)
                        s = x.parent.right

                    s.red = x.parent.red
                    x.parent.red = False
                    s.right.red = False
                    self.rotate_left(x.parent)
                    x = self.root
            else:
                if x == x.parent.right:
                    s = x.parent.left
                    if s.red is True:
                        s.red = False
                        x.parent.red = True
                        self.rotate_right(x.parent)
                        s = x.parent.left

                    if s.right.red is False and s.left.red is False:
                        s.red = True
                        x = x.parent
                    else:
                        if s.left.red is False:
                            s.right.red = False
                            s.red = True
                            self.rotate_left(s)
                            s = x.parent.left

                        s.color = x.parent.red
                        x.parent.red = False
                        s.left.red = False
                        self.rotate_right(x.parent)
                        x = self.root
        x.red = False

    def find_minumum(self, node):
        if node is None:
            node = self.root
        if self.root == self.nil:
            return self.nil
        while node.left != self.nil:
            node = node.left
        return node

    def visualizator(self, current):
        if current.value is None:
            return
        self.graph.node(str(current.value), style='filled', fillcolor='red' if current.red else 'black', fontcolor='white')
        self.graph.render('RBT_Visualisation/RBT.gv', view=True)
        time.sleep(time_pause)
        if current.right.value is not None:
            self.graph.node(str(current.right.value), style='filled', fillcolor='red' if current.red else 'black', fontcolor='white')
            self.graph.edge(str(current.value), str(current.right.value))
            self.graph.render('RBT_Visualisation/RBT.gv', view=True)
            time.sleep(time_pause)
        if current.left.value is not None:
            self.graph.node(str(current.left.value), style='filled', fillcolor='red' if current.red else 'black', fontcolor='white')
            self.graph.edge(str(current.value), str(current.left.value))
            self.graph.render('RBT_Visualisation/RBT.gv', view=True)
            time.sleep(time_pause)
        self.visualizator(current.right)
        self.visualizator(current.left)

    def in_order(self, current, result):
        if current == self.nil:
            return
        self.in_order(current.left, result)
        result.append(current.value)
        self.in_order(current.right, result)
        return result

    def pre_order(self, current, result):
        if current == self.nil:
            return
        result.append(current.value)
        self.pre_order(current.left, result)
        self.pre_order(current.right, result)
        return result

    def post_order(self, current, result):
        if current == self.nil:
            return
        self.post_order(current.left, result)
        self.post_order(current.right, result)
        result.append(current.value)
        return result

    def __repr__(self):
        lines = []
        print_tree(self.root, lines)
        return '\n'.join(lines)


def print_tree(node, lines, level=0):
    if node.value is not None:
        print_tree(node.right, lines, level+1)
        lines.append('-' * 4 * level + '> ' + str(node.value) + ' ' + ('r' if node.red else 'b'))
        print_tree(node.left, lines, level+1)
