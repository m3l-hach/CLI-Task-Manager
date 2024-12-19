from datetime import datetime

todos = []

class Todo:
	def __init__(self, title, created_at, is_completed = False):
		self.title = title
		self.created_at = created_at
		self.is_completed = is_completed

def	print_all_todos():
	print("+----+----------------------------------------+--------------------+--------------------+")
	print("| ID |              Title                     |     created at     |       status       |")
	print("+----+----------------------------------------+--------------------+--------------------+")

	for i, todo in enumerate(todos):
		print(f"| {i + 1:2} |  {todo.title:36}  | {todo.created_at:^18} |{'✅' if todo.is_completed == True else '❌':^19}|")
	if 	len(todos) > 0:
		print("+----+----------------------------------------+--------------------+--------------------+")

def add_todo():
	todo = input("Enter you to todo: ")
	todos.append(Todo(todo,datetime.now().strftime("%m/%d, %H:%M")))

def del_todo():
	while True:
		try:
			id_to_del = int(input("Change status of: ")) - 1
			if id_to_del >= 0 and id_to_del < len(todos):
				del todos[id_to_del]
				break
			else:
				print("Invalid ID, try again: ")
		except ValueError:
				print("please enter a valid number.")

def change_status():
	while True:
		try:
			id = int(input("id for changing status: ")) - 1
			if id >= 0 and id < len(todos):
				if todos[id].is_completed == False:
					todos[id].is_completed = True
				else:
					todos[id].is_completed = False
				break
			else:
				print("Invalid ID, try again: ")
		except ValueError:
			print("please enter a valid number.")

while True:
	print_all_todos()
	choice = input("(A)dd, (D)el, (C)hange status, (Q)uit: ")
	if choice.lower() == 'a':
		add_todo()
	elif choice.lower() == 'd':
		del_todo()
	elif choice.lower() == 'c':
		change_status()
	elif choice.lower() == 'q':
		exit(0)
	else :
		print("Invalid option, try again.")	

