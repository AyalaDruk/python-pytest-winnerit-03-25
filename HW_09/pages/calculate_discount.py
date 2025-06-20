def calculate_discount(price:float,discount_percent:float):
    if price < 0 or discount_percent < 0:
        raise ValueError ("price and discount must be not-negative")
    else:
        return price*(1-discount_percent/100)
