Exercise 6
1. Compare advantages and disadvantages of arrays vs linked list
(complexity of task completion) 
    * **Access:**  
        Linked Lists allow only sequential access to elements, meaning traversal is required to find an element (O(n) complexity).  
        Arrays support random access, allowing elements to be accessed directly using an index(O(1)complexity).  
    **Advantage:**
        Arrays offer fast element lookup due to direct indexing while Linked lists are slow for element access since each node must be visited sequentially.
    * **Size Management:**  
        Linked Lists are dynamic in nature, meaning they can grow and shrink as needed without requiring preallocation of memory.  
        Arrays have a fixed size that must be declared during initialization, making resizing difficult.  
    **Advantage:**
        Linked lists are flexible and do not require resizing while Arrays have a size constraint and may run out of space or require expensive resizing
    * **Insertion & Deletion**:  
        Linked Lists allow fast insertion and deletion at any position. No shifting of elements is needed, making it O(1) for head operations and O(n) for arbitrary positions.  
        Arrays require shifting elements during insertion/deletion, making these operations O(n) in the worst case. Additionally, memory reallocation may fail due to fragmentation.  
    **Advantage:**
        Linked lists allow efficient insertion and deletion at any point while Arrays require shifting of elements, making insertion/deletion slower.
    * **Complexity of Implementation:**  
        Arrays are simpler to implement, manage, and use in most programming languages.  
        Linked Lists require complex pointer handling, making them harder to code and debug.  
    **Advantage:**
        Arrays are easier to code and use while Linked lists require complex memory management and pointer operations.
    * **Storage:**  
        Linked Lists require additional memory for pointers, as each node stores a reference to the next node. This makes them inefficient for small data types like characters or boolean values.  
        Arrays store only data without extra pointers, making them more space-efficient.  
    **Advantage:**
        Arrays have lower memory overhead since no extra space is used for references while Linked lists consume more memory per element due to extra storage for pointers.

2. For arrays, we are interested in implementing a replace function
that acts as a deletion followed by insertion. How can this function
be implemented to minimize the impact of each of the standalone
tasks?
    >Instead of deleting and shifting elements, we can directly replace an element at an index. If a shift is needed, perform block operations to reduce individual shifts. Optimized Approach: Use a buffered swap or circular buffer to minimize reallocation costs.

3. Assuming you are tasked to implement a doubly linked list with a
sort function, given the list of sort functions below, state the
feasibility of using each one of them and elaborate why is it
possible or not to use them. 
    1. **Insertion sort:**  
        Possible and works well for small doubly linked lists or nearly sorted data.  
    **Why it is possible:**
        >Since doubly linked lists allow bi-directional traversal, insertion sort can efficiently find the correct position for each element.No need for shifting elements like in arrays, only pointer adjustments.
        Complexity: 
    2. **Merge sort:**  
        It is Highly efficient and the preferred sorting method for large doubly linked lists.
        Can be implemented using a divide-and-conquer approach, which suits linked lists well.  
    **Why it is possible:**
        >Merge sort is feasible for a doubly linked list because it works efficiently with sequential access and avoids shifting elements. Instead of copying data, it rearranges pointers during splitting and merging, making it memory-efficient. With O(n log n) complexity, it is well-suited for sorting large linked lists.

4. Also show the expected complexity for each and how it differs from
applying it to a regular array.
    1. **Insertion sort:**  
    Insertion sort has a time complexity of O(n²) for both doubly linked lists and arrays. However, in arrays, insertion requires shifting elements, which increases overhead, while in doubly linked lists, insertion is done by adjusting pointers, making it slightly more efficient.
    2. **Merge sort:**  
    Merge sort has a time complexity of O(n log n) in both doubly linked lists and arrays. In arrays, merging requires additional memory for temporary storage, whereas in doubly linked lists, merging can be done in place by modifying pointers, making it more memory-efficient.
