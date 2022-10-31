
import sys
sys.path.insert(0,"..")
import BestTimeBuySellStock
from BestTimeBuySellStock import bestTimeBuySellStockII


s1 = [1,2,3,4,5,6]
s2 = [7,1,5,3,6,4]
s3 = [1,2,3,4,5]
s4 = [7,6,4,3,1]

test = bestTimeBuySellStockII.

def test_s1():
    assert test.maxProfit(s1) == 5

def test_s2():
    assert test.maxProfit(s2) == 7

def test_s3():
    assert test.maxProfit(s3) == 4

def test_s4():
    assert test.maxProfit(s4) == 0
