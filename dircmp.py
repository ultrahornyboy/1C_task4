import os

import Levenshtein


def compare_files(dir1, dir2, similarity):
    # список файлов у которых обнаружилась ошибка при попытке считывания
    banned_file_paths = []

    # функция для попытки открытия фаля для чтения
    def read_file(filepath):
        try:
            with open(filepath, 'rb') as f:
                # в случае удачного открытия мы возвращаем истину и содержимое файла
                return True, f.read().decode('utf-8')
        except Exception as ex:
            # мы словили исключение и сообщаем это Тони
            print(f"An exception occurred while reading read {filepath}: ", ex)
            return False, None

    # пробуем открыть директории
    try:
        dir1_files = set(os.listdir(dir1))
        dir2_files = set(os.listdir(dir2))
    except Exception as ex:
        # в случае неудачного открытия директорий мы сообщаем это Тони
        print("Something went wrong, sorry Tony, here is the exception", ex)
        return

    for file1 in dir1_files:
        # получения пути файла
        path1 = os.path.join(dir1, file1)
        (could_read_file1, file1_content) = read_file(path1)
        if not could_read_file1:
            continue

        for file2 in dir2_files:
            # получаем пути файла
            path2 = os.path.join(dir2, file2)

            if path2 in banned_file_paths:
                continue

            (could_read_file2, file2_content) = read_file(path2)
            if not could_read_file2:
                # кидаем в бан те файлы которые не открылись
                banned_file_paths.append(path2)

            if file1_content == file2_content:
                # если файлы полностью схожи то мы просто выводим этот факт
                print(f"{path1} - {path2}")
            else:
                # порверка на точность сходства
                similarity_percent = Levenshtein.ratio(
                    file1_content, file2_content) * 100
                if similarity_percent >= similarity:
                    print(f"{path1} - {path2} - {similarity_percent:.2f}%")

    first_diff = ', '.join(dir1_files.difference(dir2_files))
    second_diff = ', '.join(dir2_files.difference(dir1_files))

    banned_file_paths_str = ', '.join(banned_file_paths)

    print(
        f"Files {banned_file_paths_str} were banned, an error occurred while trying to read them")
    print(f"{first_diff} these files present in directory dir1, but not found in dir2")
    print(f"{second_diff} these files present in directory dir2, but not found in dir1")
