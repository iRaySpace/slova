import csv


_special_chars = ",()"

def _clean_word(word):
    return "".join(
        letter.lower()
        for letter in word
        if letter not in _special_chars
    )

def _parse_file():
    with open("input.txt", "r") as file:
        return list(map(_clean_word, file.read().split()))


def _get_frequency(words):
    frequency = {}
    for word in words:
        current_frequency = frequency.get(word, 0)
        frequency[word] = current_frequency + 1
    return frequency


def _sort_from_highest(frequency):
    frequency_list = [x for x in frequency.items()]
    frequency_list.sort(key=lambda x: x[1], reverse=True)
    return frequency_list


def _write_to_csv(frequency_list):
    with open("output.csv", mode="w") as file:
        writer = csv.writer(file)
        for row in frequency_list:
            writer.writerow(row)


if __name__ == "__main__":
    words = _parse_file()
    frequency = _get_frequency(words)
    frequency_list = _sort_from_highest(frequency)
    _write_to_csv(frequency_list)
