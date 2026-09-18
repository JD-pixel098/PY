def cat(food = "soup" , state='still hungry', action='growl', breed='Sphinx'):
    print(f"-- This cat wouldn't {action}", end=' ')
    print(f"if you gave it {food}")
    print(f"-- Lovely fur, the {breed}")
    print(f"-- It's {state}!")


cat()
