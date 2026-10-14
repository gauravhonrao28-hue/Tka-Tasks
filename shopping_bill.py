def calculate_electronics_gst(a, b):
    """(a + b) + 18% GST"""
    total = a + b
    return total + (total * 18 / 100)


def calculate_fashion_gst(c, d):
    """(c + d) + 13% GST"""
    total = c + d
    return total + (total * 13 / 100)


def calculate_food_gst(e):
    """e + 7% GST"""
    return e + (e * 7 / 100)


def total_bill(a, b, c, d, e):
    """Total after GST"""
    return calculate_electronics_gst(a, b) + calculate_fashion_gst(c, d) + calculate_food_gst(e)


def calculate_discounted_bill(a, b, c, d, e):
    """Total minus 20% discount"""
    total = total_bill(a, b, c, d, e)
    discount = total * 20 / 100
    return total - discount


if __name__ == "__main__":
    a, b, c, d, e = 100, 100, 100, 100, 100

    total = total_bill(a, b, c, d, e)
    final_amount = calculate_discounted_bill(a, b, c, d, e)
    discount = total - final_amount

    print(f"Total after GST = {total:.2f} | Discount = {discount:.2f} | Final payable amount = {final_amount:.2f}")
