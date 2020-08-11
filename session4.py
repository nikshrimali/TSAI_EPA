import random
import decimal
from decimal import Decimal
import math

class Qualean():
    def __init__(self,rand_num):
        self.rand_num = rand_num
        self.input_valid()

    def input_valid(self):
        with decimal.localcontext() as ctx:
            ctx.prec = 10

            if self.rand_num == 1 or self.rand_num == -1:
                self.rand_num = (self.rand_num)
                self._imgnum = Decimal(random.uniform(-1,1))
                self._state = (self.rand_num * self._imgnum)
                # print(self._state)
                return self._state

            elif self.rand_num == 0:
                self._state = 0
                return self._state
            else:
                raise ValueError('Only numbers between 0, 1 and -1 are allowed')
    def get_value(self):
        return self._state


    def __and__(self, other):
        if isinstance(other, Qualean):
            return bool(self._state) and bool(other._state)
        else:
            False


    def __or__(self,other):
        if isinstance(other, Qualean):
            return bool(self._state) or bool(other._state)
        else:
            return None

    def __repr__(self):
        return 'Qualean({0})'.format(self._state)

    
    def __str__(self):
        return 'Qualean({0})'.format(self._state)
    
    def __add__(self, other):
        if isinstance(other,Qualean):
            return self._state + other._state
        else:
            return None

    def __eq__(self, other):
        if isinstance(other,Qualean):
            return True if self._state == other._state else False

    def __float__(self):
        return (self._state/1.0)

    
    def __ge__(self, other):
        if isinstance(other,Qualean):
            return True if self._state >= other._state else False

    def __gt__(self, other):
        if isinstance(other,Qualean):
            return True if self._state > other._state else False

    
    def __invertsign__(self):
        return self._state*(-1)

    def __mul__(self, other):
        if isinstance(other,Qualean):
            return self._state * other._state
        else:
            return False
    
    def __sqrt__(self):
        a = Decimal.sqrt(self._state)
        return a

    def __bool__(self):
        return bool(self._state)