class FileUtils:
    @classmethod
    def count_lines(cls, file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                lines = file.readlines()
                return len(lines)
        except FileNotFoundError:
            print(f"Помилка: файл {file_path} не знайдено.")
            return 0
        except Exception as e:
            print(f"Виникла помилка: {str(e)}.")
            return 0


file_path = 'example.txt'
lines_count = FileUtils.count_lines(file_path)

if lines_count > 0:
    print(f"Кількість рядків у файлі {file_path}: {lines_count}")
