"""
Модуль управления памятью калькулятора
Реализует функции M+, M-, MR, MC
"""


class MemoryManager:
    """Класс для управления памятью калькулятора"""
    
    def __init__(self):
        self.memory_value = 0.0
        self.memory_status = False 
    
    def clear_memory(self):
        """Очищает память (MC)"""
        self.memory_value = 0.0
        self.memory_status = False
    
    def recall_memory(self):
        """Возвращает значение из памяти (MR)"""
        return self.memory_value
    
    def add_to_memory(self, value):
        """Добавляет значение в память (M+)"""
        try:
            self.memory_value += float(value)
            self.memory_status = True
        except:
            pass
    
    def subtract_from_memory(self, value):
        """Вычитает значение из памяти (M-)"""
        try:
            self.memory_value -= float(value)
            self.memory_status = True
        except:
            pass
    
    def has_memory(self):
        """Проверяет, есть ли что-то в памяти"""
        return self.memory_status