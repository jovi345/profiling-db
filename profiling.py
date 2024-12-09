import csv
import random

mbti_types = [
    "INTJ",
    "INTP",
    "ENTJ",
    "ENTP",
    "INFJ",
    "INFP",
    "ENFJ",
    "ENFP",
    "ISTJ",
    "ISFJ",
    "ESTJ",
    "ESFJ",
    "ISTP",
    "ISFP",
    "ESTP",
    "ESFP",
]

preferred_category = [
    "pantai",
    "alam",
    "tujuan_wisata",
    "sejarah_budaya",
    "hotel",
    "tourist_attraction",
    "budaya_sejarah",
    "taman",
    "hiking_area",
    "rekreasi_keluarga",
    "snorkling_area",
    "kebun_binatang",
]

travel_style = ["solo", "family", "partner"]

locations = [
    "jakarta",
    "medan",
    "lombok",
    "bali",
    "padang",
    "batam",
    "yogyakarta",
]


output_file = "./dataset/survey_result.csv"

with open(output_file, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(
        [
            "mbti",
            "location",
            "preffered_category",
            "travel_style",
            "age",
            "past_trip_rating",
            "travel_frequency",
        ]
    )
    for mbti in mbti_types:
        for category in preferred_category:
            for style in travel_style:
                for city in locations:
                    age = random.randint(18, 70)
                    past_trip_rating = random.randint(3, 5)
                    travel_frequency = random.randint(1, 5)
                    writer.writerow(
                        [mbti, category, style, age, past_trip_rating, travel_frequency]
                    )
