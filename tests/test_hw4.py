import hw4
import pytest
import logging

def test_init(capsys): #date instance creating test
    dt1=hw4.Date("a","b","c")
    captured=capsys.readouterr()
    logging.debug("creating Date instance with invalid parameters")
    assert  "invalid" in captured.out
    logging.info("result for invalid parameters printed '"+captured.out+"' ,instance created: date="+dt1.__str__())
    dt1=hw4.Date(1,1,2001)
    assert dt1._day==1
    assert dt1._month==1
    assert dt1._year==2001

def test_str(): #__str__ test
    dt1=hw4.Date(1,2,2012)
    str1=dt1.__str__()
    assert str1=="1\\2\\2012"
    logging.info("instance of date(1.2.2012) __str__ func result:"+str1)

def test_isValid():
    dt1=hw4.Date(31,2,2001) #invalid feb days
    logging.info("isValid func result on invalid date 31.2.2001")
    assert dt1.isValid()==False
    dt1=hw4.Date(29,2,2000) #valid feb days leap year
    logging.info("isValid func result on valid date 29.2.2000")
    assert dt1.isValid()==True

def test_getNextDay():
    dt1=hw4.Date(29,2,2000)
    dt2=dt1.getNextDay()
    logging.debug("getnextday func triggered on 29.2.2000 date instance expected result-1.3.2000")
    dt3=hw4.Date(1,3,2000)
    assert dt3==dt2

def test_getNextDays():
    dt1=hw4.Date(29,2,2000)
    dt2=dt1.getNextDays(2)
    dt3=hw4.Date(2,3,2000)
    logging.debug("getnextdays(2) func triggered on 29.2.2000 date instance expected result-2.3.2000")
    assert dt3==dt2

def test_sub(): #__sub__ function test
    dt3=hw4.Date(2,3,2000)
    dt1=hw4.Date(29,2,2000)
    logging.debug("2.3.2000-29.02.2000 expected result 2")
    assert dt3-dt1==2

def test_operators(): #operators lt,gt etc. tests
    logging.debug("operators tests")
    dt3=hw4.Date(2,3,2000)
    dt1=hw4.Date(29,2,2000)
    assert dt3>dt1
    assert not dt3<dt1
    assert dt3!=dt1
    dt3=hw4.Date(29,2,2000)
    assert dt3==dt1
    assert dt3<=dt1
    assert dt3>=dt1





