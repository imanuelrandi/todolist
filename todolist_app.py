import json
import os
from datetime import datetime

class TodoApp:
    def __init__(self, filename='todos.json'):
        self.filename = filename
        self.todos = []
        self.load_todos()

    def load_todos(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                self.todos = json.load(f)

    def save_todos(self):
        with open(self.filename, 'w') as f:
            json.dump(self.todos, f, indent=4)

    def add_task(self, nama, deadline, mata_pelajaran):
        task = {
            'nama': nama,
            'deadline': deadline,
            'mata_pelajaran': mata_pelajaran
        }
        self.todos.append(task)
        self.save_todos()
        print("Tugas berhasil ditambahkan!")

    def remove_task(self, nama):
        for task in self.todos:
            if task['nama'] == nama:
                self.todos.remove(task)
                self.save_todos()
                print("Tugas berhasil dihapus!")
                return
        print("Tugas tidak ditemukan!")

    def display_tasks(self):
        if not self.todos:
            print("Tidak ada tugas.")
            return
        print("Daftar Tugas:")
        for i, task in enumerate(self.todos, 1):
            print(f"{i}. Nama: {task['nama']}, Deadline: {task['deadline']}, Mata Pelajaran: {task['mata_pelajaran']}")

def main():
    app = TodoApp()
    while True:
        print("\nMenu:")
        print("1. Tambah Tugas")
        print("2. Hapus Tugas")
        print("3. Tampilkan Tugas")
        print("4. Keluar")
        choice = input("Pilih opsi: ")
        if choice == '1':
            nama = input("Nama tugas: ")
            deadline = input("Deadline (YYYY-MM-DD): ")
            mata_pelajaran = input("Mata pelajaran: ")
            app.add_task(nama, deadline, mata_pelajaran)
        elif choice == '2':
            nama = input("Nama tugas yang akan dihapus: ")
            app.remove_task(nama)
        elif choice == '3':
            app.display_tasks()
        elif choice == '4':
            break
        else:
            print("Opsi tidak valid!")

if __name__ == "__main__":
    main()
