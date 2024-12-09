import csv
import random

mbti_destinations = {
    "INTJ": ["budaya_sejarah", "sejarah_budaya", "tujuan_wisata", "taman"],
    "INTP": ["budaya_sejarah", "sejarah_budaya", "alam", "hiking_area"],
    "ENTJ": ["tujuan_wisata", "hotel", "taman", "tourist_attraction"],
    "ENTP": [
        "budaya_sejarah",
        "sejarah_budaya",
        "tujuan_wisata",
        "pantai",
        "tourist_attraction",
    ],
    "INFJ": ["sejarah_budaya", "alam", "rekreasi_keluarga"],
    "INFP": ["alam", "pantai", "hiking_area"],
    "ENFJ": ["rekreasi_keluarga", "hotel", "tujuan_wisata"],
    "ENFP": ["pantai", "taman", "rekreasi_keluarga"],
    "ISTJ": ["sejarah_budaya", "hotel", "tujuan_wisata"],
    "ISFJ": ["hotel", "rekreasi_keluarga", "sejarah_budaya", "tourist_attraction"],
    "ESTJ": ["tujuan_wisata", "hotel", "taman", "tourist_attraction"],
    "ESFJ": ["rekreasi_keluarga", "hotel", "pantai", "tourist_attraction"],
    "ISTP": ["alam", "hiking_area", "pantai"],
    "ISFP": ["pantai", "alam", "hiking_area"],
    "ESTP": ["snorkling_area", "pantai", "rekreasi_keluarga", "tourist_attraction"],
    "ESFP": ["pantai", "rekreasi_keluarga", "snorkling_area", "tourist_attraction"],
}

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
            "id",
            "mbti",
            "location",
            "preffered_category",
            "travel_style",
            "age",
            "past_trip_rating",
            "travel_frequency",
        ]
    )

    id += 1
