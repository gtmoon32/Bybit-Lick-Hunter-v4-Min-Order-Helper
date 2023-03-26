# Bybit-Lick-Hunter-v4-Min-Order-Helper

I created a python script to automatically list coins in the format for putting in the blacklist section, if the coin's min order size is a certain usdt value. This is very useful for small accounts to eliminate any coins that will use a large precent of the account. Simply change the value of 0.05 in this line warning = "WARNING" if min_order_value_result > 0.05 else "" to whatever usdt value, the default it 5 cents
