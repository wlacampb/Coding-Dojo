users = {
 'students': [ 
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Trey', 'last_name' : 'Villafane'}
  ]
 }

print ""
for key, data in users.items(): 
      print "%s" %key.title() #KEYS refers to students and instructors
      iterator = 0

      for value in data: #DATA refers to the keys and VALUE iterates over the values
            iterator += 1
            tmp_initial = value["first_name"] + " " + value["last_name"]
            tmp_final = tmp_initial.upper()
            name_length = len(value["first_name"]) + len(value["last_name"])
            print "%d - %s - %d" %(iterator, tmp_final, name_length) # %x where x refers to the type
print ""