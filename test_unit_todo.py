import unittest
from unittest.mock import patch
import io
import todo_list  # import modul todo_list.py

class TestTodoListUnit(unittest.TestCase):

    def setUp(self):
        """Reset data sebelum setiap test dijalankan"""
        todo_list.tasks.clear()
        todo_list.next_id = 1

    # ==================== POSITIVE CASE ====================

    @patch('todo_list.clear_screen')
    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input')
    def test_add_task_positive(self, mock_input, mock_stdout, mock_clear):
        """Positive case: Tambah task berhasil"""
        mock_input.side_effect = ['Belajar Python', 'selesai', '']  # nama, status, tekan enter

        todo_list.add_task()

        self.assertEqual(len(todo_list.tasks), 1)
        self.assertEqual(todo_list.tasks[0]['task'], 'Belajar Python')
        self.assertEqual(todo_list.tasks[0]['status'], 'selesai')
        self.assertEqual(todo_list.tasks[0]['id'], 1)

        output = mock_stdout.getvalue()
        self.assertIn('✅ Task berhasil ditambahkan', output)

    @patch('todo_list.clear_screen')
    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input')
    def test_mark_task_positive(self, mock_input, mock_stdout, mock_clear):
        """Positive case: Menandai task berhasil"""
        # Siapkan 1 task dulu
        todo_list.tasks.append({'id': 1, 'task': 'Test Task', 'status': 'pending'})
        todo_list.next_id = 2

        mock_input.side_effect = ['1', '1', '']  # nomor task, pilihan 1=selesai, tekan enter

        todo_list.mark_task()

        self.assertEqual(todo_list.tasks[0]['status'], 'selesai')

    @patch('todo_list.clear_screen')
    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input')
    def test_delete_task_positive(self, mock_input, mock_stdout, mock_clear):
        """Positive case: Hapus task berhasil"""
        todo_list.tasks.append({'id': 1, 'task': 'Test Task', 'status': 'pending'})
        todo_list.next_id = 2

        mock_input.side_effect = ['1', 'y', '']  # nomor, konfirmasi y, tekan enter

        todo_list.delete_task()

        self.assertEqual(len(todo_list.tasks), 0)

    @patch('todo_list.clear_screen')
    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input')
    def test_edit_task_positive(self, mock_input, mock_stdout, mock_clear):
        """Positive case: Edit nama task berhasil"""
        todo_list.tasks.append({'id': 1, 'task': 'Old Task', 'status': 'pending'})
        todo_list.next_id = 2

        mock_input.side_effect = ['1', 'New Task Name', '']  # nomor, nama baru, tekan enter

        todo_list.edit_task()

        self.assertEqual(todo_list.tasks[0]['task'], 'New Task Name')

    @patch('todo_list.clear_screen')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_table_positive(self, mock_stdout, mock_clear):
        """Positive case: Tampilan tabel muncul dengan benar"""
        todo_list.tasks.append({'id': 1, 'task': 'Test Task', 'status': 'pending'})

        todo_list.print_table()

        output = mock_stdout.getvalue()
        self.assertIn('+-----+----------------', output)      # header tabel
        self.assertIn('|   1 | Test Task', output)           # isi baris
        self.assertIn('pending', output)

if __name__ == '__main__':
    unittest.main(verbosity=2)