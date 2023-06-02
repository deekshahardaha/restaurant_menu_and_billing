import shutil
import datetime

columns = shutil.get_terminal_size().columns
name = input("Enter your name :").title()
print("*" * 145)
print("WELCOME TO SOON FATT".center(columns))
print("Mig 22 A , Sonagiri  Bhopal, 462022 ".center(columns))
print("Contacts: 9876543210 07642-250815".center(columns))
print("Email-SOONFATTservices@gmail.com".center(columns))
print("Date:", datetime.date(2022, 9, 21))
print("Customer Name:", name)
print("*" * 145)
total = 0
description = []


# Function
def calc(cat, no, quant):
    global total
    global description
    disc = {1: {'1': [25,'Tea'], '2': [35,'Coffee'], '3': [40,'Cold Coffee'], '4': [30,'ButterMilk'], '5': [50,'Lassi'], '6': [20,'Soda']},
            2: {'1': [60,'French fries'], '2': [70,'Potato Wedges'], '3': [75,'Sandwich'], '4': [60,'Kothe'], '5': [120,'Burger']}, 3: {'1': [35,'Idli Sambhar'], '2': [40,'Medu Wada'], '3': [45,'Plain Dosa'] ,'4': [50,'Masala Dosa'] ,'5': [65,'Uttapam']},
            4: {'1': [120,'Manchurian'], '2': [200,'Noodles'], '3': [100,'Manchaw'], '4': [100,'Spring Rolls'], '5': [250,'Prauns']}, 5: {'1': [15,'Roti'], '2': [35,'Naan'], '3': [20,'Paratha'], '4': [25,'Tandoori Roti'], '5': [25,'Rumali Roti']},
            6: {'1': [45,'Steamed rice'], '2': [65,'Jeera Rice'], '3': [100,'Veg Pulao'], '4': [120,'Khichdi'], '5': [145,'Veg Biryani']}, 7: {'1': [80,'Dal Fry'], '2': [90,'Dal Tadka'], '3': [90,'Dal Masala'], '4': [125,'Dal Makhni'], '5': [125,'Kadhi Pakoda']}}
    here = disc[cat]
    inside = here[no]
    loc=inside[0]*quant
    total += loc
    str = []
    str.append(inside[1])
    str.append(inside[0])
    str.append(quant)
    str.append(loc)
    description.append(str)
    print(str)


# Table
table = {'2': 10, '4': 12, '6': 8}
print("-" * 10, "Table Description", "-" * 10)
print("2 person")
print("4 person")
print("6 person")
tb = input("Choose Table : ")
print("-" * 145)
if tb not in table:
    print("Invalid value entered ! \n Try Again and Enter 2,4 or 6.")
