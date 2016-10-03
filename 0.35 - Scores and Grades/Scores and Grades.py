import sys

def scores_and_grades():
      iterate_ten_times = 0
      grade_arr = []
      
      print ""
      while iterate_ten_times < 10:
            tmp = input("FEED ME GRADES: ")
            if 0 < tmp < 100: 
                  grade_arr.append(tmp)
                  iterate_ten_times += 1
            else: 
                  print "\nYeah, if you could give me a value between 0 - 100, that'd be great . . .\n"
                  sys.exit()
      print ""
      print "Scores and Grades"
      for item in grade_arr:
            if item < 60:
                  print "Score: " + str(item) + "; Your grade is F"
            elif 60 < item < 70:
                  print "Score: " + str(item) + "; Your grade is D"
            elif 70 < item < 80:
                  print "Score: " + str(item) + "; Your grade is C"
            elif 80 < item < 90:
                  print "Score: " + str(item) + "; Your grade is B"
            elif 90 < item < 101:
                  print "Score: " + str(item) + "; Your grade is A"
      print "End of the program. Bye!"
      print ""

scores_and_grades()