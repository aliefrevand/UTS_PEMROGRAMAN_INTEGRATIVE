import re

def baca_file(nama_file):
  with open(nama_file, "r") as file:
    data = file.read()
  bilangan = re.findall(r"\d+", data)
  return [int(x) for x in bilangan]

def format_ribuan(angka):
  return "{:,d}".format(angka)

nama_file = "D:/input.txt"
bilangan = baca_file(nama_file)
jumlah_bilangan = sum(bilangan)

print(f"Jumlah bilangan dalam file {nama_file} adalah: {format_ribuan(jumlah_bilangan)}")
