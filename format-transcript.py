import json, re, sys

#  get this from the console
# file_path = "asrOutput7.json"
file_path = sys.argv[1]

with open(file_path, "r") as file:
    data = json.load(file)

current_speaker = None
results = []


def get_content(item):
    return item["alternatives"][0]["content"]


for item in data["results"]["items"]:
    if current_speaker and current_speaker[0] == item["speaker_label"]:
        current_speaker.append(get_content(item))
    elif not current_speaker or current_speaker[0] != item["speaker_label"]:
        current_speaker = []
        results.append(current_speaker)
        current_speaker.append(item["speaker_label"])
        current_speaker.append(get_content(item))


def remove_spaces_before_punctuation(text):
    pattern = r"\s+(?=[,.?])"
    modified_text = re.sub(pattern, "", text)
    return modified_text


for i in results:
    print(remove_spaces_before_punctuation(" ".join([i[0]] + [": "] + i[1:])))
