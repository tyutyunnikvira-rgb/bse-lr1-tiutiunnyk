# renderpen.py

class RenderPen:
    """Модуль керування 3D-проєктами RenderPen"""

    def __init__(self):
        self.max_file_size_mb = 50.0
        self.allowed_extension = ".glb"

    def validate_upload(self, filename: str, size_mb: float) -> bool:
        """
        Перевіряє можливість завантаження файлу (FR-01).
        Логіка: правильне розширення та розмір від 0 до 50 МБ.
        """
        if not filename.lower().endswith(self.allowed_extension):
            raise ValueError("Invalid file extension. Only .glb is allowed.")
        
        if size_mb <= 0:
            raise ValueError("File size must be greater than 0.")
            
        if size_mb > self.max_file_size_mb:
            return False  # Занадто великий файл
            
        return True

    def validate_label(self, x: float, y: float, z: float, text: str) -> bool:
        """
        Валідація мітки (FR-02). 
        Логіка: координати в межах [-1000, 1000], текст від 1 до 100 символів.
        """
        # Перевірка координат
        for coord in [x, y, z]:
            if coord < -1000 or coord > 1000:
                return False
        
        # Перевірка тексту
        text_len = len(text.strip())
        if text_len == 0 or text_len > 100:
            return False
            
        return True

    def format_public_link(self, project_id: str, is_published: bool) -> str:
        """
        Генерує публічне посилання (FR-04).
        Логіка: посилання створюється тільки якщо статус True та ID не порожній.
        """
        if not project_id:
            raise ValueError("Project ID cannot be empty.")
            
        if is_published:
            return f"https://renderpen.com/view/{project_id}"
        else:
            return "Project is private"