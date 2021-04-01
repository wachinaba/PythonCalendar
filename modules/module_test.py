import datatypes

l = datatypes.Childs()
l.append(1)
l.printall()
l.append(2)
l.printall()
x = l.append(0)
l.printall()
l.append(3)
l.printall()

l.move_top(x)
l.printall()