

while(True):
    price_A4_sheet = float(input('Cost of A4sheet:'))
    if price_A4_sheet<0:break
    price_pen = float(input('Cost of pen:'))
    if price_pen<0:break
    price_pencil = float(input('Cost of pencil:'))
    if price_pencil<0:break
    price_eraser = float(input('Cost of eraser:'))
    if price_eraser<0:break

    print("Items Details")
    print(f"A4sheet:{price_A4_sheet:.2f}")
    print(f"Pen:{price_pen:.2f}")
    print(f"Pencil:{price_pencil:.2f}")
    print(f"Eraser:{price_eraser:.2f}")
    break