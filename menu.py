""" Create empty list """
order_list = [
  {
    "Item name": "string",
    "Price": float,
    "Quantity": int
  },
  {
    "Item name": "string",
    "Price": float,
    "Quantity": int
  },
]

for item in order_list:
    print(f"Here is the menu option {item}")

keep_ordering = True
while True:
        keep_ordering = input("Would you like to keep ordering? (Y)es or (N)o ")
        match keep_ordering.lower():
            case 'y':
                place_order = True
                break
            case 'n':
                place_order = False
                break
        
            case _:
                print("Please retry selecting only Y or N")
      

