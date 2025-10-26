import requests
import random

import warnings
warnings.filterwarnings("ignore", category=UserWarning, module="urllib3")

def get_random_ayah():
    surah = random.randint(1, 114)
    ayah = random.randint(1, 7)
    res = requests.get(f"https://api.alquran.cloud/v1/ayah/{surah}:{ayah}/en.asad")
    data = res.json()["data"]
    return {
        "english": data["text"],
        "translation": data["edition"]["englishName"],
        "reference": f"{data['surah']['englishName']} {data['numberInSurah']}"
    }

if __name__ == "__main__":
    a = get_random_ayah()
    print(f"{a['english']}\n{a['translation']}\n{a['reference']}")


print("this is a print statement")