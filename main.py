import csv
import random

nama_file = "./dataset/dest_id.csv"

with open(nama_file, mode="r") as file:
    csv_reader = csv.DictReader(file)
    headers = csv_reader.fieldnames

    arrNumber = []

    for i, row in enumerate(csv_reader):
        if i < 150:
            arrNumber.append(int(row["id"]))
        else:
            break


output_file = "user_rating.csv"

with open(output_file, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["user_id", "place_id", "rating"])

    i = 1

    while i <= 400:
        j = 1
        while j <= 30:
            user_id = i
            randomNum = int(random.random() * 150)
            place_id = arrNumber[randomNum]
            rating = random.randint(3, 5)
            writer.writerow([user_id, place_id, rating])
            j += 1
        i += 1
