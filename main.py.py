"""
Главный модуль инженерного калькулятора
Точка входа в программу, связывает все модули
"""

from calculator_engine import CalculatorEngine
from memory_manager import MemoryManager
from gui_interface import CalculatorGUI
import tkinter as tk


def main():
    """
    Основная функция для запуска калькулятора
    """
    try:
        # Создание экземпляров модулей
        engine = CalculatorEngine()
        memory = MemoryManager()
        
        # Создание графического интерфейса
        root = tk.Tk()
        app = CalculatorGUI(root, engine, memory)
        
        # Запуск основного цикла
        root.mainloop()
        
    except Exception as e:
        print(f"Ошибка при запуске программы: {e}")


if __name__ == "__main__":
    main()