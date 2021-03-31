import datatypes

l = datatypes.Childs()
l.append(1)
l.append(2)
x = l.append(0)
l.append(3)
l.printall()

l.move_top(x)
l.printall()