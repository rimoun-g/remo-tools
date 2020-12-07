# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 15:40:44 2020

@author: Rimoun
"""
import sys
sys.path.append("../")

from data_tools import DataTools  as dtools


def test_digits_only_0():
    assert (dtools.digits_only("as12as58")=="1258")

def test_digits_only_1():
    assert (dtools.digits_only("as")==None)
    
def test_email_format_check_0():
    assert (dtools.email_format_check("somemail@domain.com")==True)

def test_email_format_check_1():
    assert (dtools.email_format_check("somemaildomain.com@")==False)
    
def test_email_format_check_2():
    assert (dtools.email_format_check("somemail@domain.com@")==False)

def test_dates_difference_1():
    assert (dtools.days_between("01/11/2020","31/12/2020","years")==0.164)
    
def test_dates_difference_2():
    assert (dtools.days_between("01/11/2020","31/12/2020","days")==60)
    
def test_dates_difference_3():
    assert (dtools.days_between("01/11/2020","31/12/2020","months")==2)