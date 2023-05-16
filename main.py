
from avltree import *

B = AVLTree()



avl_insert(B,"G",14)
avl_insert(B,"F",10)
avl_insert(B,"I",3.5)
avl_insert(B,"D",3)
avl_insert(B,"B",4)
avl_insert(B,"M",11)

avl_insert(B,"E",6)
avl_insert(B,"C",12)
avl_insert(B,"A",8)
avl_insert(B,"L",9)
avl_insert(B,"K",7)
avl_insert(B,"H",1)

avl_insert(B,"J",5)
avl_insert(B,"O",15)
avl_insert(B,"N",13)
avl_delete(B,"K")



imprimirarbol__P(B, B.root)