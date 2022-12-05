class TodoItem:
    name = ""
    index = 0


class TodoItemService:
    def __init__(self):
        self.item_list = []

    def add(self, item):
        self.item_list.append(item)


TodoItemService().add(TodoItem())
