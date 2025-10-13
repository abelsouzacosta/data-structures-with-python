"""
This method performs a binary search in the following manner:
- It takes the element at the middle of the array.
- If this element is higher than the target, it discards the second half
  by setting the new last element to the one just before the middle.
- If this element is lower than the target, it discards the first half
  by setting the new first element to the one just after the middle.
- It repeats this process until the target is found or the range becomes empty.

Time complexity: O(log n)
Space complexity: O(1) - constant space, since no new space will be allocated
"""
