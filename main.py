from datetime import datetime

todos = []

class Todo:
	def __init__(self, title, created_at, is_completed = False):
		self.title = title
		self.created_at = created_at
		self.is_completed = is_completed

def	print_all_todos():
	print("+----+----------------------------------------+--------------------+--------------------+")
	print("| ID |              Title                     |     created at     |      completed     |")
	print("+----+----------------------------------------+--------------------+--------------------+")

	for i, todo in enumerate(todos):
		print(f"| {i + 1:2} |  {todo.title:36}  | {todo.created_at:^18} |{'✅' if todo.is_completed == True else '❌':^19}|")
	if 	len(todos) > 0:
		print("+----+----------------------------------------+--------------------+--------------------+")

def add_todo():
	todo = input("Enter you to todo: ")
	todos.append(Todo(todo,datetime.now().strftime("%m/%d, %H:%M")))

def del_todo():
	id_to_del = input("id of the todo to remove: ")
	id_to_del = int(id_to_del) - 1
	del todos[id_to_del]

def mark_as_complete():
	id_completed = input("id of the todo to mark as completed: ")
	id_completed = int(id_completed) - 1
	todos[id_completed].is_completed = True

while True:
	print_all_todos()
	choice = input("(A)dd, (D)el, (C)ompleted, (Q)uit: ")
	if choice.lower() == 'a':
		add_todo()
	elif choice.lower() == 'd':
		del_todo()
	elif choice.lower() == 'c':
		mark_as_complete()
	elif choice.lower() == 'q':
		exit(0)
	else :
		print("invalid option, try again")	

