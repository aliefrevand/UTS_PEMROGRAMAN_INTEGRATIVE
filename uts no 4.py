class BMI:
    def __init__(self, weight, height):
        self.weight = weight  # Berat badan dalam kilogram
        self.height = height  # Tinggi badan dalam meter

    def BMI_Value(self):
        # Menghitung nilai BMI
        bmi = self.weight / (self.height ** 2)
        return bmi

    def __eq__(self, other):
        # Membandingkan berat dan tinggi dari dua objek BMI
        return self.weight == other.weight and self.height == other.height

# Contoh penggunaan:
if __name__ == "__main__":
    # Membuat objek BMI
    person1 = BMI(75, 1.75)  # Berat: 75 kg, Tinggi: 1.75 m
    person2 = BMI(80, 1.79)  # Berat: 80 kg, Tinggi: 1.79 m

 # Menggunakan method BMI_Value untuk mendapatkan nilai BMI
    print("Nilai BMI person1:", person1.BMI_Value())
    print("Nilai BMI person2:", person2.BMI_Value())

    # Membandingkan dua objek BMI
    if person1 == person2:
        print("person1 memiliki BMI yang sama dengan person2")
    else:
        print("person1 tidak memiliki BMI yang sama dengan person2")
