class ListNode:
    def __init__(self, data, next=None):
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

if __name__ == "__main__":
    head = ListNode(0)

    for i in range(1,10):
        insert_node(head, i)

    show_list(head)

    delete_node(search_list(head, 5))

    show_list(head)
