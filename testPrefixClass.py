import prefix

# checks if special char exists
# p = prefix.Prefix('@')
# if p.containsSpecialChar() == True:
#     print("contains special char")
# else:
#     print("does not contain special char")

# checks if countOperators func works
# p = prefix.Prefix('+/*')
# num = p.getNumOperators()
# print(num)

# checks if countOperands func works
# p = prefix.Prefix('1A2b3c')
# num = p.getNumOperands()
# print(num)

# checks if operator < operand
# p = prefix.Prefix('1A2b3c')
# if p.operatorLessThanOperand == True:
#     print("eyyy nice one")
# else:
#     print("oh no dapat less than ang operator sah operand")

# checks if expression contains an operator and at least 2 operands
# p = prefix.Prefix('+ 3')
# num1 = p.getNumOperands()
# print(num1)
# num = p.getNumOperands()
# print(num)
# if p.completePrefix == True:
#     print("eyyy nice one")
# else:
#     print("luh kulangan")

# p = prefix.Prefix('+ 35')
# num1 = p.getNumOperators()
# print(num1)
# num = p.getNumOperands()
# print(num)
# if p.completePrefix() == True:
#     print("eyyy nice one")
# else:
#     print("luh kulangan")

# print(p.isPrefix())

p = prefix.Prefix('+ 35 -')
num1 = p.getNumOperators()
print(num1)
num = p.getNumOperands()
print(num)
if p.completePrefix() == True:
    print("eyyy nice one")
else:
    print("luh kulangan")

print(p.isPrefix())
