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
