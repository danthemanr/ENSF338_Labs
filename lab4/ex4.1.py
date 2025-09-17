# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# def processdata(li):
#   for i in range(len(li)):
#     if li[i] > 5:
#       for j in range(len(li)):
#         li[i] *= 2
#
#1. The best case is that all elements are less than 5, meaning
#   that the inner for loop never runs; the best case complexity
#   is O(n) because there is one comparsion for every item in
#   the list.
#   The worst case is when all elements are greater than 5,
#   making the inner for loop always run; the worst case
#   complexity is O(n^2) because the inner for loop does n
#   operations and it is run n times.
#   The average case is when half of the elements are greater
#   than 5 so that the inner loop runs half the times; average
#   case complexity is O(n^2) because dividing n^2 by 2 is still
#   quadratic complexity.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
#2.
def processdata(li):
  for i in range(len(li)):
    if li[i] > 5:
      for j in range(len(li)):
        li[i] *= 2
    else:
      for j in range(len(li)):
        li[i] /= 2