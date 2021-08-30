print("FRUIT SHOP \n")

fruit={}
cart=[]

def add_fruit():
	fruit_id = int(input("\tEnter the Fruit ID "))
	if fruit_id not in fruit.keys():
		fruit_name = input("\tEnter name ")
		rate= int(input("\tEnter rate "))
		imported_from = input("\tEnter where it is imported from ")
		import_date = input("\tEnter the import date ")
		buying_price = int(input("\tEnter the buying price "))
		temp ={
			"fruit_name":fruit_name,
			"rate":rate,
			"imported_from":imported_from,
			"import_date":import_date,
			"buying_price":buying_price,
		}
		fruit[fruit_id] = temp
	else:
		print("\tFruit ID has already been taken")

def delete_fruit():
	a=int(input("Enter the Fruit_ID of the fruit to be deleted\n"))
	if a in fruit.keys():
		del fruit[a]
	else:
		print("Fruit doesnot exist in the shop.\n")
def search_fruit():
	name=input("Enter the fruit name you want to search\t")
	rate=int(input("Enter the fruit rate you want to search\t"))
	found = False
	for i in fruit.values():
		if (i["fruit_name"] == name) and (i["rate"] == rate):
			found = True
			print("Fruit exists in inventory.")
			break
	if(found == False):
		print("Fruit doesnot exist in the inventory.")
def update_fruit():
	for i,j in fruit.items():
		print(f"{i} :")
		for x in j.values():
			print(f"\t{x}")
	a = int(input('Enter the fruit id : '))
	if a not in fruit.keys():
		print('Please provide right fruit id ')
	else:
		print('Update the fruit data')
		fruit[a]['fruit_name'] = input('Enter new fruit name :')
		fruit[a]['rate'] =input('Enter new rate : ')
def add_cart():
	for i,j in fruit.items():
		print(f"Enter {i} for adding {j['fruit_name']} to cart")
	select_ID=int(input('Enter fruit id to add on cart : '))
	cart.append(fruit[select_ID])
def buy_mainmenu():
	print("Enter required choice:\n1 for Adding fruits to cart\n2 for Delete fruit from cart\n3 for displaying cart\n4 for Bill\n5 for exiting\n")
def delete_cart():
	for i,j in fruit.items():
		print(f"Enter {i} for deleting {j['fruit_name']} to cart")
	select_ID=int(input('Enter fruit id to delete from the cart : '))
	cart.remove(fruit[select_ID])
def bill():
	amount=0
	for i in cart:
		amount=int(amount)+i['rate']
	y=1	
	for i in range(len(cart)):
		print(f"{y}.)")
		y+=1
		print(f"\t{cart[i]['fruit_name']} | {cart[i]['rate']}")	
	print(f"Total amount billed = {amount}")
def display_buy_fruit():
	for i,j in fruit.items():
		print(f"{i} :")
		for x in j.values():
			print(f"\t{x}")
			
	while True:
		buy_mainmenu()
		ch=int(input())
		if ch == 1:
			add_cart()
		elif ch == 2:
			delete_cart()
		elif ch == 3:
			display_cart()
		elif ch == 4:
			bill()
		elif ch == 5:
			break
		else:
			print("Invalid choice\n")
def display_cart():
	print("\nElements in cart:")
	y=1	
	print(" ")		
	for i in range(len(cart)):
		print(f"{y}.)")
		y+=1
		print(f"\t{cart[i]['fruit_name']} | {cart[i]['rate']}")

while True:

	choice=int(input("Enter a choice for following functions.\n1 - Add Fruit.\n2 - Delete Fruit\n3 - Search Fruit info from inventory\n4 - Update name and rate of fruit\n5 - Display all and buy from the lot\n6 - Bill\n7 - Quit\t"))
	if(choice == 1 or fruit):
		if choice == 1:
			add_fruit()
			
		elif choice == 2:
			delete_fruit()
								
		elif choice == 3:
			search_fruit()
			
		elif choice == 4:
			update_fruit()
				
		elif choice == 5:
			display_buy_fruit()
			
		elif choice == 6:
			bill()
		
		elif choice == 7:
			break
				
		else:
			print("Invalid input.\n")
			
	else:
		print("Fruit shop is empty.\n")
