import csv
import re

try:
    with open("contact.csv"):
        pass
except FileNotFoundError:
    with open("contact.csv", "w") as file:
        write = csv.DictWriter(file, fieldnames=["Name", "Contact"])
        write.writeheader()
while True:
    try:
        menu = int(input("Choose from menu:\n 1 -- Add contact\n 2 -- Search by name\n 3 -- View all contact\n 4 -- Update any contact\n 5 -- Delete any contact\n 6 -- Quit "))
    except ValueError:
        print("Only numbers are supported\n")
        continue
    if menu == 1:
        nam = input("\nEnter name: ").strip().title()
        with open("contact.csv") as file:
            see = list(csv.DictReader(file))
        if duplicate := any(line['Name'] == nam for line in see): 
            print("A contact with same name already exists\n")
        else:
            while True:
                cont = input("Enter contact: ")
                if re.match(r"^(?:\+91)?(9|8|7|6)\d{9}$", cont):
                    with open("contact.csv", "a") as file:
                       write = csv.DictWriter(file, fieldnames=["Name", "Contact"])
                       write.writerow({"Name": nam, "Contact": cont})
                       print("Contact information added\n")
                       break     
                else:
                   print("\nKindly enter a valid Indian contact which:\n 1.Only have digits.\n 2.Have no special characters.\n 3.Have only 10 digits (+91 is optional).\n 4. Must starts with 9 or 8 or 7 or 6.\n")
                   ask = input("Do you want to retry: (yes/no) ").strip().lower()
                   if ask != "yes":
                       break
                   else:
                       continue
    elif menu == 2:
        srch = input("\nEnter the name to search: ").strip().title()
        with open("contact.csv") as file:
            read = list(csv.DictReader(file))
            for row in read:
                    if row["Name"] == srch:
                        print(f"The contact info of {srch} is {row['Contact']}\n")
                        break
            else:
                print("No contact exist with such name.\n")
    elif menu == 3:            
           with open("contact.csv") as file:
               read = list(csv.DictReader(file))
           if not read:
               print("No contacts saved yet\n")
           else:
               print(f"\n{'Name': <20} {'Contact': <15}")
               print("-" * 35)
               for row in read:
                   print(f"{row['Name']: <20} {row['Contact']: <15}")
               print(f"\nTotal contacts: {len(read)}\n")
           continue
    elif menu == 4:
        updat = input("\nEnter the name to update: ").strip().title()
        with open("contact.csv") as file:
            read = list(csv.DictReader(file))
            find = any(row["Name"] == updat for row in read)
        if not find:
            print("No contact found with that name\n")
        else:
            while True:
                new = input("\nEnter the updated contact: ")
                if re.match(r"^(?:\+91)?(9|8|7|6)\d{9}$", new):
                    remain = [row for row in read if row["Name"] != updat]
                    remain.append({"Name": updat, "Contact": new})
                    with open("contact.csv", "w", newline="") as file:
                        write = csv.DictWriter(file, fieldnames=["Name", "Contact"])
                        write.writeheader()
                        write.writerows(remain)
                    print(f"{updat} updated successfully\n") 
                    break
                else:
                    print("\nKindly enter a valid Indian contact which:\n 1.Only have digits.\n 2.Have no special characters.\n 3.Have only 10 digits (+91 is optional).\n 4. Must starts with 9 or 8 or 7 or 6.\n")
                    ask = input("Do you want to retry: (yes/no) ").strip().lower()
                    if ask != "yes":
                        print("\nUpdate cancelled. Contact unchanged.\n")
                        break           
    elif menu == 5:
        dlt = input("\nEnter the name to delete: ").strip().title()
        with open("contact.csv") as file:
            read = list(csv.DictReader(file))
            found = any(row["Name"] == dlt for row in read)
        if not found:
            print("No contact found with that name\n")
        else:
            updated = [row for row in read if row["Name"] != dlt]
            with open("contact.csv", "w", newline="") as file:
                write = csv.DictWriter(file, fieldnames=["Name", "Contact"])
                write.writeheader()
                write.writerows(updated)
            print(f"{dlt} deleted successfully\n")    
    elif menu == 6:
        print("\nContact book closed.")
        break
    else:
        print("Invalid input\n")
        continue