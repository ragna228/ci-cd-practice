import unittest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from task_app import add_task, list_tasks


class TestTaskApp(unittest.TestCase):
    def test_add_task_returns_dict(self):
        tasks = []
        result = add_task("Тест", tasks)
        self.assertIsInstance(result, dict)

    def test_add_task_sets_title(self):
        tasks = []
        result = add_task("Купить хлеб", tasks)
        self.assertEqual(result["title"], "Купить хлеб")

    def test_add_task_sets_done_false(self):
        tasks = []
        result = add_task("Уборка", tasks)
        self.assertFalse(result["done"])

    def test_add_task_appends_to_list(self):
        tasks = []
        add_task("Задача 1", tasks)
        self.assertEqual(len(tasks), 1)

    def test_blank_title_is_rejected(self):
        tasks = []
        with self.assertRaises(ValueError):
            add_task("", tasks)

    def test_whitespace_only_title_is_rejected(self):
        tasks = []
        with self.assertRaises(ValueError):
            add_task("   ", tasks)

    def test_list_tasks_empty(self):
        self.assertEqual(list_tasks([]), "Задач нет")

    def test_list_tasks_shows_done_mark(self):
        tasks = [{"title": "A", "done": True}]
        self.assertIn("[x]", list_tasks(tasks))

    def test_list_tasks_shows_undone_mark(self):
        tasks = [{"title": "B", "done": False}]
        self.assertIn("[ ]", list_tasks(tasks))

    def test_title_is_stripped(self):
        tasks = []
        result = add_task("  Тест  ", tasks)
        self.assertEqual(result["title"], "Тест")

    def test_multiple_tasks_added(self):
        tasks = []
        add_task("A", tasks)
        add_task("B", tasks)
        add_task("C", tasks)
        self.assertEqual(len(tasks), 3)


if __name__ == "__main__":
    unittest.main()