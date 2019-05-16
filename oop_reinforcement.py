class Task:

  def __init__(self, description, due_date):
    self.description = description
    self.due_date = due_date

  def __str__(self):
    return f"{self.description} - Due: {self.due_date}"

laundry = Task("Do the week's laundry", "2019-04-15")
groceries = Task("Go grocery shopping", "2019-05-16")
sweep = Task("Sweep daddio.", "2020-07-18")

class TodoList:

  def __init__(self, name):
    self.name = name
    self.tasks = []

  def add_task(self, task):
    self.tasks.append(task)

  def print_list(self):
    print("Tasks:")
    for task in self.tasks:
      print(task)

my_todo_list = TodoList("My ToDo List")

my_todo_list.add_task(laundry)
my_todo_list.add_task(groceries)
my_todo_list.add_task(sweep)

my_todo_list.print_list()
