from SingleTask import Task
from TaskList import TaskList
from Dailies import Daily

SingleTask = []
TaskLists = []
Dailies = []
user = input('Welcome to Task Manager! Would you like a tutorial(Y/N)')
tutorial = False

def main():
  user = input('Ok! What would you like to do?')
  if user == 'task':
    user = input('Ok! What would you like to do with the task(type create to create and view to view)')
    if user == 'create':
      name = input('What is your task called?')
      due = input('When is your task due?')
      priority = input('What is the priority of your task?(1,2,3)')
      newTask = Task(name , due, priority)
      SingleTask.append(newTask)
      user = input('Ok! Your task is made! Continue using the app')
    elif user == 'view':
     print(SingleTask)
     user = input('Ok! Continue using the app')
  elif user == 'list':
    user = input('Ok! What would you like to do with the list(type create to create and view to view)')
    if user == 'create':
      tasks = input('Type a list of your tasks, separated by commas')
      List = [tasks.split(',')]
      count = len(List)
      newList = TaskList(List, count)
      TaskLists.append(newList)
      user = input('Ok! Your list is made! Continue using the app')
    elif user == 'view':
      print(TaskLists)
      user = input('Ok! Continue using the app')
  elif user == 'daily':
    user = input('Ok! What would you like to do with the daily(type create to create and view to view)')
    if user == 'create':
      title = input('What is the name of your daily?')
      freq = input('How often do you want to do this daily?')
      newDaily = Daily(title, freq)
      Dailies.append(newDaily)
      user = input('Ok! Your daily is made! Continue using the app')
    elif user == 'view':
      print(Dailies)
      user = input('Ok! Continue using the app')
      
def start():
  global user
  if user == 'Y':
    tutorial = True
    user == input('Ok! Please press enter.')
    while tutorial == True:
      user = input('Ok! Task lists are lists of related tasks. To work with a list, type list. You will get instructions from there to add to, create, or view a list. Tasks are things you need to get done. To work with a task, type task. You will get instructions from there to add to, create, or view a task. Dailies are things you need to do every day. To work with a daily, type daily. You are now ready to use the app!')
      tutorial = False
    main()
      
while True:
  start()
