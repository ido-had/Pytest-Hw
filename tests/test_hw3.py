import hw3
import pytest
import logging
import sys


@pytest.fixture
def data_load():
    return {3322117:{"name": "Tal", "sex": "male", "age": 12},332117:{"name": "Tl", "sex": "male", "age": 1},
              176864301:{"sex": "female", "age": 57, "height": 1.65,"name": "Anat"},
              1764301:{"sex": "female", "age": 5, "height": 1.65,"name": "Ana"}}

def test_split_male_female(data_load):
    male,female=hw3.split_male_female(data_load)
    logging.info(male)
    lst=[]
    for key,values in male.items():
        lst.append(values["sex"])
    lst2=[]
    for key,values in female.items():
        lst2.append(values["sex"])
    assert ("male") in lst
    assert ("female") not in lst
    assert len(lst)==2
    assert len(lst2)==2
    assert ("male") not in lst2
    assert ("female")  in lst2


def test_mean_median(capsys,data_load):
    hw3.find_median_average(data_load)
    captured=capsys.readouterr()
    str=captured.out
    assert "18.75" in str
    assert "8.5" in str
    #mean=18.75 median=8.5

def test_print_above(capsys,data_load):
    pass

