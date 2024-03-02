import streamlit as st
import yaml, sys, logging, os
import pandas as pd
import logging.config
from models.model import Stock, Item, Admin, Transaction

#log_file_dir = os.environ['LOG_FILE_PATH']  # Log file directory supplied from command line
logging_config_file = "logging.yaml"

# Read the logging configuration file and substitute the log file directory
with open(logging_config_file, "r") as f:
    logging_config = f.read()

# Configure logging
logging.config.dictConfig(yaml.safe_load(logging_config))
#logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def initialize_stock():
    if 'stock' not in st.session_state:
        st.session_state.stock = Stock()
# Initialize the stock object
initialize_stock()
# Create a global Stock instance

# Create a global Admin instance
admin = Admin(st.session_state.stock)

# Create a global Transaction instance
transaction = Transaction()

#from auth import authenticate, logout, get_user_email
# Authenticate user
#authenticate()

# Main application logic

# Helper function to display available stocks
def display_stocks():
    logger.info(f"Displaying stocks:{admin.stock}")
    st.subheader("Available Stocks")
    if admin.stock.items:
        st.write("Items in Stock:")
        # Convert items to a list of dictionaries for table display
        item_data = [{"Item": item.name, "Price": item.price, "Quantity": item.quantity} for item in admin.stock.items]
        st.table(item_data)
    else:
        st.write("No items in stock.")


# Main function for the Streamlit app
def main():
    st.title("Inventory Management System")

    menu = ["View Stocks", "Add Item", "Remove Item", "Update Item", "Record Transaction"]
    choice = st.sidebar.selectbox("Menu", menu)

    try:
        if choice == "View Stocks":
            display_stocks()
        elif choice == "Add Item":
            st.subheader("Add New Item")
            name = st.text_input("Name")
            price = st.number_input("Price", min_value=0.0)
            quantity = st.number_input("Quantity", min_value=0, step=1)
            if st.button("Add"):
                logger.info("Adding new item")
                if name.strip() and price > 0 and quantity >= 0:
                    logger.info(f"Adding new item:{name}, {price}, {quantity}")
                    new_item = Item(name, price, quantity)
                    admin.add_stock_item(new_item)
                    st.success("Item added successfully!")
                    logger.info(f"Added new item: {admin.stock}")
                else:
                    st.error("Invalid input!")
                    logger.error("Invalid input for adding item.")

        elif choice == "Remove Item":
            st.subheader("Remove Item")
            item_name = st.text_input("Item Name")
            if st.button("Remove"):
                if item_name.strip():
                    item = admin.check_stock(item_name)
                    if item:
                        admin.remove_stock_item(item)
                        st.success("Item removed successfully!")
                        logger.info(f"Removed item: {item_name}")
                    else:
                        st.error("Item not found!")
                        logger.error(f"Item not found for removal: {item_name}")
                else:
                    st.error("Invalid input!")
                    logger.error("Invalid input for removing item.")

        elif choice == "Update Item":
            st.subheader("Update Item")
            item_name = st.text_input("Item Name")
            new_name = st.text_input("New Name")
            new_price = st.number_input("New Price", min_value=0.0)
            new_quantity = st.number_input("New Quantity", min_value=0, step=1)
            if st.button("Update"):
                if item_name.strip() and (new_name.strip() or new_price > 0 or new_quantity >= 0):
                    item = admin.check_stock(item_name)
                    if item:
                        updated_item = Item(new_name, new_price, new_quantity)
                        admin.update_stock_item(item_name, updated_item)
                        st.success("Item updated successfully!")
                        logger.info(
                            f"Updated item: {item_name} - New Name: {new_name}, New Price: {new_price}, New Quantity: {new_quantity}")
                    else:
                        st.error("Item not found!")
                        logger.error(f"Item not found for update: {item_name}")
                else:
                    st.error("Invalid input!")
                    logger.error("Invalid input for updating item.")

        elif choice == "Record Transaction":
            st.subheader("Record Transaction")
            item_name = st.text_input("Item Name")
            quantity_sold = st.number_input("Quantity Sold", min_value=0, step=1)
            if st.button("Record Transaction"):
                if item_name.strip() and quantity_sold > 0:
                    item = admin.check_stock(item_name)
                    if item and item.quantity >= quantity_sold:
                        # Update stock
                        updated_quantity = item.quantity - quantity_sold
                        item.update_quantity(updated_quantity)
                        # Record transaction
                        transaction.add_sale(item, quantity_sold)
                        st.success("Transaction recorded successfully!")
                        logger.info(f"Recorded transaction for item: {item_name}, Quantity Sold: {quantity_sold}")
                    else:
                        st.error("Insufficient stock!")
                        logger.error(f"Insufficient stock for transaction: {item_name}, Quantity Sold: {quantity_sold}")
                else:
                    st.error("Invalid input!")
                    logger.error("Invalid input for recording transaction.")

    except Exception as e:
        st.error("An error occurred. Please try again.")
        logger.error(f"An error occurred: {str(e)}")

def load_stocks_from_csv():
    if len(admin.stock.items) == 0:
        stocks_data = pd.read_csv('stocks.csv')
        for index, row in stocks_data.iterrows():
            item = Item(row['name'], row['quantity'], row['price'])
            admin.add_stock_item(item)

load_stocks_from_csv()

if __name__ == "__main__":
    main()
