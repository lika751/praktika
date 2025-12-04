"""
Модуль графического интерфейса калькулятора
Создаёт и управляет пользовательским интерфейсом
"""

import tkinter as tk
from tkinter import font


class CalculatorGUI:
    """Класс для графического интерфейса калькулятора"""
    
    def __init__(self, root, engine, memory):
        self.root = root
        self.engine = engine
        self.memory = memory
        
        self.root.title("Инженерный калькулятор")
        self.root.geometry("500x700")
        self.root.configure(bg='#2e2e2e')
        self.root.resizable(False, False)
        
        self.display_font = font.Font(family="Arial", size=24, weight="bold")
        self.button_font = font.Font(family="Arial", size=12)
        
        self.create_widgets()
        
    def create_widgets(self):
        """Создает все элементы интерфейса"""
        
        main_frame = tk.Frame(self.root, bg='#2e2e2e')
        main_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        
        self.display_var = tk.StringVar(value="0")
        display_frame = tk.Frame(main_frame, bg='#1a1a1a', relief=tk.RIDGE, bd=3)
        display_frame.pack(pady=(0, 10), fill=tk.X)
        
        display = tk.Entry(
            display_frame,
            textvariable=self.display_var,
            font=self.display_font,
            bg='#1a1a1a',
            fg='#00ff44',
            bd=0,
            justify=tk.RIGHT,
            readonlybackground='#1a1a1a',
            state='readonly'
        )
        display.pack(fill=tk.BOTH, padx=5, pady=5)
        
        buttons_frame = tk.Frame(main_frame, bg='#2e2e2e')
        buttons_frame.pack(fill=tk.BOTH, expand=True)
        
        buttons = [
            [
                ("MC", self.memory_clear, "#145a32"),
                ("MR", self.memory_recall, "#145a32"),
                ("M+", self.memory_add, "#145a32"),
                ("M-", self.memory_subtract, "#145a32"),
                ("CE", self.clear_entry, "#00cc44")
            ],
            [
                ("sin", lambda: self.scientific_func("sin"), "#1e8449"),
                ("cos", lambda: self.scientific_func("cos"), "#1e8449"),
                ("tan", lambda: self.scientific_func("tan"), "#1e8449"),
                ("√", lambda: self.scientific_func("√"), "#1e8449"),
                ("C", self.clear_all, "#00cc44")
            ],
            [
                ("x²", lambda: self.scientific_func("x²"), "#1e8449"),
                ("x³", lambda: self.scientific_func("x³"), "#1e8449"),
                ("1/x", lambda: self.scientific_func("1/x"), "#1e8449"),
                ("⌫", self.backspace, "#1e8449"),
                ("/", lambda: self.button_click("/"), "#1e8449")
            ],
            [
                ("7", lambda: self.button_click("7"), "#2e2e2e"),
                ("8", lambda: self.button_click("8"), "#2e2e2e"),
                ("9", lambda: self.button_click("9"), "#2e2e2e"),
                ("log", lambda: self.scientific_func("log"), "#1e8449"),
                ("*", lambda: self.button_click("*"), "#1e8449")
            ],
            [
                ("4", lambda: self.button_click("4"), "#2e2e2e"),
                ("5", lambda: self.button_click("5"), "#2e2e2e"),
                ("6", lambda: self.button_click("6"), "#2e2e2e"),
                ("ln", lambda: self.scientific_func("ln"), "#1e8449"),
                ("-", lambda: self.button_click("-"), "#1e8449")
            ],
            [
                ("1", lambda: self.button_click("1"), "#2e2e2e"),
                ("2", lambda: self.button_click("2"), "#2e2e2e"),
                ("3", lambda: self.button_click("3"), "#2e2e2e"),
                ("π", lambda: self.scientific_func("π"), "#1e8449"),
                ("+", lambda: self.button_click("+"), "#1e8449")
            ],
            [
                ("0", lambda: self.button_click("0"), "#2e2e2e"),
                (".", lambda: self.button_click("."), "#2e2e2e"),
                ("e", lambda: self.scientific_func("e"), "#1e8449"),
                ("^", lambda: self.button_click("^"), "#1e8449"),
                ("=", self.calculate, "#1e8449")
            ]
        ]
        
        for row_idx, row in enumerate(buttons):
            row_frame = tk.Frame(buttons_frame, bg='#2e2e2e')
            row_frame.pack(fill=tk.BOTH, expand=True, pady=2)
            
            for col_idx, (text, command, color) in enumerate(row):
                btn = tk.Button(
                    row_frame,
                    text=text,
                    command=command,
                    font=self.button_font,
                    bg=color,
                    fg='white',
                    activebackground='#4a4a4a',
                    activeforeground='white',
                    relief=tk.RAISED,
                    bd=2,
                    width=8,
                    height=2
                )
                btn.pack(side=tk.LEFT, padx=2, fill=tk.BOTH, expand=True)
    
    def button_click(self, value):
        """Обработка нажатия цифр и операторов"""
        current = self.display_var.get()
        
        if current == "0" or current == "Error":
            self.display_var.set(value)
        else:
            self.display_var.set(current + value)
    
    def clear_all(self):
        """Очистка всего дисплея"""
        self.display_var.set("0")
    
    def clear_entry(self):
        """Очистка текущего ввода"""
        self.display_var.set("0")
    
    def backspace(self):
        """Удаление последнего символа"""
        current = self.display_var.get()
        if current not in ["0", "Error"]:
            if len(current) > 1:
                self.display_var.set(current[:-1])
            else:
                self.display_var.set("0")
    
    def calculate(self):
        """Вычисление выражения"""
        expression = self.display_var.get()
        result = self.engine.evaluate_expression(expression)
        self.display_var.set(result)
    
    def scientific_func(self, func):
        """Обработка научных функций"""
        current = self.display_var.get()
        
        if func in ["π", "e"]:
            if current == "0" or current == "Error":
                result = self.engine.calculate_scientific(func, "0")
            else:
                result = self.engine.calculate_scientific(func, current)
            self.display_var.set(result)
        elif func in ["sin", "cos", "tan", "log", "ln"]:
            if current == "0" or current == "Error":
                result = self.engine.calculate_scientific(func, "0")
            else:
                result = self.engine.calculate_scientific(func, current)
            self.display_var.set(result)
        elif func in ["√", "x²", "x³", "1/x"]:
            if current not in ["0", "Error"]:
                result = self.engine.calculate_scientific(func, current)
                self.display_var.set(result)
    
    def memory_clear(self):
        """Очистка памяти"""
        self.memory.clear_memory()
    
    def memory_recall(self):
        """Восстановление из памяти"""
        value = self.memory.recall_memory()
        self.display_var.set(str(value))
    
    def memory_add(self):
        """Добавление в память"""
        current = self.display_var.get()
        if current not in ["0", "Error"]:
            self.memory.add_to_memory(current)
    
    def memory_subtract(self):
        """Вычитание из памяти"""
        current = self.display_var.get()
        if current not in ["0", "Error"]:
            self.memory.subtract_from_memory(current)