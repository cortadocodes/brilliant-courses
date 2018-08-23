## Data types

List/array
* Good for access
* O(1) access time
* O(n) insertion time

Linked list 
* Good for insertion/deletion
* Defined by a set of nodes with a `.next` attribute (a pointer to the next note) and a `.data` attribute (the value 
of the linked list at this point)
* Doubly-linked lists also have a `.previous` attribute (a pointer to the previous node)
* Linked lists take up more memory as they have to store a pointer to the next/previous elements
* O(n) access time
* O(1) insertion/deletion time

Stack
* Good for keeping an "undo list" and reversing elements
* Implements a "last in, first out" data type
* Two definied operations:
    * `.push` puts an element on top of the stack
    * `.pop` ejects and returns the element at the top of the stack
    * `.peek` returns the value of the top element without popping it
* Stack overflow - trying to push something on to a full stack
* Stack underflow - trying to pop something from an empty stack
