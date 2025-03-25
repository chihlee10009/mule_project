""" 
#define a class called Nation that has
# 3 attributes {smithore, food, energy}
# 3 methods {sell, buy, grow}
# for grow: random number between[0,6] of a unit of attribute
#    introduce a environmental event that correspond to the random growth number
#[0,6] = from 0 to 6 , including 0 and 6
#(0,6) = from 0 to 6, not including 0 and 6
#[0,6) = from 0 to 6, including 0 but not 6
#(0,6] = from 0 to 6, not including 0 but include 6
"""
import random

class Nation:
  """my_fancy_nation_class"""
  def __init__(self, smithore, food, energy, gold):
    """my_fancy_init_method"""
    self.smithore = smithore
    self.food = food
    self.energy = energy
    self.gold = gold
    self.food_cost = 2
    self.smithore_cost = 3
    self.energy_cost = 1

  def sell(self, unit_type, quantity):
  # unit_type = input("what do you want to sell:\n")
  # quantity = input("how many would you like to sell?:\n")
    if quantity <= 0:
      print("can't sell more than what you have")
      
      #raise means "throw an error"
      raise     

    if unit_type == "smithore":
      if quantity <= self.smithore:
        self.smithore -= quantity 
        self.gold += quantity * self.smithore_cost
      else:
        print("you can't sell more than what you have")

    elif unit_type == "food":
      if quantity <= self.food:
        self.food -= quantity 
        self.gold += quantity * self.food_cost
      else:
        print("you can't sell more than what you have")

    elif unit_type == "energy":
      if quantity <= self.energy:
        self.energy -= quantity 
        self.gold += quantity * self.energy_cost
      else:
        print("you can't sell more than what you have")

  def buy(self, unit_type, quantity):
    if unit_type == "smithore":
      if self.gold >= quantity * self.smithore_cost:
        self.gold -= quantity * self.smithore_cost
        self.smithore += quantity
      else:
        print("you don't have enough gold!")

    elif unit_type == "food":
      if self.gold >= quantity * self.food_cost:
        self.gold -= quantity * self.food_cost
        self.food += quantity
      else:
        print("you don't have enough gold!")
    
    elif unit_type == "energy":
      if self.gold >= quantity * self.energy_cost:
        self.gold -= quantity * self.energy_cost 
        self.energy += quantity
      else:
        print("you don't have enough gold!")
  
  def grow(self):
    #random number [0,6] for each smithore, food and energy
    #evaluate the lowest output number for either smithore, food, or energy
    #corelate to a environmental attribute {rain, energystorm, comet}
    #food = if food is the lowest number then {comet}
    #energy = if energy is the lowest number then {rain}
    #smithore = if smithore is the lowest number then {energystorm}
    num_smithore = random.randint(0,6)
    num_food     = random.randint(0,6)
    num_energy   = random.randint(0,6)
    if num_smithore < num_food and num_smithore < num_energy:
      print("An energy storm has hit the planet!")
    
    elif num_food < num_smithore and num_food < num_energy:
      print("A comet has hit the planet!")

    elif num_energy < num_food and num_energy < num_smithore:
      print("A rainstorm has hit the planet!")

    else:
      self.grow()

    
help(Nation)
exit()


nation_obj = Nation(2, 0, 0, 6)
#nation_obj.sell("smithore", 3)
nation_obj.buy("smithore", 1)
print("you have", nation_obj.gold, "gold")