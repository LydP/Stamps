import random

# create list of stamps and prices
# arbitrary price range
stamp_sell_price = [round(random.uniform(0, 10), 2) for i in range(1000)]
print("Most expensive stamp's price:", max(stamp_sell_price))

for i in range(7):
    # divide list in half
    stamps1 = stamp_sell_price[len(stamp_sell_price) // 2:]
    stamps2 = stamp_sell_price[:len(stamp_sell_price) // 2]

    # find the list with the most value
    biggest_sale = [sum(stamps1), sum(stamps2)]
    biggest_sale_index = biggest_sale.index(max(biggest_sale))

    if biggest_sale_index == 0:
        stamp_sell_price = stamps1
    else:
        stamp_sell_price = stamps2

print("Most expensive stamp's price after sorting:", max(stamp_sell_price))
