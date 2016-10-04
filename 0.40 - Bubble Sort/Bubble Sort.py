def bubbleSort(arr):
      print ""
      print "UNSORTED LIST"
      print arr
      print ""

      # RANGE is a GENERATOR, which means it GENERATES a NEW LIST
      for passthrough in range(len(arr) - 1):  # iterates i from 0 to 3 via a NEW LIST || range(len(arr)) ensures the algorithm passes through enough times, i.e. i, to sort the list, which you can confirm if you want manually by, well, executing the code in your head to find out the time complexity of the sort is at worst, which are current arr is, n^2 and with the iterator iterating through another iterator (0 - 4, 3, 2, 1; 1 - 4, 3, 2, 1; 2 - 4, 3, 2, 1; and so on), this constitutes n^2 comparisons
            for index in range(len(arr) - 1, 0, -1):  # iterates k from 4 to 1 via a NEW LIST || len(arr) - 1 ensures that since the list ends at 1 [index - 1] in the subsequent lines compares to the [0]-th index instead of the [-1]-th index, which is out-of-range and thus -- presumably -- would make everything grind to a halt and catch fire
                  if (arr[index] < arr[index - 1]):
                        swap(arr, index, index - 1)

      print "SORTED LIST"
      print arr
      print ""

def swap(arr, x, y):
      tmp = arr[x]
      arr[x] = arr[y]
      arr[y] = tmp

bubbleSort([5,4,3,2,1])
