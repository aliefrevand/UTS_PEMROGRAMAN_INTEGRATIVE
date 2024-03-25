def perkalian_hingga(n):
  hasil = 1
  for i in range(1, n + 1):
    hasil *= i
  return hasil

tanggal_ujian = int(input("Masukkan tanggal ujian hari ini: "))
hasil_perkalian = perkalian_hingga(tanggal_ujian)

print(f"Hasil perkalian semua nilai dari 1 hingga {tanggal_ujian} adalah: {hasil_perkalian}")
