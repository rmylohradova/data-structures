from sllist import Node, SLlist

a = SLlist()
a.add(1)
a.add(2)
a.add(3)
a.push(9)
a.printList()
a.add_position(1, 8)
a.printList()
print("second last", a.second_last())
a.remove()
a.printList()
a.set(1, 7)
a.printList()
a.remove_position(3)
a.printList()
print("element on position 1 is", a.get(1))
print("second last", a.second_last())
a.push(3)
a.push(4)
a.push(9)
a.set(1, 7)
a.printList()
print("element on position 5 is", a.get(5))
a.add(5)
a.push(3)
a.add_position(7, 3)
a.printList()


