import json
import sys
from pathlib import Path


def load_tasks(path="tasks.json"):
    p = Path(path)
    if not p.exists():
        return []
    with open(p, "r", encoding="utf-8") as f:
        return json.load(f)


def save_tasks(tasks, path="tasks.json"):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(tasks, f, ensure_ascii=False, indent=2)


def add_task(title, tasks):
    if not title or not title.strip():
        raise ValueError("Название задачи не может быть пустым")
    task = {"title": title.strip(), "done": False}
    tasks.append(task)
    return task


def list_tasks(tasks):
    if not tasks:
        return "Задач нет"
    return "\n".join(
        f"[{'x' if t['done'] else ' '}] {t['title']}" for t in tasks
    )


def main():
    if len(sys.argv) < 2:
        print("Использование: python task_app.py <команда> [аргументы]")
        print("Команды: add <название>, list")
        return
    cmd = sys.argv[1]
    tasks = load_tasks()
    if cmd == "add" and len(sys.argv) >= 3:
        title = " ".join(sys.argv[2:])
        add_task(title, tasks)
        save_tasks(tasks)
        print(f"Добавлена задача: {title}")
    elif cmd == "list":
        print(list_tasks(tasks))
    else:
        print("Неизвестная команда")


if __name__ == "__main__":
    main()