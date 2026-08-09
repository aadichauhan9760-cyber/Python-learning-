import json
import os


FILE_NAME = "tasks.json"


def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []

    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        return []


def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)


def show_tasks(tasks):
    print("\n" + "=" * 50)
    print("                 YOUR TASKS")
    print("=" * 50)

    if not tasks:
        print("No tasks found.")
        return

    for task in tasks:
        status = "✅" if task["completed"] else "⬜"
        print(f"{task['id']}. {status} {task['title']}")

    print("=" * 50)


def add_task(tasks):
    print("\n--- Add Task ---")

    title = input("Enter task: ").strip()

    if not title:
        print("❌ Task cannot be empty.")
        return

    new_id = max([task["id"] for task in tasks], default=0) + 1

    task = {
        "id": new_id,
        "title": title,
        "completed": False
    }

    tasks.append(task)
    save_tasks(tasks)

    print("✅ Task added successfully!")


def complete_task(tasks):
    show_tasks(tasks)

    if not tasks:
        return

    try:
        task_id = int(input("Enter task ID to complete: "))

        for task in tasks:
            if task["id"] == task_id:
                if task["completed"]:
                    print("ℹ️ Task is already completed.")
                else:
                    task["completed"] = True
                    save_tasks(tasks)
                    print("✅ Task completed!")
                return

        print("❌ Task ID not found.")

    except ValueError:
        print("❌ Please enter a valid task ID.")


def delete_task(tasks):
    show_tasks(tasks)

    if not tasks:
        return

    try:
        task_id = int(input("Enter task ID to delete: "))

        for task in tasks:
            if task["id"] == task_id:
                tasks.remove(task)
                save_tasks(tasks)
                print("🗑️ Task deleted successfully!")
                return

        print("❌ Task ID not found.")

    except ValueError:
        print("❌ Please enter a valid task ID.")


def main():
    tasks = load_tasks()

    while True:
        print("\n" + "=" * 50)
        print("                  TO-DO LIST")
        print("=" * 50)
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")
        print("=" * 50)

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_task(tasks)

        elif choice == "2":
            show_tasks(tasks)

        elif choice == "3":
            complete_task(tasks)

        elif choice == "4":
            delete_task(tasks)

        elif choice == "5":
            print("\n👋 Thanks for using To-Do List!")
            break

        else:
            print("❌ Invalid choice. Please select 1-5.")


if __name__ == "__main__":
    main()
