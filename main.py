# RenderPen - сервіс анотування 3D-моделей
# Реалізація базової функції перевірки формату файлу (FR-01)

def validate_model_format(filename):
    """
    Перевіряє, чи є файл форматом .glb, як того вимагає SRS.
    """
    if filename.lower().endswith('.glb'):
        return True
    else:
        return False

if __name__ == "__main__":
    print("--- RenderPen System: Перевірка завантаження ---")
    
    test_file = "engine_model.glb"
    
    if validate_model_format(test_file):
        print(f"Файл '{test_file}' валідний. Модель завантажується...")
    else:
        print(f"Помилка: Файл '{test_file}' не підтримується. Оберіть .glb")
        