# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 15:00:22 2017

@author: Malek
"""

import pyodbc
#import pandas as pd

def gen(cursor, sql):
   cursor.execute(sql)
   while True:
       row = cursor.fetchmany(1000)
       if row is None:
           break
       yield row

def dbSources():
    sources = pyodbc.dataSources()
    keys = sources.keys()
    for key in keys: 
        print(key)
   
def main():

    con = pyodbc.connect('Driver={Microsoft Access Driver (*.mdb, *.accdb)};Dbq=Campaign_Template.mdb ;Uid=;Pwd=;')    
    cur = con.cursor()
    sql = "SELECT * from Invoice" # I have a query table which is pivoting the data inside the access.    
    
    for x in gen(cur,sql):
        print(x)
        
main()