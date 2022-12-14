from linked_list import LinkedList

c = LinkedList(None, 12)
b = LinkedList(c, 11)
a = LinkedList(b, 10)

a.move(9)

print(a.pos, b.pos, c.pos)
