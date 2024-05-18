import heapq

def min_cost_to_connect_cables(cables):
    '''Створюємо мін-купу з довжин кабелів'''
    heapq.heapify(cables)

    total_cost = 0

    while len(cables) > 1:
        # Витягуємо два найменших кабелі
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)

        # Об'єднуємо їх та додаємо вартість до загальної суми
        combined_length = first + second
        total_cost += combined_length

        # Поміщаємо об'єднаний кабель назад у купу
        heapq.heappush(cables, combined_length)

    return total_cost

# Приклад використання
cables = [4, 3, 2, 6]
print(f"Мінімальна вартість об'єднання кабелів: {min_cost_to_connect_cables(cables)}")
