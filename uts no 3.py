from datetime import datetime, timedelta

# Mencari hari ini
today = datetime.today()

# Mendapatkan jumlah Hari dari pengguna
days_to_add = int(input("Enter the number of days: "))

# Menghitung tanggal masa depan dengan menambahkan hari
future_date = today + timedelta(days=days_to_add)

# Format  date string 
formatted_date = future_date.strftime("%A on %d %B %Y")

# Print the formatted date
print(f"The date {days_to_add} days from now is: {formatted_date}")
