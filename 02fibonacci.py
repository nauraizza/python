a, b, c = 0, 1, 0

batas= int (input('Masukkan batas : '))
for i in range(batas):
    print(a, ' ', end='')
    c=a+b
    a=b
    b=c