product1 = input().split(" ")
product2 = input().split(" ")

'''
Python 2 muda para raw_input, ex.:
product1 = raw_input().split(" ")
'''

code1 = product1[0]
units1 = int(product1[1])
price1 = float(product1[2])

code2 = product2[0]
units2 = int(product2[1])
price2 = float(product2[2])

result1 = units1 * price1
result2 = units2 * price2
total = result1 + result2

print("VALOR A PAGAR: R$ %1.2f" %(total))
