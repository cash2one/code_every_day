# coding:utf-8
"""
单链表：
首先定位要删除的元素
若k<=0，说明要删除的元素为第i个,k+i-1=0
特别的有k=1，为第一个节点

对于双向链表，只需要主要前驱结点跟后驱节点即可
"""


class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node


def remove_last_k_node(head, k):
    cur = head
    while cur is not None:
        cur = cur.next_node
        k -= 1

    if k < 0:
        cur = head
        for _ in range(k, 0 - 1):
            cur = cur.next_node
        # 此时cur为待删除节点的前一个节点
        cur.next_node = cur.next_node.next_node
    elif k == 0:
        return head.next_node

    return head


if __name__ == '__main__':
    link1 = Node(1, Node(2, Node(3, Node(4, Node(5)))))
    remove_last_k_node(link1, 2)
