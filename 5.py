for n in range(200, 1, -1):
    b = bin(n)[2:]
    if n % 2 == 0:
        b += '01'
    else:
        b = '1' + b + '10'
    r = int(b, 2)
    if r < 105:
        print(n)
        break
        
