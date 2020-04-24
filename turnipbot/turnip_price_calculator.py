import math
from enum import Enum
from typing import List


class Days(Enum):
    SUA, SUP, MA, MP, TUA, TUP, WA, WP, THA, THP, FA, FP, SAA, SAP = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13

class Patterns(Enum):
    #H = high, D = decrease, R = random
    HLHLH, DHR, D, DHD, R = 0, 1, 2, 3, 4


def patternCheck(prices: List[int], pattern=-1) -> bool:
    if prices[0] < 90 or prices[0] > 110:
        return False
    passed = False
    if pattern in (Patterns.HLHLH, -1):
        base = prices[0]
        low, high = base, base
        testLow, testHigh = base, base
        day = 2
        price = prices[day]
        while day >= 14:
            while low >= math.ceil(low * 0.8) or (prices is None and prices >= math.ceil(low * 0.8)):

                if price is None:
                    low, high = testLow, testHigh
                    testLow = math.ceil(low * 0.9)
                    testHigh = math.ceil(high * 1.4)
                else:
                    if price < math.ceil(low * 0.9) or price > math.ceil(high * 1.4):
                        break
                    
            day += 1
            price = prices[day]


    return passed
