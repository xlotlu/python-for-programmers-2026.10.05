# Write a program that will compute the net price and VAT for a product. First,
# ask the user what product they bought. Then, ask them how much they paid for
# that product. Considering VAT is 19% of the price, compute the net price of
# the product and the VAT value. Then, display the following message:
# You bought a <product_name> for which you paid <net_price> + <vat_value> VAT.

product = input("What did you buy? ")
price = float(input("How much did you pay for it? "))

net_price = price / 1.19
vat = price - net_price
print(f"You bought a {product} for which you paid {net_price:.2f} + {vat:.2f}"
      " VAT.")
