class Task:

   def __init__(self,name, due, priority):
     self.name = name
     self.due = due
     self.priority = priority
     
     def makeTask(self):
      self.name = str(input('What is your task called?'))
      self.due = str((input('When is it due?')))
      self.priority = int(input('What is the priority?(1,2,3)'))
      if str(input('Ok, your task is called'+ self.name + 'and due on ' + self.due + 'and is priority number ' + str(self.priority) + 'Is this information all correct?(Y/N)')) == 'Y':
        print('Ok! Your task has been created! Type *list* to view a list of your tasks.')
      else:
        print('Ok, please try again.')