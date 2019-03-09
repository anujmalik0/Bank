#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3, 01:48:58 2018

@author: Anuj Malik
"""



#import openpyxl

    
#df=pd.read_excel("/Users/orbaa5/Desktop/Duplicate.xls",
#skiprows=12,header=0,index_col=3,nrows=343,na_values=None,keep_default_na=False)
#df = df.drop('Unnamed: 0', 1)

#df=pd.read_excel("/Users/orbaa5/Desktop/Dissertation/Thesis/Data/TrainingData/FY2013_14.xls",
#skiprows=12,header=0,index_col=None,na_values=None,keep_default_na=False)
#df = df.drop('Unnamed: 0', 1)

#---------------------# LEVEL 1 :
# Account Balance
# Average Expenditure
# Question1 : Show withdrawls,purchase for august, last month 2017.
# Question2 : Show withdrawls,purchase for amazon, Electricity for Aug 2017
# Question3 : When was last payment to BSES, MTNL, etc    
#---------------------# LEVEL 2 :    
#--------#To Bank Team ( Chart / Graph, etc )
#Show me spending details for 1st entire year, all months, 6 months,  months, first 2 weeks, 1st week, 1st day.    
# AI response1 (NPA 1) : Show me months where spending(Salary) > expenditure
# AI response1 (NPA 2 ) : For how many months expenditure > saving(Salary)  
# AI Response ( NPA 3) : For how many months expenditure > 75% savings ( Salary )
# AI Response ( NPA 4) : Has customer paying electricity, telephone, water bill regularly
# AI Response ( NPA 5 ) : How much spending during first 2 weeks OF SALARY.

############### BIL   #############

#--------------------Telephone
#RELIANCECOMM
#MTNL
#TATADOCOMO
#IDEACELLULAR
#IIN/(anywhere MTNL )

#----------------Recharge
#PREPAID MOBILE RECH
#PREPAID MOBILE RECHARGE 
#DOCOMOPREP
#AIRTELPREP
#RELIANCEJIO
#IIN/Tata Doco
#IIN/( anywhere) BSES

#Non ICICI ATM withdrawl

#------------Marriage    
#MATRIMONY

#------------Entertainment
#BOOKMYSHOW

#RBI-NEFT

#Recharge:    
#OXIGENPMR

#Others:
#PAYU

#Institute
#IIN/Birla Insti

#--------#To Clients--------------
# AI response1 ( savings) : You have crossed ATM cash Withdl.limit this month.Now Rs 20 /tnx. 



#########12 Times : Salary : 
    
######business loan ( Machineery, raw materials, etc )
######Farmer loan ( crop, fertilizer, etc )
####Personal loan ( marriage, education, etc )

#######---------COMPONENT 1-----------------------

#dff=pd.read_excel("/Users/orbaa5/Desktop/Dissertation/Thesis/Data/TrainingData/Training.xls",
#skiprows=12,header=0,index_col=None,na_values=None,keep_default_na=False,nrows=1848)
#dff = dff.drop('Unnamed: 0', 1)

#-------------------------------------------Packages,Libraries------------------------
import pandas as pd
import re
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.corpus import state_union
#from nltk.tokenize import PunktSentenceTokenizer
#nltk.download()
import numpy as np
import matplotlib.pyplot as plt 
import calendar
import time
from datetime import datetime
from datetime import date
from time import strftime
pd.options.display.max_rows = 4000
pd.options.display.max_columns = 4000
pd.options.display.max_seq_items = 2000
import datetime
import dateutil.relativedelta
#from PyPDF2 import PdfFileReader
#import os
from wand.image import Image as Img
from PIL import Image, ImageEnhance, ImageFilter
import pytesseract
import cv2
import webbrowser
import bs4
from bs4 import BeautifulSoup
import requests
from requests.exceptions import ConnectionError
from urllib3.exceptions import NewConnectionError
import html.parser
import lxml
import os
import platform
import threading
from multiprocessing import Process
from multiprocessing import Pool
import multiprocessing

#import xlrd

#-------Total Records 1847-------------------

df=pd.read_excel("/Users/orbaa5/Desktop/Dissertation/Thesis/Data/TrainingData/Training.xls",
skiprows=12,header=0,index_col=None,na_values=None,keep_default_na=False,nrows=1847)
df = df.drop('Unnamed: 0', 1)

df1=pd.read_excel("/Users/orbaa5/Desktop/Dissertation/Thesis/Data/TrainingData/Training.xls",
skiprows=12,header=0,index_col=None,na_values=None,keep_default_na=False,nrows=1847)
df1 = df1.drop('Unnamed: 0', 1)

##################  df1 = ICICI ATM Cash Withdrawl ########################
##################  df2 = Electricity BSES ###############################
df2=df.copy()
##################  df3 =  Telephone MTNL  ###############################
df3=df.copy()
##################  df4 = Water DJB #####################################
df4=df.copy()
##################  df5 = Online Shooping ################################
df5=df.copy()
##################  df6 = Travel - Train, Air, Road ######################
df6=df.copy()
##################  df7 = Debit - Fund Transfer ( Sent )##########################
df7=df.copy()
##################  df8 = Other Bank ATM Cash withdrawl ##################
df8=df.copy()
##################  df9 = Recharge #######################################
df9=df.copy()
#################   df10 = Loan - EMI Installments   #####################
df10=df.copy()
#################   df11 = Salary   #####################
df11=df.copy()
#################   df12 = Interest   #####################
df12=df.copy()
#################   df13 = Auto Reversal   #####################
df13=df.copy()
#################   df14 = Credit - Fund Transfer ( Received )   #####################
df14=df.copy()
#################   Account Balance   #####################
df15=df.copy()
#################   Average Expenditure   #####################
df16=df.copy()
#################   Average monthly Balance   #####################
df17=df.copy()
#################   Mini Statement   #####################
df18=df.copy()
#################   Account Detailed Statement   #####################
df19=df.copy()
#################   By Air expenditure   #####################
df25=df.copy()
#################   Amazon expenditure   #####################
df26=df.copy()
df27=df.copy()




def Assessment_Norms_Violated(TotalViolation,y1,y2,y3,y4,y5):
            print("\n==========Assessment==================\n")
            print("\n 1. Financial statement subjected to violation = Balance Sheet of Bhushan Steel Limited ")
            print("\n 2. Act under which violation occurred         = GOI, Ministry of Corporate Affairs, The Companies Act 1956, Amendment 2013" )    
            print("\n 3. Chapter violated                           = CHAPTER XII - MEETINGs OF BOARD AND ITS POWERS")
            print("   a. Section violated                          = Section 180")
            print("   b. Sub-section violated                      = sub-section (I)")
            print("\n 4. No. of times Violation occurred            = ",TotalViolation," times ,Balance Sheet as at",y1,",",y2,",",y3,",",y4,",",y5)            
            #print("Clause Violated under Companies Act = )
            print("\n 5. Risk                                       = Repayment of Long term borrowings ")
            print("\n 6. Impact                                     = Frequency increases for Delayed Payments and Loan Restructing")
            
            print("\n 7. Risk Exposure in Banking industry          = State Bank of India and Punjab National Bank")
                  
            print("\n==============   Risk Mitigation ===============")
            
            print("\n8. GOI, MCA, The Companies Act 1956, Amendment 2013, CHAPTER XV,XVI,XVIII PROTECTION OF CREDITORS")
            
            print("\n================   Solution     ================\n")
            
            print("9. Short term                                    = Extension of further credit limit shall be revoked\n")
            print("10. Long term                                    = Legal proceedings shall be exercised within 30 days" )
    
            #return
#import minecart
####################  IMPORTANT      ################
#tesseract - not a python library hencePython  wrapper ( pytesseract is used) along with PIL and pillow to manipulate images
#To identify and extract characters from images/files- tesseract
#To manipulate images/files - PIL( python imaging library) and openCV

#Toimproveaccuracy - Image Pre Processing is must

#GitHub - https://github.com/tesseract-ocr/tesseract/wiki/ImproveQuality
#Tesseract works best on images which have a DPI of at least 300 dpi,


#img = cv2.imread("/Users/orbaa5/Desktop/Dissertation/Thesis/Data/TrainingData/Bhushan_SEBI_2012_final.pdf",resolution=300)
#print("cv2 result :",img)

##############  SCANNED pdf Annual Report ########################

#im = Image.open("/Users/orbaa5/Desktop/Dissertation/Thesis/Data/TrainingData/Bhushan_SEBI_2012_final.jpg")
#im=  im.convert('L').resize([3 * _ for _ in im.size], Image.BICUBIC)
#im= im.point(lambda p: p > 75 and p + 100)
#im = im.filter(ImageFilter.MedianFilter())
#enhancer = ImageEnhance.Contrast(im)
#im = enhancer.enhance(2)

#print("fl1",fl1)

#ig5 = cv2.GaussianBlur(fl1, (5, 5), 0)

#print(ig5)

#kernel = np.ones((1, 1), np.uint8)
#ig1 = cv2.dilate(ig5, kernel, iterations=1)
#ig2 = cv2.erode(ig1, kernel, iterations=1)
#ig3 = cv2.GaussianBlur(ig2, (5, 5), 0)

#ig4 = cv2.threshold(ig3, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
#cv2.imwrite("/Users/orbaa5/Desktop/Dissertation/Thesis/Data/TrainingData/Bhushan_SEBI_2012_final2.jpg", ig4)

#i1 = Image.open("/Users/orbaa5/Desktop/Dissertation/Thesis/Data/TrainingData/Bhushan_SEBI_2012_final.jpg")
#crop_img = i1.crop((10,100,1450,1450))
#crop_img.save("/Users/orbaa5/Desktop/Dissertation/Thesis/Data/TrainingData/Bhushan_SEBI_2012_final1.jpg")

################ Balance Sheet 2011 and 2012 SCANNED B[;alance sheet Image signed by Chairman, Directors, Auditor submitted to SEBI##########



# extract 14 values, compute 8 rations ( including MCA Govt. norms ) RETURN 8   RATIOS
            
def BhushanSteel2011_2012(): 
    #print("fn called")
    with Img(filename="/Users/orbaa5/Desktop/Dissertation/Thesis/Data/TrainingData/Bhushan_SEBI_2012_final.pdf", resolution=300) as imge:
 #imge.compression_quality = 99
 #imge.type = 'grayscale';
     imge.save(filename="/Users/orbaa5/Desktop/Dissertation/Thesis/Data/TrainingData/Bhushan_SEBI_2012_final.jpg")

    text = pytesseract.image_to_string(Image.open("/Users/orbaa5/Desktop/Dissertation/Thesis/Data/TrainingData/Bhushan_SEBI_2012_final.jpg"),config="tessedit_char_whitelist=0123456789") 
    #print("should be string",type(text))
    #print("post pytesseract",type(text))
    #a=str(text)
#print(text)
    token=word_tokenize(text)
    #print("should be list",type(token))
    #print("token should be list",type(token))
#stop_words = set(stopwords.words("english"))
    #print(token)

    
#=========================GOI, MCA Norms====================================================
    
    #print("post fn called")
    for i in range(len(token)):
        if token[i] == "Reserves":
            #print("2012_12")
            x1=token[i+8]
            x2=token[i+9]
            x3=token[i+27]
            x4=token[i+28]
            FY2012=token[i-13]
            FY2011=token[i-12]
    
    #print("FY2011",FY2011)
    #print("FY2012",FY2012)        
    EQTY_2012=int(float(x1))
    EQTY_2011=int(float(x2))
    LTB_2012=int((float(x3))/100)
    LTB_2011=int((float(x4))/100)
        
    if LTB_2012 >= EQTY_2012:
        #print("During Financial Year 2012, MCA_Norms_2013 violated")
        violation_2012=1
    elif LTB_2012 < EQTY_2012:
        #print("No MCA norms violation observed")
        violation_2012=0
    
    if  LTB_2011 >= EQTY_2011:
        #print("During Financial Year 2011, MCA_Norms_2013 violated")
        violation_2011=1
    elif LTB_2011 < EQTY_2011:
        #print("No MCA norms violation observed")
        violation_2011=0
        #a,b,c = Default(v1,y1,y2)
        #return violation,y1,y2
    #print("q3",q3, "q1",q1,"q4",q4,"q2",q2)    
#=========================GOI, MCA Norms====================================================
        
          
#=========================Quick Ratio START====================================================
    for i in range(len(token)):
        #print("in for")
        if token[i] == "Current" and token[i+1] == "Assets":
            TR_2011=token[i+15]
            TR_2012=token[i+14]
            CBB_2011=token[i+22]
            CBB_2012=token[i+21]
    
    TR_2011=int(float(TR_2011))
    TR_2012=int(float(TR_2012))
    CBB_2011=int(float(CBB_2011))
    CBB_2012=int(float(CBB_2012))

    #print("TR_2011",TR_2011)
    #print("\nTR_2012",TR_2012)
    #print("\nCBB_2011",CBB_2011)
    #print("\nCBB_2012",CBB_2012)    
    
    for i in range(len(token)):
        #print("in for")
        if token[i] == "Current" and token[i+1] == "Liabilities" and token[i+3] == "Borrowings":
            CL_2011=token[i+24]
            CL_2012=token[i+23]

    CL_2011=int(float(CL_2011))
    CL_2012=int(float(CL_2012))
    
    #print("\nCL_2011",CL_2011)
    #print("\nCL_2012",CL_2012)   
    
    CA_2011=TR_2011+CBB_2011
    CA_2012=TR_2012+CBB_2012
    
    Quick_Ratio_2011=round(CA_2011/CL_2011,2)
    Quick_Ratio_2012=round(CA_2012/CL_2012,2)
    
    #print("Quick_Ratio_BS_2011:",Quick_Ratio_BS_2011)
    #print("Quick_Ratio_BS_2012:",Quick_Ratio_BS_2012)
    
    #Quick_Ratio_BS_2011=round(Quick_Ratio_BS_2011,2)
    #Quick_Ratio_BS_2012=round(Quick_Ratio_BS_2012,2)
    
    #print("Quick_Ratio_BS_2011:",Quick_Ratio_BS_2011)
    #print("Quick_Ratio_BS_2012:",Quick_Ratio_BS_2012)
     
#=========================Absolute Ratio START====================================================
    Absolute_Liquid_ratio_2011=round(CBB_2011/CL_2011,3)
    Absolute_Liquid_ratio_2012=round(CBB_2012/CL_2012,2)                
    
    #print("Absolute_Liquid_Ratio_2011",Absolute_Liquid_BS_2011)
    #print("Absolute_Liquid_Ratio_2012",Absolute_Liquid_BS_2012)

#=========================Debt Equity Ratio Start====================================================

    #print(token)

    for i in range(len(token)):
         #print("in for")
         if token[i] == "EQUITY" and token[i+2] == "LIABILITIES":
             EQT_2011=token[i+20]
             EQT_2012=token[i+19]
#            C_LIAB_2011=token[i+22]
 #           C_LIAB_2012=token[i+21]
#            NC_LIAB_2011=token[]
#            NC_LIAB_2012=tpken[]    
    EQT_2011=int(float(EQT_2011))
    EQT_2012=int(float(EQT_2012))

    #print("equity 2011",EQT_2011)
    #print("\n equity 2012",EQT_2012)

    for i in range(len(token)):
         #print("in for")
         if token[i] == "Non-Current" and token[i+1] == "Liabilities":
             NCLIAB_2011=token[i+23]
             NCLIAB_2012=token[i+22]

    #CL_2011
    #CL_2012
    
    NCLIAB_2011=int(float(int(NCLIAB_2011)/100))
    NCLIAB_2012=int(float(int(NCLIAB_2012)/100))
    
    #print("\nNCLIAB_2011",NCLIAB_2011)
    #print("NCLIAB_2012",NCLIAB_2012)
    #print("CLIAB_2011",CL_2011)
    #print("CLIAB_2012",CL_2012)
    
    TL_2011=CL_2011+NCLIAB_2011
    TL_2012=CL_2012+NCLIAB_2012
    
    Debt_Equity_ratio_2011=round(TL_2011/EQT_2011,2)
    Debt_Equity_ratio_2012=round(TL_2012/EQT_2012,2)
    

    
    return violation_2011,violation_2012,Quick_Ratio_2011,Quick_Ratio_2012,Absolute_Liquid_ratio_2011,Absolute_Liquid_ratio_2012,Debt_Equity_ratio_2011,Debt_Equity_ratio_2012,FY2011,FY2012

  
#=========================debt_equity END====================================================



### extract 7 values, compute 4 rations ( including MCA Govt. norms ) RETURN 4  RATIOS
    
def BhushanSteel2013():    
    
    with Img(filename="/Users/orbaa5/Desktop/Dissertation/Thesis/Data/TrainingData/Bhushan_SEBI_2013_final.pdf", resolution=300) as imge1:
 #imge.compression_quality = 99
 #imge.type = 'grayscale';
     imge1.save(filename="/Users/orbaa5/Desktop/Dissertation/Thesis/Data/TrainingData/Bhushan_SEBI_2013_final.jpg")

    text1 = pytesseract.image_to_string(Image.open("/Users/orbaa5/Desktop/Dissertation/Thesis/Data/TrainingData/Bhushan_SEBI_2013_final.jpg")) 
    #a=str(text)
#print(text)
    token1=word_tokenize(text1)        
    #print("2012\n",token1)        
    for i in range(len(token1)):
        if token1[i] == "Reserves":
            #print("2012_12")
            x1=token1[i+6]
            x2=token1[i+29]
            FY2013=token1[i-13]

    EQTY_2013=int(float(x1)) 
    LTB_2013=int(float(x2))
    #print("shar",q1)
    #print("br",q2)
    #print(y1)
    #print(y1)  y1 = year  

    if LTB_2013 >= EQTY_2013 :
        #print("During Financial Year 2013, MCA_Norms_2013 violated")
        violation_2013=1
    elif LTB_2013 < EQTY_2013 :
        #print("No MCA norms violation observed")
        violation_2013=0

    #print("EQTY_2013",EQTY_2013,"LTB_2013",LTB_2013)

#=========================Quick Ratio START====================================================
    for i in range(len(token1)):
        #print("in for")
        if token1[i] == "Current" and token1[i+1] == "Assets":
            TR_2013=token1[i+14]
            CBB_2013=token1[i+21]
    
    TR_2013=int(float(TR_2013))
    CBB_2013=int(float(CBB_2013))

    #print("\nTR_2013",TR_2013)
    #print("\nCBB_2013",CBB_2013)    
    

    for i in range(len(token1)):
         #print("in for")
         if token1[i] == "Current" and token1[i+1] == "Liabilities" and token1[i+3] == "Borrowings":
             CL_2013=token1[i+23]
 
    CL_2013=int(float(CL_2013))
     
    #print("\nCL_2013",CL_2013)   

    CA_2013=TR_2013+CBB_2013
    
    Quick_Ratio_2013=round(CA_2013/CL_2013,2)

    #print(token1)
    
    #print("Quick_Ratio_BS_2013:",Quick_Ratio_BS_2013)
    #print("Quick_Ratio_BS_2013 TYPE:",type(Quick_Ratio_BS_2013))
     
#=========================Absolute Ratio START====================================================

    Absolute_Liquid_ratio_2013=round(CBB_2013/CL_2013,2)                
    
    #print("Absolute_Liquid_Ratio_2013",Absolute_Liquid_BS_2013)

    
#=========================Debt Equity Ratio Start====================================================

    #print(token)

    for i in range(len(token1)):
         #print("in for")
         if token1[i] == "EQUITY" and token1[i+2] == "LIABILITIES":
             EQT_2013=token1[i+17]
#            C_LIAB_2011=token[i+22]
 #           C_LIAB_2012=token[i+21]
#            NC_LIAB_2011=token[]
#            NC_LIAB_2012=tpken[]    
    EQT_2013=int(float(EQT_2013))
    
    #print("equity 2013",EQT_2013)
    
    for i in range(len(token1)):
         #print("in for")
         if token1[i] == "Non-Current" and token1[i+1] == "Liabilities":
             NCLIAB_2013=token1[i+22]

    #print(type(float(NCLIAB_2013)))
    
    #NCLIAB_2013=int(float(int(NCLIAB_2013)))
    
    NCLIAB_2013=int(float(NCLIAB_2013))
    
    #print("NCLIAB_2013",NCLIAB_2013)
    

    #print("NC Liability",(NCLIAB_2013)/100)
    #NCLIAB_2013=int(float(int(
    
    #print("\nNCLIAB_2013",NCLIAB_2013)
    #print("CLIAB_2013",CL_2013)
    #print("EQUITY_2013",EQT_2013)
    
    TL_2013=CL_2013+NCLIAB_2013
    
    Debt_Equity_ratio_2013=round(TL_2013/EQT_2013,2)
    
    #print("debt_equity_BS_2011",debt_equity_BS_2013)

    return violation_2013,Quick_Ratio_2013,Absolute_Liquid_ratio_2013,Debt_Equity_ratio_2013,FY2013
  
#=========================debt_equity END====================================================

    

# extract 14 values, compute 8 rations ( including MCA Govt. norms ) RETURN 8   Ratios
    
def BhushanSteel2014_2015():
        
    with Img(filename="/Users/orbaa5/Desktop/Dissertation/Thesis/Data/TrainingData/Bhushan_SEBI_2015_final.pdf", resolution=300) as imge2:
 #imge.compression_quality = 99
 #imge.type = 'grayscale';
     imge2.save(filename="/Users/orbaa5/Desktop/Dissertation/Thesis/Data/TrainingData/Bhushan_SEBI_2015_final.jpg")

    text2 = pytesseract.image_to_string(Image.open("/Users/orbaa5/Desktop/Dissertation/Thesis/Data/TrainingData/Bhushan_SEBI_2015_final.jpg")) 
    #a=str(text)
#print(text)
    token=word_tokenize(text2)        
    #print("2014_15\n",token2)        

    for i in range(len(token)):
        if token[i] == "Reserves":
            #print("2014_15")
            x1=token[i+6]
            x2=token[i+7]
            x3=token[i+20]
            x4=token[i+21]
            FY2015=token[i-13]
            FY2014=token[i-12]
    
    #print("FY2014",FY2014)
    #print("FY2015",FY2015) 
    EQTY_2015=int(float(x1))
    EQTY_2014=int(float(x2))
    LTB_2015=int(float(x3))
    LTB_2014=int(float(x4))
    #print(q1,q2,q3,q4)
    #print(q1,q2,q3,q4)
    
    if LTB_2015 >= EQTY_2015:
        #print("During Financial Year 2015, MCA_Norms_2013 violated")
        violation_2015=1
    elif LTB_2015 < EQTY_2015:
        #print("No MCA norms violation observed")
        violation_2015=0
    
    if LTB_2014 >= EQTY_2014:
        #print("During Financial Year 2014, MCA_Norms_2013 violated")
        violation_2014=1
    elif LTB_2014 < EQTY_2014:
        #print("No MCA norms violation observed")
        violation_2014=0

    #print("LTB_2014",LTB_2014)
    #print("LTB_2015",LTB_2015)
    #print("EQTY_2014",EQTY_2014)
    #print("EQTY_2015",EQTY_2015)
#=========================Quick Ratio START====================================================
    for i in range(len(token)):
        #print("in for")
        if token[i-1] != "Other" and token[i] == "Current" and token[i+1] == "Assets":
            TR_2014=token[i+10]
            TR_2015=token[i+9]
            CBB_2014=token[i+17]
            CBB_2015=token[i+16]
    
    TR_2014=int(float(TR_2014))
    TR_2015=int(float(TR_2015))
    CBB_2014=int(float(CBB_2014))
    CBB_2015=int(float(CBB_2015))
    
    #print("CBB_2014",CBB_2014)
    #print("CBB_2015",CBB_2015)
    #print("TR_2014",TR_2014)
    #print("TR_2015",TR_2015)
    
    #TR_2011=int(float(TR_2011))
    #TR_2012=int(float(TR_2012))
    #CBB_2011=int(float(CBB_2011))
    #CBB_2012=int(float(CBB_2012))

    #print("TR_2011",TR_2011)
    #print("\nTR_2012",TR_2012)
    #print("\nCBB_2011",CBB_2011)
    #print("\nCBB_2012",CBB_2012)    
    
    for i in range(len(token)):
        #print("in for")
        if token[i] == "Current" and token[i+1] == "Liabilities" and token[i+3] == "Borrowings":
            CL_2014=token[i+24]
            CL_2015=token[i+23]

    CL_2014=int(float(CL_2014))
    CL_2015=int(float(CL_2015))
    
    #print("\nCL_2014",CL_2014)
    #print("\nCL_2015",CL_2015)   
    
    CA_2014=TR_2014+CBB_2014
    CA_2015=TR_2015+CBB_2015
    
    Quick_Ratio_2014=round(CA_2014/CL_2014,2)
    Quick_Ratio_2015=round(CA_2015/CL_2015,2)
    
    #print("Quick_Ratio_BS_2011:",Quick_Ratio_BS_2011)
    #print("Quick_Ratio_BS_2012:",Quick_Ratio_BS_2012)
    
    #Quick_Ratio_BS_2011=round(Quick_Ratio_BS_2011,2)
    #Quick_Ratio_BS_2012=round(Quick_Ratio_BS_2012,2)
    
    #print("Quick_Ratio_BS_2014:",Quick_Ratio_BS_2014)
    #print("Quick_Ratio_BS_2015:",Quick_Ratio_BS_2015)
     
#=========================Absolute Ratio START====================================================
    Absolute_Liquid_ratio_2014=round(CBB_2014/CL_2014,3)
    Absolute_Liquid_ratio_2015=round(CBB_2015/CL_2015,3)                
    
    #print("Absolute_Liquid_Ratio_2014",Absolute_Liquid_BS_2014)
    #print("Absolute_Liquid_Ratio_2015",Absolute_Liquid_BS_2015)

#=========================Debt Equity Ratio Start====================================================

    #print(token)

    for i in range(len(token)):
         #print("in for")
         if token[i] == "EQUITY" and token[i+2] == "LIABILITIES":
             EQT_2014=token[i+18]
             EQT_2015=token[i+17]
#            C_LIAB_2011=token[i+22]
 #           C_LIAB_2012=token[i+21]
#            NC_LIAB_2011=token[]
#            NC_LIAB_2012=tpken[]    
    
    EQT_2014=int(float(EQT_2014))
    EQT_2015=int(float(EQT_2015))

    #print("equity 2014",EQT_2014)
    #print("equity 2015",EQT_2015)

    for i in range(len(token)):
         #print("in for")
         if token[i] == "Non-Current" and token[i+1] == "Liabilities":
             NCLIAB_2014=token[i+23]
             NCLIAB_2015=token[i+22]

    NCLIAB_2014=int(float(NCLIAB_2014))
    NCLIAB_2015=int(float(NCLIAB_2015))
    
    #print("NCLIAB_2014:",NCLIAB_2014)
    #print("NCLIAB_2015",NCLIAB_2015)
    
    #print("\nNCLIAB_2011",NCLIAB_2011)
    #print("\nNCLIAB_2012",NCLIAB_2012)
    #print("\nCLIAB_2011",CL_2011)
    #print("\nCLIAB_2012",CL_2012)
    #print("\nequity 2011:",EQT_2011)
    #print("\nequity 2012:",EQT_2012)
    
    TL_2014=CL_2014+NCLIAB_2014
    TL_2015=CL_2015+NCLIAB_2015
    
    Debt_Equity_ratio_2014=round(TL_2014/EQT_2014,2)
    Debt_Equity_ratio_2015=round(TL_2015/EQT_2015,2)
    
    #print("debt_equity_BS_2014",debt_equity_BS_2014)
    #print("debt_equity_BS_2015",debt_equity_BS_2015)
    
    
    return violation_2014,violation_2015,Quick_Ratio_2014,Quick_Ratio_2015,Absolute_Liquid_ratio_2014,Absolute_Liquid_ratio_2015,Debt_Equity_ratio_2014,Debt_Equity_ratio_2015,FY2014,FY2015
  
#=========================debt_equity END====================================================

    # to open the page:webbrowser.open("https://www.icicipruamc.com/icici-prudential-mutual-fund/funds/equity-funds/icici-prudential-bluechip-fund")
#    start=datetime.datetime.now()
    #Use proxy, avoid IP blacklisting 
    #proxies = { "http":"http://10.10.0.0:0000" , "https":"http://120.10.0.0:0000"}
    #print("fine1",proxies)##proxies=proxies
    # Checking internet connection status
    #dt=datetime.datetime.now()
    #a= dt.strftime('%d-%B-%Y %H:%M:%S')
    #dt1=dt.strftime('%d-%b-%Y')   
    #tm=datetime.datetime.now().time()
    #tm1=tm.strftime('%H:%M:%S')
    
    #tt = datetime.datetime.now()
    
    #print("today day is===> ")
###---START--Selection of current system day, month,year, hour, minutes#
    

    #print("difference month:",d3.month)

    #print("difference year:",d3.year)
    #d3.month
    #usery=d3.year
    #userd=d3.day
    #userh=d3.hour
    #usermn=d3.minute
    #users=d3.second
    
#  important#    
    #print("final month", calendar.month_abbr[userm])
    #print("final year",usery)
    #print("final day",userd)
    #print("hour",userh)
    #print("minuteFINAL",usermn)
#---END---Selection of current system day, month,year, hour, minutes#
    #print("minute",userm)
    #print("second",users)
    #print("current date",d3)
    
    #mt10=time.strftime('%d-%B-%Y %H:%M:%S'

    #if( dt.hour > 12):   
     #   print("modified date is==>",mt2.day,"",calendar.month_abbr[mt2.month],"",mt2.year,",",mt2.hour-12,":",mt2.minute,"PM")
            
    #elif ( dt.hour <= 12):   
     #   print("modified date is==>",mt2.day,"",calendar.month_abbr[mt2.month],"",mt2.year,",",mt2.hour,":",mt2.minute,"AM")
    
### Code to run when Intranet Connecton / ICICI Banl Product system is not under maintenance ##########    


    


def Investment(url,Product,NAV):    
        
        try:
            now10 = datetime.datetime.now()
            
            now1=now10.strftime('%Y-%m-%d %H:%M:%S')
                    #print(now)
                    #now=now.date()    
            now=str(now1)
                    #now=now.strftime('%d-%b-%Y')
        #-----------------------------------------------------------
                    #b=df14["Month"].max()
            d = datetime.datetime.strptime(now,"%Y-%m-%d %H:%M:%S")
            d2=str(d)
            d3=datetime.datetime.strptime(d2, "%Y-%m-%d %H:%M:%S")
            

                
   #             print("time",d3.hour)
  #              print("### ONLINE Mode Started ###")
        
                #print("befor res\n")
                #start=datetime.datetime.now()
            #res = requests.get("https://www.icicipruamc.com/icici-prudential-mutual-fund/funds/equity-funds/icici-prudential-bluechip-fund",timeout=60)
            res = requests.get(url,timeout=60)
            #print("respnse object",type(res))
            #print("\n content",res.content)
            #print("\n encoding",res.encoding)
            a=len(res.text)
                #print("code",res.raise_for_status)
                #Connection_Success=1
                ##START##
            if( d3.hour >= 7 ) and ( d3.hour <= 17 ):
                print("\n ##### ONLINE MODE STARTED [ 7AM to 6PM or during Business Hours]; chatbot access to ICICI Bank System #####\n")
                ##END##
                
                ##### --------Program logical clock(to be designed) which will switch to Offline mode post business hours #######
                
                if (res.status_code == requests.codes.ok):
                    if( d3.hour > 12): 
                        print("\n1. Intranet Connection ( To connect ICICI Bank System )   : Status = Success, verified on ",d3.day,"",calendar.month_abbr[d3.month],"",d3.year,",",d3.hour-12,":",d3.minute,"PM")
                    elif ( d3.hour <= 12):
                        print("\n1. Intranet Connection ( To connect ICICI Bank System )   : Status = Success, verified on ",d3.day,"",calendar.month_abbr[d3.month],"",d3.year,",",d3.hour,":",d3.minute,"AM")
                    print("2. Download Product document ( From ICICI Bank site )     : Status = Success, Code =",res.status_code,)    
                    
                    file1=open("/Users/orbaa5/Desktop/Dissertation/Thesis/Data/TrainingData/ICICIPrudential.html","wb")
                    for i in res.iter_content(a):
                        file1.write(i)
                    file1.close()
                    #end=datetime.datetime.now()
                    print("3. Save Product Document [ Local system hard drive ]      : Status = Success, Saved as HTML file")
                    file=open("/Users/orbaa5/Desktop/Dissertation/Thesis/Data/TrainingData/ICICIPrudential.html")
                    bs=BeautifulSoup(file,"lxml") # "lxml parser" is fast as compared to "HTML parser"
                    #print("beautiful soup type",type(bs))
                    #print("proceed",type(s))
                    c1=bs.div(id="container")
                    c2=bs.div(id="rightpart")
                    c3=bs.div(id="DivContent")
                    c4=bs.div(id="Content_ctl01_ctl00_ctl00_detailContainer")
                    c5=bs.div(id="Content_C003_divNav")
                    
                    if(c1==[] or c2== [] or c3==[] or c4==[] or c5==[]):
                        print("Warning!!! Site content changed. Will be fixed in next 24 hours")
                        file.close()
                    else:
                       
                        if( d3.hour >= 12) and ( d3.hour <= 23 ): 
                            print("4. Verify Change in Product document [ HTML]              : Status = up-to date content / Not modified by ICICI Bank, verified on ",d3.day,"",calendar.month_abbr[d3.month],"",d3.year,",",d3.hour-12,":",d3.minute,"PM")
                        elif ( d3.hour >= 0 ) and ( d3.hour <= 11 ): 
                            print("4. Verify Change in Product document [ HTML]              : Status = up-to date content / Not modified by ICICI Bank verified on ",d3.day,"",calendar.month_abbr[d3.month],"",d3.year,",",d3.hour,":",d3.minute,"AM") 

                    
            else:
                if(os.path.isfile("/Users/orbaa5/Desktop/Dissertation/Thesis/Data/TrainingData/ICICIPrudential.html")):
    ###         
                    rp=os.path.isfile("/Users/orbaa5/Desktop/Dissertation/Thesis/Data/TrainingData/ICICIPrudential.html")
                    #True / False ( response file check )            
                    #print("Not run!!!!!!!!!!!!!!!!!!!!!!!!",os.path.isfile("/Users/orbaa5/Desktop/Dissertation/Thesis/Data/TrainingData/ICICIPrudential.html"))
                    print("\n##### OFFLINE MODE STARTED [ 6PM to 7AM or during Network Failure]; chatbot access to local system instead of ICICI Bank System #####\n")
                    file=open("/Users/orbaa5/Desktop/Dissertation/Thesis/Data/TrainingData/ICICIPrudential.html")
                    bs=BeautifulSoup(file,"lxml") # "lxml parser" is fast as compared to "HTML parser"
                    #print("beautiful soup type",type(bs))
                    #print("testing")
                    #print("proceed",type(s))
                    c1=bs.div(id="container")
                    c2=bs.div(id="rightpart")
                    c3=bs.div(id="DivContent")
                    c4=bs.div(id="Content_ctl01_ctl00_ctl00_detailContainer")
                    c5=bs.div(id="Content_C003_divNav")
                    
                    if(c1==[] or c2== [] or c3==[] or c4==[] or c5==[]):
                        print("Warning!!! Site content changed. Will be fixed in next 24 hours")
                        file.close()
                    else:
                        
                        mt1=os.path.getctime("/Users/orbaa5/Desktop/Dissertation/Thesis/Data/TrainingData/ICICIPrudential.html")        
            #mt2=time.ctime(int(mt1))
                        mt=time.strftime('%d-%B-%Y %H:%M:%S',time.localtime(int(mt1)))
                        mt2= datetime.datetime.strptime(mt,'%d-%B-%Y %H:%M:%S')
                        
                        if( d3.hour >= 12) and ( d3.hour <= 23 ): 
                            print("1. Product document exist on local system Hard Drive     : Status = Success , Code =",rp)
                            print("2. Product Modified date [ Local system hard drive ]     : HTML file Verified on ",mt2.day,"",calendar.month_abbr[mt2.month],"",mt2.year,",",mt2.hour-12,":",mt2.minute,"PM")
 
                        elif ( d3.hour >= 0 ) and ( d3.hour <= 11 ): 
                            print("1. Product document exist on local system Hard Drive     : Status = Success , Code =",rp)
                            print("2. Product Modified date [ Local system hard drive ]     : HTML file Verified on ",mt2.day,"",calendar.month_abbr[mt2.month],"",mt2.year,",",mt2.hour,":",mt2.minute,"AM")                            
                        
                        #print("lets see heading",bs.find_all("h1"))
                        
                        #print("find class=>",bs.find(class_="fundDetail"))
                else:
                    print("File Not Found Error")
            try:
                
                #t=bs.table
                
                #t=bs.table
                #t1=bs.tr , #return span
                #print("table",t.attrs)
                #print("\ntext\n:",bs.contents,"\n\n\n\n\n\n\n\n")
                
                #tw=t.contents
                #print("table",t.contents)
                #print("\n\n\n\nrecord:::",t1.__getitem__(0))
                #print("\n")
                
                s = bs.find_all(class_="fundDetail")
                #print("s tpe", type(s))
                print("\n ##### Following is the Product suggested as per your requirement ##### \n")
                print("\n*  Mutual Fund Name                                    : ",s[0].text.strip())
                #print("Scheme Name:\n\n")
# Imp: This removes any whitespace (newlines, spaces, tabs, etc.) between two newlines.                    
                
                #Not working---s1 = bs.find_all(class_="applicationFormTable navUpRate")
                #Not working print("Scheme==>\n",s1[0].text.strip())
                s1 = bs.find_all("td", string=re.compile("Direct"))
                #print("Latest=>",s1)
                
                tb=bs.find_all("table", attrs={"class":"applicationFormTable navUpRate"})
                #print("table is \n\n\n",tb)
                
                #print("before split",tb)
                
                # Split to get comma separated tokens, in order to iterate and extract the values
                tb1=str(tb[0].text).split()
                
                #print("what is this:",tb1)
                #print("type",type(tb1))
                #print(tb1)s
                #print(type(tb1))
                #print("length tb1:",len(tb1))
                
                #print("\n\n\n\n\n",tb1[9])
                #print("\n\n\n\n",tb1[10])
                
                #######Business Rule, [ Total Risk weightege = 100 ]########
                
                ########Growth Plan
                #Moderate Spending = 20 [ <= 75 % of salary ]
                #Long Term = 20 [ Existing products for long term perspective ]
                #Infrequent Product Switch = 20 [ <=2 ATM , <=1 credit card, <= 2 Loans   ]
                #Savings Oriented = 20 [ Travelling, shopping etc ]
                #Salaried = 20 [ Annual income 5 Lacs]
                
                ########Dividend Plan
                #High Spending = 20 [ > 75% of salary ]
                #Short / Medium Term = 20 [ Existing multiple products, demat account, trading transactions ]
                #Frequent Product Switch = 20 [ multiple debit and credit cards, loans ]
                #Savings Oriented = 20 [ travelling, shoping ]
                #Salaried = 20 [ Annual income up-to 36 lacs ]
                
                
                ##########NLTK to be done for input!!!!!!!!!
                RiskCapacity="moderate"
                if (RiskCapacity == "low" or RiskCapacity=="moderate"):
                    
                    for i in range(len(tb1)):
                        if tb1[i] == Product:
                            if tb1[i+1] == "Plan":
                                if tb1[i+3] == "Dividend":
                                    d1=tb1[i]
                                    d2=tb1[i+1]
                                    d3=tb1[i+3]
                                    val1=tb1[i+4]
                                    d4=tb1[i+5]
                                    d5=tb1[i+6]
                                    d6=tb1[i+7]
                            
                for j in range(len(tb1)):
                    for j in range(len(tb1)):
                        if tb1[j] == Product:
                            if tb1[j+1] == "Plan":
                                if tb1[j+3] == "Growth":
                                    g1=tb1[j]
                                    g2=tb1[j+1]
                                    g3=tb1[j+3]
                                    val2=tb1[j+4]
                                    g4=tb1[j+5]
                                    g5=tb1[j+6]
                                    g6=tb1[j+7]
                            
                 
                #print(d1,d2,val1,d3,d4,d5,d6)
                #print("\n",g1,g2,val2,g3,g4,g5,g6)
                
                p=bs.find_all("li",attrs={"class":"bullet05"})
                p1 = str(p[1].text).split('\n')
                ul = []
                
                for a in range(len(p1)):
                    b=p1[a]
                    ul.append(b)
                
                e=" ".join(ul)
                #print("exact list is:",ul)
                
                #print(p1)
                #print("ans",type(p1))
                #print("ans",p[1].strip('\n').split())
                #print(p2)
            
                ft=bs.find_all("div", attrs={"class":"keyFeatureCont"})
                
                ##Imp start ##
                ft1=str(ft[0].text).split() 
                ##Ump end ##
                
                for i in range(len(ft1)):
                    if ft1[i] == "Application":
                        if ft1[i+1] == "Amount":
                                    dd1=ft1[i]
                                    dd2=ft1[i+1]
                                    dd3=ft1[i+2]
                                    val3=ft1[i+3]
                                    dd4=ft1[i+4]
                                    dd5=ft1[i+5]
                                    dd6=ft1[i+6]
                                    dd7=ft1[i+7]
                            
                for j in range(len(ft1)):
                    if ft1[j] == "Minimum":
                        if ft1[j+1] == "Redemption":
                                if ft1[j+2] == "Amt.":
                                    gg1=ft1[j]
                                    gg2=ft1[j+1]
                                    gg3=ft1[j+2]
                                    val4=ft1[j+3]
                                    gg4=ft1[j+4]
                                    gg5=ft1[j+5]
                                    gg6=ft1[j+6]
                                    gg7=ft1[j+7]
                                    gg8=ft1[j+8]
                  
                #print("\nfeatures:  \n\n\n\n",type(ft1),ft1)
                
                if val2 > val1:
                    print("\n*  Scheme Name                                         :",g1,g2,g3)
                    print("\n ##### Following are the key features #####")
                    print("\n1. Latest NAV =",val2)
                    print("\n2." ,e )
                    print("\n3.",dd1,dd2,"=" ,dd3,val3,dd4,dd5,dd6,dd7)
                    print("\n4.",gg1,gg2,gg3,"=" ,val4,gg4,gg5,gg6,gg7,gg8 )
                elif val2 < val1:
                    print("\n*  Scheme Name                                         :",g1,g2,g3)
                    print("\n ##### Following are the key features #####")
                    print("\n1. Latest NAVt=",val1) 
                    print("\n2" ,e )
                    print("\n3",dd1,dd2, "=" ,dd3,val3,dd4,dd5,dd6,dd7)
                    print("\n4.",gg1,gg2,gg3, "=" ,val4,gg4,gg5,gg6,gg7,gg8 )

                elif val1 == val2:
                    print("\n*  Scheme Name                                          :" ,g1,g2,g3)
                    print("\n ##### Following are the key features #####",d4,d5,d6)
                    print("\n1. Latest NAV=",val2)  
                    print("\n2.",e )
                    print("\n3.",dd1,dd2,  "=" ,dd3,val3,dd4,dd5,dd6,dd7)
                    print("\n4.",gg1,gg2,gg3,"=" ,val4,gg4,gg5,gg6,gg7,gg8 )                    
                    
                #elif(RiskCapacity == "High")
                
                #print(" ".join(tb1.split()))
                
                #----------------------------q=tb[0].text.strip().split('\n')
                #print(q)
                
                #print("check :\n\n\n\n",q)
                
                
                #tb=str(q)
                
                #tkn=word_tokenize(tb)
                #print("token\n\n\n\n",tkn)
                
                #print("lets see \n\n\n",tb.findall("tr"))

                
                #print("table",type(t))
                #s1=bs.find_all("div", attrs={"class": "fundDetail"})
                #print("finally:",s1[0].text.strip())
                #print("check re:",bs.find_all("div", attrs={"class": "fundDetail"}),"\n\n\n")
                
                #usage:print("check re modified:",bs.find_all("div", attrs={"class": "fundDetail"}, string=re.compile("fundDetail"))
                
                #print("answer2",s[1].text)
                #ff=s[0].text
                #print(ff.stripped_strings)
                #print("finally")
                #print(mylist[0].get_text())
                #a=t1.__getitem__(0)
                #print("\n\n\n\ndata2:",bs.find_all(string=re.compile("Prudential")))
                
                #print(bs.tr.get_text())
                #aaa=bs.tr.get_text()
                
               # print("final:",
                
                #for b in a.stripped_strings:
                #    print (b)
                
                #print("result",a)
                #print("final",a.attrs)
                #print("final",a.string[0])
                
                #tt=t.contents[0]
                #a=t1.__getitem__(1)
                #print("\n\n\n\nzero",tw.
                
                #print(bs)
                
                #print("\n para : ",t1.string)

            except AttributeError as e:
                print(e)
            
            b=input("\nDo you want to see more details ? Entering *Yes* will access your system browser to display product.\n")

            if(b=="Yes" or b=="YES" or b=="yes" or b=="y" or b=="Y"):
                webbrowser.open(url)
                print("Thank you, Visit again!!!")
            else:
                print("Thank You, Visit again!!!")
            
            file.close()       
       # print("Response Time:",end-start) 

    
### Irrespective of Business Hours, CODE to run when System Maintenance / CBS is down  / Internet connection is down ###########    
        
        #Connection_Success=0
        
        except ConnectionError:            
            now10 = datetime.datetime.now()
            
            now1=now10.strftime('%Y-%m-%d %H:%M:%S')
                    #print(now)
                    #now=now.date()    
            now=str(now1)
                    #now=now.strftime('%d-%b-%Y')
        #-----------------------------------------------------------
                    #b=df14["Month"].max()
            d = datetime.datetime.strptime(now,"%Y-%m-%d %H:%M:%S")
            d2=str(d)
            d3=datetime.datetime.strptime(d2, "%Y-%m-%d %H:%M:%S")
            
            if(os.path.isfile("/Users/orbaa5/Desktop/Dissertation/Thesis/Data/TrainingData/ICICIPrudential.html")):
    ###         
                    rp=os.path.isfile("/Users/orbaa5/Desktop/Dissertation/Thesis/Data/TrainingData/ICICIPrudential.html")
                    #True / False ( response file check )            
                    #print("Not run!!!!!!!!!!!!!!!!!!!!!!!!",os.path.isfile("/Users/orbaa5/Desktop/Dissertation/Thesis/Data/TrainingData/ICICIPrudential.html"))
                    print("\n##### OFFLINE MODE STARTED [ 6PM to 7AM or during Network Failure]; chatbot access to local system instead of ICICI Bank System #####\n")
                    file=open("/Users/orbaa5/Desktop/Dissertation/Thesis/Data/TrainingData/ICICIPrudential.html")
                    bs=BeautifulSoup(file,"lxml") # "lxml parser" is fast as compared to "HTML parser"
                    #print("proceed",type(bs))
                    c1=bs.div(id="container")
                    c2=bs.div(id="rightpart")
                    c3=bs.div(id="DivContent")
                    c4=bs.div(id="Content_ctl01_ctl00_ctl00_detailContainer")
                    c5=bs.div(id="Content_C003_divNav")
                    
                    if(c1==[] or c2== [] or c3==[] or c4==[] or c5==[]):
                        print("Warning!!! Site content changed. Will be fixed in next 24 hours")
                        file.close()
                    else:
                        #print("type importabt",type(c1))
                        #print("type",type(bs))
                        mt1=os.path.getctime("/Users/orbaa5/Desktop/Dissertation/Thesis/Data/TrainingData/ICICIPrudential.html")        
            #mt2=time.ctime(int(mt1))
                        mt=time.strftime('%d-%B-%Y %H:%M:%S',time.localtime(int(mt1)))
                        mt2= datetime.datetime.strptime(mt,'%d-%B-%Y %H:%M:%S')
                        
                        if( d3.hour >= 12) and ( d3.hour <= 23 ): 
                            print("1. Product document exist on local system Hard Drive     : Status = Success , Code =",rp)
                            print("2. Product Modified date [ Local system hard drive ]     : HTML file Verified on ",mt2.day,"",calendar.month_abbr[mt2.month],"",mt2.year,",",mt2.hour-12,":",mt2.minute,"PM")
 
                        elif ( d3.hour >= 0 ) and ( d3.hour <= 11 ): 
                            print("1. Product document exist on local system Hard Drive     : Status = Success , Code =",rp)
                            print("2. Product Modified date [ Local system hard drive ]     : HTML file Verified on ",mt2.day,"",calendar.month_abbr[mt2.month],"",mt2.year,",",mt2.hour,":",mt2.minute,"AM")                 
            
                #now10 = datetime.datetime.now()
                #now1=now10.strftime('%Y-%m-%d %H:%M:%S')
                #print(now)
                #now=now.date()    
                #now=str(now1)
                #now=now.strftime('%d-%b-%Y')
    #-----------------------------------------------------------
                #b=df14["Month"].max()
                #dz = datetime.datetime.strptime(now,"%Y-%m-%d %H:%M:%S")
                #d2z=str(dz)
                #d3z=datetime.datetime.strptime(d2z, "%Y-%m-%d %H:%M:%S")
                        
                        s10 = bs.find_all(class_="fundDetail")
                        print("\n ##### Following is the Product suggested as per your requirement ##### \n")
                        print("\n*  Mutual Fund Name                                    : ",s10[0].text.strip())
                        
                        #print("Scheme Name:\n\n")
    # Imp: This removes any whitespace (newlines, spaces, tabs, etc.) between two newlines.                    
                        
                        #Not working---s1 = bs.find_all(class_="applicationFormTable navUpRate")
                        #Not working print("Scheme==>\n",s1[0].text.strip())
                        s1 = bs.find_all("td", string=re.compile("Direct"))
                        #print("Latest=>",s1)
                        
                        tb=bs.find_all("table", attrs={"class":"applicationFormTable navUpRate"})
                        #print("table type",type(tb),"\n\n\n")
                        #print("tb is",tb)
                        
                        #print("type important", type(tb[0].text))
                        #tb1=str(tb[0].text).split()
                        tb1=tb[0].text.split() # Convert Sting TO LIST ( of tokens ) for iteration

                        #print(tb1)
                        #print(type(tb1))
                        #print("length tb1:",len(tb1))
                        
                        #print("\n\n\n\n\n",tb1[9])
                        #print("\n\n\n\n",tb1[10])
                        
                        #######Business Rule, [ Total Risk weightege = 100 ]########
                        
                        ########Growth Plan
                        #Moderate Spending = 20 [ <= 75 % of salary ]
                        #Long Term = 20 [ Existing products for long term perspective ]
                        #Infrequent Product Switch = 20 [ <=2 ATM , <=1 credit card, <= 2 Loans   ]
                        #Savings Oriented = 20 [ Travelling, shopping etc ]
                        #Salaried = 20 [ Annual income 5 Lacs]
                        
                        ########Dividend Plan
                        #High Spending = 20 [ > 75% of salary ]
                        #Short / Medium Term = 20 [ Existing multiple products, demat account, trading transactions ]
                        #Frequent Product Switch = 20 [ multiple debit and credit cards, loans ]
                        #Savings Oriented = 20 [ travelling, shoping ]
                        #Salaried = 20 [ Annual income up-to 36 lacs ]
                        
                        
                        ##########NLTK to be done for input!!!!!!!!!
                        RiskCapacity="moderate"
                        if (RiskCapacity == "low" or RiskCapacity=="moderate"):
                            
                            for i in range(len(tb1)):
                                if tb1[i] == Product:
                                    if tb1[i+1] == "Plan":
                                        if tb1[i+3] == "Dividend":
                                            d1=tb1[i]
                                            d2=tb1[i+1]
                                            d3=tb1[i+3]
                                            val1=tb1[i+4]
                                            d4=tb1[i+5]
                                            d5=tb1[i+6]
                                            d6=tb1[i+7]
                                    
                        for j in range(len(tb1)):
                            for j in range(len(tb1)):
                                if tb1[j] == Product:
                                    if tb1[j+1] == "Plan":
                                        if tb1[j+3] == "Growth":
                                            g1=tb1[j]
                                            g2=tb1[j+1]
                                            g3=tb1[j+3]
                                            val2=tb1[j+4]
                                            g4=tb1[j+5]
                                            g5=tb1[j+6]
                                            g6=tb1[j+7]
                                    
                         
                        #print(d1,d2,val1,d3,d4,d5,d6)
                        #print("\n",g1,g2,val2,g3,g4,g5,g6)
                        
                        p=bs.find_all("li",attrs={"class":"bullet05"})
                        p1 = str(p[1].text).split('\n')
                        ul = []
                        
                        for a in range(len(p1)):
                            b=p1[a]
                            ul.append(b)
                        
                        e=" ".join(ul)
                        #print("exact list is:",ul)
                        
                        #print(p1)
                        #print("ans",type(p1))
                        #print("ans",p[1].strip('\n').split())
                        #print(p2)
                    
                        ft=bs.find_all("div", attrs={"class":"keyFeatureCont"})
                        
                        ##Imp start ##
                        ft1=str(ft[0].text).split() 
                        ##Ump end ##
                        
                        for i in range(len(ft1)):
                            if ft1[i] == "Application":
                                if ft1[i+1] == "Amount":
                                            dd1=ft1[i]
                                            dd2=ft1[i+1]
                                            dd3=ft1[i+2]
                                            val3=ft1[i+3]
                                            dd4=ft1[i+4]
                                            dd5=ft1[i+5]
                                            dd6=ft1[i+6]
                                            dd7=ft1[i+7]
                                    
                        for j in range(len(ft1)):
                            if ft1[j] == "Minimum":
                                if ft1[j+1] == "Redemption":
                                        if ft1[j+2] == "Amt.":
                                            gg1=ft1[j]
                                            gg2=ft1[j+1]
                                            gg3=ft1[j+2]
                                            val4=ft1[j+3]
                                            gg4=ft1[j+4]
                                            gg5=ft1[j+5]
                                            gg6=ft1[j+6]
                                            gg7=ft1[j+7]
                                            gg8=ft1[j+8]
                          
                        #print("\nfeatures:  \n\n\n\n",type(ft1),ft1)
                        
                        if NAV == "Higher":

                            if val2 > val1:
                                print("\n*  Scheme Name                                         :",g1,g2,g3)
                                print("\n ##### Following are the key features #####")
                                print("\n1. Latest NAV =",val2)
                                print("\n2." ,e )
                                print("\n3.",dd1,dd2,"=" ,dd3,val3,dd4,dd5,dd6,dd7)
                                print("\n4.",gg1,gg2,gg3,"=" ,val4,gg4,gg5,gg6,gg7,gg8 )
                            elif val2 < val1:
                                print("\n*  Scheme Name                                          :",g1,g2,g3)
                                print("\n ##### Following are the key features #####")
                                print("\n1. Latest NAVt=",val1) 
                                print("\n2" ,e )
                                print("\n3",dd1,dd2, "=" ,dd3,val3,dd4,dd5,dd6,dd7)
                                print("\n4.",gg1,gg2,gg3, "=" ,val4,gg4,gg5,gg6,gg7,gg8 )
        
                            elif val1 == val2:
                                print("\n*  Scheme Name                                           :" ,g1,g2,g3)
                                print("\n ##### Following are the key features #####")
                                print("\n1. Latest NAV=",val2)  
                                print("\n2.",e )
                                print("\n3.",dd1,dd2,  "=" ,dd3,val3,dd4,dd5,dd6,dd7)
                                print("\n4.",gg1,gg2,gg3,"=" ,val4,gg4,gg5,gg6,gg7,gg8 )                    
                                                        
                        b=input("Do you want to see more details ? Entering *Yes* will access your system browser to display product.\n")
                        if(b=="Yes" or b=="YES" or b=="yes" or b=="Y" or b=="y"):
                            webbrowser.open(url)
                            print("Thank You, Visit Again !!!")
                        else:
                            print("Thank You !!! Visit again")
                        file.close()
            else:
                    print("file does not eixst")


def Average_Exp():    
    df16["Transaction Date"] = pd.to_datetime(df16["Transaction Date"], format="%d/%m/%Y" )
    df16["Year"] = df16["Transaction Date"].apply(lambda x: (x.year))
    df16["Week"] = df16["Transaction Date"].apply(lambda x: (x.week))
    df16["Day"] = df16["Transaction Date"].apply(lambda x: (x.day))
    df16["MonthInDays"] = df16["Transaction Date"].apply(lambda x: (x.month))
    df16["Month"] = df16["MonthInDays"].apply(lambda x: calendar.month_abbr[x])
    df16.drop(df16.columns[[9]], axis = 1, inplace=True )
    #print(df16)
    #a=df16.pivot_table(index=["Year"],values=["Withdrawal Amount (INR )"],aggfunc=sum)
    #print("\n Total Expenditure is : \n\n",a)
    #a1=input("\n Anything else, Aman>> ")
   # if (a1=="avg exp"):
    avg=df16.pivot_table(index=["Year"],values=["Withdrawal Amount (INR )"],aggfunc=np.mean)
    #a3=df16.pivot_table(index=["Year"],values=["Withdrawal Amount (INR )"],aggfunc=np.std)
        #print("\n Average expenditure is: \n\n ",a2)
        #print("\\nn Compared to Average, you have spend following additional amount: \n",a3)
    
    avg=str(avg).split()
    
    
    for i in range(len(avg)):
        if avg[i]=="Amount":
            ct1=avg[i+5]
            ct2=avg[i+7]
            ct3=avg[i+9]
            ct4=avg[i+11]
            ct5=avg[i+13]
            ct6=avg[i+15]
    
    ct1 = int(float(ct1))
    ct2 = int(float(ct2))
    ct3 = int(float(ct3))
    ct4 = int(float(ct4))
    ct5 = int(float(ct5))
    ct6 = int(float(ct6))

    
    aver=int((ct1+ct2+ct3+ct4+ct5+ct6))/6
    aver = int(aver)
      
    return aver
        

def AverageMonthly_Bal():    
    df17["Transaction Date"] = pd.to_datetime(df17["Transaction Date"], format="%d/%m/%Y" )
    df17["Year"] = df17["Transaction Date"].apply(lambda x: (x.year))
    df17["Week"] = df17["Transaction Date"].apply(lambda x: (x.week))
    df17["Day"] = df17["Transaction Date"].apply(lambda x: (x.day))
    df17["MonthInDays"] = df17["Transaction Date"].apply(lambda x: (x.month))
    df17["Month"] = df17["MonthInDays"].apply(lambda x: calendar.month_abbr[x])
    df17.drop(df17.columns[[9]], axis = 1, inplace=True )
    #print(df16)
    #a1=df17.pivot_table(index=["Year"],values=["Withdrawal Amount (INR )"],aggfunc=sum)
    a2=df17.pivot_table(index=["Month"],values=["Balance (INR )"] )
    z=a2.mean().round()
    z1=int(z)
    #print(a2)
    #print("\nchatBOT>>> Average Monthly Balance is: INR",int(z))

    return z1        

def Electricity_BSES():
    df2["Electricity"] = np.where(df2["Transaction Remarks"].str.contains(('^BIL/............/*BSES*')) |
    df2["Transaction Remarks"].str.contains(('^BIL/............/BPC - Bill Desk/BSES*'))|
    df2["Transaction Remarks"].str.contains(('^BIL/............/PGMIB-/BSES*')) |
    df2["Transaction Remarks"].str.contains(('^IIN/I-Debit/BSES...../*')), 1,0)
    df2.drop(df2.columns[[0,1,3]], axis = 1, inplace=True )
#print(df2)
#    for index, row in df2.iterrows():
 #       if row['Electricity'] == 0:
  #          df2.drop(index,inplace=True)   
    for i in range(len(df2)):    
        if df2.loc[:,'Electricity'][i] == 0:
            df2.drop(index = [i], axis=0,inplace=True) 
    df2.reset_index(inplace=True)
    df2.drop(df2.columns[0],axis=1,inplace=True)        
    
    for i in range(len(df2)):    
       if df2.loc[:,'Withdrawal Amount (INR )'][i] == 0 and df2.loc[:,'Deposit Amount (INR )'][i] > 0 :
 #          if df7.bool(df7["Transaction Remarks"].str.contains(('^MMT/............/*'))) :
            df2.drop(index = [i], axis=0,inplace=True ) 
    df2.reset_index(inplace=True)
    df2.drop(df2.columns[0],axis=1,inplace=True)    
    

    df2["Transaction Date"] = pd.to_datetime(df2["Transaction Date"], format="%d/%m/%Y" )                   
    df2["Year"] = df2["Transaction Date"].apply(lambda x: (x.year))
    df2["Week"] = df2["Transaction Date"].apply(lambda x: (x.week))             
    df2["Day"]  = df2["Transaction Date"].apply(lambda x: (x.day))
    df2["MonthInDays"] = df2["Transaction Date"].apply(lambda x: (x.month))
    df2["Month"] = df2["MonthInDays"].apply(lambda x: calendar.month_abbr[x])
     
    df100 = df2[ (df2['Year']==2017) | (df2['Year']==2018 )]
    #https://stackoverflow.com/questions/40885318/create-a-new-dataframe-from-selecting-specific-rows-from-existing-dataframe-pyth?rq=1
    #print(df100)     

    df100.pivot_table(index=["Month"],values=["Withdrawal Amount (INR )"])
    df100.reset_index(drop=True, inplace=True)
    #df100 = df100[df100['Withdrawal Amount (INR )']==1290)]
    #print(df100)
    #print(df100)

    #print(df100)
    #print("\n=================Electricity Bill Summary===============\n")
    total = 0
    for i in range(len(df100)):
        #count=0
        #if i == len(df100): 
         #   break
         if df100.loc[:,'Year'][i] == 2017:
          #   if df100.loc[:,'Withdrawal Amount (INR )'][i] == 3760:
           #   return
           # or df100.loc[:,'Year'][i] == 2018 :
            #print(df100.loc[:,'Year'][i])
          #df18["Transaction Date"] = pd.to_dateti1e( df18.loc[:,'Transaction Date'][i], format="%d/%m/%Y" )      
          #df18.loc[:,'Transaction Date'][i]
             old=df100.loc[:,'Withdrawal Amount (INR )'][i]
             new=df100.loc[:,'Withdrawal Amount (INR )'][i+1]
             diff=new-old
              
             if diff < 0:
                  exp=old-new
                  #print(df100["Month"][i],df100.loc[:,'Year'][i],",INR",int(round(df100.loc[:,'Withdrawal Amount (INR )'][i])),"Savings in",df100["Month"][i+1],"=",int(round((exp*100)/new)),"% [ INR",int(round(exp)),"]")
                  #print("\n")
                  total = total+exp
             if diff > 0:
                  #print(df100["Month"][i],df100.loc[:,'Year'][i],",INR",int(round(df100.loc[:,'Withdrawal Amount (INR )'][i])))       
                  #print("\n")
                  amount=5000
    if total <=amount:
        day1=290
        day2=590
        date1="March 2018"
        #print("\n===========Savings and Future Investments=============")
        #print("\nTotal Savings :INR",int(round(total)),"/Year\n\n""Investment: Since your amount is <=INR",int(round(amount)),"hence you are eligible to invest in X% p.a",day1,"days or",day2,"days FD [applicable upto]",date1) 
        
        total=int(total/12)
        return total
           
def Telephone_MTNL():
    df3["Telephone"] = np.where(df3["Transaction Remarks"].str.contains(('^BIL/............/BPC - Bill Desk/MTNL*')) |
    df3["Transaction Remarks"].str.contains(('^IIN/MTNL*'))|
    df3["Transaction Remarks"].str.contains(('^VIN/MTNL*')) |
    df3["Transaction Remarks"].str.contains(('^BIL/............/PGMIB-/MTNL*'))|
    df3["Transaction Remarks"].str.contains(('^BIL/............//MTNL*')) |
    df3["Transaction Remarks"].str.contains(('^IIN/I-Debit/M T N L*')) |
    df3["Transaction Remarks"].str.contains(('^BIL/............/Mahanagar Telephone Nigam/MTNL*')), 1,0)
    df3.drop(df3.columns[[0,1,3]], axis = 1, inplace=True )
    
    #for index, row in df3.iterrows():
     #if row['Telephone'] == 0:
      #      df3.drop(index,inplace=True)
    for i in range(len(df3)):    
        if df3.loc[:,'Telephone'][i] == 0:
            df3.drop(index = [i], axis=0,inplace=True) 
    df3.reset_index(inplace=True)
    df3.drop(df3.columns[0],axis=1,inplace=True)        

    for i in range(len(df3)):    
       if df3.loc[:,'Withdrawal Amount (INR )'][i] == 0 and df3.loc[:,'Deposit Amount (INR )'][i] > 0 :
 #          if df7.bool(df7["Transaction Remarks"].str.contains(('^MMT/............/*'))) :
            df3.drop(index = [i], axis=0,inplace=True ) 
    df3.reset_index(inplace=True)
    df3.drop(df3.columns[0],axis=1,inplace=True)              
            
   # if (b == "Telephone" or "MTNL" or "phone" or "PHONE" or "TELEPHONE" or "mtnl") :
    #    print("\nResponse->>>>>>>>>>>>Hi Aman!!! You have paid:",df3["Telephone"].sum(),"MTNL bills \n")
     #   c=input("Do you also want to see transactions graphically ( YES / NO ) " )

    #if(c=="YES"):
    #print("got it Here is the solution -------")
    df3["Transaction Date"] = pd.to_datetime(df3["Transaction Date"], format="%d/%m/%Y" )                   
    df3["Year"] = df3["Transaction Date"].apply(lambda x: (x.year))
    df3["Week"] = df3["Transaction Date"].apply(lambda x: (x.week))             
    df3["Day"]  = df3["Transaction Date"].apply(lambda x: (x.day))
    df3["MonthInDays"] = df3["Transaction Date"].apply(lambda x: (x.month))
    df3["Month"] = df3["MonthInDays"].apply(lambda x: calendar.month_abbr[x])
    df3.drop(df3.columns[[9]], axis = 1, inplace=True )

    #df3.groupby(["Year","Telephone"]).size()
    d = df3.pivot_table(index="Year",values=["Withdrawal Amount (INR )"],aggfunc=np.mean)
    #print(d)
    #plt.plot(df3["Month"],df3["Telephone"])
    df3.to_excel("/Users/orbaa5/Desktop/Dissertation/Thesis/Data/TrainingResult/MTNL.xls")
        #print(df1)
    #print(d)
    
    d=str(d).split()
    
    for i in range(len(d)):
        if d[i]=="Amount":
            ct1=d[i+5]
            ct2=d[i+7]
            ct3=d[i+9]
            ct4=d[i+11]
            ct5=d[i+13]
            ct6=d[i+15]
    
    ct1 = int(float(ct1))
    ct2 = int(float(ct2))
    ct3 = int(float(ct3))
    ct4 = int(float(ct4))
    ct5 = int(float(ct5))
    ct6 = int(float(ct6))

    
    aver1=int((ct1+ct2+ct3+ct4+ct5+ct6))/6
    aver1 = int(aver1)
    
    return aver1


def Water_DJB():
    df4["Water"] = np.where(df4["Transaction Remarks"].str.contains(('^VIN/Delhi_Jal_B*')) |
#    BIL/000740008562/CITRUS PAYMENT SOLUT/DELHIJALBO01        
    df4["Transaction Remarks"].str.contains(('^BIL/............/*.*/DELHIJAL*')), 1,0)
    df4.drop(df4.columns[[0,1,3]], axis = 1, inplace=True )

    for i in range(len(df4)):    
        if df4.loc[:,'Water'][i] == 0:
            df4.drop(index = [i], axis=0,inplace=True) 
    df4.reset_index(inplace=True)
    df4.drop(df4.columns[0],axis=1,inplace=True)      
    
    for i in range(len(df4)):    
       if df4.loc[:,'Withdrawal Amount (INR )'][i] == 0 and df4.loc[:,'Deposit Amount (INR )'][i] > 0 :
 #          if df7.bool(df7["Transaction Remarks"].str.contains(('^MMT/............/*'))) :
            df4.drop(index = [i], axis=0,inplace=True ) 
    df4.reset_index(inplace=True)
    df4.drop(df4.columns[0],axis=1,inplace=True)    
    #for index, row in df4.iterrows():
     #   if row['Water'] == 0:
      #      df4.drop(index,inplace=True)
            
    #if (b == "Water" or "DJB" ) :
     #   print("\nResponse->>>>>>>>>>>>Hi Aman!!! You have paid:",df4["Water"].sum(),"Water bills \n")
      #  c=input("Do you also want to see transactions graphically ( YES / NO ) " )

       # if(c=="YES"):
            
    df4["Transaction Date"] = pd.to_datetime(df4["Transaction Date"], format="%d/%m/%Y" )                   
    df4["Year"] = df4["Transaction Date"].apply(lambda x: (x.year))
    df4["Week"] = df4["Transaction Date"].apply(lambda x: (x.week))             
    df4["Day"]  = df4["Transaction Date"].apply(lambda x: (x.day))
    df4["MonthInDays"] = df4["Transaction Date"].apply(lambda x: (x.month))
    df4["Month"] = df4["MonthInDays"].apply(lambda x: calendar.month_abbr[x])
    df4.drop(df4.columns[[9]], axis = 1, inplace=True )

    df4.groupby(["Month","Water"]).size()
    d = df4.pivot_table(index="Month",values=["Withdrawal Amount (INR )"],aggfunc=np.mean)
    #print(d)
    #plt.plot(df4["Month"],df4["Water"])
    df4.to_excel("/Users/orbaa5/Desktop/Dissertation/Thesis/Data/TrainingResult/DJB.xls")
            #print(df1)
        
    d = str(d).split()    
    for i in range(len(d)):
        if d[i]=="Amount":
            ct1=d[i+5]
            ct2=d[i+7]
            ct3=d[i+9]
    
    ct1 = int(float(ct1))
    ct2 = int(float(ct2))
    ct3 = int(float(ct3))
    
    aver1=int((ct1+ct2+ct3))/3
    aver2 = int(aver1)

    return aver2



def Shopping(m,d):
    df5["Shopping"] = np.where(df5["Transaction Remarks"].str.contains(('^BIL/............/PGMIB-/AMAZON*')) |          
    df5["Transaction Remarks"].str.contains(('^BIL/............/BPC - Bill Desk/AMAZON*')) |   
    df5["Transaction Remarks"].str.contains(('^BIL/............//AMAZON*')) |   
    df5["Transaction Remarks"].str.contains(('^BIL/............/Amazon Seller Services Pv*')) |       
    df5["Transaction Remarks"].str.contains(('^UPI/............/*.*/amazon@apl*')) |   
    df5["Transaction Remarks"].str.contains(('^BIL/ONL/............/EMVANTAGE')) |    
    df5["Transaction Remarks"].str.contains(('^^BIL/............/*.*/SNAPDEAL.COM*')) |   
    df5["Transaction Remarks"].str.contains(('^BIL/............/flipkart.com/MP_FLIPKART*')) |   
    df5["Transaction Remarks"].str.contains(('^BIL/............/PGMIB-/MP_FLIPKART*')) |   
    df5["Transaction Remarks"].str.contains(('^BIL/............/PGMIB-/EBAY*')) |   
    df5["Transaction Remarks"].str.contains(('^BIL/............/BPC - Bill Desk/EBAY*')) |   
    df5["Transaction Remarks"].str.contains(('^BIL/............/eBay India/EBAY*')) |
    df5["Transaction Remarks"].str.contains(('^IPS/*.*/............../0')) |
    df5["Transaction Remarks"].str.contains(('^VIN/*.*/..............*')) |
    df5["Transaction Remarks"].str.contains(('^VPS/*.*/............../*')) |
    df5["Transaction Remarks"].str.contains(('^BIL/............/eBay India/EBAY*')) |
    df5["Transaction Remarks"].str.contains(('^BIL/............/COMMUNITY MATRIMONY./*')) |
    df5["Transaction Remarks"].str.contains(('^BIL/............//...............')) |
    df5["Transaction Remarks"].str.contains(('^BIL/ONL/............/BILL DESK*')) |
    df5["Transaction Remarks"].str.contains(('^IIN/homeshop18*')), 1,0)
   
    df5.drop(df5.columns[[0,1,3]], axis = 1, inplace=True )
    #for index, row in df5.iterrows():
     #   if row['Shopping'] == 0:
      #      df5.drop(index,inplace=True)    
#---------------------------------------------Amazon--------------------------------------

    df26["Shopping"] = np.where(df26["Transaction Remarks"].str.contains(('^BIL/............/PGMIB-/AMAZON*')) |          
    df26["Transaction Remarks"].str.contains(('^BIL/............/BPC - Bill Desk/AMAZON*')) |   
    df26["Transaction Remarks"].str.contains(('^BIL/............//AMAZON*')) |   
    df26["Transaction Remarks"].str.contains(('^BIL/............/Amazon Seller Services Pv*')) |       
    df26["Transaction Remarks"].str.contains(('^UPI/............/*.*/amazon@apl*')) |   
    df26["Transaction Remarks"].str.contains(('^BIL/ONL/............/EMVANTAGE')),1,0)     

    df26.drop(df26.columns[[0,1,3]], axis = 1, inplace=True )
    
    for i in range(len(df26)):    
        if df26.loc[:,'Shopping'][i] == 0:
            df26.drop(index = [i], axis=0,inplace=True) 
    df26.reset_index(inplace=True)
    df26.drop(df26.columns[0],axis=1,inplace=True) 

    for i in range(len(df26)):    
       if df26.loc[:,'Withdrawal Amount (INR )'][i] == 0 and df26.loc[:,'Deposit Amount (INR )'][i] > 0 :
 #          if df7.bool(df7["Transaction Remarks"].str.contains(('^MMT/............/*'))) :
            df26.drop(index = [i], axis=0,inplace=True ) 
    df26.reset_index(inplace=True)
    df26.drop(df26.columns[0],axis=1,inplace=True)

#----------------------------------------------------------------------------
    for i in range(len(df5)):    
        if df5.loc[:,'Shopping'][i] == 0:
            df5.drop(index = [i], axis=0,inplace=True) 
    df5.reset_index(inplace=True)
    df5.drop(df5.columns[0],axis=1,inplace=True) 

    for i in range(len(df5)):    
       if df5.loc[:,'Withdrawal Amount (INR )'][i] == 0 and df5.loc[:,'Deposit Amount (INR )'][i] > 0 :
 #          if df7.bool(df7["Transaction Remarks"].str.contains(('^MMT/............/*'))) :
            df5.drop(index = [i], axis=0,inplace=True ) 
    df5.reset_index(inplace=True)
    df5.drop(df5.columns[0],axis=1,inplace=True)
    
    df5.drop(df5[df5["Transaction Remarks"].str.contains(('^VIN/MTNL*'))].index, axis=0, inplace=True)
    df5.drop(df5[df5["Transaction Remarks"].str.contains(('^VIN/AIR INDIA L*'))].index, axis=0, inplace=True)
    df5.drop(df5[df5["Transaction Remarks"].str.contains(('^VIN/CLEARTRIP*'))].index, axis=0, inplace=True)
    df5.drop(df5[df5["Transaction Remarks"].str.contains(('^VIN/MAKEMYTRIP*'))].index, axis=0, inplace=True)
    df5.drop(df5[df5["Transaction Remarks"].str.contains(('^VIN/Delhi_Jal_B*'))].index, axis=0, inplace=True)
    df5.drop(df5[df5["Transaction Remarks"].str.contains(('^VIN/IBPS*'))].index, axis=0, inplace=True)
    df5.drop(df5[df5["Transaction Remarks"].str.contains(('^VIN/ETS.ets*'))].index, axis=0, inplace=True)
    
    #if (b == "shopping" or "amazon" or "Shopping" or "shop" or "SHOP" or "SHOPPING" ) :
        #print("\nResponse->>>>>>>>>>>>Hi Aman!!! You have performed :",df5["Shopping"].sum(),"Transactions on Shopping \n")
        
        #df5["Total Expenditure"] = df5.loc[:,'Withdrawal Amount (INR )'].sum()
        #print("\nResponse->>>>>>>>>>>>Hi Aman!!! Total expenditure :",df5["Total Expenditure"],"Transactions on Shopping \n")
        
        #c=input("What do you want to see now , enter as follows : 1 = 'Yearly expenditure', 2 = 'Max. Expenditure" )

       
            #print("got it Here is the solution -------")
    df5["Transaction Date"] = pd.to_datetime(df5["Transaction Date"], format="%d/%m/%Y" )                   
    df5["Year"] = df5["Transaction Date"].apply(lambda x: (x.year))
    df5["Week"] = df5["Transaction Date"].apply(lambda x: (x.week))             
    df5["Day"]  = df5["Transaction Date"].apply(lambda x: (x.day))
    df5["MonthInDays"] = df5["Transaction Date"].apply(lambda x: (x.month))
    df5["Month"] = df5["MonthInDays"].apply(lambda x: calendar.month_abbr[x])
    df5.drop(df5.columns[[9]], axis = 1, inplace=True )
        
#----------------------------Amazon-------------------------------------------------
    df26["Transaction Date"] = pd.to_datetime(df26["Transaction Date"], format="%d/%m/%Y" )                   
    df26["Year"] = df26["Transaction Date"].apply(lambda x: (x.year))
    df26["Week"] = df26["Transaction Date"].apply(lambda x: (x.week))             
    df26["Day"]  = df26["Transaction Date"].apply(lambda x: (x.day))
    df26["MonthInDays"] = df26["Transaction Date"].apply(lambda x: (x.month))
    df26["Month"] = df26["MonthInDays"].apply(lambda x: calendar.month_abbr[x])
            #print(df25)
            #test=df6.groupby("Month")
            #t=test.agg(len)
            #print(test.get_group("Jan"))
            #d = df6.pivot_table(index="Year",columns="Travel",aggfunc=sum)
    df26.rename(columns={'Withdrawal Amount (INR )': 'Amazon Amount'},inplace=True)
    #df26.drop(df26.columns[[0,1,3,4,5,7,8,9]], axis = 1, inplace=True )
            #print(df6)
            #print(df6)
    test26=df26.pivot_table(index=["Year"],columns=["Month"])
    test26=test26.unstack()
        
#---------------------------------Amazon purchases-------------------
    #now1 = datetime.datetime.now()
            #print(now)
            #now=now.date()
    #now=str(now1.date())
            #now=now.strftime('%d-%b-%Y')
#-----------------------------------------------------------
            #b=df14["Month"].max()
    #d = datetime.datetime.strptime(now, "%Y-%m-%d")
    #print(d.month)
            #print(d)
    #print("user entered month",m)
    #print("user enter date",d)
    #d2 = d - dateutil.relativedelta.relativedelta(months=m)
            #d2=d2.strftime('%d-%b-%Y')
            
    #print(d2)
    #d2=str(d2.date())
    #d3=datetime.datetime.strptime(d2, "%Y-%m-%d")
    #print("difference month:",d3.month)
    
#    5 march
    y=df26["Year"].max()
    #print("difference year:",d3.year)
    userm=m
    usery=y
    date=d
    total=0
    #print("year",y)
    #print("month",m)
    #print("day",d)
    #print(df26)
    #if df14.loc[:,'MonthInDays'][i] == userm and df14.loc[:,'Year'][i] == usery :

    #aa=df15["Transaction Date"].max()
    #bal=df15[df15["MonthInDays"]==userm]     
     #   df15[df15["MonthInDays"]==userm]["Balance (INR )"]       
    for i in range(len(df26)):
        count=0     
        if df26.loc[:,'MonthInDays'][i] == userm and df26.loc[:,'Year'][i] == usery and df26.loc[:,'Day'][i] == date:
            total+= df26.loc[:,'Amazon Amount'][i]
            #mth=df14.loc[:,'Month'][i]
            count=count+1
            #print(int(round(total)))
            #print(count)
            #print("df date",a)    
    for i in range(len(df26)):
        c=0
        if df26.loc[:,'MonthInDays'][i] == userm and df26.loc[:,'Year'][i] == usery and df26.loc[:,'Day'][i] == date :
            mth1=df26.loc[:,'Month'][i] 
            c=c+1
            print("\nExpenditure incurred on",d,"th of",mth1,",",usery,"is INR ",int(round(total)))
            break
        
#--------------------------------------Disabled----------------------------------------------
        
    df5.rename(columns={'Withdrawal Amount (INR )': 'Shopping Amount'},inplace=True)
    TotalShoppingExp=df5["Shopping Amount"].sum()
            #test=df6.groupby("Month")
            #t=test.agg(len)
            #print(test.get_group("Jan"))
            #d = df6.pivot_table(index="Year",columns="Travel",aggfunc=sum)
    #df5.drop(df5.columns[[0,1,3,4,5,7,8,9]], axis = 1, inplace=True )
            #print(df6)
            #print(df6)
    test=df5.pivot_table(index=["Year"],columns=["Month"])
    test=test.unstack()
    NoOfMonthsTotal=test.count()
            #NoOfMonthsTotal=test.nunique()
    MonthlyExpTotal=TotalShoppingExp / NoOfMonthsTotal.sum()
    TotalAmazonExp=df26["Amazon Amount"].sum()
    #print("\n\nchatBOT>>>==========Shopping Summary=========\n",df5.pivot_table(index=["Year"],values=["Shopping Amount"],aggfunc=sum))
            #Exp = z / Totalcount
            #print("\ncorrect:",z)
            #test.set_index("Month", inplace=True)
            #test["Month"][0]
            #total=df6["Withdrawal Amount (INR )"].sum()
            #yeartotal=year.mean().round()
            #count=df6["MonthInDays"].sum()
            #avg=total/count
            #df6.groupby(["Month"]).nunique()
            #df6.groupby(["Month"])
            #round1 = Diff*100/TotalTravelExp
            
    Diff=TotalShoppingExp-TotalAmazonExp#--------Others--------
    #print("\nchatBOT>>> Total Shopping Amount : INR",int(round(TotalShoppingExp)))
    #print("\nchatBOT>>> Amazon Expenditure : INR ",int(round(TotalAmazonExp)),"","[",int(round(TotalAmazonExp*100/TotalShoppingExp)),"% ]")
    #print("\nchatBOT>>> Others [ Flipkart, eBAY ] : INR ",int(round(Diff)),"","[",int(round(Diff*100/TotalShoppingExp)),"% ]")
    #print("\nchatBOT>>> Average Monthly Expenditure : INR",int(round(MonthlyExpTotal)))        
        #if(c=="1"):
            #df5.groupby(["Month","Shopping"]).size()
            #d = df5.pivot_table(index=["Year","Month"],columns="Withdrawal Amount (INR )",aggfunc=sum)
            #sum1 = df5.pivot_table(df5,index=["Year"],values=["Year"])
            #print("Total Expenditure is follows\n",sum1)
        #elif(c=="2"):   
         #   max1 = df5.pivot_table(df5,index=["Year"],aggfunc=max)            
          #  print("Total Expenditure is follows\n",max1)
            #plt.plot(df5["Month"],df5["Withdrawal Amount (INR )"])   
        #elif(c=="3"):   
         #   max1 = df5.pivot_table(df5,index=["Year"],aggfunc=mean)            
          #  print("Total Expenditure is follows\n",max1)
            
    df5.to_excel("/Users/orbaa5/Desktop/Dissertation/Thesis/Data/TrainingResult/Shopping.xls")
            #print(df1)
    
    #print("Yearly Avg. exp",MonthlyExpTotal)
    
    MonthlyExpTotal=int(MonthlyExpTotal)
    return MonthlyExpTotal





def Travel():
    df6["Travel"] = np.where(df6["Transaction Remarks"].str.contains(('IIN/www.irctc.c/............../0')) | 
            
    df6["Transaction Remarks"].str.contains(('^BIL/............/IRCTC INDIAN RAILWAY*')) |
    df6["Transaction Remarks"].str.contains(('^BIL/............/IRCTC MUMBAI SUBURBA*')) |
    df6["Transaction Remarks"].str.contains(('^IIN/www.irctc.c*')) |
    df6["Transaction Remarks"].str.contains(('^IIN/I-Debit/www.irctc.c*')) |
    df6["Transaction Remarks"].str.contains(('^IIN/I-Debit/irctc.c*')) |
    df6["Transaction Remarks"].str.contains(('^VIN/MAKEMYTRIP*')) |
    df6["Transaction Remarks"].str.contains(('^VIN/CLEARTRIP*')) |
    df6["Transaction Remarks"].str.contains(('^IIN/Clear Trip*')) |
    df6["Transaction Remarks"].str.contains(('^VIN/AIR INDIA L*')) |
    df6["Transaction Remarks"].str.contains(('^BIL/............/SPICEJET LTD/SPICEJET*')) |
    df6["Transaction Remarks"].str.contains(('^BIL/............/Bill Desk/RSRTC*')) |
    df6["Transaction Remarks"].str.contains(('^BIL/............/T Chg Rs10 ST Rs1.40*')) |
    df6["Transaction Remarks"].str.contains(('^BIL/............/PGMIB-/RSRTC*')) |
    df6["Transaction Remarks"].str.contains(('^BIL/............//RSRTC*')), 1,0)
    
    df6.drop(df6.columns[[0,1,3]], axis = 1, inplace=True )
    
#---------------------By Air-----------------------------------------------------    
    df25["Travel"] = np.where(df25["Transaction Remarks"].str.contains(('^VIN/MAKEMYTRIP*')) |
    df25["Transaction Remarks"].str.contains(('^VIN/CLEARTRIP*')) |
    df25["Transaction Remarks"].str.contains(('^IIN/Clear Trip*')) |
    df25["Transaction Remarks"].str.contains(('^VIN/AIR INDIA L*')) |
    df25["Transaction Remarks"].str.contains(('^BIL/............/SPICEJET LTD/SPICEJET*')), 1,0)
    
    df25.drop(df25.columns[[0,1,3]], axis = 1, inplace=True )
    #print(df25["Travel"])
    for i in range(len(df25)):    
        if df25.loc[:,'Travel'][i] == 0:
            df25.drop(index = [i], axis=0,inplace=True) 
    df25.reset_index(inplace=True)
    df25.drop(df25.columns[0],axis=1,inplace=True) 

    for i in range(len(df25)):    
       if df25.loc[:,'Withdrawal Amount (INR )'][i] == 0 and df25.loc[:,'Deposit Amount (INR )'][i] > 0 :
 #          if df7.bool(df7["Transaction Remarks"].str.contains(('^MMT/............/*'))) :
            df25.drop(index = [i], axis=0,inplace=True ) 
    df25.reset_index(inplace=True)
    df25.drop(df25.columns[0],axis=1,inplace=True)
    #print(df25)
#---------------------------------------------------------------------------------------    
    #print(df6.loc[:,"Travel"][0])
    #print(df6.loc[:,"Travel"][28])    
    for i in range(len(df6)):    
        if df6.loc[:,'Travel'][i] == 0:
            df6.drop(index = [i], axis=0,inplace=True) 
    df6.reset_index(inplace=True)
    df6.drop(df6.columns[0],axis=1,inplace=True) 

    for i in range(len(df6)):    
       if df6.loc[:,'Withdrawal Amount (INR )'][i] == 0 and df6.loc[:,'Deposit Amount (INR )'][i] > 0 :
 #          if df7.bool(df7["Transaction Remarks"].str.contains(('^MMT/............/*'))) :
            df6.drop(index = [i], axis=0,inplace=True ) 
    df6.reset_index(inplace=True)
    df6.drop(df6.columns[0],axis=1,inplace=True)
   
    #if (b == "Travel" or "TRAVEL" or "train" or "TRAIN" or "IRCTC" or "irctc" or "travel" ) :
        #print("\nResponse->>>>>>>>>>>>Hi Aman!!! You have booked your online travelling :",df6["Travel"].sum(),"times \n")
        #c=input("Do you also want to see transactions graphically ( YES / NO ) " )
            #print("got it Here is the solution -------")
    df6["Transaction Date"] = pd.to_datetime(df6["Transaction Date"], format="%d/%m/%Y" )                   
    df6["Year"] = df6["Transaction Date"].apply(lambda x: (x.year))
    df6["Week"] = df6["Transaction Date"].apply(lambda x: (x.week))             
    df6["Day"]  = df6["Transaction Date"].apply(lambda x: (x.day))
    df6["MonthInDays"] = df6["Transaction Date"].apply(lambda x: (x.month))
    df6["Month"] = df6["MonthInDays"].apply(lambda x: calendar.month_abbr[x])
    #df6.drop(df6.columns[[9]], axis = 1, inplace=True )
    
#----------------------By Air--------------------------------------------------
    df25["Transaction Date"] = pd.to_datetime(df25["Transaction Date"], format="%d/%m/%Y" )                   
    df25["Year"] = df25["Transaction Date"].apply(lambda x: (x.year))
    df25["Week"] = df25["Transaction Date"].apply(lambda x: (x.week))             
    df25["Day"]  = df25["Transaction Date"].apply(lambda x: (x.day))
    df25["MonthInDays"] = df25["Transaction Date"].apply(lambda x: (x.month))
    df25["Month"] = df25["MonthInDays"].apply(lambda x: calendar.month_abbr[x])
    #print(df25)
    TotalByAirExp=df25["Withdrawal Amount (INR )"].sum()
    #test=df6.groupby("Month")
    #t=test.agg(len)
    #print(test.get_group("Jan"))
    #d = df6.pivot_table(index="Year",columns="Travel",aggfunc=sum)
    df25.rename(columns={'Withdrawal Amount (INR )': 'Travel Amount'},inplace=True)
    df25.drop(df25.columns[[0,1,3,4,5,7,8,9]], axis = 1, inplace=True )
    #print(df6)
    #print(df6)
    test25=df25.pivot_table(index=["Year"],columns=["Month"])
    test25=test25.unstack()
    #NoOfMonthsAir=test25.count()
    #print("by air",test25)
    #test25.
    #MonthlyExpAir=TotalByAirExp / NoOfMonthsAir.sum()
    #print("total sum", TotalExpAir)
    #print("incorrect:", z25)
    #print("\nchatBOT>>> Average Monthly Expenditure [ Airlines ] : INR",int(MonthlyExpAir))
#---------------------------------------------------------------------------------------------            
    df6.rename(columns={'Withdrawal Amount (INR )': 'Travel Amount'},inplace=True)
    TotalTravelExp=df6["Travel Amount"].sum()
    #test=df6.groupby("Month")
    #t=test.agg(len)
    #print(test.get_group("Jan"))
    #d = df6.pivot_table(index="Year",columns="Travel",aggfunc=sum)
    df6.drop(df6.columns[[0,1,3,4,5,7,8,9]], axis = 1, inplace=True )
    #print(df6)
    #print(df6)
    test=df6.pivot_table(index=["Year"],columns=["Month"])
    test=test.unstack()
    NoOfMonthsTotal=test.count()
    #NoOfMonthsTotal=test.nunique()
    MonthlyExpTotal=TotalTravelExp / NoOfMonthsTotal.sum()
    #print("\nchatBOT>>>==========Travel Charges Summary=========\n",df6.pivot_table(index=["Year"],values=["Travel Amount"],aggfunc=sum))
    #Exp = z / Totalcount
    #print("\ncorrect:",z)
    #test.set_index("Month", inplace=True)
    #test["Month"][0]
    #total=df6["Withdrawal Amount (INR )"].sum()
    #yeartotal=year.mean().round()
    #count=df6["MonthInDays"].sum()
    #avg=total/count
    #df6.groupby(["Month"]).nunique()
    #df6.groupby(["Month"])
    #round1 = Diff*100/TotalTravelExp
    
    #Diff=TotalTravelExp-TotalByAirExp#--------Others--------
    #print("\nchatBOT>>> Total  : INR",int(round(TotalTravelExp)))
    #print("\nchatBOT>>> By Air : INR ",int(round(TotalByAirExp)),"","[",int(round(TotalByAirExp*100/TotalTravelExp)),"% ]")
    #print("\nchatBOT>>> Others [ Railways + Roadways ] : INR ",int(round(Diff)),"","[",int(round(Diff*100/TotalTravelExp)),"% ]")
    #print("\nchatBOT>>> Average Monthly Expenditure : INR",int(round(MonthlyExpTotal)))
    #print("\nchatBOT>>> Average Monthly Expenditure  : INR",int(z))
    #print("\nchatBOT>>> Yearly Average Expenditure  : INR\n",df6)
    #print("\nchatBOT>>> Yearly Average Expenditure  : INR",test.loc["Month"])
    #month=df6.pivot_table(index=["Month"],values=["Withdrawal Amount (INR )"] )
    #year1=year.mean().round()
    #month1=month.mean().round()
    #print("\nchatBOT>>> Average Travel Expenditure / Year  : INR",int(year1))  

    #print("\nchatBOT>>> Average Travel Expenditure / Month : INR",int(month1))
    #print(d)
    #plt.plot(df6["Month"],df6["Travel"])
    df6.to_excel("/Users/orbaa5/Desktop/Dissertation/Thesis/Data/TrainingResult/Travel.xls")
    #print(df1)

    MonthlyExpTotal =int(MonthlyExpTotal)

    return MonthlyExpTotal

def Debit_FundTransfer():
    df7["FundTransfer"] = np.where(df7["Transaction Remarks"].str.contains(('^BIL/............/RBI-NEFT*')) | 
    df7["Transaction Remarks"].str.contains(('^BIL/............//\d')) |
    df7["Transaction Remarks"].str.contains(('^BIL/000492052323/COMMUNITY MATRIMONY./*')) |
    df7["Transaction Remarks"].str.contains(('^BIL/............/*.*/NSP')) |
    df7["Transaction Remarks"].str.contains(('^BIL/............/MIB-/*')) |
    df7["Transaction Remarks"].str.contains(('^BIL/............/BPC - BTill Desk/IBPS*')) |
    df7["Transaction Remarks"].str.contains(('^BIL/............/BILL JUNCTION PAYMEN/*')) |
    df7["Transaction Remarks"].str.contains(('^BIL/............/PGMIB-/........._WWW*')) |
    df7["Transaction Remarks"].str.contains(('^BIL/............/CITRUS PAYMENT SOLUT/*')) |
    df7["Transaction Remarks"].str.contains(('^BIL/............/eazypayICICIBANK/*')) |
    df7["Transaction Remarks"].str.contains(('^BIL/............/PGMIB-/...............')) |
    df7["Transaction Remarks"].str.contains(('^BIL/ONL/............/BILL DESK')) |
    df7["Transaction Remarks"].str.contains(('^BIL/............/PGMIB-/')) |
    df7["Transaction Remarks"].str.contains(('^IIN/ISA*')) |
    df7["Transaction Remarks"].str.contains(('^MMT/............/*')) |
    df7["Transaction Remarks"].str.contains(('^MMT/IMPS/............/')) |
    df7["Transaction Remarks"].str.contains(('^CAM/CASH DEPOSIT*')) |
    df7["Transaction Remarks"].str.contains(('^UPI/............/*')) |
    df7["Transaction Remarks"].str.contains(('^INF/............/........../............/2/0')) |
    df7["Transaction Remarks"].str.contains(('^VIN/IBPS*')) |
    df7["Transaction Remarks"].str.contains(('^VIN/ETS.ets*')) |    
    df7["Transaction Remarks"].str.contains(('^IIN/Birla Insti*')), 1,0)              
    
    df7.drop(df7.columns[[0,1,3]], axis = 1, inplace=True )
    
    for i in range(len(df7)):    
       if df7.loc[:,'FundTransfer'][i] == 0:
           df7.drop(index = [i], axis=0,inplace=True)     
    df7.reset_index(inplace=True)
    df7.drop(df7.columns[0],axis=1,inplace=True)    
    
    for i in range(len(df7)):    
       if df7.loc[:,'Withdrawal Amount (INR )'][i] == 0 and df7.loc[:,'Deposit Amount (INR )'][i] > 0 :
 #          if df7.bool(df7["Transaction Remarks"].str.contains(('^MMT/............/*'))) :
            df7.drop(index = [i], axis=0,inplace=True ) 
    df7.reset_index(inplace=True)
    df7.drop(df7.columns[0],axis=1,inplace=True)
    
    
    df7.drop(df7[df7["Transaction Remarks"].str.contains(('^VIN/MTNL*'))].index, axis=0, inplace=True)
    df7.drop(df7[df7["Transaction Remarks"].str.contains(('^BIL/............/PGMIB-/MTNL*'))].index, axis=0, inplace=True)
    df7.drop(df7[df7["Transaction Remarks"].str.contains(('^BIL/............/PGMIB-/AMAZON*'))].index, axis=0, inplace=True)
    df7.drop(df7[df7["Transaction Remarks"].str.contains(('^BIL/............/PGMIB-/BSES*'))].index, axis=0, inplace=True)
    df7.drop(df7[df7["Transaction Remarks"].str.contains(('^BIL/............/PGMIB-/EBAY*'))].index, axis=0, inplace=True)
    df7.drop(df7[df7["Transaction Remarks"].str.contains(('^BIL/............/CITRUS PAYMENT SOLUT/DELHIJAL*'))].index, axis=0, inplace=True)
    df7.drop(df7[df7["Transaction Remarks"].str.contains(('^BIL/............/PGMIB-/RSRTC*'))].index, axis=0, inplace=True)
    df7.drop(df7[df7["Transaction Remarks"].str.contains(('^BIL/............/PGMIB-/MP_FLIPKART*'))].index, axis=0, inplace=True)    
    df7.drop(df7[df7["Transaction Remarks"].str.contains(('^BIL/............/PGMIB-/DOCOMOPREP*'))].index, axis=0, inplace=True)
    df7.drop(df7[df7["Transaction Remarks"].str.contains(('^BIL/............/CITRUS PAYMENT SOLUT/AIRTEL*'))].index, axis=0, inplace=True)
    df7.drop(df7[df7["Transaction Remarks"].str.contains(('^BIL/............/PGMIB-/AIRTEL*'))].index, axis=0, inplace=True)
    df7.drop(df7[df7["Transaction Remarks"].str.contains(('^BIL/............/PGMIB-/RELIANCE*'))].index, axis=0, inplace=True)
    df7.drop(df7[df7["Transaction Remarks"].str.contains(('^BIL/............/PGMIB-/AIRT* '))].index, axis=0, inplace=True)

    #if (b == "Fundtransfer" or "FT" ) :
     #   print("\nResponse->>>>>>>>>>>>Hi Aman!!! You have performed :",df7["FundTransfer"].sum(),"Fund transfers online \n")
      #  c=input("Do you also want to see transactions graphically ( YES / NO ) " )

       # if(c=="YES"):
    #print("got it Here is the solution -------")
    df7["Transaction Date"] = pd.to_datetime(df7["Transaction Date"], format="%d/%m/%Y" )                   
    df7["Year"] = df7["Transaction Date"].apply(lambda x: (x.year))
    df7["Week"] = df7["Transaction Date"].apply(lambda x: (x.week))             
    df7["Day"]  = df7["Transaction Date"].apply(lambda x: (x.day))
    df7["MonthInDays"] = df7["Transaction Date"].apply(lambda x: (x.month))
    df7["Month"] = df7["MonthInDays"].apply(lambda x: calendar.month_abbr[x])
    df7.drop(df7.columns[[9]], axis = 1, inplace=True )

    df7.groupby(["Month","FundTransfer"]).size()
    
    
    d = df7.pivot_table(index="Month",values=["Withdrawal Amount (INR )"],aggfunc=np.sum)
    #print(d)
    #plt.plot(df7["Month"],df7["FundTransfer"])
    df7.to_excel("/Users/orbaa5/Desktop/Dissertation/Thesis/Data/TrainingResult/Debit_Fund_Transfer.xls")
            #print(df1)
    
    #for index, row in df7.iterrows():
     #   if row['FundTransfer'] == 0:
      #      df7.drop(index,inplace=True)    
    
    aq=df7["Withdrawal Amount (INR )"].sum()
    aq1=df7["Month"].count()
    
    
    #print("type of D",type(d))
    #print("aq",aq)
    #print("aq1",aq1)
    #print("average",aq/aq1)
    #print("round",int(aq/aq1))
    
    e=int(aq/aq1)
    d = str(d).split()    
    
    #command+4 = Comment
    
    #print(d)
    j=-1
    z=0
    #ct1=[]
    
    for i in range(len(d)):
        j+=1
        if d[i] =="Month":
            z=j
           # print(j)
    #print("z",z)
    #print("text",d[z])
    #print("j",j)
    
    #print(d)
    
    ct=[]    
    k=1
    z=0
    for i in d:
        w=2
        k+=1
        z=w*k
        i=z+2
        ct.append(d[i])
        if ( i==j ):
            break;
    
    #print("ct",ct)
    #print("type",type(ct))
    
    a=ct[0]
    b=ct[1]
    #print("first",a,b,type(a))
    
    #ct=int(float(ct))
    #print("ans",np.sum(ct))
    #ct=str(ct)

    
    #print("final",ct)
    #sum=0
    #for i in ct:
     #   c[i]=ct[i] + ct[i+1]
    
    #for i in ct:
     #   ct[i] = ct[i+1]
    
    #print("final\n",ct)    
    
    #ct=int(ct)
    #print("final",ct)
        
# =============================================================================
#     z=2*2, d[z+2]
#     z=2*3, d[z+2] k=8
#     z=2*4, d[z+2] k=10
#     z=2*5,d[z+2] k=12
#     z=2*6,k=14
#     z=2*7,k=16
#     z=2*8,k=18
#     
# =============================================================================
    
    
    
# =============================================================================
#     for i in range(len(d)):
#         if d[i]=="Month":
#                 #for k in range(len(d)):
#                     #i=4, i=i+1 
#                     j+6=> count
#                     #i=7, i+8=>count
#                     #i=9, i+10->count
#                     #i=11,i+12=>count
#                     #i=13,i+!4=>count
#                     #i=15,i+16=>count
# =============================================================================
                    
# =============================================================================
#             ct4=d[i+11]
#             ct1=d[i+13]
#             ct2=d[i+15]
#             ct3=d[i+17]
#             ct4=d[i+19]
#             ct1=d[i+21]
#             ct2=d[i+23]
#             ct3=d[i+25]
#             ct4=d[i+27]
# =============================================================================
       
    #ct1 = int(float(ct1))
    #ct2 = int(float(ct2))
    #ct3 = int(float(ct3))
    
    #aver1=int((ct1+ct2+ct3))/3
    #aver2 = int(aver1)
  
    return e


def ICICIATM_CashWithdrawl():
    df1["ICICI ATM Cash Withdrawl"] = np.where( df1["Transaction Remarks"].str.contains(('^ATM/CASH WDL*')), 1, 0 )
    df1.drop(df1.columns[[0,1,3]], axis = 1, inplace=True )   

    #print(df6.loc[:,"Travel"][0])
    #print(df6.loc[:,"Travel"][28])
    for i in range(len(df1)):    
        if df1.loc[:,'ICICI ATM Cash Withdrawl'][i] == 0:
            df1.drop(index = [i], axis=0,inplace=True) 
    df1.reset_index(inplace=True)
    df1.drop(df1.columns[0],axis=1,inplace=True)
    
    for i in range(len(df1)):    
       if df1.loc[:,'Withdrawal Amount (INR )'][i] == 0 and df1.loc[:,'Deposit Amount (INR )'][i] > 0 :
 #          if df7.bool(df7["Transaction Remarks"].str.contains(('^MMT/............/*'))) :
            df1.drop(index = [i], axis=0,inplace=True ) 
    df1.reset_index(inplace=True)
    df1.drop(df1.columns[0],axis=1,inplace=True)    

#At this ppoint----------
#df1 = 8 colms (0-tnxdate,tnxremark=1,withdl amt=2,depositAmt= 3,withdrl=4,savings(int.)=5,savings(neft=6,rmks=7 )  
    df1["Transaction Date"] = pd.to_datetime(df1["Transaction Date"], format="%d/%m/%Y" )
#At this point, df1 = 2 columns [Transaction Date = 0, Transaction remarks/ICICI ATM Cash Withdrwl = 1 ]       
            #df1["Year"] = df1["Transaction Date"].apply(lambda x: (x.day,x.week,x.year))
    df1["Year"] = df1["Transaction Date"].apply(lambda x: (x.year))
    df1["Week"] = df1["Transaction Date"].apply(lambda x: (x.week))
    df1["Day"] = df1["Transaction Date"].apply(lambda x: (x.day))
    df1["MonthInDays"] = df1["Transaction Date"].apply(lambda x: (x.month))
    df1["Month"] = df1["MonthInDays"].apply(lambda x: calendar.month_abbr[x])
            #df1.drop(df1.columns[[9]], axis = 1, inplace=True )
#At this point-----
#df1 = 7 colms [Tnx date=0,Tnx Cash wthd=1,year=2,week=3,day=4,monthInNumb(1,2etc)=5,Month(Jan,feb etc)=6 ]             
            #print(df1)
            #df1["month"] = df1["Transaction Date"].apply(lambda x: (x.month, dt.month_name()))
            #print(df1)

    aq=df1["Withdrawal Amount (INR )"].sum()
    aq1=df1["Month"].count()
    
    #print("aq",aq)
    #print("aq1",aq1)
    
    ag=aq/aq1
#-------------------------------
    now1 = datetime.datetime.now()
            #print(now)
            #now=now.date()
    now=str(now1.date())
            #now=now.strftime('%d-%b-%Y')
#-----------------------------------------------------------
            #b=df14["Month"].max()
    d = datetime.datetime.strptime(now, "%Y-%m-%d")
    #print(d.month)
            #print(d)
    #print("user entered month",b)
    d2 = d - dateutil.relativedelta.relativedelta(months=2)
            #d2=d2.strftime('%d-%b-%Y')
            
    #print(d2)
    d2=str(d2.date())
    d3=datetime.datetime.strptime(d2, "%Y-%m-%d")
    #print("difference month:",d3.month)
    
    
    #print("difference year:",d3.year)
    userm=d3.month
    usery=d3.year
    total=0
    count=0
        
    for i in range(len(df1)):


            
        if df1.loc[:,'MonthInDays'][i] == userm and df1.loc[:,'Year'][i] == usery :
            total+= df1.loc[:,'Withdrawal Amount (INR )'][i]
            #mth=df14.loc[:,'Month'][i]
            count=count+1
            #print(int(round(total)))
            #print(count)
            #print("df date",a)    
    for i in range(len(df1)):
        c=0
        if df1.loc[:,'MonthInDays'][i] == userm and df1.loc[:,'Year'][i] == usery :
            #mth1=df1.loc[:,'Month'][i] 
            c=c+1
            #print("\na) Total AMT transaction performed is ",mth1,",",usery,"is",count)
            #print("\nb) Amount withdrawn during",mth1,",",usery,"is INR ",int(round(total)))
            break
            #count1=count1+1
            #i12=z12+1
            
            
            #df1.groupby(["Month","ICICI ATM Cash Withdrawl"]).size()
            #d = df1.pivot_table(index="Month",columns="ICICI ATM Cash Withdrawl",aggfunc=sum)
            #print(d)
            #plt.plot(df1["Month"],df1["ICICI ATM Cash Withdrawl"])
            #df1.to_excel("/Users/orbaa5/Desktop/Dissertation/Thesis/Data/TrainingResult/ATM_CashWithdrawl.xls")
    if count<=5:
        #print("\nANUJ Digital Virtual Assistant>>> No. You have not exceeded monthyl ATM limit in",mth1,"",usery,"\n")
        #print("ANUJ Digital Virtual Assistant>>>Is this answered your query ?")
        #input("Customer>>>")
        #if (z100 or z101 or z102 or z103):
        #print("\n\n\n\n\nANUJ Digital Virtual Assistant>>>==========Fine, Here are the details=========== ")
        limit=5
        charges=20
        z=limit-count
    
        #print("\na) During",mth1,",",usery,"Your ICICI AMT transactions count =",count,",Total Amount withdrawn [INR",int(round(total)),"]")
        #print("\na) This is less than limit of",limit,"hence you could have easily performed",z,"more transactions")
    #print("\nb) Amount withdrawn INR",int(round(total)))
        #print("\nNOTE: After exceeding limit, bank will charge INR",charges,"per transaction")
#print(count)
    
    ag=int(ag)
    
    return ag


def NonICICIATM_CashWithdrawl():
    df8["NonICICI Cash Withdrawl"] = np.where( df8["Transaction Remarks"].str.contains(('^NFS/CASH WDL*')) |
    df8["Transaction Remarks"].str.contains(('^VAT/CASH WDL*')), 1,0)
    
    df8.drop(df8.columns[[0,1,3]], axis = 1, inplace=True )
    
    #print(df6.loc[:,"Travel"][0])
    #print(df6.loc[:,"Travel"][28])    
    for i in range(len(df8)):    
        if df8.loc[:,'NonICICI Cash Withdrawl'][i] == 0:
            df8.drop(index = [i], axis=0,inplace=True) 
    df8.reset_index(inplace=True)
    df8.drop(df8.columns[0],axis=1,inplace=True) 

    for i in range(len(df8)):    
       if df8.loc[:,'Withdrawal Amount (INR )'][i] == 0 and df8.loc[:,'Deposit Amount (INR )'][i] > 0 :
 #          if df7.bool(df7["Transaction Remarks"].str.contains(('^MMT/............/*'))) :
            df8.drop(index = [i], axis=0,inplace=True ) 
    df8.reset_index(inplace=True)
    df8.drop(df8.columns[0],axis=1,inplace=True)
   
    # (b == "Non ICICI" or "nonicici" or "othericici" or "other ATM") :
     #   print("\nResponse->>>>>>>>>>>>Hi Aman!!! You have performed :",df8["NonICICI Cash Withdrawl"].sum(),"Transactions from Non ICICI ATM's \n")
      #  c=input("Do you also want to see transactions graphically ( YES / NO ) " )

       # if(c=="YES"):
    #print("got it Here is the solution -------")
    df8["Transaction Date"] = pd.to_datetime(df8["Transaction Date"], format="%d/%m/%Y" )                   
    df8["Year"] = df8["Transaction Date"].apply(lambda x: (x.year))
    df8["Week"] = df8["Transaction Date"].apply(lambda x: (x.week))             
    df8["Day"]  = df8["Transaction Date"].apply(lambda x: (x.day))
    df8["MonthInDays"] = df8["Transaction Date"].apply(lambda x: (x.month))
    df8["Month"] = df8["MonthInDays"].apply(lambda x: calendar.month_abbr[x])
    df8.drop(df8.columns[[9]], axis = 1, inplace=True )

    #df8.groupby(["Month","NonICICI Cash Withdrawl"]).size()
    d = df8.pivot_table(index="Month",columns="NonICICI Cash Withdrawl" )
    #print(d)
    #plt.plot(df8["Month"],df8["NonICICI Cash Withdrawl"])
    df8.to_excel("/Users/orbaa5/Desktop/Dissertation/Thesis/Data/TrainingResult/NonICICI_ATM.xls")
    #print(df1)
    
    aq=df8["Withdrawal Amount (INR )"].sum()
    aq1=df8["Month"].count()
    
    q=aq/aq1
    q=int(q)
    
    #print(aq)
    #print(aq1)
    
    return q

def Recharge():
    df9["Recharge"] = np.where( df9["Transaction Remarks"].str.contains(('^BIL/............/BPC - Bill Desk/RELIANCECOMM*')) |
    df9["Transaction Remarks"].str.contains(('^BIL/............/*.*/BOOKMYSHOW*')) |            
    df9["Transaction Remarks"].str.contains(('^BIL/............/OXIGENPMR*')) |            
    df9["Transaction Remarks"].str.contains(('^BIL/............/C.C. AVENUES/INFIBEAM.COM*')) |            
    df9["Transaction Remarks"].str.contains(('^BIL/............/PGMIB-/RELIANCECOMM*')) |            
    df9["Transaction Remarks"].str.contains(('^BIL/............/BPC - Bill Desk/TATADOCOMO*')) |            
    df9["Transaction Remarks"].str.contains(('^BIL/............/PGMIB-/IDEACELLULAR*')) |            
    df9["Transaction Remarks"].str.contains(('^BIL/............/PGMIB-/DOCOMOPREP*')) |  
    df9["Transaction Remarks"].str.contains(('^BIL/............/CITRUS PAYMENT SOLUT/AIRTELPREP*')) | 
    df9["Transaction Remarks"].str.contains(('^BIL/............/PGMIB-/AIRTELPREP*')) | 
    df9["Transaction Remarks"].str.contains(('^IIN/Paytm.com*')) |
    df9["Transaction Remarks"].str.contains(('^IIN/I-Debit/Tata Doco/*')) |    
    df9["Transaction Remarks"].str.contains(('^IIN/PayTm Mobil/*')) |    
    df9["Transaction Remarks"].str.contains(('^BIL/............//HTTPS://PAY.AIR*')) | 
    df9["Transaction Remarks"].str.contains(('^TOP/ATM TOPUP/*')) | 
    df9["Transaction Remarks"].str.contains(('^BIL/............/PGMIB-/HTTPS://PAY.AIR*')) |           
    df9["Transaction Remarks"].str.contains(('^BIL/............/PGMIB-/AIRT*')) |            
    df9["Transaction Remarks"].str.contains(('^BIL/............//AIRT*')) |
    df9["Transaction Remarks"].str.contains(('^BIL/............/PGMIB-/RELIANCEJIO*')) |
    df9["Transaction Remarks"].str.contains(('^BIL/............/BPC - Bill Desk/DOCOMOPREP*')) |
    df9["Transaction Remarks"].str.contains(('^BIL/............/CITRUS PAYMENT SOLUT/AIRTE*')) |
    df9["Transaction Remarks"].str.contains(('^BIL/............//HTTP://WWW.AIRT*')) |
    df9["Transaction Remarks"].str.contains(('^BIL/............//HTTP://WWW.AIRT*')) |
    df9["Transaction Remarks"].str.contains(('^BIL/............/..../..........')), 1,0)
    
#--------------------------------------------------------------------------------------------------    
    df9.drop(df9.columns[[0,1,3]], axis = 1, inplace=True )
    
    #print(df6.loc[:,"Travel"][0])
    #print(df6.loc[:,"Travel"][28])    
    for i in range(len(df9)):    
        if df9.loc[:,'Recharge'][i] == 0:
            df9.drop(index = [i], axis=0,inplace=True) 
    df9.reset_index(inplace=True)
    df9.drop(df9.columns[0],axis=1,inplace=True) 

    for i in range(len(df9)):    
       if df9.loc[:,'Withdrawal Amount (INR )'][i] == 0 and df9.loc[:,'Deposit Amount (INR )'][i] > 0 :
 #          if df7.bool(df7["Transaction Remarks"].str.contains(('^MMT/............/*'))) :
            df9.drop(index = [i], axis=0,inplace=True ) 
    df9.reset_index(inplace=True)
    df9.drop(df9.columns[0],axis=1,inplace=True)

    df9.drop(df9[df9["Transaction Remarks"].str.contains(('^BIL/............/MIB-/*'))].index, axis=0, inplace=True)
#------------------------------------------------------------------------------------------------------   
    #if (b == "recharge" or "Recharge" or "RECHARGE" ) :
    df9["Transaction Date"] = pd.to_datetime(df9["Transaction Date"], format="%d/%m/%Y" )                   
    df9["Year"] = df9["Transaction Date"].apply(lambda x: (x.year))
    df9["Week"] = df9["Transaction Date"].apply(lambda x: (x.week))             
    df9["Day"]  = df9["Transaction Date"].apply(lambda x: (x.day))
    df9["MonthInDays"] = df9["Transaction Date"].apply(lambda x: (x.month))
    df9["Month"] = df9["MonthInDays"].apply(lambda x: calendar.month_abbr[x])
    #df9.drop(df9.columns[[9]], axis = 1, inplace=True )
    TotalRechargeExp=df9["Withdrawal Amount (INR )"].sum()

    df9.drop(df9.columns[[0,1,3,4,5,7,8,9]], axis = 1, inplace=True )
    test=df9.pivot_table(index=["Year"],columns=["Month"])
    test = test.unstack()
    #NoOfMonthsTotal=test.nunique()
    df9.rename(columns={'Withdrawal Amount (INR )': 'Recharge Amount'},inplace=True)
    #print(test)
    #print("\nchatBOT>>> Following recharge done\n",df9.pivot_table(index=["Year"],values=["Recharge Amount"],aggfunc=sum))
    #print("\n")
    decide=df9.pivot_table(index=["Year"],values=["Recharge Amount"],aggfunc=sum)
    #print(len(decide))
    decide.reset_index(drop=True, inplace=True)
    
    for i in range(len(decide)-1,0,-1): 
        total=0
        
        if decide.loc[:,'Recharge Amount'][i] < decide.loc[:,'Recharge Amount'][i-1] :

            total=total+decide.loc[:,'Recharge Amount'][i]
            reduced=decide.loc[:,'Recharge Amount'][i-1]-decide.loc[:,'Recharge Amount'][i]
            no=decide.loc[:,'Recharge Amount'][i-1]
            #print(decide.loc[:,'Year'][i])
            #print("Recharge of INR",total,"[",int(round(reduced*100 / no)),"% Savings]" )
            #print(total)
        elif decide.loc[:,'Recharge Amount'][i] > decide.loc[:,'Recharge Amount'][i-1] :
            total=total+decide.loc[:,'Recharge Amount'][i]
            #print("Recharge of INR",total )
            break
    NoOfMonthsTotal=test.count()
    #print(NoOfMonthsTotal)
    #print(NoOfMonthsTotal.sum())
    MonthlyExpTotal=TotalRechargeExp / NoOfMonthsTotal.sum()            
    #print("\nchatBOT>>> Total Recharge : INR",int(round(TotalRechargeExp)))
    #print("\nchatBOT>>> Average Monthly Recharge : INR",int(round(MonthlyExpTotal)))
    #print(NoOfMonthsTotal)
    #df9.groupby(["Month","Recharge"]).size()
    #d = df9.pivot_table(index="Month",columns="Recharge",aggfunc=sum)
    #print(d)
    #plt.plot(df9["Month"],df9["Withdrawal Amount (INR )"])
    df9.to_excel("/Users/orbaa5/Desktop/Dissertation/Thesis/Data/TrainingResult/Recharge.xls")
    #print(df1)

    MonthlyExpTotal=int(MonthlyExpTotal)    
    
    return MonthlyExpTotal

def Loan_EMI():
    
    #print ( "\nANUJ Digital Virtual Assistant>>> Hello Anuj, You have paid emi of Rs 4,96,224 up-to Sept 2018\n\n\n\n\n\n\n\n\n\n\n\n\n\n" )
    df10["LoanEMI"] = np.where( df10["Transaction Remarks"].str.contains(('^LBKNL*')), 1,0)
    
    df10.drop(df10.columns[[0,1,3]], axis = 1, inplace=True )
    
    #print(df6.loc[:,"Travel"][0])
    #print(df6.loc[:,"Travel"][28])    
    for i in range(len(df10)):    
        if df10.loc[:,'LoanEMI'][i] == 0:
            df10.drop(index = [i], axis=0,inplace=True) 
    df10.reset_index(inplace=True)
    df10.drop(df10.columns[0],axis=1,inplace=True) 

    for i in range(len(df10)):    
       if df10.loc[:,'Withdrawal Amount (INR )'][i] == 0 and df10.loc[:,'Deposit Amount (INR )'][i] > 0 :
 #          if df7.bool(df7["Transaction Remarks"].str.contains(('^MMT/............/*'))) :
            df10.drop(index = [i], axis=0,inplace=True ) 
    df10.reset_index(inplace=True)
    df10.drop(df10.columns[0],axis=1,inplace=True)
   
    #if (b == "repayment" or b=="capacity" or b=="loan" or b=="show me EMI status of Malik" or b=="repayment" or b=="emi") :
        
                
    df10["Transaction Date"] = pd.to_datetime(df10["Transaction Date"], format="%d/%m/%Y" )                   
    df10["Year"] = df10["Transaction Date"].apply(lambda x: (x.year))
    df10["Week"] = df10["Transaction Date"].apply(lambda x: (x.week))             
    df10["Day"]  = df10["Transaction Date"].apply(lambda x: (x.day))
    df10["MonthInDays"] = df10["Transaction Date"].apply(lambda x: (x.month))
    df10["Month"] = df10["MonthInDays"].apply(lambda x: calendar.month_abbr[x])
    #df10.drop(df10.columns[[9]], axis = 1, inplace=True )

#------------------------------------------------------------------------
    a=df10["Transaction Date"].max()
    #a = pd.to_datetime([df10["Transaction Date"].max()])
    #new = datetime.strptime(a, '%Y-%b-%d 00:00:00')
    #ab=datetime.datetime.strptime(a, '%Y-%m-%d').date()
    #print(a.date())
    z=a.date()
    z=z.strftime('%d-%b-%Y')
    #print(a.date())
    #print(new.strftime('%d-%m-%Y'))
    #df10.assign(Date=df.Date.dt.round('H'))
    #a2=df10["Month"].max()
    #bal=df10[df10["Transaction Date"]==a]["Month"]
    #bal1=df10[df10["Transaction Date"]==a]["Year"]
    #print(a.assign(Date=a.Date.dt.round('H')))
    #print(a)H
    #bal2=int(round(df10[df10["Transaction Date"]==a]["Withdrawal Amount (INR )"]))
    #print("\nchatBOT>>>Last EMI paid in",bal,",",bal1,"of amount INR",bal2)
    #print("\nchatBOT>>>Latest EMI month is: INR",a2)
    
    TotalRechargeExp=df10["Withdrawal Amount (INR )"].sum()
    TotalRechargeExp1=df10["Withdrawal Amount (INR )"].count()

    df10.drop(df10.columns[[0,1,3,4,5,7,8,9]], axis = 1, inplace=True )
    test=df10.pivot_table(index=["Year"],columns=["Month"])
    test = test.unstack()
    #NoOfMonthsTotal=test.nunique()
    df10.rename(columns={'Withdrawal Amount (INR )': 'EMI Amount'},inplace=True)
    
    #print(test)
    #print("\n")
    decide=df10.pivot_table(index=["Year"],values=["EMI Amount"],aggfunc=sum)
    #print(len(decide))
    decide.reset_index(drop=True, inplace=True)
    NoOfMonthsTotal=test.count()
    #print(NoOfMonthsTotal)
    #print(NoOfMonthsTotal.sum())
    MonthlyExpTotal=TotalRechargeExp / NoOfMonthsTotal.sum()          
    #print("\na) Last EMI paid on ",z)
    #print("\nb)",int(round(TotalRechargeExp1)),"EMI's Paid with Total Amount INR", int(round(TotalRechargeExp)))
    #Penalty=0.05
    #ChequeBounceCharges=0.25
    #InterestCharges=.08
    #PenaltyCharges=Penalty + ChequeBounceCharges + InterestCharges
    #Principal = 0.75
    #Interest = 
    #Charges = 
    #print("\nchatBOT>>> Total EMI Paid : INR",int(round(TotalRechargeExp)))
    TotalEMI = 31
    monthlyEMI = MonthlyExpTotal
    yearEMI= MonthlyExpTotal*12
    y2016 =  MonthlyExpTotal*12
    y2017 =  MonthlyExpTotal*12
    y2018 =  MonthlyExpTotal*7
    
    #yp2016 = 
    
    yyy=0
    #print("\na) Total Loan Amount = Rs 70,00,000")
    #print("b) Monthly EMI         = Rs",int(round(MonthlyExpTotal))) 
    #print("c) Yearly EMI          = Rs",int(round(MonthlyExpTotal*12))) 
    #print("\nc) Yearly EMI Customer is obliged to honor: INR",int(round(MonthlyExpTotal*12))) 
    #print("\n=========Summary of EMI Paid by Mr. XYZ ==========\n\n",df10.pivot_table(index=[],columns=["Year"],values=["EMI Amount"],aggfunc=sum))

    #print("\n=========Summary End==========")
    
    q=int(round(MonthlyExpTotal))
    
    for i in range(len(decide)): 
        total=0
        
        if decide.loc[:,'EMI Amount'][i] < yearEMI :
            total=total+decide.loc[:,'EMI Amount'][i]
            yyy+=1
            #reduced=decide.loc[:,'EMI Amount'][i]-yearEMI
            #no=decide.loc[:,'EMI Amount'][i-1]
            #print(decide.loc[:,'Year'][i])
            #print("\nFor EMI INR",int(round(total)),",Amount still unpaid is [ INR",yearEMI-total,"]" )
            #print(total)
        #elif decide.loc[:,'EMI Amount'][i] >= decide.loc[:,'EMI Amount'][i-1] or decide.loc[:,'EMI Amount'][i] < decide.loc[:,'EMI Amount'][i-1]:
            #total=total+decide.loc[:,'Salary Amount'][i]
         #   total=total+decide.loc[:,'EMI Amount'][i]
            #yyy=total
          #  reduced=decide.loc[:,'EMI Amount'][i]-decide.loc[:,'EMI Amount'][i-1]
           # no=decide.loc[:,'EMI Amount'][i-1]
            #print(decide.loc[:,'Year'][i])
            #print("EMI of INR",total,"[",int(round(reduced*100 / no)),"% Change]",yearEMI-total )
            #break
    #print("\n===========Customer has defaulted",yyy,"times=================")           
                
    for i in range(len(decide)): 
        total=0
        
        if decide.loc[:,'EMI Amount'][i] < yearEMI :
            total=total+decide.loc[:,'EMI Amount'][i]
            #yyy+=1
            #reduced=decide.loc[:,'EMI Amount'][i]-yearEMI
            #no=decide.loc[:,'EMI Amount'][i-1]
            #print(decide.loc[:,'Year'][i])
     #       print("\nTotal EMI=INR",int(round(MonthlyExpTotal*12)),"EMI received =INR",int(round(total)),",EMI Defaulted = INR",int(round(yearEMI-total)),"/per year[",int(round((yearEMI-total)*100/yearEMI)),"%]\n" )
            #print(total)
        #elif decide.loc[:,'EMI Amount'][i] >= decide.loc[:,'EMI Amount'][i-1] or decide.loc[:,'EMI Amount'][i] < decide.loc[:,'EMI Amount'][i-1]:

    
#-----------------------------------------------------            

    #df10.groupby(["Month","LoanEMI"]).size()
    #d = df10.pivot_table(index="Month",columns="LoanEMI",aggfunc=sum)
    #print(d)
    #plt.plot(df10["Month"],df10["LoanEMI"])
    df10.to_excel("/Users/orbaa5/Desktop/Dissertation/Thesis/Data/TrainingResult/LoanEMI.xls")
    #print(df1)

    return q


def Salary():
    df11["Salary"] = np.where( df11["Transaction Remarks"].str.contains(('^INF/............/SAL FOR*')) |
    df11["Transaction Remarks"].str.contains(('^INF/............/SALARY FOR*')) |
    df11["Transaction Remarks"].str.contains(('^......-SALARY ADVANCE')) |
    df11["Transaction Remarks"].str.contains(('^Salary arrears*')) |
    df11["Transaction Remarks"].str.contains(('^SALARY FOR*')),1, 0)
                   
    df11.drop(df11.columns[[0,1,3]], axis = 1, inplace=True )
    
    #print(df6.loc[:,"Travel"][0])
    #print(df6.loc[:,"Travel"][28])    
    for i in range(len(df11)):    
        if df11.loc[:,'Salary'][i] == 0:
            df11.drop(index = [i], axis=0,inplace=True) 
    df11.reset_index(inplace=True)
    df11.drop(df11.columns[0],axis=1,inplace=True) 

    for i in range(len(df11)):    
       if df11.loc[:,'Withdrawal Amount (INR )'][i] > 0 and df11.loc[:,'Deposit Amount (INR )'][i] == 0 :
 #          if df7.bool(df7["Transaction Remarks"].str.contains(('^MMT/............/*'))) :
            df11.drop(index = [i], axis=0,inplace=True ) 
    df11.reset_index(inplace=True)
    df11.drop(df11.columns[0],axis=1,inplace=True)
   
    #if (b == "Salary" or "SALARY" or "salary") :
    df11["Transaction Date"] = pd.to_datetime(df11["Transaction Date"], format="%d/%m/%Y" )                   
    df11["Year"] = df11["Transaction Date"].apply(lambda x: (x.year))
    df11["Week"] = df11["Transaction Date"].apply(lambda x: (x.week))             
    df11["Day"]  = df11["Transaction Date"].apply(lambda x: (x.day))
    df11["MonthInDays"] = df11["Transaction Date"].apply(lambda x: (x.month))
    df11["Month"] = df11["MonthInDays"].apply(lambda x: calendar.month_abbr[x])
    df11.drop(df11.columns[[9]], axis = 1, inplace=True )

#-------------------------------------------------------------
    TotalRechargeExp=df11["Deposit Amount (INR )"].sum()

    df11.drop(df11.columns[[0,1,2,4,5,7,8]], axis = 1, inplace=True )
    test=df11.pivot_table(index=["Year"],columns=["Month"])
    test = test.unstack()
    #NoOfMonthsTotal=test.nunique()
    df11.rename(columns={'Deposit Amount (INR )': 'Salary Amount'},inplace=True)
    
    #print(test)
    #print("\nchatBOT>>>========Salary Summary========= \n",df11.pivot_table(index=["Year"],values=["Salary Amount"],aggfunc=sum))
    decide=df11.pivot_table(index=["Year"],values=["Salary Amount"],aggfunc=sum)
    #print(len(decide))
    decide.reset_index(drop=True, inplace=True)
    #print("\n=============Salary Change over Past Years========\n")
    for i in range(len(decide)-1,0,-1): 
        total=0
        
        if decide.loc[:,'Salary Amount'][i] < decide.loc[:,'Salary Amount'][i-1] :
            total=total+decide.loc[:,'Salary Amount'][i]
            reduced=decide.loc[:,'Salary Amount'][i]-decide.loc[:,'Salary Amount'][i-1]
            no=decide.loc[:,'Salary Amount'][i-1]
            #print(decide.loc[:,'Year'][i])
            #print("Salary of INR",total,"[",int(round(reduced*100 / no)),"% Change]" )
            #print(total)
        elif decide.loc[:,'Salary Amount'][i] > decide.loc[:,'Salary Amount'][i-1] :
            #total=total+decide.loc[:,'Salary Amount'][i]
            total=total+decide.loc[:,'Salary Amount'][i]
            reduced=decide.loc[:,'Salary Amount'][i]-decide.loc[:,'Salary Amount'][i-1]
            no=decide.loc[:,'Salary Amount'][i-1]
            #print(decide.loc[:,'Year'][i])
            #print("Salary of INR",total,"[",int(round(reduced*100 / no)),"% Change]" )
            #break
    NoOfMonthsTotal=test.count()
    #print(NoOfMonthsTotal)
    #print(NoOfMonthsTotal.sum())
    MonthlyExpTotal=TotalRechargeExp / NoOfMonthsTotal.sum()            
    #print("\nchatBOT>>> Total Salary Amount : INR",int(round(TotalRechargeExp)))
    #print("\nchatBOT>>> Average Monthly Salary : INR",int(round(MonthlyExpTotal)))            
    
#------------------------------------------------------------------            
    #df11.groupby(["Month","Salary"]).size()
    #d = df11.pivot_table(index="Month",aggfunc=sum)
    #print(d)
    #plt.plot(df11["Month"],df11["Salary"])
    df11.to_excel("/Users/orbaa5/Desktop/Dissertation/Thesis/Data/TrainingResult/Salary.xls")
    #print(df1)

    MonthlyExpTotal=int(round(MonthlyExpTotal))

    return MonthlyExpTotal

def Interest():
    df12["Interest"] = np.where( df12["Transaction Remarks"].str.contains(('^029801508002:Int.Pd:*')),1, 0)
                            
    df12.drop(df12.columns[[0,1,3]], axis = 1, inplace=True )
    
    #print(df6.loc[:,"Travel"][0])
    #print(df6.loc[:,"Travel"][28])    
    for i in range(len(df12)):    
        if df12.loc[:,'Interest'][i] == 0:
            df12.drop(index = [i], axis=0,inplace=True) 
    df12.reset_index(inplace=True)
    df12.drop(df12.columns[0],axis=1,inplace=True) 

    for i in range(len(df12)):    
       if df12.loc[:,'Withdrawal Amount (INR )'][i] > 0 and df12.loc[:,'Deposit Amount (INR )'][i] == 0 :
 #          if df7.bool(df7["Transaction Remarks"].str.contains(('^MMT/............/*'))) :
            df12.drop(index = [i], axis=0,inplace=True ) 
    df12.reset_index(inplace=True)
    df12.drop(df12.columns[0],axis=1,inplace=True)
   
    #if (b == "Interest" or "INTEREST" or "interest") :
    df12["Transaction Date"] = pd.to_datetime(df12["Transaction Date"], format="%d/%m/%Y" )                   
    df12["Year"] = df12["Transaction Date"].apply(lambda x: (x.year))
    df12["Week"] = df12["Transaction Date"].apply(lambda x: (x.week))             
    df12["Day"]  = df12["Transaction Date"].apply(lambda x: (x.day))
    df12["MonthInDays"] = df12["Transaction Date"].apply(lambda x: (x.month))
    df12["Month"] = df12["MonthInDays"].apply(lambda x: calendar.month_abbr[x])
    df12.drop(df12.columns[[9]], axis = 1, inplace=True )
    
#-------------------------------------------------------------
    TotalRechargeExp=df12["Deposit Amount (INR )"].sum()

    df12.drop(df12.columns[[0,1,2,4,5,7,8]], axis = 1, inplace=True )
    test=df12.pivot_table(index=["Year"],columns=["Month"])
    test = test.unstack()
    #NoOfMonthsTotal=test.nunique()
    df12.rename(columns={'Deposit Amount (INR )': 'Interest Amount'},inplace=True)
    
    #print(test)
    #print("\nchatBOT>>> Following Salary credited \n",df12.pivot_table(index=["Year"],values=["Interest Amount"],aggfunc=sum))
    #print("\n")
    decide=df12.pivot_table(index=["Year"],values=["Interest Amount"],aggfunc=sum)
    #print(len(decide))
    decide.reset_index(drop=True, inplace=True)
    
    for i in range(len(decide)-1,0,-1): 
        total=0
        
        if decide.loc[:,'Interest Amount'][i] < decide.loc[:,'Interest Amount'][i-1] :
            total=total+decide.loc[:,'Interest Amount'][i]
            reduced=decide.loc[:,'Interest Amount'][i]-decide.loc[:,'Interest Amount'][i-1]
            no=decide.loc[:,'Interest Amount'][i-1]
            #print(decide.loc[:,'Year'][i])
            #print("Interest of INR",total,"[",int(round(reduced*100 / no)),"% Change]" )
            #print(total)
        elif decide.loc[:,'Interest Amount'][i] > decide.loc[:,'Interest Amount'][i-1] :
            #total=total+decide.loc[:,'Salary Amount'][i]
            total=total+decide.loc[:,'Interest Amount'][i]
            reduced=decide.loc[:,'Interest Amount'][i]-decide.loc[:,'Interest Amount'][i-1]
            no=decide.loc[:,'Interest Amount'][i-1]
            #print(decide.loc[:,'Year'][i])
            #print("Interest of INR",total,"[",int(round(reduced*100 / no)),"% Change]" )
            #break
    NoOfMonthsTotal=test.count()
    #print(NoOfMonthsTotal)
    #print(NoOfMonthsTotal.sum())
    MonthlyExpTotal=TotalRechargeExp / NoOfMonthsTotal.sum()            
    #print("\nchatBOT>>> Total Interest Amount : INR",int(round(TotalRechargeExp)))
    #print("\nchatBOT>>> Average Monthly Interest : INR",int(round(MonthlyExpTotal)))            
    
#-----------------------------------------
    #df12.groupby(["Month","Interest"]).size()
    #d = df12.pivot_table(index="Month",columns="Interest",aggfunc=sum)
    #print(d)
    #plt.plot(df12["Month"],df12["Interest"])
    #df12.to_excel("/Users/orbaa5/Desktop/Dissertation/Thesis/Data/TrainingResult/Interest.xls")
    #print(df1)
    
    MonthlyExpTotal= int(round(MonthlyExpTotal))
    
    return MonthlyExpTotal

def Auto_Reversal():
    df13["reversal"] = np.where( df13["Transaction Remarks"].str.contains(('^ACH/BHIM REWARD/*')) |
    df13["Transaction Remarks"].str.contains(('^ATM/WDL RVSL/*')) |
    df13["Transaction Remarks"].str.contains(('^ATM/XFR CR/*')) |
    df13["Transaction Remarks"].str.contains(('^BIL/............/*.*/NSP')) |
    df13["Transaction Remarks"].str.contains(('^BIL/AUTORECON TID.*')) |
    df13["Transaction Remarks"].str.contains(('^BIL/REVERSAL*')) |
    df13["Transaction Remarks"].str.contains(('^CAM/CASH DEPOSIT*')) |
    df13["Transaction Remarks"].str.contains(('^IIN/www.irctc.c/............../2')) |
    df13["Transaction Remarks"].str.contains(('^IIN/RFND/I-Debit/*')) |
    df13["Transaction Remarks"].str.contains(('^IPS/PAYMNT RVSL/*')) |
    df13["Transaction Remarks"].str.contains(('^TOP/ATM TOPUP REV/*')) |
    df13["Transaction Remarks"].str.contains(('^MMT/............/*')) |
    df13["Transaction Remarks"].str.contains(('^NFS/WDL RVSL/*')) |
    df13["Transaction Remarks"].str.contains(('^UPI/............/*')) |
    df13["Transaction Remarks"].str.contains(('^Reversal ForTrxID*')) |
    df13["Transaction Remarks"].str.contains(('^VPS/PAYMNT RVSL/*')),1, 0)  
       
    df13.drop(df13.columns[[0,1,3]], axis = 1, inplace=True )
    
    #print(df6.loc[:,"Travel"][0])
    #print(df6.loc[:,"Travel"][28])    
    for i in range(len(df13)):    
        if df13.loc[:,'reversal'][i] == 0:
            df13.drop(index = [i], axis=0,inplace=True) 
    df13.reset_index(inplace=True)
    df13.drop(df13.columns[0],axis=1,inplace=True) 

    for i in range(len(df13)):    
       if df13.loc[:,'Withdrawal Amount (INR )'][i] > 0 and df13.loc[:,'Deposit Amount (INR )'][i] == 0 :
 #          if df7.bool(df7["Transaction Remarks"].str.contains(('^MMT/............/*'))) :
            df13.drop(index = [i], axis=0,inplace=True ) 
    df13.reset_index(inplace=True)
    df13.drop(df13.columns[0],axis=1,inplace=True)
   
    #if (b == "reversal" or "Autoreversal" or "AUTOREVERSAL" or "autoreversal" or "auto reversal" or "rev" or "auto" or "AUTO") :
    #print("\nResponse->>>>>>>>>>>>Hi Aman!!! : Your have received amount in your account ",df13["reversal"].sum()," times for incomplete withdrawls ( i.e N/w failure, Timed out,etc )  \n")
    #c=input("Do you also want to see transactions graphically ( YES / NO ) " )

#        if(c=="YES"):
    #print("got it Here is the solution -------")
    df13["Transaction Date"] = pd.to_datetime(df13["Transaction Date"], format="%d/%m/%Y" )                   
    df13["Year"] = df13["Transaction Date"].apply(lambda x: (x.year))
    df13["Week"] = df13["Transaction Date"].apply(lambda x: (x.week))             
    df13["Day"]  = df13["Transaction Date"].apply(lambda x: (x.day))
    df13["MonthInDays"] = df13["Transaction Date"].apply(lambda x: (x.month))
    df13["Month"] = df13["MonthInDays"].apply(lambda x: calendar.month_abbr[x])
    df13.drop(df13.columns[[9]], axis = 1, inplace=True )

    df13.groupby(["Month","reversal"]).size()
    d = df13.pivot_table(index="Month",columns="reversal",aggfunc=sum)
    #print(d)
    #plt.plot(df13["Month"],df13["reversal"])
    df13.to_excel("/Users/orbaa5/Desktop/Dissertation/Thesis/Data/TrainingResult/Auto_Reversal.xls")
    #print(df1)
    
    aq=df13["Deposit Amount (INR )"].sum()
    aq1=df13["Month"].count()
    
    q=aq/aq1
    q=int(q)
    
    return q

                
def Credit_FundTransfer():
    df14["FundTransfer"] = np.where( df14["Transaction Remarks"].str.contains(('^NEFT*')),1, 0)
                            
    df14.drop(df11.columns[[0,1,3]], axis = 1, inplace=True )
    
    #print(df6.loc[:,"Travel"][0])
    #print(df6.loc[:,"Travel"][28])    
    for i in range(len(df14)):    
        if df14.loc[:,'FundTransfer'][i] == 0:
            df14.drop(index = [i], axis=0,inplace=True) 
    df14.reset_index(inplace=True)
    df14.drop(df14.columns[0],axis=1,inplace=True) 

    for i in range(len(df14)):    
       if df14.loc[:,'Withdrawal Amount (INR )'][i] > 0 and df14.loc[:,'Deposit Amount (INR )'][i] == 0 :
 #          if df7.bool(df7["Transaction Remarks"].str.contains(('^MMT/............/*'))) :
            df14.drop(index = [i], axis=0,inplace=True ) 
    df14.reset_index(inplace=True)
    df14.drop(df14.columns[0],axis=1,inplace=True)
   
    df14["Transaction Date"] = pd.to_datetime(df14["Transaction Date"], format="%d/%m/%Y" )                   
    df14["Year"] = df14["Transaction Date"].apply(lambda x: (x.year))
    df14["Week"] = df14["Transaction Date"].apply(lambda x: (x.week))             
    df14["Day"]  = df14["Transaction Date"].apply(lambda x: (x.day))
    df14["MonthInDays"] = df14["Transaction Date"].apply(lambda x: (x.month))
    df14["Month"] = df14["MonthInDays"].apply(lambda x: calendar.month_abbr[x])
            #df14.drop(df14.columns[[9]], axis = 1, inplace=True )

#----------------------------------------------------------
    #a=df14["Transaction Date"].max()
    #z=str(a.date())
            #z=z.strftime('%d-%b-%Y')
#------------To get current date/time in standard format------------- 
    now1 = datetime.datetime.now()
            #print(now)
            #now=now.date()
    now=str(now1.date())
            #now=now.strftime('%d-%b-%Y')
#-----------------------------------------------------------
            #b=df14["Month"].max()
    d = datetime.datetime.strptime(now, "%Y-%m-%d")
    #print(d.month)
            #print(d)
    #print("user entered month",b)
    b=2
    d2 = d - dateutil.relativedelta.relativedelta(months=b)
            #d2=d2.strftime('%d-%b-%Y')
            
    #print(d2)
    d2=str(d2.date())
    d3=datetime.datetime.strptime(d2, "%Y-%m-%d")
    #print("difference month:",d3.month)
    
    
    #print("difference year:",d3.year)
    userm=d3.month
    usery=d3.year
    total=0

    #if df14.loc[:,'MonthInDays'][i] == userm and df14.loc[:,'Year'][i] == usery :

    #aa=df15["Transaction Date"].max()
    #bal=df15[df15["MonthInDays"]==userm]     
     #   df15[df15["MonthInDays"]==userm]["Balance (INR )"]
     
     
        
    for i in range(len(df14)):

        count=0
            
        if df14.loc[:,'MonthInDays'][i] == userm and df14.loc[:,'Year'][i] == usery :
            total+= df14.loc[:,'Deposit Amount (INR )'][i]
            #mth=df14.loc[:,'Month'][i]
            count=count+1
            #print(int(round(total)))
            #print(count)
            #print("df date",a)    
    for i in range(len(df14)):
        c=0
        if df14.loc[:,'MonthInDays'][i] == userm and df14.loc[:,'Year'][i] == usery :
            mth1=df14.loc[:,'Month'][i] 
            c=c+1
            print("\nAmount received during",mth1,",",usery,"is INR ",int(round(total)))
            break
            #count1=count1+1
            #i12=z12+1
            

         
    #print(total)
 
    #TotalRechargeExp=df14["Deposit Amount (INR )"].sum()
  
            
    #df14.drop(df14.columns[[0,1,2,4,5,7,8]], axis = 1, inplace=True )
    #test=df14.pivot_table(index=["Year"],columns=["Month"])
    #test = test.unstack()
            #NoOfMonthsTotal=test.nunique()
    #df14.rename(columns={'Deposit Amount (INR )': 'Funds Received'},inplace=True)
            
            #print(test)
    #print("\nchatBOT>>> Following Funds Received \n",df14.pivot_table(index=["Year"],values=["Funds Received"],aggfunc=sum))
    #print("\n")
    #decide=df14.pivot_table(index=["Year"],values=["Funds Received"],aggfunc=sum)
            #print(len(decide))
    #decide.reset_index(drop=True, inplace=True)
    #NoOfMonthsTotal=test.count()
            #print(NoOfMonthsTotal)
            #print(NoOfMonthsTotal.sum())
    #MonthlyExpTotal=TotalRechargeExp / NoOfMonthsTotal.sum()            
    #print("\na) Total Funds Received : INR",int(round(TotalRechargeExp)))
    #print("\nb) Average Monthly Funds Received : INR",int(round(MonthlyExpTotal)))

            
#--------------------------------------                    
            #df14.groupby(["Month","FundTransfer"]).size()
    d1 = df14.pivot_table(index="Month",columns="FundTransfer",aggfunc=sum)
    #print(d1)
            #plt.plot(df14["Month"],df14["FundTransfer"])
    df14.to_excel("/Users/orbaa5/Desktop/Dissertation/Thesis/Data/TrainingResult/Credit_FundTransfer.xls")
            #print(df1)
    
    aq3=df14["Deposit Amount (INR )"].sum()
    aq4=df14["Month"].count()
    
    qv=aq3/aq4
    qb=int(qv)
    
    return qb


def Inv_Input_analysis():

    cft = Credit_FundTransfer()
    print("\n1.Execution completed : NEFT/RTGS Cash received from friends, family \n")
    avgExp = Average_Exp()
    print("2.Execution completed : Average Expenditure\n")
    amb=AverageMonthly_Bal()
    print("3.Execution completed : Average Monthly Balance\n")
    eb=Electricity_BSES()
    print("4.Execution completed : Average Electricity Bill\n") 
    tb=Telephone_MTNL()
    print("5.Execution completed : Average Telephone Bill\n")
    wb=Water_DJB()
    print("6.Execution completed : Average Water bill\n")
    shp = Shopping(2,2018)
    print("7.Execution completed : Average Shopping expenditure\n")
    tl = Travel()
    print("8.Execution completed : Average Travelling expenditure\n")
    dft=Debit_FundTransfer()
    print("9.Execution completed : NEFT/RTGS Cash sent to friends, family \n")
    iatm=ICICIATM_CashWithdrawl()
    print("10.Execution completed : Average Cash withdrawl from ICICI ATM \n")
    natm=NonICICIATM_CashWithdrawl()
    print("11.Execution completed : Average Cash withdrawl from Non ICICI ATM\n")
    rc=Recharge()
    print("12.Execution completed : Average mobile Recharge expenditure\n")
    emi=Loan_EMI()
    print("13.Execution completed : Monthly EMI paid for Home Loan \n")
    sal=Salary()
    print("14.Execution completed : Average monthly salary received \n")
    intt=Interest()
    print("15.Execution completed : Average interest received from investments \n")
    ar=Auto_Reversal()
    print("16.Execution completed : Auto reversal charges due to network failure \n")
    
    TC=cft+ar+intt+sal
    NE=shp+tl+rc
    E=eb+wb+tb+emi+iatm+natm+dft
    Svgs=TC-(NE+E)
    at="Savings"
        
    #if( weight >= 6):
    #    print( "Successfull")
    return Svgs,intt,NE,emi,at,sal

def BusinessLogic_Inv(Svgs,intt,NE,emi,at,sal):
    
   #svgs > 50, Int > 3500, Loan: Regular, Shp : Spending   
### business Rules ######   
    
    if Svgs >= 0 and Svgs < sal/2:
        w1=2
    elif Svgs > sal/2:
        w1=1
   
    if intt >= 5000 and intt <=10000:
        w2=2    
    elif intt < 5000:
        w2=1
    
    if NE >=0 and NE <=25:
        w3=2
    elif NE >25:
        w3=1
    
    if emi >=0 and emi <=25000:
        w4=2
    elif emi > 25000:
        w4=1
    
    if at =="Savings":
        w5=2
    elif at =="Current":
        w5=1
    
    
    weight = w1 + w2 + w3 + w4 + w5
   #Savings ( 2 if <= 50% ,  1 > 50% ), 
   #Tax Free Int ( 2 - If >5K <=10K, 1 - >=0 and <=5K), 
   #[2 - NE <= 25%, 1- >25% ], 
   #[Monthloan < 25k ( 2 ),  >25k [ 1]
   #Accounttype= savings salary [ 2] , 1 - current ] 
   
    #NE=shp+tl+rc
    #E=eb+wb+tb+emi+iatm+natm+dft
    #TC=cft+ar+it+sal
    #E = eb+wb+tb+emi+
    
    #emiT=
    
    #print("NE",NE,"\n")
    #print("E",E,"\n")
    #print("TC",TC,"\N")
    
    #print("svg",TC-(NE+E))
    #print()
    
    #Notessential-shp+tl+ auto. rev
    #Essential-eb+tb+wb+emi+iatm+natm+rc+dft
    
    #av. Exp, AVG. Mthly bal
    
    #cash , cft, ar, Int., sal

   
    if (weight >= 5):
        url = "https://www.icicipruamc.com/icici-prudential-mutual-fund/funds/equity-funds/icici-prudential-bluechip-fund"
        Product = "Direct"
        NAV = "Higher"  
        return url,Product,NAV
    
    elif (weight < 5):
        url = "https://www.icicipruamc.com/icici-prudential-mutual-fund/funds/equity-funds/icici-prudential-bluechip-fund"
        Product = "Dividend"
        NAV = "Higher"
        return url,Product,NAV
    
    #svgs = int((amb*100)/sal)
    #print(svgs)

# =============================================================================
# 

# 
# 
#     BhushanSteel2011_2012()
#     BhushanSteel2013()
#     BhushanSteel2014_2015()
#     
#     stable=5
#     risk=3
#     unstable=1
#     MCA = -5
#     
#     QuickRatio=Quick_ratio
#     DebtEquity=Debt_Equity_ratio
#     MCA=MCA_Rules
#     
#     weight=QuickRatio+DebtEquity+MCA
#     
#     if weight > 0 and weight <= 7.5:
#         risk
# =============================================================================
    
#    if weight > 7.5 


# while( QuickRatio fails, check quick ratio )
# multiple functions 1,2,3,4... - top 5 industries,  specific ratio ( Tata, Jindal, JSW, etc) 
# only 1 function  - industry standard
# only 1 function - global standard        

#while(current ratio fails, check current ratio)
# multiple functions 1,2,3,4 - top 5 industries, ration ( Tata, Jindal, JSW, etc)
# only 1 function  - industry standard
# only 1 function - global standard  
        
  
      
#Indian industry average =, standard
#gloabl industry standard
    
#  industry average :  1.39, standard = 2    
        
        
#LiquidityRatio - short term solvency ( current obligations )        
#AbsoluteQuickRatio ( Cash+BanK+marketable securities)/TotalCurrentLiab. )


#1. current ratio - currentsassets/current liabilities
#[ high indicated : very high utilization of current assets / under utilization or improper utilization of assets )]
#low indicated : not able to pay short term debt on time ;if situaiton continues for 3 years, credit worthiness affect ] 
#value => 2 

#2. quick ratio- exclude inventory, [ aCID tEST rATIO ],    
#3. absolute liquidity ratio        
# =============================================================================
#     
#     if QuickRatio > 2:
#         stable
#     elif QuickRatio >1.39 and QuickRatio <=2:
#         risk
#     elif QuickRatio <1:
#         unstable
# 
# #Solvency ratio:
# # Cmpany more reliant or borrowing or owner's funds to fund asset/activities [ Total debt /equity]              
#         #1:1
# 
# #Indian industry average =, standard
# #gloabl industry standard
#             
#     if DebtEquity <= 0.5:
#         stable
#     elif DebtEquity > 0.5 and DebtEquity <=1:
#         risk
#     elif DebtEquity > 1:
#         unstable
# 
#     #MCA=Long Term Debt <= Reserves and surplus 
#     if MCA == "True":
#         MCA
#         
# 
# #if Interest coverage ratio ( EBITDA / Int. Expense) , industry standard = 2, average = 1-2, <1, unstable
# 
# 
# 
# #Top Steel produing companies in the world
# 
# #Arcelor Mittal
# 
# Hebei Steel Group
# 
# Nippon Steel and Sumitomo 
# Metal Corporation (NSSMC)
# 
# POSCO
# 
# Baosteel Group
# 
# Shagang Group
# 
# No. 10 Tata Steel Group
# 
# No. 26 SAIL 
# 
# No. 30 JSW Steel Limited 
# 
# tata
# essar
# jindal
# ispat
# =============================================================================


#def process2():
    #time.sleep(2)
# =============================================================================
# =============================================================================
# #    
#      start=datetime.datetime.now()
#      print("child process ID:",os.getpid())
#      print("no. of core",multiprocessing.cpu_count())
# =============================================================================
     #Shopping(2,2018)
     #print("11111   stop !!!!!!! execution")
#     
#     a=98490545
#     b=3454456
#     asd1=a*b
#     
#     c=9984905345
#     d=3454454345
#     asd2=c+d
#     
#     e=92
#     f=34
#     asd3=e*f
#     
#     g=98994905
#     h=3454454
#     asd4=g*h
#     
#     i=984905
#     j=34254454
#     asd5=i*j
#     
#     print(asd1*asd2*asd3*asd4*asd5)
#     
# =============================================================================
# =============================================================================
# =============================================================================
# =============================================================================
# =============================================================================
# =============================================================================
   

       

def Business_Logic_NPA(violation_2011,violation_2012,Quick_Ratio_2011,Quick_Ratio_2012,Absolute_Liquid_ratio_2011,Absolute_Liquid_ratio_2012,Debt_Equity_ratio_2011,Debt_Equity_ratio_2012,FY2011,FY2012,violation_2013,Quick_Ratio_2013,Absolute_Liquid_ratio_2013,Debt_Equity_ratio_2013,FY2013,violation_2014,violation_2015,Quick_Ratio_2014,Quick_Ratio_2015,Absolute_Liquid_ratio_2014,Absolute_Liquid_ratio_2015,Debt_Equity_ratio_2014,Debt_Equity_ratio_2015,FY2014,FY2015):
      
      #   Industry - 6 RINL, SAIL, Tata Steel, JSW, JSPL
    
# =============================================================================
#     print("violation1",violation_2011)
#     print("violation2",violation_2012)
#     print(Quick_Ratio_2011)
#     print(Quick_Ratio_2012)
#     print(Absolute_Liquid_ratio_2011)
#     print(Absolute_Liquid_ratio_2012)
#     print(Debt_Equity_ratio_2011)
#     print(Debt_Equity_ratio_2012)
#     print("violation3",violation_2013)
#     print(Quick_Ratio_2013)
#     print(Absolute_Liquid_ratio_2013)
#     print(Debt_Equity_ratio_2013)
#     print("violation4",violation_2014)
#     print("violation5",violation_2015)
#     print(Quick_Ratio_2014)
#     print(Quick_Ratio_2015)
#     print(Absolute_Liquid_ratio_2014)
#     print(Absolute_Liquid_ratio_2015)
#     print(Debt_Equity_ratio_2014)
#     print(Debt_Equity_ratio_2015)
# =============================================================================
    
    TotalViolation = violation_2011+violation_2012+violation_2013+violation_2014+violation_2015
    
    Quick_Ratio_RINL=0.13
    Absolute_liquid_RINL=0.91
    debt_equity_RINL=0.68
    
    Quick_Ratio_SAIL=0.21
    Absolute_liquid_SAIL=0.39
    debt_equity_SAIL=1.15
    
    Quick_Ratio_Tata=0.42
    Absolute_liquid_Tata=0.67
    debt_equity_Tata=0.44
    
    Quick_Ratio_JSW=0.68
    Absolute_liquid_JSW=0.74
    debt_equity_JSW=1.2
    
    Quick_Ratio_JSPL=0.45
    Absolute_liquid_JSPL=0.43
    debt_equity_JSPL=0.94
    
    Quick_Ratio_avg=0.65
    Absolute_liquid_avg=0.24
    debt_equity_avg=2.54
    
    Quick_Ratio_global=0.41
    Absolute_liquid_global=0.86
    debt_equity_global=0.31
    
    if TotalViolation >=0:
        #weight = 5
        Performance=0
    elif TotalViolation == 0:
        #weight = 4
        Performance=1
    
    if Performance == 0:
        return TotalViolation,FY2011,FY2012,FY2013,FY2014,FY2015,Performance
    
    elif Performance ==1:
        if Quick_Ratio_2011 > Quick_Ratio_RINL:
            Quick_Ratio_2011_RINL=1
        elif Quick_Ratio_2011 <= Quick_Ratio_RINL:
            Quick_Ratio_2011_RINL=0
            
        if Quick_Ratio_2012 > Quick_Ratio_RINL:
            Quick_Ratio_2012_RINL=1
        elif Quick_Ratio_2012 <= Quick_Ratio_RINL:
            Quick_Ratio_2012_RINL=0 
        
        if Quick_Ratio_2013 > Quick_Ratio_RINL:
            Quick_Ratio_2013_RINL=1
        elif Quick_Ratio_2013 <= Quick_Ratio_RINL:
            Quick_Ratio_2013_RINL=0
            
        if Quick_Ratio_2014 > Quick_Ratio_RINL:
            Quick_Ratio_2014_RINL=1
        elif Quick_Ratio_2014 <= Quick_Ratio_RINL:
            Quick_Ratio_2014_RINL=0 
                    
        if Quick_Ratio_2015 > Quick_Ratio_RINL:
            Quick_Ratio_2015_RINL=1
        elif Quick_Ratio_2015 <= Quick_Ratio_RINL:
            Quick_Ratio_2015_RINL=0 
            
####################################        
        if Absolute_Liquid_ratio_2011 > Absolute_liquid_RINL:
            Absolute_Liquid_ratio_2011_RINL=1
        elif Absolute_Liquid_ratio_2011 <= Absolute_liquid_RINL:
            Absolute_Liquid_ratio_2011_RINL=0
            
        if Absolute_Liquid_ratio_2012 > Absolute_liquid_RINL:
            Absolute_Liquid_ratio_2012_RINL=1
        elif Absolute_Liquid_ratio_2012 <= Absolute_liquid_RINL:
            Absolute_Liquid_ratio_2012_RINL=0 
        
        if Absolute_Liquid_ratio_2013 > Absolute_liquid_RINL:
            Absolute_Liquid_ratio_2013_RINL=1
        elif Absolute_Liquid_ratio_2013 <= Absolute_liquid_RINL:
            Absolute_Liquid_ratio_2013_RINL=0
            
        if Absolute_Liquid_ratio_2014 > Absolute_liquid_RINL:
            Absolute_Liquid_ratio_2014_RINL=1
        elif Absolute_Liquid_ratio_2014 <= Absolute_liquid_RINL:
            Absolute_Liquid_ratio_2014_RINL=0 
                    
        if Absolute_Liquid_ratio_2015 > Absolute_liquid_RINL:
            Absolute_Liquid_ratio_2015_RINL=1
        elif Absolute_Liquid_ratio_2015 <= Absolute_liquid_RINL:
            Absolute_Liquid_ratio_2015_RINL=0
####################################        
        if Debt_Equity_ratio_2011 > debt_equity_RINL:
            Debt_Equity_ratio_2011_RINL=1
        elif Debt_Equity_ratio_2011 <= debt_equity_RINL:
            Debt_Equity_ratio_2011_RINL=0
            
        if Debt_Equity_ratio_2012 > debt_equity_RINL:
            Debt_Equity_ratio_2012_RINL=1
        elif Debt_Equity_ratio_2012 <= debt_equity_RINL:
            Debt_Equity_ratio_2012_RINL=0 
        
        if Debt_Equity_ratio_2013 > debt_equity_RINL:
            Debt_Equity_ratio_2013_RINL=1
        elif Debt_Equity_ratio_2013 <= debt_equity_RINL:
            Debt_Equity_ratio_2013_RINL=0
            
        if Debt_Equity_ratio_2014 > debt_equity_RINL:
            Debt_Equity_ratio_2014_RINL=1
        elif Debt_Equity_ratio_2014 <= debt_equity_RINL:
            Debt_Equity_ratio_2014_RINL=0 
                    
        if Debt_Equity_ratio_2015 > debt_equity_RINL:
            Debt_Equity_ratio_2015_RINL=1
        elif Debt_Equity_ratio_2015 <= debt_equity_RINL:
            Debt_Equity_ratio_2015_RINL=0        
########################################        
        if Quick_Ratio_2011 > Quick_Ratio_SAIL:
            Quick_Ratio_2011_SAIL=1
        elif Quick_Ratio_2011 <= Quick_Ratio_SAIL:
            Quick_Ratio_2011_SAIL=0
            
        if Quick_Ratio_2012 > Quick_Ratio_SAIL:
            Quick_Ratio_2012_SAIL=1
        elif Quick_Ratio_2012 <= Quick_Ratio_SAIL:
            Quick_Ratio_2012_SAIL=0 
        
        if Quick_Ratio_2013 > Quick_Ratio_SAIL:
            Quick_Ratio_2013_SAIL=1
        elif Quick_Ratio_2013 <= Quick_Ratio_SAIL:
            Quick_Ratio_2013_SAIL=0
            
        if Quick_Ratio_2014 > Quick_Ratio_SAIL:
            Quick_Ratio_2014_SAIL=1
        elif Quick_Ratio_2014 <= Quick_Ratio_SAIL:
            Quick_Ratio_2014_SAIL=0 
                    
        if Quick_Ratio_2015 > Quick_Ratio_SAIL:
            Quick_Ratio_2015_SAIL=1
        elif Quick_Ratio_2015 <= Quick_Ratio_SAIL:
            Quick_Ratio_2015_SAIL=0 
####################################        
        if Absolute_Liquid_ratio_2011 > Absolute_liquid_SAIL:
            Absolute_Liquid_ratio_2011_SAIL=1
        elif Absolute_Liquid_ratio_2011 <= Absolute_liquid_SAIL:
            Absolute_Liquid_ratio_2011_SAIL=0
            
        if Absolute_Liquid_ratio_2012 > Absolute_liquid_SAIL:
            Absolute_Liquid_ratio_2012_SAIL=1
        elif Absolute_Liquid_ratio_2012 <= Absolute_liquid_SAIL:
            Absolute_Liquid_ratio_2012_SAIL=0 
        
        if Absolute_Liquid_ratio_2013 > Absolute_liquid_SAIL:
            Absolute_Liquid_ratio_2013_SAIL=1
        elif Absolute_Liquid_ratio_2013 <= Absolute_liquid_SAIL:
            Absolute_Liquid_ratio_2013_SAIL=0
            
        if Absolute_Liquid_ratio_2014 > Absolute_liquid_SAIL:
            Absolute_Liquid_ratio_2014_SAIL=1
        elif Absolute_Liquid_ratio_2014 <= Absolute_liquid_SAIL:
            Absolute_Liquid_ratio_2014_SAIL=0 
                    
        if Absolute_Liquid_ratio_2015 > Absolute_liquid_SAIL:
            Absolute_Liquid_ratio_2015_SAIL=1
        elif Absolute_Liquid_ratio_2015 <= Absolute_liquid_SAIL:
            Absolute_Liquid_ratio_2015_SAIL=0
####################################        
        if Debt_Equity_ratio_2011 > debt_equity_SAIL:
            Debt_Equity_ratio_2011_SAIL=1
        elif Debt_Equity_ratio_2011 <= debt_equity_SAIL:
            Debt_Equity_ratio_2011_SAIL=0
            
        if Debt_Equity_ratio_2012 > debt_equity_SAIL:
            Debt_Equity_ratio_2012_SAIL=1
        elif Debt_Equity_ratio_2012 <= debt_equity_SAIL:
            Debt_Equity_ratio_2012_SAIL=0 
        
        if Debt_Equity_ratio_2013 > debt_equity_SAIL:
            Debt_Equity_ratio_2013_SAIL=1
        elif Debt_Equity_ratio_2013 <= debt_equity_SAIL:
            Debt_Equity_ratio_2013_SAIL=0
            
        if Debt_Equity_ratio_2014 > debt_equity_SAIL:
            Debt_Equity_ratio_2014_SAIL=1
        elif Debt_Equity_ratio_2014 <= debt_equity_SAIL:
            Debt_Equity_ratio_2014_SAIL=0 
                    
        if Debt_Equity_ratio_2015 > debt_equity_SAIL:
            Debt_Equity_ratio_2015_SAIL=1
        elif Debt_Equity_ratio_2015 <= debt_equity_SAIL:
            Debt_Equity_ratio_2015_SAIL=0                
########################################        
        if Quick_Ratio_2011 > Quick_Ratio_Tata:
            Quick_Ratio_2011_Tata=1
        elif Quick_Ratio_2011 <= Quick_Ratio_Tata:
            Quick_Ratio_2011_Tata=0
            
        if Quick_Ratio_2012 > Quick_Ratio_Tata:
            Quick_Ratio_2012_Tata=1
        elif Quick_Ratio_2012 <= Quick_Ratio_Tata:
            Quick_Ratio_2012_Tata=0 
        
        if Quick_Ratio_2013 > Quick_Ratio_Tata:
            Quick_Ratio_2013_Tata=1
        elif Quick_Ratio_2013 <= Quick_Ratio_Tata:
            Quick_Ratio_2013_Tata=0
            
        if Quick_Ratio_2014 > Quick_Ratio_Tata:
            Quick_Ratio_2014_Tata=1
        elif Quick_Ratio_2014 <= Quick_Ratio_Tata:
            Quick_Ratio_2014_Tata=0 
                    
        if Quick_Ratio_2015 > Quick_Ratio_Tata:
            Quick_Ratio_2015_Tata=1
        elif Quick_Ratio_2015 <= Quick_Ratio_Tata:
            Quick_Ratio_2015_Tata=0 
####################################        
        if Absolute_Liquid_ratio_2011 > Absolute_liquid_Tata:
            Absolute_Liquid_ratio_2011_Tata=1
        elif Absolute_Liquid_ratio_2011 <= Absolute_liquid_Tata:
            Absolute_Liquid_ratio_2011_Tata=0
            
        if Absolute_Liquid_ratio_2012 > Absolute_liquid_Tata:
            Absolute_Liquid_ratio_2012_Tata=1
        elif Absolute_Liquid_ratio_2012 <= Absolute_liquid_Tata:
            Absolute_Liquid_ratio_2012_Tata=0 
        
        if Absolute_Liquid_ratio_2013 > Absolute_liquid_Tata:
            Absolute_Liquid_ratio_2013_Tata=1
        elif Absolute_Liquid_ratio_2013 <= Absolute_liquid_Tata:
            Absolute_Liquid_ratio_2013_Tata=0
            
        if Absolute_Liquid_ratio_2014 > Absolute_liquid_Tata:
            Absolute_Liquid_ratio_2014_Tata=1
        elif Absolute_Liquid_ratio_2014 <= Absolute_liquid_Tata:
            Absolute_Liquid_ratio_2014_Tata=0 
                    
        if Absolute_Liquid_ratio_2015 > Absolute_liquid_Tata:
            Absolute_Liquid_ratio_2015_Tata=1
        elif Absolute_Liquid_ratio_2015 <= Absolute_liquid_Tata:
            Absolute_Liquid_ratio_2015_Tata=0
####################################        
        if Debt_Equity_ratio_2011 > debt_equity_Tata:
            Debt_Equity_ratio_2011_Tata=1
        elif Debt_Equity_ratio_2011 <= debt_equity_Tata:
            Debt_Equity_ratio_2011_Tata=0
            
        if Debt_Equity_ratio_2012 > debt_equity_Tata:
            Debt_Equity_ratio_2012_Tata=1
        elif Debt_Equity_ratio_2012 <= debt_equity_Tata:
            Debt_Equity_ratio_2012_Tata=0 
        
        if Debt_Equity_ratio_2013 > debt_equity_Tata:
            Debt_Equity_ratio_2013_Tata=1
        elif Debt_Equity_ratio_2013 <= debt_equity_Tata:
            Debt_Equity_ratio_2013_Tata=0
            
        if Debt_Equity_ratio_2014 > debt_equity_Tata:
            Debt_Equity_ratio_2014_Tata=1
        elif Debt_Equity_ratio_2014 <= debt_equity_Tata:
            Debt_Equity_ratio_2014_Tata=0 
                    
        if Debt_Equity_ratio_2015 > debt_equity_Tata:
            Debt_Equity_ratio_2015_Tata=1
        elif Debt_Equity_ratio_2015 <= debt_equity_Tata:
            Debt_Equity_ratio_2015_Tata=0         
#####################################          
        if Quick_Ratio_2011 > Quick_Ratio_JSW:
            Quick_Ratio_2011_JSW=1
        elif Quick_Ratio_2011 <= Quick_Ratio_JSW:
            Quick_Ratio_2011_JSW=0
            
        if Quick_Ratio_2012 > Quick_Ratio_JSW:
            Quick_Ratio_2012_JSW=1
        elif Quick_Ratio_2012 <= Quick_Ratio_JSW:
            Quick_Ratio_2012_JSW=0 
        
        if Quick_Ratio_2013 > Quick_Ratio_JSW:
            Quick_Ratio_2013_JSW=1
        elif Quick_Ratio_2013 <= Quick_Ratio_JSW:
            Quick_Ratio_2013_JSW=0
            
        if Quick_Ratio_2014 > Quick_Ratio_JSW:
            Quick_Ratio_2014_JSW=1
        elif Quick_Ratio_2014 <= Quick_Ratio_JSW:
            Quick_Ratio_2014_JSW=0 
                    
        if Quick_Ratio_2015 > Quick_Ratio_JSW:
            Quick_Ratio_2015_JSW=1
        elif Quick_Ratio_2015 <= Quick_Ratio_JSW:
            Quick_Ratio_2015_JSW=0 
####################################        
        if Absolute_Liquid_ratio_2011 > Absolute_liquid_JSW:
            Absolute_Liquid_ratio_2011_JSW=1
        elif Absolute_Liquid_ratio_2011 <= Absolute_liquid_JSW:
            Absolute_Liquid_ratio_2011_JSW=0
            
        if Absolute_Liquid_ratio_2012 > Absolute_liquid_JSW:
            Absolute_Liquid_ratio_2012_JSW=1
        elif Absolute_Liquid_ratio_2012 <= Absolute_liquid_JSW:
            Absolute_Liquid_ratio_2012_JSW=0 
        
        if Absolute_Liquid_ratio_2013 > Absolute_liquid_JSW:
            Absolute_Liquid_ratio_2013_JSW=1
        elif Absolute_Liquid_ratio_2013 <= Absolute_liquid_JSW:
            Absolute_Liquid_ratio_2013_JSW=0
            
        if Absolute_Liquid_ratio_2014 > Absolute_liquid_JSW:
            Absolute_Liquid_ratio_2014_JSW=1
        elif Absolute_Liquid_ratio_2014 <= Absolute_liquid_JSW:
            Absolute_Liquid_ratio_2014_JSW=0 
                    
        if Absolute_Liquid_ratio_2015 > Absolute_liquid_JSW:
            Absolute_Liquid_ratio_2015_JSW=1
        elif Absolute_Liquid_ratio_2015 <= Absolute_liquid_JSW:
            Absolute_Liquid_ratio_2015_JSW=0
####################################        
        if Debt_Equity_ratio_2011 > debt_equity_JSW:
            Debt_Equity_ratio_2011_JSW=1
        elif Debt_Equity_ratio_2011 <= debt_equity_JSW:
            Debt_Equity_ratio_2011_JSW=0
            
        if Debt_Equity_ratio_2012 > debt_equity_JSW:
            Debt_Equity_ratio_2012_JSW=1
        elif Debt_Equity_ratio_2012 <= debt_equity_JSW:
            Debt_Equity_ratio_2012_JSW=0 
        
        if Debt_Equity_ratio_2013 > debt_equity_JSW:
            Debt_Equity_ratio_2013_JSW=1
        elif Debt_Equity_ratio_2013 <= debt_equity_JSW:
            Debt_Equity_ratio_2013_JSW=0
            
        if Debt_Equity_ratio_2014 > debt_equity_JSW:
            Debt_Equity_ratio_2014_JSW=1
        elif Debt_Equity_ratio_2014 <= debt_equity_JSW:
            Debt_Equity_ratio_2014_JSW=0 
                    
        if Debt_Equity_ratio_2015 > debt_equity_JSW:
            Debt_Equity_ratio_2015_JSW=1
        elif Debt_Equity_ratio_2015 <= debt_equity_JSW:
            Debt_Equity_ratio_2015_JSW=0
######################################3
        if Quick_Ratio_2011 > Quick_Ratio_JSPL:
            Quick_Ratio_2011_JSPL=1
        elif Quick_Ratio_2011 <= Quick_Ratio_JSPL:
            Quick_Ratio_2011_JSPL=0
            
        if Quick_Ratio_2012 > Quick_Ratio_JSPL:
            Quick_Ratio_2012_JSPL=1
        elif Quick_Ratio_2012 <= Quick_Ratio_JSPL:
            Quick_Ratio_2012_JSPL=0 
        
        if Quick_Ratio_2013 > Quick_Ratio_JSPL:
            Quick_Ratio_2013_JSPL=1
        elif Quick_Ratio_2013 <= Quick_Ratio_JSPL:
            Quick_Ratio_2013_JSPL=0
            
        if Quick_Ratio_2014 > Quick_Ratio_JSPL:
            Quick_Ratio_2014_JSPL=1
        elif Quick_Ratio_2014 <= Quick_Ratio_JSPL:
            Quick_Ratio_2014_JSPL=0 
                    
        if Quick_Ratio_2015 > Quick_Ratio_JSPL:
            Quick_Ratio_2015_JSPL=1
        elif Quick_Ratio_2015 <= Quick_Ratio_JSPL:
            Quick_Ratio_2015_JSPL=0 
####################################        
        if Absolute_Liquid_ratio_2011 > Absolute_liquid_JSPL:
            Absolute_Liquid_ratio_2011_JSPL=1
        elif Absolute_Liquid_ratio_2011 <= Absolute_liquid_JSPL:
            Absolute_Liquid_ratio_2011_JSPL=0
            
        if Absolute_Liquid_ratio_2012 > Absolute_liquid_JSPL:
            Absolute_Liquid_ratio_2012_JSPL=1
        elif Absolute_Liquid_ratio_2012 <= Absolute_liquid_JSPL:
            Absolute_Liquid_ratio_2012_JSPL=0 
        
        if Absolute_Liquid_ratio_2013 > Absolute_liquid_JSPL:
            Absolute_Liquid_ratio_2013_JSPL=1
        elif Absolute_Liquid_ratio_2013 <= Absolute_liquid_JSPL:
            Absolute_Liquid_ratio_2013_JSPL=0
            
        if Absolute_Liquid_ratio_2014 > Absolute_liquid_JSPL:
            Absolute_Liquid_ratio_2014_JSPL=1
        elif Absolute_Liquid_ratio_2014 <= Absolute_liquid_JSPL:
            Absolute_Liquid_ratio_2014_JSPL=0 
                    
        if Absolute_Liquid_ratio_2015 > Absolute_liquid_JSPL:
            Absolute_Liquid_ratio_2015_JSPL=1
        elif Absolute_Liquid_ratio_2015 <= Absolute_liquid_JSPL:
            Absolute_Liquid_ratio_2015_JSPL=0
####################################        
        if Debt_Equity_ratio_2011 > debt_equity_JSPL:
            Debt_Equity_ratio_2011_JSPL=1
        elif Debt_Equity_ratio_2011 <= debt_equity_JSPL:
            Debt_Equity_ratio_2011_JSPL=0
            
        if Debt_Equity_ratio_2012 > debt_equity_JSPL:
            Debt_Equity_ratio_2012_JSPL=1
        elif Debt_Equity_ratio_2012 <= debt_equity_JSPL:
            Debt_Equity_ratio_2012_JSPL=0 
        
        if Debt_Equity_ratio_2013 > debt_equity_JSPL:
            Debt_Equity_ratio_2013_JSPL=1
        elif Debt_Equity_ratio_2013 <= debt_equity_JSPL:
            Debt_Equity_ratio_2013_JSPL=0
            
        if Debt_Equity_ratio_2014 > debt_equity_JSPL:
            Debt_Equity_ratio_2014_JSPL=1
        elif Debt_Equity_ratio_2014 <= debt_equity_JSPL:
            Debt_Equity_ratio_2014_JSPL=0 
                    
        if Debt_Equity_ratio_2015 > debt_equity_JSPL:
            Debt_Equity_ratio_2015_JSPL=1
        elif Debt_Equity_ratio_2015 <= debt_equity_JSPL:
            Debt_Equity_ratio_2015_JSPL=0            
#####################################
        if Quick_Ratio_2011 > Quick_Ratio_avg:
            Quick_Ratio_2011_AVG=1
        elif Quick_Ratio_2011 <= Quick_Ratio_avg:
            Quick_Ratio_2011_AVG=0
            
        if Quick_Ratio_2012 > Quick_Ratio_avg:
            Quick_Ratio_2012_AVG=1
        elif Quick_Ratio_2012 <= Quick_Ratio_avg:
            Quick_Ratio_2012_AVG=0 
        
        if Quick_Ratio_2013 > Quick_Ratio_avg:
            Quick_Ratio_2013_AVG=1
        elif Quick_Ratio_2013 <= Quick_Ratio_avg:
            Quick_Ratio_2013_AVG=0
            
        if Quick_Ratio_2014 > Quick_Ratio_avg:
            Quick_Ratio_2014_AVG=1
        elif Quick_Ratio_2014 <= Quick_Ratio_avg:
            Quick_Ratio_2014_AVG=0 
                    
        if Quick_Ratio_2015 > Quick_Ratio_avg:
            Quick_Ratio_2015_AVG=1
        elif Quick_Ratio_2015 <= Quick_Ratio_avg:
            Quick_Ratio_2015_AVG=0 
####################################        
        if Absolute_Liquid_ratio_2011 > Absolute_liquid_avg:
            Absolute_Liquid_ratio_2011_AVG=1
        elif Absolute_Liquid_ratio_2011 <= Absolute_liquid_avg:
            Absolute_Liquid_ratio_2011_AVG=0
            
        if Absolute_Liquid_ratio_2012 > Absolute_liquid_avg:
            Absolute_Liquid_ratio_2012_AVG=1
        elif Absolute_Liquid_ratio_2012 <= Absolute_liquid_avg:
            Absolute_Liquid_ratio_2012_AVG=0 
        
        if Absolute_Liquid_ratio_2013 > Absolute_liquid_avg:
            Absolute_Liquid_ratio_2013_AVG=1
        elif Absolute_Liquid_ratio_2013 <= Absolute_liquid_avg:
            Absolute_Liquid_ratio_2013_AVG=0
            
        if Absolute_Liquid_ratio_2014 > Absolute_liquid_avg:
            Absolute_Liquid_ratio_2014_AVG=1
        elif Absolute_Liquid_ratio_2014 <= Absolute_liquid_avg:
            Absolute_Liquid_ratio_2014_AVG=0 
                    
        if Absolute_Liquid_ratio_2015 > Absolute_liquid_avg:
            Absolute_Liquid_ratio_2015_AVG=1
        elif Absolute_Liquid_ratio_2015 <= Absolute_liquid_avg:
            Absolute_Liquid_ratio_2015_AVG=0
####################################        
        if Debt_Equity_ratio_2011 > debt_equity_avg:
            Debt_Equity_ratio_2011_AVG=1
        elif Debt_Equity_ratio_2011 <= debt_equity_avg:
            Debt_Equity_ratio_2011_AVG=0
            
        if Debt_Equity_ratio_2012 > debt_equity_avg:
            Debt_Equity_ratio_2012_AVG=1
        elif Debt_Equity_ratio_2012 <= debt_equity_avg:
            Debt_Equity_ratio_2012_AVG=0 
        
        if Debt_Equity_ratio_2013 > debt_equity_avg:
            Debt_Equity_ratio_2013_AVG=1
        elif Debt_Equity_ratio_2013 <= debt_equity_avg:
            Debt_Equity_ratio_2013_AVG=0
            
        if Debt_Equity_ratio_2014 > debt_equity_avg:
            Debt_Equity_ratio_2014_AVG=1
        elif Debt_Equity_ratio_2014 <= debt_equity_avg:
            Debt_Equity_ratio_2014_AVG=0 
                    
        if Debt_Equity_ratio_2015 > debt_equity_avg:
            Debt_Equity_ratio_2015_AVG=1
        elif Debt_Equity_ratio_2015 <= debt_equity_avg:
            Debt_Equity_ratio_2015_AVG=0 
########################################3
        if Quick_Ratio_2011 > Quick_Ratio_global:
            Quick_Ratio_2011_AVG=1
        elif Quick_Ratio_2011 <= Quick_Ratio_global:
            Quick_Ratio_2011_AVG=0
            
        if Quick_Ratio_2012 > Quick_Ratio_global:
            Quick_Ratio_2012_AVG=1
        elif Quick_Ratio_2012 <= Quick_Ratio_global:
            Quick_Ratio_2012_AVG=0 
        
        if Quick_Ratio_2013 > Quick_Ratio_global:
            Quick_Ratio_2013_AVG=1
        elif Quick_Ratio_2013 <= Quick_Ratio_global:
            Quick_Ratio_2013_AVG=0
            
        if Quick_Ratio_2014 > Quick_Ratio_global:
            Quick_Ratio_2014_AVG=1
        elif Quick_Ratio_2014 <= Quick_Ratio_global:
            Quick_Ratio_2014_AVG=0 
                    
        if Quick_Ratio_2015 > Quick_Ratio_global:
            Quick_Ratio_2015_AVG=1
        elif Quick_Ratio_2015 <= Quick_Ratio_global:
            Quick_Ratio_2015_AVG=0 
####################################        
        if Absolute_Liquid_ratio_2011 > Absolute_liquid_global:
            Absolute_Liquid_ratio_2011_global=1
        elif Absolute_Liquid_ratio_2011 <= Absolute_liquid_global:
            Absolute_Liquid_ratio_2011_global=0
            
        if Absolute_Liquid_ratio_2012 > Absolute_liquid_global:
            Absolute_Liquid_ratio_2012_global=1
        elif Absolute_Liquid_ratio_2012 <= Absolute_liquid_global:
            Absolute_Liquid_ratio_2012_global=0 
        
        if Absolute_Liquid_ratio_2013 > Absolute_liquid_global:
            Absolute_Liquid_ratio_2013_global=1
        elif Absolute_Liquid_ratio_2013 <= Absolute_liquid_global:
            Absolute_Liquid_ratio_2013_global=0
            
        if Absolute_Liquid_ratio_2014 > Absolute_liquid_global:
            Absolute_Liquid_ratio_2014_global=1
        elif Absolute_Liquid_ratio_2014 <= Absolute_liquid_global:
            Absolute_Liquid_ratio_2014_global=0 
                    
        if Absolute_Liquid_ratio_2015 > Absolute_liquid_global:
            Absolute_Liquid_ratio_2015_global=1
        elif Absolute_Liquid_ratio_2015 <= Absolute_liquid_global:
            Absolute_Liquid_ratio_2015_global=0
####################################        
        if Debt_Equity_ratio_2011 > debt_equity_global:
            Debt_Equity_ratio_2011_global=1
        elif Debt_Equity_ratio_2011 <= debt_equity_global:
            Debt_Equity_ratio_2011_global=0
            
        if Debt_Equity_ratio_2012 > debt_equity_global:
            Debt_Equity_ratio_2012_global=1
        elif Debt_Equity_ratio_2012 <= debt_equity_global:
            Debt_Equity_ratio_2012_global=0 
        
        if Debt_Equity_ratio_2013 > debt_equity_global:
            Debt_Equity_ratio_2013_global=1
        elif Debt_Equity_ratio_2013 <= debt_equity_global:
            Debt_Equity_ratio_2013_global=0
            
        if Debt_Equity_ratio_2014 > debt_equity_global:
            Debt_Equity_ratio_2014_global=1
        elif Debt_Equity_ratio_2014 <= debt_equity_global:
            Debt_Equity_ratio_2014_global=0 
                    
        if Debt_Equity_ratio_2015 > debt_equity_global:
            Debt_Equity_ratio_2015_global=1
        elif Debt_Equity_ratio_2015 <= debt_equity_global:
            Debt_Equity_ratio_2015_global=0       
    
    #Quick_ratio_RNL_Total=Quick_Ratio_2011_RINL+Quick_Ratio_2012_RINL+Quick_Ratio_2013_RINL+Quick_Ratio_2014_RINL+Quick_Ratio_2015_RINL
    #Absolute_Liquid_ratio_RNL_Total=Absolute_Liquid_ratio_2011+Absolute_Liquid_ratio_2012+Absolute_Liquid_ratio_2013+Absolute_Liquid_ratio_2014+Absolute_Liquid_ratio_2015
        

####################################
        #interest_coverage_RINL=11.67
        #inventory_turnover_RINL=2.59
        #asset_turnover_RINL=2.52
        #returnon_assets_RINL=8.45   
                
        #interest_coverage_SAIL=8.65
        #inventory_turnover_SAIL=2.44
        #asset_turnover_SAIL=2.08
        #returnon_assets_SAIL=2.62
    
        
        #interest_coverage_Tata=5.89
        #inventory_turnover_Tata=6.13
        #asset_turnover_Tata=1.97
        #returnon_assets_Tata=14.39
        
        
        
        #interest_coverage_JSW=3.04
        #inventory_turnover_JSW=7.10
        #asset_turnover_JSW=1.11
        #return_on_capital_JSW=7.66
        
        

        #interest_coverage_JSPL=0.86
        #inventory_turnover_JSPL=5.65
        #asset_turnover_JSPL=0.38
        #returnon_assets_JSPL=4.67
        
    #   6 Industry Average - 1

        #interest_coverage_avg=6.87
        #inventory_turnover_avg=7.5
        #asset_turnover_avg=2.15
        #returnon_assets_avg=5.38
    
    #   Global Industry - 1 ( Arcelor Mittal )

        #interest_coverage_global=6.18
        #inventory_turnover_global=3.3
    #asset_turnover_global= 0.86
    #returnon_assets_global=5.3

# =============================================================================
#     v,year1,year2  = BhushanSteel2011_2012()
#          
#     v1,year3       = BhushanSteel2013()
#          
#     v2,year4,year5 = BhushanSteel2014_2015()
#          
#     Violations=v+v1+v2
#     
#     AssessmentBhushanSteel(Violations,year2,year1,year3,year5,year4)
# =============================================================================
    
    #Govt_Norms=Equity_Long_Term_Liability
#      #print("child process ID:",os.getpid())   
#      end=datetime.datetime.now()
#      print("Child Time:",end-start)
# =============================================================================
     
# =============================================================================
# =============================================================================
# =============================================================================
# =============================================================================
        #end = datetime.datetime.now()


## RETURN computed 25 variables/values (20 Ratios + 5 FYear's) / 40 numeric values extracted from 5 B.S ( 1 B.S Per year)

def NPA_Input_analysis():
    print("\n1. Execution Started: F.Y 2011,2012 balance sheet PDF to jpeg image conversion + applying OCR Tesseract ")
    violation_2011,violation_2012,Quick_Ratio_2011,Quick_Ratio_2012,Absolute_Liquid_ratio_2011,Absolute_Liquid_ratio_2012,Debt_Equity_ratio_2011,Debt_Equity_ratio_2012,FY2011,FY2012 = BhushanSteel2011_2012()
    print("1. Execution Completed")
    
    print("\n2. Execution Started: F.Y 2013 balance sheet PDF to jpeg image conversion + applying OCR Tesseract ")
    violation_2013,Quick_Ratio_2013,Absolute_Liquid_ratio_2013,Debt_Equity_ratio_2013,FY2013 = BhushanSteel2013()
    print("2. Execution Completed")

    print("\n3. Execution Started: F.Y 2014,2015 balance sheet PDF to jpeg image conversion + applying OCR Tesseract ")
    violation_2014,violation_2015,Quick_Ratio_2014,Quick_Ratio_2015,Absolute_Liquid_ratio_2014,Absolute_Liquid_ratio_2015,Debt_Equity_ratio_2014,Debt_Equity_ratio_2015,FY2014,FY2015=BhushanSteel2014_2015()
    print("3. Execution Completed")

    return violation_2011,violation_2012,Quick_Ratio_2011,Quick_Ratio_2012,Absolute_Liquid_ratio_2011,Absolute_Liquid_ratio_2012,Debt_Equity_ratio_2011,Debt_Equity_ratio_2012,FY2011,FY2012,violation_2013,Quick_Ratio_2013,Absolute_Liquid_ratio_2013,Debt_Equity_ratio_2013,FY2013,violation_2014,violation_2015,Quick_Ratio_2014,Quick_Ratio_2015,Absolute_Liquid_ratio_2014,Absolute_Liquid_ratio_2015,Debt_Equity_ratio_2014,Debt_Equity_ratio_2015,FY2014,FY2015
   
    
def main():
    
    #print("main() ID:",os.getpid())
    #print("\nparent ID",os.getppid())
    #print("\nPcount:",os.cpu_count())
    
    start = datetime.datetime.now()
    a=input("Kindly enter your query : ")
    # print("type input",type(a))
 #a="invest"
# ===================ENABLE==========================================================
#     print("\n===Please sit back !!! Response may take 20-25 seconds\n" )
#     print("Because scanned image pdf 5 BS ( Year 2011 to 2015 ) undergoing these steps :-\n") 
#     print("1. pdf to jpeg conversion using Wand ( MagickWand API binding)") 
#     print("2) Optical Character Recognition using pytesseract ( Tesseract OCR engine)") 
#     print("3) Token extraction using NLTK")
#     print("4) NPA condition validation for each non uniform (Format) Balance Sheets using MCA Act 1956, 2013")
#     print("5) Aggregating and display the result from multiple functions")
#     
# =============================================================================
    stop_words = set(stopwords.words("english"))
    
    #yesprint("stop words type",type(stop_words))
    
    word_tokens = word_tokenize(a)
    #print("type after tokenization",type(word_tokens))
    filtered_sentence = [w for w in word_tokens if not w in stop_words]
    #print("Words Tokenization:",word_tokens,"\n\n\n\n\n")
    #print("Tokens Post removing stop words :",filtered_sentence)
    #print("type foltered sentence",type(filtered_sentence))
    z1=[w for w in filtered_sentence if re.search('^BHUSHAN', w)]
    z2=[w for w in filtered_sentence if re.search('^Bhushan', w)]
    z3=[w for w in filtered_sentence if re.search('^bhushan', w)]
    z4=[w for w in filtered_sentence if re.search('^BHUSHAN$', w)]
    z5=[w for w in filtered_sentence if re.search('^Bhushan$', w)]
    z6=[w for w in filtered_sentence if re.search('^bhushan$', w)]
    z7=[w for w in filtered_sentence if re.search('^STEEL', w)]
    z8=[w for w in filtered_sentence if re.search('^Steel', w)]
    z9=[w for w in filtered_sentence if re.search('^steel', w)]
    z10=[w for w in filtered_sentence if re.search('^STEEL', w)]
    z11=[w for w in filtered_sentence if re.search('^Steel$', w)]
    z12=[w for w in filtered_sentence if re.search('^steel$', w)]
    z13=[w for w in filtered_sentence if re.search('^BHUSHANSTEEL', w)]
    z14=[w for w in filtered_sentence if re.search('^bhushansteel', w)]
    z15=[w for w in filtered_sentence if re.search('^BS', w)]
    z16=[w for w in filtered_sentence if re.search('^Bs', w)]
    z17=[w for w in filtered_sentence if re.search('^bs', w)]
    z18=[w for w in filtered_sentence if re.search('^BS$', w)]
    z19=[w for w in filtered_sentence if re.search('^Bs$', w)]
    z20=[w for w in filtered_sentence if re.search('^bs$', w)]
    z21=[w for w in filtered_sentence if re.search('^emi', w)]
    z22=[w for w in filtered_sentence if re.search('^EMI', w)]
    z23=[w for w in filtered_sentence if re.search('^Emi', w)]
    z24=[w for w in filtered_sentence if re.search('^emi$', w)]
    z25=[w for w in filtered_sentence if re.search('^EMI$', w)]
    z26=[w for w in filtered_sentence if re.search('^Emi$', w)]
    
    z27=[w for w in filtered_sentence if re.search('^HIGHEST', w)]
    z28=[w for w in filtered_sentence if re.search('^Highest', w)]
    z29=[w for w in filtered_sentence if re.search('^highest', w)]
    z30=[w for w in filtered_sentence if re.search('^HIGHEST$', w)]
    z31=[w for w in filtered_sentence if re.search('^Highest$', w)]
    z32=[w for w in filtered_sentence if re.search('^highest$', w)]
    z33=[w for w in filtered_sentence if re.search('^RETURN', w)]
    z34=[w for w in filtered_sentence if re.search('^Return', w)]
    z35=[w for w in filtered_sentence if re.search('^return', w)]
    z36=[w for w in filtered_sentence if re.search('^RETURN$', w)]
    z37=[w for w in filtered_sentence if re.search('^Return$', w)]
    z38=[w for w in filtered_sentence if re.search('^return$', w)]
    z39=[w for w in filtered_sentence if re.search('^INVESTMENT', w)]
    z40=[w for w in filtered_sentence if re.search('^Investment', w)]
    z41=[w for w in filtered_sentence if re.search('^investment', w)]
    z42=[w for w in filtered_sentence if re.search('^INVESTMENT$', w)]
    z43=[w for w in filtered_sentence if re.search('^Investment$', w)]
    z44=[w for w in filtered_sentence if re.search('^investment$', w)]
    z45=[w for w in filtered_sentence if re.search('^INVEST', w)]
    z46=[w for w in filtered_sentence if re.search('^Invest', w)]
    z47=[w for w in filtered_sentence if re.search('^invest', w)]
    z48=[w for w in filtered_sentence if re.search('^INVEST$', w)]
    z49=[w for w in filtered_sentence if re.search('^Invest$', w)]
    z50=[w for w in filtered_sentence if re.search('^invest$', w)]

########### Enable ##########

#   v,year1,year2 = BhushanSteel2011_2012()
    
    #v1,year3      = BhushanSteel2013()
    
   # v2,year4,year5= BhushanSteel2014_2015()
    
    #Violations=v+v1+v2

############# Enable ##############
    
    
        
     #   AssessmentBhushanSteel(Violations,year2,year1,year3,year5,year4)
        #end = datetime.datetime.now()
    #elif ( z21 or z22 or z23 or z24 or z25 or z26):
     #   Loan_EMI(z21)
      #  print("Enter correct name ")   
    
    #print("\n===Response Time:",end-start,"seconds")    
    ###### Response time #####    
    #while a!=


###########        NPA functions call   #####################    

    if (z1 or z2 or z3 or z4 or z5 or z6 or z7 or z8 or z9 or z10 or z11 or z12 or z13 or z14 or z15 or z16 or z17 or z18 or z19 or z20 or z21 or z22 or z23 or z24 or z25 or z26 ):
    
        start1=datetime.datetime.now()
        violation_2011,violation_2012,Quick_Ratio_2011,Quick_Ratio_2012,Absolute_Liquid_ratio_2011,Absolute_Liquid_ratio_2012,Debt_Equity_ratio_2011,Debt_Equity_ratio_2012,FY2011,FY2012,violation_2013,Quick_Ratio_2013,Absolute_Liquid_ratio_2013,Debt_Equity_ratio_2013,FY2013,violation_2014,violation_2015,Quick_Ratio_2014,Quick_Ratio_2015,Absolute_Liquid_ratio_2014,Absolute_Liquid_ratio_2015,Debt_Equity_ratio_2014,Debt_Equity_ratio_2015,FY2014,FY2015 = NPA_Input_analysis()

        TotalViolation,FY2011,FY2012,FY2013,FY2014,FY2015,Performance = Business_Logic_NPA(violation_2011,violation_2012,Quick_Ratio_2011,Quick_Ratio_2012,Absolute_Liquid_ratio_2011,Absolute_Liquid_ratio_2012,Debt_Equity_ratio_2011,Debt_Equity_ratio_2012,FY2011,FY2012,violation_2013,Quick_Ratio_2013,Absolute_Liquid_ratio_2013,Debt_Equity_ratio_2013,FY2013,violation_2014,violation_2015,Quick_Ratio_2014,Quick_Ratio_2015,Absolute_Liquid_ratio_2014,Absolute_Liquid_ratio_2015,Debt_Equity_ratio_2014,Debt_Equity_ratio_2015,FY2014,FY2015)        
        
    #print("total",end-start)
    
        if Performance == 0:
            Assessment_Norms_Violated(TotalViolation,FY2011,FY2012,FY2013,FY2014,FY2015)
            end1=datetime.datetime.now()
            #print("Total time",end1-start1 )
        elif Performance == 1:
            print("Not under investigation")

#########         INVESTMENT functions call        ###############    

    elif ( z27 or z28 or z29 or z30 or z31 or z32 or z33 or z34 or z35 or z36 or z37 or z38 or z39 or z40 or z41 or z42 or z43 or z44 or z45 or z46 or z47 or z48 or z49 or z50 ):
    
        start2=datetime.datetime.now()
    
        Svgs,intt,NE,emi,at,sal = Inv_Input_analysis() ### 16 functions ###
    
        url,Product,NAV = BusinessLogic_Inv(Svgs,intt,NE,emi,at,sal) 
 
        Investment(url,Product,NAV)
    
        end2=datetime.datetime.now()
        #print("total time",end2-start2)
        
    else:
        print("\nKindly enter the input as per Demo. More efficient less lines fast code is surely coming shortly!!!!")

#######             Main Funtion call         ######################

if __name__ == "__main__":

    main()

#######      Multi-Processing working ( few modifcations )   #####################
    
# Multi-Processing working ##    
# ===total response time for both investment + NPA = 33 seconds ==========================================================================
#    
#      start=datetime.datetime.now()
#     obj1=Process(target=testmain)
#     obj=Process(target=process2)
#     obj1.start()
#     obj.start()
#     print("child alive ID:",obj.pid,obj.is_alive())
#     print("main alive ID:",obj1.pid,obj1.is_alive())
# 
#     obj1.join()
#     obj.join()
# =============================================================================
    #print("p:",obj1.pid)
    #obj.join()
    #end=datetime.datetime.now()
    #print("t:",end-start)
    #print("childtest",os.getpid())

    
    #ifobj1.is_alive()
    #start=datetime.datetime.now()
    #obj=Process(target=process2)
    #obj1.join()
    #end=datetime.datetime.now()
    #print("t:",end-start)
        
            #print ("Parent Time:",end-start)
        #print("main process ID:",os.getppid())
    
        #Investment()
                
        #if( d3a.hour >= 8 ) and ( d3a.hour <= 18 ):
         #   off_on_mode=1
          #  print("online",d3a.hour)
        #Investment()
# =============================================================================
  
       
# =============================================================================
# =============================================================================
# =============================================================================
           
            
       #print("time",end-start)
       
        #elif( d3a.hour > 18 ) and (d3a.hour < 8 ):
         #   off_on_mode=0 
          #  print("\noffline",d3a.hour)
           # Investment(off_on_mode)
    #stop = datetime.datetime.now()
    #stop-start

    #print("Processing Time",stop-start,"seconds")
    ######## Response time #########
    
    #print("violations",TV)
    #print("\nyears",y2,y1,y3,y5,y4)
    
    #print("violation:",a)
    #print("\ndate 2012",b)
    #print("\n date 2011",c)


#is_alive()
#exitcode -None is not yet terminated
    
    #print("childtest",os.getpid())

    

    


    

# =============================================================================
#     start=datetime.datetime.now()
#     obj=Process(target=test)
#     obj.start()
#     print("pid",obj.pid)
#     obj.join()
#     end=datetime.datetime.now()
#     print("paralleltime:",end-start)
# =============================================================================

# =============================================================================
#     start=datetime.datetime.now()
#     test()
#     end=datetime.datetime.now()
#     print("originaltime:",end-start)
#     print("main:",os.getpid())
# 

    






            
 