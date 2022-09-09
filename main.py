a = 0
b = 0

changed_references = False
while not changed_references:
    if a is b:
        a += 1
        b += 1
    else:  # a is not b
        print("Share reference for int <", a or b)
        changed_references = True
