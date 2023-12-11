import json

class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description):
        task = {'title': title, 'description': description, 'status': 'Not started'}
        self.tasks.append(task)
        print(f'Task "{title}" added to the to-do list.')

    def list_tasks(self):
        if not self.tasks:
            print('No tasks in the to-do list.')
        else:
            for index, task in enumerate(self.tasks, start=1):
                print(f'{index}. [{task["status"]}] {task["title"]} - {task["description"]}')

    def update_task_status(self, task_index, status):
        if 1 <= task_index <= len(self.tasks):
            self.tasks[task_index - 1]['status'] = status
            print(f'Task status updated for task {task_index}.')
        else:
            print('Invalid task index.')

    def remove_task(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            removed_task = self.tasks.pop(task_index - 1)
            print(f'Task "{removed_task["title"]}" removed from the to-do list.')
        else:
            print('Invalid task index.')

    def save_to_file(self, filename='todo.json'):
        with open(filename, 'w') as file:
            json.dump(self.tasks, file)
        print(f'To-do list saved to {filename}.')

    def load_from_file(self, filename='todo.json'):
        try:
            with open(filename, 'r') as file:
                self.tasks = json.load(file)
            print(f'To-do list loaded from {filename}.')
        except FileNotFoundError:
            print(f'File {filename} not found. Starting with an empty to-do list.')

def main():
    todo_list = TodoList()
    todo_list.load_from_file()

    while True:
        print("\n=== To-Do List ===")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Update Task Status")
        print("4. Remove Task")
        print("5. Save and Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            todo_list.add_task(title, description)
        elif choice == '2':
            todo_list.list_tasks()
        elif choice == '3':
            todo_list.list_tasks()
            task_index = int(input("Enter the index of the task to update: "))
            status = input("Enter the new status: ")
            todo_list.update_task_status(task_index, status)
        elif choice == '4':
            todo_list.list_tasks()
            task_index = int(input("Enter the index of the task to remove: "))
            todo_list.remove_task(task_index)
        elif choice == '5':
            todo_list.save_to_file()
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()

