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

def reverse_sublist(L: ListNode, start: int, end: int):
    subHead = L
    for _ in range(1, start):
        subHead = subHead.next
    
    itr = subHead.next 
    for _ in range(end-start):
        temp = itr.next
        itr.next, temp.next, subHead.next = (temp.next, subHead.next, temp)

def is_list_cyclic(Head: ListNode) -> ListNode:
    def cycle_len(end):
        step, start = 0, end
        while True:
            step += 1
            start = start.next 
            if start is end:
                return step
    
    fast = slow = Head
    while fast and fast.next and fast.next.next:
        slow, fast = slow.next, fast.next.next
        if slow is fast:
            cycle_len_itr = Head
            for _ in range(cycle_len(fast)):
                cycle_len_itr = cycle_len_itr.next
            it = Head
            while it is not cycle_len_itr:
                it = it.next
                cycle_len_itr = cycle_len_itr.next
            return it



if __name__ == "__main__":
    head = ListNode()
    for i in range(11):
        insert_node(head, i)
    show_list(head)
    node10 = search_list(head, 10)
    node10.next = search_list(head, 7)
    cycle_start = is_list_cyclic(head)
    print(f'\n{cycle_start.data}')
    # head = merge_list(head1.next, head2.next)

    # reverse_sublist(head, 2, 5)

    # show_list(head)

