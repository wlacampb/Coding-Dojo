a = [1, 2, 5, 10, 255, 3]
sum_list = 0
counter = 0

for items in a:
      sum_list += items
      counter += 1

average_list = sum_list / counter

print average_list

# prints average of list

b = [1, 2, 5, 10, 255, 3]

def average_list(arr): 
      sum_list = 0
      counter = 0
      
      for items in arr:
            sum_list += items
            counter += 1

      average_list = sum_list / counter

      print average_list

average_list([1, 2, 5, 10, 255, 3])

# finds average of list without global declarations