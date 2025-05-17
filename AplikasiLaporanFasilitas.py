import tkinter as tk
from tkinter import ttk, messagebox

class LaporanKerusakanApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplikasi Manajemen Laporan Kerusakan Fasilitas Umum")

        # Frame input
        input_frame = ttk.Frame(root, padding=10)
        input_frame.pack(fill='x')

        # Lokasi
        ttk.Label(input_frame, text="Lokasi:").grid(row=0, column=0, sticky='w')
        self.lokasi_entry = ttk.Entry(input_frame)
        self.lokasi_entry.grid(row=0, column=1, sticky='ew')

        # Jenis Fasilitas
        ttk.Label(input_frame, text="Jenis Fasilitas:").grid(row=1, column=0, sticky='w')
        self.fasilitas_entry = ttk.Entry(input_frame)
        self.fasilitas_entry.grid(row=1, column=1, sticky='ew')

        # Deskripsi Kerusakan
        ttk.Label(input_frame, text="Deskripsi Kerusakan:").grid(row=2, column=0, sticky='w')
        self.deskripsi_entry = ttk.Entry(input_frame)
        self.deskripsi_entry.grid(row=2, column=1, sticky='ew')

        # Tombol tambah laporan
        self.add_button = ttk.Button(input_frame, text="Tambah Laporan", command=self.tambah_laporan)
        self.add_button.grid(row=3, column=0, columnspan=2, pady=5)

        input_frame.columnconfigure(1, weight=1)

        # Treeview untuk daftar laporan
        self.tree = ttk.Treeview(root, columns=('Lokasi', 'Fasilitas', 'Deskripsi', 'Status'), show='headings')
        self.tree.heading('Lokasi', text='Lokasi')
        self.tree.heading('Fasilitas', text='Jenis Fasilitas')
        self.tree.heading('Deskripsi', text='Deskripsi Kerusakan')
        self.tree.heading('Status', text='Status')
        self.tree.pack(fill='both', expand=True, padx=10, pady=10)

        # Tombol update status
        self.update_button = ttk.Button(root, text="Tandai Sudah Diperbaiki", command=self.update_status)
        self.update_button.pack(pady=5)

    def tambah_laporan(self):
        lokasi = self.lokasi_entry.get()
        fasilitas = self.fasilitas_entry.get()
        deskripsi = self.deskripsi_entry.get()

        if not lokasi or not fasilitas or not deskripsi:
            messagebox.showwarning("Input Tidak Lengkap", "Semua kolom harus diisi!")
            return

        self.tree.insert('', 'end', values=(lokasi, fasilitas, deskripsi, 'Belum Diperbaiki'))

        self.lokasi_entry.delete(0, tk.END)
        self.fasilitas_entry.delete(0, tk.END)
        self.deskripsi_entry.delete(0, tk.END)

    def update_status(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showinfo("Pilih Laporan", "Pilih laporan yang ingin diperbarui.")
            return

        for item in selected_item:
            values = self.tree.item(item, 'values')
            new_values = (values[0], values[1], values[2], 'Sudah Diperbaiki')
            self.tree.item(item, values=new_values)

if __name__ == "__main__":
    root = tk.Tk()
    app = LaporanKerusakanApp(root)
    root.mainloop()
