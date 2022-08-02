Given a pointer to the head of a singly-linked list, print each data value from the reversed list. If the given list is empty, do not print anything.

Example

head* refers to the linked list with data values 1->2->3->Null

Print the following:
3
2
1


Function Description:

Complete the reversePrint function in the editor below.

reversePrint has the following parameters:

SinglyLinkedListNode pointer head: a reference to the head of the list


Prints

The data values of each node in the reversed list.


Input Format:

The first line of input contains t, the number of test cases.

The input of each test case is as follows:
          1. The first line contains an integer n, the number of elements in the list.
          2. Each of the next n lines contains a data element for a list node.


Constraints:
          1.   1<=n<=1000
          2.   1<=list[i]<=1000 where list[i] is the ith element in the list.
        
Sample Input

3
5
16
12
4
2
5
3
7
3
9
5
5
1
18
3
13
Sample Output

5
2
4
12
16
9
3
7
13
3
18
1
5
Explanation

There are three test cases. There are no blank lines between test case output.

The first linked list has 5 elements: 16--> 12--> 4-->2-->5 . Printing this in reverse order produces:
5
2
4
12
16

The second linked list has 3 elements:7-->3-->7=9-->NULL. Printing this in reverse order produces:
9
3
7
The third linked list has 5 elements:5-->1 -->18-->3-->13-->NULL. Printing this in reverse order produces:
13
3
18
1
5

# Complete the 'reversePrint' function below.
#
# The function accepts INTEGER_SINGLY_LINKED_LIST llist as parameter.
#

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
#Code:- python

def reversePrint(llist):
    # Write your code here
    if llist is None:
        return
    reversePrint(llist.next)
    print(llist.data)
    

if __name__ == '__main__':
    tests = int(input())
