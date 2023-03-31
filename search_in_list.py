class ListNode:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

def search_list(L: ListNode, key: int) -> ListNode :
    while L and L.data != key:
        L = L.next
    return L

def insert_node(head: ListNode, data: int):
    temp = head
    while temp.next != None:
        temp = temp.next
    temp.next = ListNode(data)

def show_list(L: ListNode):
    print()
    while L :
        print(f'{L.data} -> ', end="")
        L = L.next

# delete the node past this one assuming it is not the tail node
def delete_node(L: ListNode):
    L.next = L.next.next

def merge_list(L1: ListNode, L2: ListNode) -> ListNode:
    dummy_head = tail = ListNode()

    while L1 and L2:
        if L1.data < L2.data:
            tail.next, L1 = L1, L1.next
        else:
            tail.next, L2 = L2, L2.next
        tail = tail.next

    tail.next = L1 or L2
    return dummy_head

if __name__ == "__main__":
    head1 = ListNode()
    head2 = ListNode()

    insert_node(head1, 2)
    insert_node(head1, 5)
    insert_node(head1, 7)

    insert_node(head2, 3)
    insert_node(head2, 11)

    show_list(head1.next)
    show_list(head2.next)

    head = merge_list(head1.next, head2.next)
    show_list(head)

