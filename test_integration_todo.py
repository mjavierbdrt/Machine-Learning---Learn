import unittest
from unittest.mock import patch
import io
import todo_list

class TestTodoListIntegration(unittest.TestCase):

    @patch('todo_list.clear_screen')
    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input')
    def test_full_flow_add_then_exit(self, mock_input, mock_stdout, mock_clear):
        """Integration test: Alur lengkap → tambah task lalu keluar"""
        # Urutan input yang akan diberikan program:
        # 1. Pilih menu 1 (tambah)
        # 2. Nama task
        # 3. Status task
        # 4. Tekan Enter setelah tambah
        # 5. Pilih menu 5 (keluar)
        mock_input.side_effect = ['1', 'Belajar Python', 'selesai', '', '5']

        # Jalankan seluruh program (main loop)
        todo_list.main()

        # Cek hasil akhir
        self.assertEqual(len(todo_list.tasks), 1)
        self.assertEqual(todo_list.tasks[0]['task'], 'Belajar Python')
        self.assertEqual(todo_list.tasks[0]['status'], 'selesai')

        output = mock_stdout.getvalue()
        self.assertIn('Selamat datang di Todo List CLI', output)
        self.assertIn('Terima kasih telah menggunakan', output)

if __name__ == '__main__':
    unittest.main(verbosity=2)