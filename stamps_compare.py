import random
from sklearn.metrics import mean_squared_error
import math

# create list of stamps and prices
# arbitrary price range
stamp_sell_price = [round(random.uniform(0, 10), 2) for i in range(1000)]

method1 = []
method2 = []
for i in range(500):
    # METHOD 1
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

    stamps = [f(x) for x in pairs for f in (lambda x: stamp_sell_price[x[0]], lambda x: stamp_sell_price[x[1]])]

    method1.append(max(stamps))

    # METHOD 2
    stamps = stamp_sell_price[:]
    for i in range(7):
        stamps1 = stamps[len(stamps) // 2:]
        stamps2 = stamps[:len(stamps) // 2]

        biggest_sale = [sum(stamps1), sum(stamps2)]
        biggest_sale_index = biggest_sale.index(max(biggest_sale))

        if biggest_sale_index == 0:
            stamps = stamps1
        else:
            stamps = stamps2

    method2.append(max(stamps))

temp = [max(stamp_sell_price) for i in range(500)]
mse1 = mean_squared_error(method1, temp)
rmse1 = math.sqrt(mse1)

mse2 = mean_squared_error(method2, temp)
rmse2 = math.sqrt(mse2)

print("RMSE of Method 1:", rmse1)
print("RMSE of Method 2:", rmse2)