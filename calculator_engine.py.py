"""
Модуль математических вычислений для инженерного калькулятора
Отвечает за выполнение всех математических операций
"""

import math


class CalculatorEngine:
    """Класс для выполнения математических вычислений"""
    
    def __init__(self):
        self.current_value = "0"
        self.reset_next_input = False
        
    def evaluate_expression(self, expression):
        """Вычисляет математическое выражение"""
        try:
            expression = expression.replace('^', '**')
            expression = expression.replace('π', str(math.pi))
            expression = expression.replace('e', str(math.e))
            
            expression = expression.replace('sin(', 'math.sin(math.radians(')
            expression = expression.replace('cos(', 'math.cos(math.radians(')
            expression = expression.replace('tan(', 'math.tan(math.radians(')
            expression = expression.replace('√(', 'math.sqrt(')
            expression = expression.replace('log(', 'math.log10(')
            expression = expression.replace('ln(', 'math.log(')
            
            result = eval(expression)
            
            if result == int(result):
                return str(int(result))
            else:
                return f"{result:.10f}".rstrip('0').rstrip('.')
                
        except Exception:
            return "Error"
    
    def calculate_scientific(self, function, value):
        """Выполняет научные вычисления"""
        try:
            num = float(value)
            
            if function == "sin":
                result = math.sin(math.radians(num))
            elif function == "cos":
                result = math.cos(math.radians(num))
            elif function == "tan":
                result = math.tan(math.radians(num))
            elif function == "√":
                result = math.sqrt(num)
            elif function == "x²":
                result = num ** 2
            elif function == "x³":
                result = num ** 3
            elif function == "1/x":
                result = 1 / num
            elif function == "log":
                result = math.log10(num)
            elif function == "ln":
                result = math.log(num)
            elif function == "π":
                result = math.pi
            elif function == "e":
                result = math.e
            else:
                return value
            
            if result == int(result):
                return str(int(result))
            else:
                return f"{result:.10f}".rstrip('0').rstrip('.')
                
        except Exception:
            return "Error"