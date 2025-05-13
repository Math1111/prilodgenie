import os
from pathlib import Path


def get_project_structure(startpath, output_file):
    EXCLUDE_DIRS = {
        '__pycache__',
        'migrations',
        'venv',
        '.git',
        '.idea',
        'env',
        'node_modules',
        'staticfiles',
        'media'
    }

    EXCLUDE_FILES = {
        '.pyc',
        '.pyo',
        '.pyd',
        '.db',
        '.sqlite3',
        '.log',
        '.env',
        '.gitignore',
        '*.swp',
        '*.tmp'
    }

    with open(output_file, 'w', encoding='utf-8') as f:
        for root, dirs, files in os.walk(startpath):
            # Удаляем исключенные директории из списка для обработки
            dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]

            level = root.replace(startpath, '').count(os.sep)
            if level > 3:  # Не показываем слишком глубокие уровни
                continue

            indent = ' ' * 4 * (level)
            f.write(f"{indent}{os.path.basename(root)}/\n")

            subindent = ' ' * 4 * (level + 1)
            for file in files:
                # Пропускаем исключенные файлы
                if not any(file.endswith(ext) for ext in EXCLUDE_FILES):
                    # Показываем только важные файлы
                    if file in {'manage.py', 'settings.py', 'urls.py', 'wsgi.py', 'asgi.py', 'requirements.txt'} or \
                            file.endswith(('.py', '.html', '.css', '.js')) and not file.startswith('.'):
                        f.write(f"{subindent}{file}\n")


if __name__ == "__main__":
    project_path = input("Введите путь к Django проекту: ").strip()
    output_file = "project_structure.txt"

    if not os.path.exists(project_path):
        print("Указанный путь не существует!")
        exit(1)

    if not os.path.isfile(os.path.join(project_path, 'manage.py')):
        print("Указанный путь не является Django проектом (не найден manage.py)!")
        exit(1)

    get_project_structure(project_path, output_file)
    print(f"Структура проекта сохранена в файл: {output_file}")