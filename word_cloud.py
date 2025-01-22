data = [
    ["Формирование сильной команды", 1],
    ["Поощрение индивидуальности и мотивация", 1],
    ["Забота и поддержка", 1],
    ["Коммуникация изменений", 1],
    ["Ответственность", 2],
    ["Осознанность в развитии", 3],
    ["Проектирование будущего опыта", 4],
    ["Аналитика и логика", 5],
    ["Синтез и системность", 5],
    ["Сценарное и стратегическое мышление", 5],
    ["Амбициозность целей", 5],
    ["Командность", 5],
    ["Коммуникация и влияние", 5],
    ["Управление конфликтами", 5],
    ["Построение отношений", 5],
    ["Развитие эффективности команды", 5],
    ["Создание долгосрочной ценности", 5],
    ["Использование технологий", 4],
    ["Поощрение разнообразия идей", 3],
    ["Постоянное совершенствование", 3],
    ["Видение клиента во всем многообразии ролей", 3],
    ["Фокус на главном, планирование", 3],
    ["Понимание себя", 2],
    ["Жизнестойкость", 2],
    ["Генерация идей", 1],
    ["Принятие решений", 1],
    ["Нацеленность на результат", 1],
    ["Управление своими ресурсами", 1],
    
]

max_lengths = [50, 80, 80, 80, 90, 80, 80, 80, 80, 50]

styles = {
    '5': {"color": "green", "font-weight": "bold", "font-size": "24px"},
    '4': {"color": "orange", "font-weight": "normal", "font-size": "20px"},
    '3': {"color": "purple", "font-weight": "normal", "font-size": "16px"},
    '2': {"color": "lightpurple", "font-weight": "normal", "font-size": "14px"},
    '1': {"color": "gray", "font-weight": "normal", "font-size": "12px"}
}

# Функция для создания div с заданным стилем
def wrap_in_div(data):
    result = []
    text, value = data
    style = styles.get(value, {"color": "black", "font-weight": "normal", "font-size": "12px"})
    div = f'<div style="color: {style["color"]}; font-weight: {style["font-weight"]}; font-size: {style["font-size"]};">{text}</div>'
    return div



# Функция для генерации строк с учетом ограничения символов
def distribute_data(data, max_lengths):
    current_line = ""
    result = []
    length_index = 0

    for item, number in data:
        text = item  # Берем текст элемента
        if length_index >= len(max_lengths):
            break  # Выходим, если больше нет ограничений на строки
        max_length = max_lengths[length_index]

        # Если текст помещается в текущую строку
        if len(current_line) + len(text) + 2 <= max_length:  # +2 для запятой и пробела
            current_line += (". " if current_line else "") + f"{text}:{number}"
        else:
            # Добавляем текущую строку в результат и начинаем новую
            result.append(current_line)
            current_line = f"{text}:{number}"
            length_index += 1

    # Добавляем последнюю строку, если она не пустая
    if current_line:
        result.append(current_line)

    return result
str = 'Ответственность, Понимание себя, Жизнестойкость, Поощрение разнообразия идей, Принятие решений, Нацеленность на результат, Управление своими ресурсами, Формирование сильной команды, Поощрение индивидуальности и мотивация, Забота и поддержка, Коммуникация изменений'


# Применяем функцию
chunked_data = distribute_data(data, max_lengths)

result = []
# Результат
for chunk in chunked_data:
    new_chunk = []
    array = chunk.split('. ')
    for item in array:
        data = item.split(':')
        new_data = wrap_in_div(data)
        # print(new_data)
        new_chunk.append(new_data)
     
    result.append(f'<div>{"".join(new_chunk)}</div>')
# result2 = [ for item in result for i in item]    
print(''.join(result))