else:
    if table[tb] == 0:
        print(f"Table for {tb} persons are full !!!")
    else:
        table[tb] -= 1
        print("Menu Card")
        more = 'Y'
        # print("Choose Category")
        # print("BEVERAGES : 'A'")
        # print("Snacks : 'B'")
        # print("South Indian : 'C'")
        # print("Chinese : 'D'")
        # print("BREAD : 'E'")
        # print("RICE : 'F'")
        # print("DAL : 'G'")
        while more == 'Y':
            menu = {'A': "Beverages", 'B': "Snacks", 'C': "South Indian", 'D': "Chinese", 'E': "Bread", 'F': "Rice",
                    'G': "Dal"}
            print(menu)
            cat = input("Enter your Choice : ").upper()
            if cat == 'A':
                print("BEVERAGES ")
                print("1.Tea\t25/-")
                print("2.Coffee\t35/-")
                print("3.Cold Coffee\t40/-")
                print("4.ButterMilk\t30/-")
                print("5.Lassi\t50/-")
                print("6.Soda\t20/-")
                taken = input("Enter item No:")
                lis = ['1','2','3','4','5','6']
                if taken not in lis:
                    print("Invalid value entered !!")
                    more = "N"
                else:
                    quant = int(input("Enter Quantity:"))
                    calc(1, taken, quant)
                    more = input("Do you want anything else?\nEnter 'y' if yes :").upper()
            elif cat == 'B':
                print("Snacks ")
                print("1.French Fries\t60/-")
                print("2.Potato Wedges\t70/-")
                print("3.Sandwich\t75/-")
                print("4.Kothe\t60/-")
                print("5.Burger\t120/-")
                taken = input("Enter item No:")
                lis = ['1','2','3','4','5']
                if taken not in lis:
                    print("Invalid value entered !!")
                    more = "N"
                else:
                    quant = int(input("Enter Quantity:"))
                    calc(2, taken, quant)
                    more = input("Do you want anything else?\nEnter 'y' if yes :").upper()
            elif cat == 'C':
                print("South Indian ")
                print("1.Idli Sambhar\t35/-")
                print("2.Medu Wada\t40/-")
                print("3.Plain Dosa\t45/-")
                print("4.Masala Dosa\t50/-")
                print("5.Uttapam\t65/-")
                taken = input("Enter item No:")
                lis = ['1','2','3','4','5','6']
                if taken not in lis:
                    print("Invalid value entered !!")
                    more = "N"
                else:
                    quant = int(input("Enter Quantity:"))
                    calc(3, taken, quant)
                    more = input("Do you want anything else?\nEnter 'y' if yes :").upper()
            elif cat == 'E':
                print("BREAD ")
                print("1.Roti\t15/-")
                print("2.Naan\t35/-")
                print("3.Paratha\t20/-")
                print("4.Tandoori Roti\t25/-")
                print("5.Rumali Roti\t25/-")
                taken = input("Enter item No:")
                lis = ['1','2','3','4','5','6']
                if taken not in lis:
                    print("Invalid value entered !!")
                    more = "N"
                else:
                    quant = int(input("Enter Quantity:"))
                    calc(5, taken, quant)
                    more = input("Do you want anything else?\nEnter 'y' if yes :").upper()
            elif cat == 'F':
                print("RICE ")
                print("1.Steamed Rice\t45/-")
                print("2.Jeera\t65/-")
                print("3.Veg Pulao\t100/-")
                print("4.Khichdi\t120/-")
                print("5.Veg Biryani\t145/-")
                taken = input("Enter item No:")
                lis = ['1','2','3','4','5','6']
                if taken not in lis:
                    print("Invalid value entered !!")
                    more = "N"
                else:
                    quant = int(input("Enter Quantity:"))
                    calc(6, taken, quant)
                    more = input("Do you want anything else?\nEnter 'y' if yes :").upper()
            elif cat == 'G':
                print("DAL ")
                print("1.Dal Fry\t80/-")
                print("2.Dal Tadka\t90/-")
                print("3.Dal Masala\t90/-")
                print("4.Dal Makhni\t125/-")
                print("5.Kadhi Pakoda\t125/-")
                taken = input("Enter item No:")
                lis = ['1','2','3','4','5','6']
                if taken not in lis:
                    print("Invalid value entered !!")
                    more = "N"
                else:
                    quant = int(input("Enter Quantity:"))
                    calc(7, taken, quant)
                    more = input("Do you want anything else?\nEnter 'y' if yes :").upper()
            elif cat == 'D':
                print("Chinese ")
                print("1.Manchurian\t120/-")
                print("2.Noodles\t200/-")
                print("3.Manchow Soup\t100/-")
                print("4.Spring Rolls\t100/-")
                print("5.Prauns\t250/-")
                taken = input("Enter item No:")
                lis = ['1','2','3','4','5','6']
                if taken not in lis:
                    print("Invalid value entered !!")
                    more="N"
                else:
                    quant = int(input("Enter Quantity:"))
                    calc(4, taken, quant)
                    more = input("Do you want anything else?\nEnter 'y' if yes :").upper()
            else:
                print("Invalid Value Entered !!")
                more = 'N'

    print("-" * 145)
    print("*" * 145)
    print("WELCOME TO SOON FATT".center(columns))
    print("Mig 22 A , Sonagiri  Bhopal, 462022 ".center(columns))
    print("Contacts: 9876543210 07642-250815".center(columns))
    print("Email-SOONFATTservices@gmail.com".center(columns))
    print("Date:", datetime.date(2022, 9, 21))
    print("Customer Name:", name)
    print("-" * 145)
    print(" " * 10, "ORDER SUMMARY", " " * 10)
    for i in description:
        print(i[0],"\t",i[1],"\t",i[2],"\t",i[3],"/-")
    print("\t\t\t\tTotal:", total,"/-")
    print("\n\n","*" * 144,"\n")
    print("THANKYOU VISIT AGAIN".center(columns),"\n")
    print("*" * 145)