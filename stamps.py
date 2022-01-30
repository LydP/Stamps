import random

# create list of stamps and prices
# arbitrary price range
stamp_sell_price = [round(random.uniform(0, 10), 2) for i in range(1000)]
print("Most expensive stamp's price:", max(stamp_sell_price))

# copy list to preserve original
stamps = stamp_sell_price[:]
pairs = []
for i in range(500):
    # two random samples without replacement
    two_stamps = random.sample(list(enumerate(stamps)), 1)
    price_temp1 = stamps.pop(two_stamps[0][0])
    index_temp1 = two_stamps[0][0]

    two_stamps = random.sample(list(enumerate(stamps)), 1)
    price_temp2 = stamps.pop(two_stamps[0][0])
    index_temp2 = two_stamps[0][0]

    pairs.append((index_temp1, index_temp2, price_temp1 + price_temp2))

# sort and retrieve 200 most expensive pairs
pairs.sort(key=lambda x: x[2])
pairs = pairs[:400]

stamps = []
for i in pairs:
    first_index = i[0]
    second_index = i[1]
    stamps.extend([stamp_sell_price[first_index], stamp_sell_price[second_index]])

print("Most expensive stamp's price after sorting:", max(stamps))
