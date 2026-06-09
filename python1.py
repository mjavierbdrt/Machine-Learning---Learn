import os

# Data task disimpan di memory (list of dictionary)
tasks = []
next_id = 1

def clear_screen():
    """Membersihkan layar terminal (cross-platform)"""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_table():
    """Menampilkan tabel task dengan format yang rapi"""
    clear_screen()
    print("=== TODO LIST CLI ===")
    if not tasks:
        print("Belum ada task. Silakan tambahkan task baru.\n")
        return
    
    # Header tabel
    print("+-----+--------------------------------+----------------+")
    print("| No  | Task                           | Status         |")
    print("+-----+--------------------------------+----------------+")
    
    # Isi tabel
    for task in tasks:
        # Potong task name jika terlalu panjang agar tabel tetap rapi
        task_name = task['task'][:30] + "..." if len(task['task']) > 30 else task['task']
        print(f"| {task['id']:3d} | {task_name:<30} | {task['status']:<14} |")
    
    print("+-----+--------------------------------+----------------+")
    print()

def add_task():
    """Menambah task baru (nama + status)"""
    global next_id
    print("--- Tambah Task Baru ---")
    nama = input("Masukkan nama task: ").strip()
    if not nama:
        print("❌ Nama task tidak boleh kosong!")
        input("\nTekan Enter untuk kembali...")
        return
    
    status = input("Masukkan status task (kosong = pending): ").strip()
    if not status:
        status = "pending"
    
    tasks.append({
        'id': next_id,
        'task': nama,
        'status': status
    })
    next_id += 1
    print(f"✅ Task berhasil ditambahkan dengan nomor {next_id-1}")
    input("\nTekan Enter untuk kembali...")

def mark_task():
    """Menandai task (selesai / ditunda / dibatalkan)"""
    if not tasks:
        print("❌ Tidak ada task untuk ditandai.")
        input("\nTekan Enter untuk kembali...")
        return
    
    print("--- Menandai Task ---")
    try:
        nomor = int(input("Masukkan nomor task yang ingin ditandai: "))
        task = next((t for t in tasks if t['id'] == nomor), None)
        
        if not task:
            print("❌ Nomor task tidak ditemukan!")
            input("\nTekan Enter untuk kembali...")
            return
        
        print("\nPilih status baru:")
        print("1. Selesai")
        print("2. Ditunda")
        print("3. Dibatalkan")
        pilihan = input("Masukkan pilihan (1/2/3): ").strip()
        
        if pilihan == "1":
            task['status'] = "selesai"
        elif pilihan == "2":
            task['status'] = "ditunda"
        elif pilihan == "3":
            task['status'] = "dibatalkan"
        else:
            print("❌ Pilihan tidak valid!")
            input("\nTekan Enter untuk kembali...")
            return
        
        print(f"✅ Task nomor {nomor} berhasil ditandai sebagai '{task['status']}'")
        input("\nTekan Enter untuk kembali...")
        
    except ValueError:
        print("❌ Masukkan nomor yang valid!")
        input("\nTekan Enter untuk kembali...")

def delete_task():
    """Menghapus task berdasarkan nomor"""
    if not tasks:
        print("❌ Tidak ada task untuk dihapus.")
        input("\nTekan Enter untuk kembali...")
        return
    
    print("--- Hapus Task ---")
    try:
        nomor = int(input("Masukkan nomor task yang ingin dihapus: "))
        index = next((i for i, t in enumerate(tasks) if t['id'] == nomor), None)
        
        if index is None:
            print("❌ Nomor task tidak ditemukan!")
            input("\nTekan Enter untuk kembali...")
            return
        
        konfirmasi = input(f"Apakah yakin menghapus task '{tasks[index]['task']}'? (y/n): ").strip().lower()
        if konfirmasi == 'y':
            del tasks[index]
            print(f"✅ Task nomor {nomor} berhasil dihapus.")
        else:
            print("❌ Penghapusan dibatalkan.")
        input("\nTekan Enter untuk kembali...")
        
    except ValueError:
        print("❌ Masukkan nomor yang valid!")
        input("\nTekan Enter untuk kembali...")

def edit_task():
    """Mengedit nama task (status tidak diubah)"""
    if not tasks:
        print("❌ Tidak ada task untuk diedit.")
        input("\nTekan Enter untuk kembali...")
        return
    
    print("--- Edit Task ---")
    try:
        nomor = int(input("Masukkan nomor task yang ingin diedit: "))
        task = next((t for t in tasks if t['id'] == nomor), None)
        
        if not task:
            print("❌ Nomor task tidak ditemukan!")
            input("\nTekan Enter untuk kembali...")
            return
        
        print(f"Nama task saat ini: {task['task']}")
        nama_baru = input("Masukkan nama task baru: ").strip()
        
        if not nama_baru:
            print("❌ Nama task tidak boleh kosong, edit dibatalkan.")
            input("\nTekan Enter untuk kembali...")
            return
        
        task['task'] = nama_baru
        print(f"✅ Task nomor {nomor} berhasil diedit.")
        input("\nTekan Enter untuk kembali...")
        
    except ValueError:
        print("❌ Masukkan nomor yang valid!")
        input("\nTekan Enter untuk kembali...")

def show_menu():
    """Menampilkan menu sesuai kondisi (kosong atau ada task)"""
    print("Perintah yang tersedia:")
    print("1. Tambah task")
    if tasks:
        print("2. Menandai task")
        print("3. Menghapus task")
        print("4. Mengedit task")
    print("5. Keluar")
    print("-" * 40)

def main():
    global next_id
    next_id = 1
    tasks.clear()
    
    print("Selamat datang di Todo List CLI!")
    print("Data hanya disimpan selama program berjalan.\n")
    
    while True:
        print_table()
        show_menu()
        
        pilihan = input("Masukkan nomor perintah: ").strip()
        
        if pilihan == "1":
            add_task()
        elif pilihan == "2" and tasks:
            mark_task()
        elif pilihan == "3" and tasks:
            delete_task()
        elif pilihan == "4" and tasks:
            edit_task()
        elif pilihan == "5":
            print("Terima kasih telah menggunakan Todo List CLI! 👋")
            break
        else:
            print("❌ Pilihan tidak valid atau menu belum tersedia.")
            input("\nTekan Enter untuk kembali...")

if __name__ == "__main__":
    main()