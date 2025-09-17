1. The for loop happens n times and most of the operations in it have constant complexity; the exception to this is the call to get_element_at_pos(), which likely has an internal for loop that runs n-i times, until it gets to the desired element. over the entire course of the outer for loop, the loop in get_element_at_pos() would run a number of times equal to the following sum:  
&emsp;$\sum_{i=1}^{n}n-i=$  
&emsp;$n^2-\sum_{i=1}^{n}i=$  
&emsp;$n^2-n(n+1)/2=$  
&emsp;$0.5n^2-0.5n$  
Thus, the reverse() method has quadratic complexity.

2. A better version of this method would go along the list and reverse the direction of all of the pointers so that it would only have to iterate through the list once. Not only does this avoid a nested for loop (and consequently quadratic complexity), but it also avoids reallocating memory because the nodes stay where they are.