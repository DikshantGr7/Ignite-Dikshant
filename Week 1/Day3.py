
from functools import reduce

class InvalidOrderError(Exception):
    pass


class Order:
    def __init__(self, order_id: str, items: list[dict]):
        self.order_id = order_id
        self.items = items  


def process_order_invoice(order: Order, tax_rate: float = 0.08) -> dict:
    if not order.items:
        raise InvalidOrderError(f"Order '{order.order_id}' contains no items.")

    for item in order.items:
        if item.get("price", 0) < 0:
            raise ValueError(f"Item '{item.get('name')}' has an invalid negative price.")

    subtotal = sum(item["price"] for item in order.items)
    
    taxable_items = list(filter(lambda x: x.get("taxable", True), order.items))
    taxable_sum = sum(item["price"] for item in taxable_items)
    tax = round(taxable_sum * tax_rate, 2)

    return {
        "order_id": order.order_id,
        "item_count": len(order.items),
        "subtotal": subtotal,
        "tax": tax,
        "grand_total": round(subtotal + tax, 2)
    }


def examples():
    print("--- 1. Lambda & Higher-Order Functions ---")
    
    data = [12.5, 45.0, 8.0, 150.0, 22.0]

    discounted = list(map(lambda price: round(price * 0.9, 2), data))
    print(f"Original Prices:   {data}")
    print(f"Discounted (10%):  {discounted}")

    
    premium_items = list(filter(lambda price: price > 20.0, discounted))
    print(f"Premium (> $20):   {premium_items}")


    total_cost = reduce(lambda acc, price: acc + price, premium_items, 0.0)
    print(f"Total Premium Sum: ${total_cost:.2f}\n")


def save_invoice_to_file(invoice: dict, filename: str = "day_3_output.txt"):
    """Demonstrates File Handling ('with') and Exception Handling."""
    print("--- 2. File Handling & Exception Handling ---")
    
    try:
        with open(filename, "a", encoding="utf-8") as file:
            file.write(f"=== INVOICE: {invoice['order_id']} ===\n")
            file.write(f"Item Count:  {invoice['item_count']}\n")
            file.write(f"Subtotal:    ${invoice['subtotal']:.2f}\n")
            file.write(f"Tax:         ${invoice['tax']:.2f}\n")
            file.write(f"Grand Total: ${invoice['grand_total']:.2f}\n")
            file.write("-" * 30 + "\n\n")
        
        print(f"Successfully appended invoice '{invoice['order_id']}' to '{filename}'.")

        print(f"\n--- Reading Contents from '{filename}' ---")
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()
            print(content)

    except IOError as ioe:
        print(f"File System Error: Could not write/read file. Details: {ioe}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    else:
        print("File operations executed with zero errors.")
    finally:
        print("Completed file processing block.\n")


def main():
    examples()
    sample_cart = [
        {"name": "Mechanical Keyboard", "price": 120.00, "taxable": True},
        {"name": "Software License", "price": 45.00, "taxable": False},
        {"name": "USB-C Cable", "price": 15.00, "taxable": True}
    ]
    valid_order = Order(order_id="ORD-2026-X9", items=sample_cart)

    try:
        invoice_data = process_order_invoice(valid_order, tax_rate=0.07)
        print("Invoice Processing Success!")
        print(f"Generated Grand Total: ${invoice_data['grand_total']:.2f}\n")
        
        save_invoice_to_file(invoice_data)

    except InvalidOrderError as ioe:
        print(f"Validation Failed: {ioe}")
    except ValueError as ve:
        print(f"Data Error: {ve}")

if __name__ == "__main__":
    main()