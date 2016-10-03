import sys

def draw_stars():
      iterator_one = 0
      arr = []
      
      print ""

      print "CONSTELLATION #"
      number_of_constellations = input("# of constellations: ")
      print ""

      print "STAR #"
      while iterator_one < number_of_constellations:
            tmp = raw_input("things in constellation #" + str(int(iterator_one + 1)) + ": ")
            arr.append(tmp)
            iterator_one += 1
      print ""

      print "INPUT"
      print arr
      print ""
      
      print "INITIAL TYPE"
      for item in arr:
            print type(item)
      print ""
      
      iterator_two = 1
      
      print "TARGET TYPE"
      for item in arr:
            if item.isalpha():
                  print "Constellation #" + str(iterator_two) + " is alpha."
                  iterator_two += 1
            elif item.isdigit():
                  print "Constellation #" + str(iterator_two) + " is digit."
                  iterator_two += 1
      print ""
      
      print "HERE BE DRAGONS"
      for item in arr:
            tmp_arr = []
            if item.isalpha():
                  tmp = len(item) # tmp stores length of str
                  while tmp > 0:
                        tmp_arr.append(item[0])
                        tmp -= 1
            elif item.isdigit():
                  tmp = int(item) # tmp stores numeric inputs converted into ints
                  while tmp > 0:
                        tmp_arr.append("*")
                        tmp -= 1
            print "".join(tmp_arr)
      print ""

draw_stars()