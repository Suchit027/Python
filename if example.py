# notice None
largest = None
print('Before:', largest)
for val in [30, 45, 12, 90, 74, 15]:
    
    # comparison with None can only be done with is; no operators like == are allowed
    if largest is None or val > largest:
        largest = val
        print('Loop', val, largest)

print('Largest', largest)