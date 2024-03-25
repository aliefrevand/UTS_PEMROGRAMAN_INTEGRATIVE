import re

def baca_file(nama_file):
    """
    Membaca file teks dan mengembalikan daftar bilangan bulat.

    Args:
        nama_file (str): Nama file teks.

    Returns:
        list: Daftar bilangan bulat.
    """
    try:
        with open(nama_file, "r") as file:
            data = file.read()
    except FileNotFoundError:
        print(f"File '{nama_file}' tidak ditemukan.")
        return []
    bilangan = re.findall(r"\d+", data)
    return [int(x) for x in bilangan]

def format_ribuan(angka):
    """
    Memformat angka dengan pemisah ribuan.

    Args:
        angka (int): Angka yang akan diformat.

    Returns:
        str: Angka dengan pemisah ribuan.
    """
    return "{:,d}".format(angka)

nama_file = "input.txt"
bilangan = baca_file(nama_file)

if bilangan:
    jumlah_bilangan = sum(bilangan)
    print(f"Jumlah bilangan dalam file '{nama_file}' adalah: {format_ribuan(jumlah_bilangan)}")
else:
    print(f"File '{nama_file}' tidak memiliki bilangan bulat.")
