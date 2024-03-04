"""
CMPS 2200  Assignment 2.
See assignment-02.pdf for details.
"""
import time

class BinaryNumber:
    """ done """
    def __init__(self, n):
        self.decimal_val = n               
        self.binary_vec = list('{0:b}'.format(n)) 
        
    def __repr__(self):
        return('decimal=%d binary=%s' % (self.decimal_val, ''.join(self.binary_vec)))
    

## Implement multiplication functions here. Note that you will have to
## ensure that x, y are appropriately sized binary vectors for a
## divide and conquer approach.
def binary2int(binary_vec): 
    if len(binary_vec) == 0:
        return BinaryNumber(0)
    return BinaryNumber(int(''.join(binary_vec), 2))

def split_number(vec):
    return (binary2int(vec[:len(vec)//2]),
            binary2int(vec[len(vec)//2:]))

def bit_shift(number, n):
    # append n 0s to this number's binary string
    return binary2int(number.binary_vec + ['0'] * n)
    
def pad(x,y):
    # pad with leading 0 if x/y have different number of bits
    # e.g., [1,0] vs [1]
    if len(x) < len(y):
        x = ['0'] * (len(y)-len(x)) + x
    elif len(y) < len(x):
        y = ['0'] * (len(x)-len(y)) + y
    # pad with leading 0 if not even number of bits
    if len(x) % 2 != 0:
        x = ['0'] + x
        y = ['0'] + y
    return x,y



def subquadratic_multiply(x, y):

  xVector = x.binary_vec
  yVector = y.binary_vec
  xVector, yVector = pad(xVector, yVector)
  if x.decimal_val <= 1 and y.decimal_val <= 1:
    return BinaryNumber(x.decimal_val * y.decimal_val)

  xLeft, xRight = split_number(xVector) 
  yLeft, yRight = split_number(yVector)

  leftProduct = subquadratic_multiply(xLeft, yLeft)
  rightProduct = subquadratic_multiply(xRight, yRight)

  xSum = BinaryNumber(xLeft.decimal_val + xRight.decimal_val)
  ySum = BinaryNumber(yLeft.decimal_val + yRight.decimal_val)

  middleTerm = BinaryNumber(subquadratic_multiply(xSum, ySum).decimal_val - leftProduct.decimal_val - rightProduct.decimal_val)

  middleTerm = bit_shift(middleTerm, len(xVector)//2)
  leftProduct = bit_shift(leftProduct, len(xVector))

  r = BinaryNumber(leftProduct.decimal_val + middleTerm.decimal_val + rightProduct.decimal_val)
  return r


def time_multiply(x, y, f):
    start = time.time()
    # multiply two numbers x, y using function f
    return (time.time() - start)*1000

    
    

