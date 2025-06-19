import os
import json
from datetime import datetime
import uuid

class CURD:
    def __init__(self, name="BlessedBug", password="#Blessed404"):
        self.name = name
        self.password = password
        self.stock_path = "/home/danzo/Documents/github/stock.json"
        self.log_path = "/home/danzo/Documents/github/timestamps.txt"

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def create_operations(self):
        stock = []

        while True:
            try:
                product_id = input("Enter the Product ID (or press Enter to finish): ")
            except (EOFError, OSError):
                break
            if product_id == "":
                break

            product_name = input("Product Name: ")
            try:
                product_price = int(input("Product Price: "))
            except ValueError:
                print("Invalid price! Must be a number.")
                continue

            description = input("Enter the Product Description: ")
            try:
                quantity = int(input("Enter Product Quantity: "))
            except ValueError:
                print("Invalid quantity! Must be a number.")
                continue

            product = {
                "product_id": product_id,
                "product_name": product_name,
                "product_price": product_price,
                "product_description": description,
                "product_quantity": quantity
            }

            stock.append(product)

            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            try:
                with open(self.log_path, 'a') as log_file:
                    log_file.write(
                        f"{timestamp} | {self.name} added product_id: {product_id}, name: {product_name}, price: {product_price}, quantity: {quantity}, description: {description}\n")
            except FileNotFoundError:
                print("Log file not found.")

        try:
            with open(self.stock_path, 'r') as stock_file:
                existing_stock = json.load(stock_file)
        except (FileNotFoundError, json.JSONDecodeError):
            existing_stock = []

        existing_stock.extend(stock)

        with open(self.stock_path, 'w') as stock_file:
            json.dump(existing_stock, stock_file, indent=4)

        print("Stock added successfully.")

    def update(self):
        try:
            with open(self.stock_path, 'r') as stock_file:
                products = json.load(stock_file)
        except (FileNotFoundError, json.JSONDecodeError):
            print("Unable to read stock file")
            return

        for product in products:
            print(f"{product['product_id']}    {product['product_name']}    {product['product_price']}    {product['product_description']}    {product['product_quantity']}")

        stock_input = input("Choose a product by product name or product id (or press Enter to return): ").strip()
        if stock_input == "":
            return

        for product in products:
            if str(product["product_id"]) == stock_input or product["product_name"].lower() == stock_input.lower():
                while True:
                    change_input = input("What do you want to change: product_id, product_name, product_price, product_description, product_quantity (or press Enter to stop): ").strip()
                    if change_input == "":
                        break
                    if change_input not in product:
                        print("Invalid field")
                        continue
                    changed_input = input(f"Enter the new {change_input}: ").strip()
                    if change_input in ["product_price", "product_id", "product_quantity"]:
                        try:
                            changed_input = int(changed_input)
                        except ValueError:
                            print("Invalid number")
                            continue
                    old_value = product[change_input]
                    product[change_input] = changed_input

                    try:
                        with open(self.stock_path, 'w') as stock_file:
                            json.dump(products, stock_file, indent=4)
                    except Exception:
                        print("Error saving file")
                        return

                    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    try:
                        with open(self.log_path, 'a') as log_file:
                            log_file.write(
                                f"{timestamp} | {self.name} updated {change_input} of product_id: {product['product_id']} from '{old_value}' to '{changed_input}'\n")
                    except FileNotFoundError:
                        print("Log file not found.")

                    print("Product updated")
                break
        else:
            print("Product not found")

    def read(self):
        try:
            with open(self.stock_path, 'r') as stock_file:
                products = json.load(stock_file)
        except (FileNotFoundError, json.JSONDecodeError):
            print("Unable to read stock file")
            return

        if not products:
            print("No stock available")
            return

        for product in products:
            print(f"{product['product_id']}    {product['product_name']}    {product['product_price']}    {product['product_description']}    {product['product_quantity']}")

    def delete(self):
        try:
            with open(self.stock_path, 'r') as stock_file:
                products = json.load(stock_file)
        except (FileNotFoundError, json.JSONDecodeError):
            print("Unable to read stock file")
            return

        if not products:
            print("No products to delete")
            return

        for product in products:
            print(f"{product['product_id']}    {product['product_name']}    {product['product_price']}    {product['product_description']}    {product['product_quantity']}")

        stock_input = input("Choose a product by product name or product id to delete (or press Enter to return): ").strip()
        if stock_input == "":
            return

        for i, product in enumerate(products):
            if str(product["product_id"]) == stock_input or product["product_name"].lower() == stock_input.lower():
                deleted = products.pop(i)

                try:
                    with open(self.stock_path, 'w') as stock_file:
                        json.dump(products, stock_file, indent=4)
                except Exception:
                    print("Error saving file")
                    return

                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                try:
                    with open(self.log_path, 'a') as log_file:
                        log_file.write(
                            f"{timestamp} | {self.name} deleted product_id: {deleted['product_id']} name: {deleted['product_name']}\n")
                except FileNotFoundError:
                    print("Log file not found")

                print("Product deleted")
                break
        else:
            print("Product not found")

    def cred(self):
        if self.name == "BlessedBug" and self.password == "#Blessed404":
            while True:
                print(
                    "\nWelcome to Stock CURD operation\n"
                    "Press 1 to Add New Stock\n"
                    "Press 2 to Update/Modify Stock\n"
                    "Press 3 to View All Stock\n"
                    "Press 4 to Delete Stock\n"
                    "Press 5 to Exit"
                )
                try:
                    uinput = input("Your choice: ")
                except (EOFError, OSError):
                    break

                if uinput == "1":
                    self.create_operations()
                elif uinput == "2":
                    self.update()
                elif uinput == "3":
                    self.read()
                elif uinput == "4":
                    self.delete()
                elif uinput == "5":
                    print("Exiting...")
                    break
                else:
                    print("Invalid option")
        else:
            print("No access")

class Customer:
    def __init__(self):
        self.stock_path = "/home/danzo/Documents/github/stock.json"
        self.log_path = "/home/danzo/Documents/github/timestamps.txt"
        self.cu_list = []
        self.customer_id = str(uuid.uuid4())[:8]

    def view_products(self):
        try:
            with open(self.stock_path, 'r') as stock_file:
                products = json.load(stock_file)
        except (FileNotFoundError, json.JSONDecodeError):
            print("Unable to read stock file")
            return

        print("\nAvailable Products:")
        for product in products:
            print(f"{product['product_id']} - {product['product_name']} - {product['product_price']} PKR")

# Entry point to control user selection

def main():
    print("Welcome to Inventory System")
    print("1. Customer View")
    print("2. Admin (CURD) View")
    try:
        choice = input("Select an option (1 or 2): ").strip()
    except (EOFError, OSError):
        print("I/O not supported in this environment")
        return

    if choice == "1":
        customer = Customer()
        customer.view_products()
    elif choice == "2":
        try:
            username = input("Enter Admin Username: ")
            password = input("Enter Admin Password: ")
        except (EOFError, OSError):
            print("Input error")
            return
        with CURD(name=username, password=password) as app:
            app.cred()
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
