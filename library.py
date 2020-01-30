# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 14:20:25 2020

@author: Pranav
"""

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkList:
    def __init__(self):
        self.head=None
    
    def addBeg(self,newdata):
        newnode =Node(newdata)
        newnode.next=None
        self.head=newnode
        
    def addLast(self,data):
        newnode=Node(data)
        temp=self.head
        while(temp.next!=None):
            temp=temp.next
        temp.next=newnode
    def printList(self):
        temp = self.head 
        if temp==None:
            print("Book Library is empty currently")
            return
        print("List of the Books is as follows")
        while(temp): 
            print (temp.data)
            temp = temp.next
            
        
    def delete(self,str):
        temp=self.head;
        if temp==None:
            print("Book Library is empty currently")
            return
        if str==temp.data:
            if temp.next==None:
                self.head=None
                print("\nBook Deleted Successfully")
                return
            else:
                self.head=temp.next
                temp=None
                print("\nBook Deleted Successfully")
                return
        while(temp is not None):
            if temp.data==str:
                break
            prev=temp
            temp=temp.next
        if(temp == None):
            print("Book is not present in the library")
            return
        prev.next=temp.next
        temp=None
        
        print("\nBook Deleted Successfully")
    def search(self,pattern):
        Dict={}
        temp=self.head
        while(temp is not None):
            #Dict.update({temp.data:temp.next})
            #print(type(temp.data),type(temp))
            z=id(temp)
            Dict[temp.data] =z
            temp = temp.next;
        #print(Dict)
        if pattern in Dict.keys():
            print("\nBook is present at location ",end="")
            print(Dict[pattern])
        else:
            print("\nBook is not present")
        #for i in Dict.keys():
         #   print(i)
        return
if __name__=='__main__':
    list1=LinkList()
    print("-------------Welcome TO Book Library-------------")
    while True:
        print("\n1.Add a Book\n2.Delete Book\n3.Print all books\n4.Search\n5.Exit\nEnter your choice")
        choice=int(input())
        if choice==1:
            print("Enter the name of the book")
            str=input()
            ##list1=LinkList()
            if list1.head==None:
                list1.addBeg(str)
                print("\nBook Added at beg Successfully")
                
            else:
                list1.addLast(str)
                print("\nBook Added Successfully")
                
        elif choice==2:
            print("Enter the name of the book to be deleted")
            str=input()
            ##list1=LinkList()
            list1.delete(str)
            
            
        elif choice==3:
            ##list1=LinkList()
            
            list1.printList()
                        
        elif choice==4:
            print("\nEnter the name of the book for searching")
            pattern=input()
            list1.search(pattern)
        elif choice==5:
            break
        else:
            print("\n Invalid input")
            
                
        
        

            
        