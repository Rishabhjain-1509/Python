class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None

# Print the linked list
    def listprint(self):
        printval = self.headval
        while printval is not None:
            print (printval.dataval)
            printval = printval.nextval
    
    def AtBegining(self,newdata):
        
        NewNode = Node(newdata)

        # Update the new nodes next val to existing node
        NewNode.nextval = self.headval
        self.headval = NewNode

    #Add the node at end of the Linked List.
    def AtEnd(self, newdata):
        NewNode = Node(newdata)
        if self.headval is None:
            self.headval = NewNode
            return
        laste = self.headval
        while(laste.nextval):
            laste = laste.nextval
        laste.nextval=NewNode

    #Adding the node in between the linked list.
    def Inbetween(self,middle_node,newdata):
        if middle_node is None:
            print("The mentioned node is absent")
            return

        NewNode = Node(newdata)
        NewNode.nextval = middle_node.nextval
        middle_node.nextval = NewNode


Value = 1

while(Value == 1):
    print("Choose the value where you want to insert the Data.\n1. Add at Begining. \n2. Add at Middle \n3. Add at End.")
    UserI = int(input("Enter the value choosen = "))

    list = SLinkedList()

    if( UserI == 1 ):

        list.AtBegining("Sun")
        list.listprint()
    
    elif( UserI == 2 ):

        list.Inbetween(list.headval.nextval,"Fri")
        list.listprint()

    elif( UserI == 3 ):

        list.AtEnd("Thu")
        list.listprint()
    
    else:
        print("Enter the proper value.")

    

    list.headval = Node("Mon")
    e2 = Node(input("Enter the data where you have to insert = "))
    e3 = Node("Wed")

    list.headval.nextval = e2
    e2.nextval = e3
    
    
    print("You want to add more data in linked list \n1. Yes \n2. No")
    Value = input("Enter the value you choosen")
