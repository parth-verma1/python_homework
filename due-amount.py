def due(bill, paid):
    amt = paid - bill
    return amt

b = float(input("bill? "))
p = float(input("paid? "))
print("return:", due(b, p))
