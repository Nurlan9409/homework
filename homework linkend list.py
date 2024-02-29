class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head =None

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def append(self,new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node

        last = self.head
        while last.next is not None:
            last=last.next
        last.next = new_node

    def push(self,new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node


    def insert(self,prev_node,new_data):
        if prev_node is None:
            print("hatolik")

        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node


a = Node(1)
b = Node(3)
c = Node(5)
d = Node(7)
e = Node(9)
f = Node(11)
g = Node(13)
h = Node(15)
j = Node(17)
k = Node(19)

ll_1= LinkedList()
ll_1.head = a
a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
f.next = g
g.next = h
h.next = j
j.next = k
print(ll_1.printList())
print(">>>>>>>>>>>>>>>>>>>>>>>")


x = (16)
z = (55)
l = (99)
n = (44)
ll_1.insert(a,z)
ll_1.insert(b,l)
ll_1.insert(j,n)


ll_1.insert(c,x)
print(ll_1.printList())

print(">>>>>>>>>>>>>>INsert<<<<<<<<<<<<<<<<<<<<<<")

y = (88)
m = (2)
m1 = (4)
m2 = (6)
m3 = (8)
m4 = (10)
m5 = (12)
ll_1.append(y)
ll_1.append(m)
ll_1.append(m1)
ll_1.append(m2)
ll_1.append(m3)
ll_1.append(m4)
ll_1.append(m5)

print(ll_1.printList())

print("Append")

a1 = (123)
a12 = (147)
a13 = (789)
a14 = (963)
a15 = (321)
a16 = (159)
a17 = (357)
a18 = (1234)
ll_1.push(a1)
ll_1.push(a12)
ll_1.push(a13)
ll_1.push(a14)
ll_1.push(a15)
ll_1.push(a16)
ll_1.push(a17)
ll_1.push(a18)
print(ll_1.printList())
print("Push")

"""Linked list2"""

x1 = Node(100)
x2 =Node (110)
x3 =Node (120)
x4 =Node (130)
x5 =Node (140)
ll_2 = LinkedList()
ll_2.head = x1
x1.next = x2
x2.next = x3
x3.next = x4
x4.next = x5

print(ll_2.printList())


x11 = (200)
x12 = (210)
x13 = (220)
x14 = (230)
x15 = (240)
ll_2.insert(x1, x11)
ll_2.insert(x2, x12)
ll_2.insert(x3, x13)
ll_2.insert(x4, x14)
ll_2.insert(x5, x15)
print(ll_2.printList())


z10 = (300)
z11 = (310)
z12 = (320)
z13 = (330)
z14 = (340)
z15 = (350)
ll_2.append(z10)
ll_2.append(z11)
ll_2.append(z12)
ll_2.append(z13)
ll_2.append(z14)
ll_2.append(z15)
print(ll_2.printList())



c10 = (400)
c11 = (410)
c12 = (420)
c13 = (430)
c14 = (440)
c15 = (450)
ll_2.push(c10)
ll_2.push(c11)
ll_2.push(c12)
ll_2.push(c13)
ll_2.push(c14)
ll_2.push(c15)
print(ll_2.printList())

a10 = Node(500)
a11 = Node(510)
a12 = Node(520)
a13 = Node(530)
a14 = Node(540)
a15 = Node(550)
ll_3 = LinkedList()
ll_3.head = a10
a10.next = a11
a11.next = a12
a12.next = a13
a13.next = a14
a14.next = a15
ll_3.push(a10)
ll_3.push(a11)
ll_3.push(a12)
ll_3.push(a13)
ll_3.push(a14)
ll_3.push(a15)
print(ll_3.printList())

b10 = (600)
b11 = (610)
b12 = (620)
b13 = (630)
b14 = (640)
ll_3.append(b10)
ll_3.append(b11)
ll_3.append(b12)
ll_3.append(b13)
ll_3.append(b14)
print(ll_3.printList())

q10 = (700)
q11 = (710)
q12 = (720)
q13 = (730)
q14 = (740)
q15 = (750)
ll_3.insert(a11, q11)
ll_3.insert(a10, q12)
ll_3.insert(a13, q13)
ll_3.insert(a12, q14)
ll_3.insert(a10, q14)
print(ll_3.printList())



a101 = Node(5000)
a111 = Node(5100)
a121 = Node(5200)
a131 = Node(5300)
a141 = Node(5400)
a151 = Node(5500)
ll_4 = LinkedList()
ll_4.head = a101
a101.next = a111
a111.next = a121
a121.next = a131
a131.next = a141
a141.next = a151
ll_4.push(a101)
ll_4.push(a111)
ll_4.push(a121)
ll_4.push(a131)
ll_4.push(a141)
ll_4.push(a151)
print(ll_4.printList())

b101 = (6000)
b111 = (6100)
b121 = (6200)
b131 = (6300)
b141 = (6400)
ll_4.append(b101)
ll_4.append(b111)
ll_4.append(b121)
ll_4.append(b131)
ll_4.append(b141)
print(ll_4.printList())

q101 = (700)
q111 = (710)
q121 = (720)
q131 = (730)
q141 = (740)
q151 = (750)
ll_4.insert(a111, q111)
ll_4.insert(a101, q121)
ll_4.insert(a131, q131)
ll_4.insert(a121, q141)
ll_4.insert(a101, q141)
print(ll_4.printList())

