# coding:utf-8
'''
平衡二叉树：要么是一棵空树，要么任何一个节点的左右子树高度差的绝对值不超过1。

后序遍历
'''


class Node:
    def __init__(self, value, left=None, right=None):
        self.left = left
        self.right = right
        self.value = value


def isBalance(head):
    is_avl = True

    def getHeight(head, level, is_avl):
        if head is None:
            return level

        # lh，rh为左右深度
        lh = getHeight(head.left, level + 1, is_avl)
        rh = getHeight(head.right, level + 1, is_avl)

        # 不平衡
        if abs(lh - rh) > 1:
            is_avl = False

        # 向上一直返回
        if is_avl is False:
            return False

        return max(lh, rh)

    return getHeight(head, 0, is_avl)


tree = Node(1, Node(2, Node(4, Node(6), Node(7)), Node(5)), Node(3))

print isBalance(tree)
