class TaskList:

  def __init__(self, List, count):
    self.List = []
    self.count = 0
    
    def makeList(self):
      self.List = input('What is your list labelled?')
      tasks = input('Type a list of your tasks, separated by commas')
      self.List = tasks.split(',')
      self.count = len(self.List)
    
    def addTask(self):
      self.List.append(input('What is your task called?'))
      self.count = len(self.List)