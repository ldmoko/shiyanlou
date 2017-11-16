#!/usr/bin/env python3
# -*- coding: utf-8 -*-

 
class Dog():
    def __init__(self, name):
        self._name = name
       
    def get_name(self):
        return self._name
      
    def set_name(self, value):
        self._name = value
     
    def make_sound(self):
        print(self.get_name() + ' is making sound wang~~~')
 

class Cat():
    def __init__(self, name):
        self._name = name
 
    def get_name(self):
      return self._name
      
    def set_name(self, value):
      self._name = value
      
    def make_sound(self):
       print(self.get_name() + ' is making sound miu~~~')
  
  
if __name__ == '__main__':
    #dog = Dog('wangcai')
    #cat = Cat('kitty')
    #dog.bark()
    #cat.mew()
    animals = [Dog('wangcai'), Cat('kitty'), Dog('laifu'), Cat('betty')]
    for animal in animals:
        animal.make_sound()
