# coding:utf-8
"""
打印两个有序链表的公共部分

如果head1的值小于head2，则head1向后
如果head2的值小于head1，则head2向后
相等的话，打印这个值。然后head1，head2都向后
"""


class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node


def print_common_part(head1, head2):
    while head1 is not None and head2 is not None:
        if head1.value < head2.value:
            head1 = head1.next_node
        elif head1.value > head2.value:
            head2 = head2.next_node
        else:
            print head1.value
            head1, head2 = head1.next_node, head2.next_node


if __name__ == '__main__':
    link1 = Node(1, Node(2, Node(3, Node(4, Node(5)))))
    link2 = Node(3, Node(5, Node(6)))

    print_common_part(link1, link2)
