def odd_even(value, maxima):
      while value < maxima:
            if value % 2 == 0:
                  print "Number is " + str(value) + "," + "\tThis is an even number."
            elif value % 2 == 1:
                  print "Number is " + str(value) + "," + "\tThis is an odd number."
            value += 1

odd_even(1, 2000)