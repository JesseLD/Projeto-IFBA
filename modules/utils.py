from datetime import date,datetime
import os


def getFormattedDate():
   nowDate = date.today()
   return(f'[{nowDate.strftime("%d|%m|%y")}]')

def getFormattedHours():
   nowDate = datetime.now()
   return(f'[{nowDate.strftime("%H:%M")}]')


def dateSuffix():
   return(f" {getFormattedDate()}-{getFormattedHours()}")


def clear():
   os.system('cls')

def next():
   return input('Pressione qualquer tecla para continuar!')