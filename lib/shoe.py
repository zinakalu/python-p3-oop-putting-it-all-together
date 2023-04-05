#!/usr/bin/env python3

class Shoe:
    
    def __init__(self, brand, condition = "Used"):
        self.brand = brand
        # self.color = color
        # self.size = size
        # self.material = material
        # self.condition = condition
        self.condition = condition
    _size = None
    def get_size(self):
        return self._size
    
    def set_size(self, size):
        if not isinstance(size, int):
            print("size must be an integer")
        
        else:
            self._size = size

    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = "New"

    size = property(get_size, set_size)
shoes = Shoe("Nike")