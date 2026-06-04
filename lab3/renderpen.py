class RenderPen:
    """Модуль керування 3D-проєктами RenderPen за стандартами Clean Code."""

    # Константи (усунення Magic Numbers)
    MAX_FILE_SIZE_MB = 50.0
    ALLOWED_EXTENSION = ".glb"
    MIN_COORD = -1000.0
    MAX_COORD = 1000.0
    MAX_TEXT_LEN = 100

    def validate_upload(self, filename: str, size_mb: float) -> bool:
        """Перевіряє валідність завантаження (Refactored)."""
        self._check_extension(filename)
        self._check_positive_size(size_mb)
        
        return size_mb <= self.MAX_FILE_SIZE_MB

    def _check_extension(self, filename: str):
        """Приватний метод для перевірки розширення (SRP)."""
        if not filename.lower().endswith(self.ALLOWED_EXTENSION):
            raise ValueError(f"Дозволено лише {self.ALLOWED_EXTENSION}")

    def _check_positive_size(self, size_mb: float):
        """Приватний метод для перевірки розміру (SRP)."""
        if size_mb <= 0:
            raise ValueError("Розмір файлу має бути більше 0")

    def validate_label(self, x: float, y: float, z: float, text: str) -> bool:
        """Валідація мітки з використанням констант."""
        coords_valid = all(self.MIN_COORD <= c <= self.MAX_COORD for c in [x, y, z])
        text_valid = 0 < len(text.strip()) <= self.MAX_TEXT_LEN
        
        return coords_valid and text_valid

    def format_public_link(self, project_id: str, is_published: bool) -> str:
        """Генерує посилання (Clean Logic)."""
        if not project_id:
            raise ValueError("ID проєкту не може бути порожнім")
            
        if not is_published:
            return "Project is private"
            
        return f"https://renderpen.com/view/{project_id}"