# Автоматическая генерация описания к видео

## Как запустить?

Установите зависимости:
```sh
pip install transformers
pip install torch
pip install SentencePiece
```

Измените пути на нужные файлы:
```sh
stt_path = "/rutube_hackathon_novosibirsk/test/test_stt" # Путь к каталогу текстовых файлов с транскрибацией
csv_path = "/rutube_hackathon_novosibirsk/test/csv.csv" # Путь к файлу CSV для выгрузки данных
```
