import random
import csv

nama_file = "place.csv"
output_file = "place_visited.csv"

with open(output_file, mode="w", newline="") as output:
    csv_writer = csv.writer(output)
    csv_writer.writerow(["user_id", "place_id", "location", "rating"])

    total_user = 4032

    for iteration in range(total_user):
        with open(nama_file, mode="r") as file:
            csv_reader = list(csv.reader(file))

            random.shuffle(csv_reader)

            bali = 0
            batam = 0
            jakarta = 0
            lombok = 0
            medan = 0
            padang = 0
            yogyakarta = 0

            max_per_kota = 4

            for row in csv_reader:
                if all(
                    [
                        bali == max_per_kota,
                        batam == max_per_kota,
                        jakarta == max_per_kota,
                        lombok == max_per_kota,
                        medan == max_per_kota,
                        padang == max_per_kota,
                        yogyakarta == max_per_kota,
                    ]
                ):
                    break

                randomNumber = random.randint(0, 218)
                rating = random.randint(3, 5)

                if row[4] == "bali" and bali < max_per_kota:
                    csv_writer.writerow([iteration + 1, row[0], row[4], rating])
                    bali += 1
                elif row[4] == "batam" and batam < max_per_kota:
                    csv_writer.writerow([iteration + 1, row[0], row[4], rating])
                    batam += 1
                elif row[4] == "jakarta" and jakarta < max_per_kota:
                    csv_writer.writerow([iteration + 1, row[0], row[4], rating])
                    jakarta += 1
                elif row[4] == "lombok" and lombok < max_per_kota:
                    csv_writer.writerow([iteration + 1, row[0], row[4], rating])
                    lombok += 1
                elif row[4] == "medan" and medan < max_per_kota:
                    csv_writer.writerow([iteration + 1, row[0], row[4], rating])
                    medan += 1
                elif row[4] == "padang" and padang < max_per_kota:
                    csv_writer.writerow([iteration + 1, row[0], row[4], rating])
                    padang += 1
                elif row[4] == "yogyakarta" and yogyakarta < max_per_kota:
                    csv_writer.writerow([iteration + 1, row[0], row[4], rating])
                    yogyakarta += 1
