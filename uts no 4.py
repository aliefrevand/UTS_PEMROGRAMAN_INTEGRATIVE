class orang:
    def __init__(self, nama, tinggi_cm, berat_kg):
        self.nama = nama
        self.tinggi_cm = tinggi_cm
        self.berat_kg = berat_kg

    def hitung_bmi(self):
        tinggi_m = self.tinggi_cm / 100
        bmi = self.berat_kg / (tinggi_m ** 2)
        return bmi

    def __str__(self):
        return f"Nama: {self.nama}\nTinggi: {self.tinggi_cm} cm\nBerat: {self.berat_kg} kg"

def main():
    # Membuat objek Person
    orang1 = orang("Alief", 172, 60)

    # Menampilkan informasi tentang orang pertama
    print("Informasi tentang orang pertama:")
    print(orang1)

    # Menghitung dan menampilkan BMI (Body Mass Index) dari orang pertama
    bmi = orang1.hitung_bmi()
    print(f"\nBMI (Body Mass Index): {bmi:.2f}")

if __name__ == "__main__":
    main()
