is_boiling = True
stri_count =5
total_actions = stri_count + is_boiling # upcasting
print(f"Total action:{total_actions}")

milk_present = 0 # no milk
print(f"Is there milk? {bool(milk_present)}")

# logical operations
# and,or ,not
# and booth should be True
water_hot =True
tea_added = False

can_server = water_hot and tea_added
print(f"Can serve chai? {can_server}")

# float -real number
import sys
from fractions import Fraction
ideal_temp = 95.5
current_temp =95.49

print(f"Ideal temp {ideal_temp}")
print(f"Curent temp {current_temp}")
print(f"Difference temp {ideal_temp-current_temp}")
print(sys.float_info)
# complex numbers- fractions

# String are immutable

Chai_type = "Ginger chai"
customer_name ="Priya"

print(f"Order for {customer_name}: {Chai_type} please?")
# Indexing string -each letter is represented by a number. starts from 0
chai_description = "Aromatic and bold"
print(f"First word:{chai_description[0:8:1]}")
print(f"Last word:{chai_description[12:1]}")
print(f"Last word:{chai_description[::-1]}")

label_text="Chai spécial"
encoded_label = label_text.encode("utf-8")
print(f"None encoded label:{label_text}")
print(f"Encoded label:{encoded_label}")
decoded_label= encoded_label.decode("utf-8")
print(f"Decoded label:{decoded_label}")

# Tuples()
# tuples are immutables
masala_spices =("cardamon","cinnamon", "cloves")
(spice1,spice2,spice3)= masala_spices

print(f"Main masala spices:{spice1},{spice2},{spice3}")

ginger_ratio,cadarmon_ratio =(2,1)
print(f"Ratio is G:{ginger_ratio} and C{cadarmon_ratio}")
ginger_ratio,cadarmon_ratio =cadarmon_ratio,ginger_ratio

# Memberiship
print(f"Is ginger in masala spices?{'ginger' in masala_spices }")

# List [] is mutable
ingredients = ["water","milk","black tea"]
ingredients.append("sugar")
print(f"Ingredients are: {ingredients}")
ingredients.remove("water")

spice_options =["ginger","cardamon"]
chai_ingredients = ["water","milk"]

chai_ingredients.extend(spice_options)
print(f"chai:{chai_ingredients}")
chai_ingredients.insert(2, "black tea")
print(f"chai:{chai_ingredients}")
last_added = chai_ingredients.pop() # remove from the list and store it in a valuable
chai_ingredients.reverse()
print(f"chai:{chai_ingredients}")

chai_ingredients.sort()
print(f"chai:{chai_ingredients}")

sugar_levels = [1,2,3,4,5]
print(f"Maximum sugar level:{max(sugar_levels)}")
print(f"Minimum sugar level:{min(sugar_levels)}")

# operators overloading
base_liquid=["water","milk"]
extra_flavor =["ginger"]
full_liquid_mix = base_liquid + extra_flavor
print(F'liquid mix {full_liquid_mix}')

strong_brew =["black tea"] * 3
print(F"strong brew: {strong_brew}")

raw_spice_data = bytearray(b"CINNAMON")
raw_spice_data=raw_spice_data.replace(b"CINNA",b"CARD")
print(f"Bytes: {raw_spice_data}")

