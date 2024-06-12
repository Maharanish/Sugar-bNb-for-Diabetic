import heapq

class FoodItem:
    def __init__(self, name, weight, value):
        self.name = name
        self.weight = weight
        self.value = value

def knapsack_01_branch_and_bound(items, max_weight):
    items.sort(key=lambda x: x.value / x.weight, reverse=True)

    def bound(i, current_weight, current_value):
        if current_weight >= max_weight:
            return 0
        bound_value = current_value
        total_weight = current_weight
        while i < len(items) and total_weight + items[i].weight <= max_weight:
            total_weight += items[i].weight
            bound_value += items[i].value
            i += 1
        if i < len(items):
            bound_value += (max_weight - total_weight) * (items[i].value / items[i].weight)
        return bound_value

    n = len(items)
    best_value = 0
    best_items = []

    pq = []
    heapq.heappush(pq, (-bound(0, 0, 0), 0, 0, 0, []))

    while pq:
        _, i, current_weight, current_value, selected_items = heapq.heappop(pq)
        
        if current_value > best_value and current_weight <= max_weight:
            best_value = current_value
            best_items = selected_items
        
        if i < n:
            if current_weight + items[i].weight <= max_weight:
                heapq.heappush(pq, (-bound(i + 1, current_weight + items[i].weight, current_value + items[i].value), 
                i + 1, current_weight + items[i].weight, current_value + items[i].value, selected_items + [items[i]]))
            heapq.heappush(pq, (-bound(i + 1, current_weight, current_value), i + 1, current_weight, current_value, selected_items))

    return best_value, best_items