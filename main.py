import os
import re
import csv
from transformers import MBartTokenizer, MBartForConditionalGeneration

model_name = "IlyaGusev/mbart_ru_sum_gazeta"
tokenizer = MBartTokenizer.from_pretrained(model_name)
model = MBartForConditionalGeneration.from_pretrained(model_name)

stt_path = "D:/download/rutube_hackathon_novosibirsk/test/test_stt" # Путь к каталогу текстовых файлов с транскрибацией
csv_path = "D:/download/rutube_hackathon_novosibirsk/test/csv.csv" # Путь к файлу CSV для выгрузки данных

def getText(item):
    if item.is_file():
        with open(item.path, "r", encoding="utf-8") as file:
            return re.sub(r'\[.*?\]', '', file.read())

def getDesc(text):
    input_ids = tokenizer(
        [text],
        max_length=1000,
        padding="max_length",
        truncation=True,
        return_tensors="pt",
    )["input_ids"]

    output_ids = model.generate(
        input_ids=input_ids,
        no_repeat_ngram_size=4
    )[0]

    return tokenizer.decode(output_ids, skip_special_tokens=True)

def writeInCsv(name, desc):
    with open(csv_path, 'a', newline='', encoding='utf-8') as file_csv:
        writer = csv.writer(file_csv)
        writer.writerows([[name, desc]])
        file_csv.close()

with open(csv_path, 'a', newline='', encoding='utf-8') as file_csv:
    writer = csv.writer(file_csv)
    writer.writerows([["stt_name", "description"]])
    file_csv.close()

for item in os.scandir(stt_path):
    text = getText(item)
    summary = getDesc(text)

    writeInCsv(item.name, summary)

    # print({item.name, summary})
