price=int(input("Ingrese el precio del producto: "))
if price<100:
    discount=(price*0.02)
else:
    discount=(price*0.10)
final_price=price-discount
print(final_price)