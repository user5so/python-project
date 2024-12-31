# --> pandas library for working with CSVs and dataframes
# --> pyplot module from matplotlib library to plot graphs
# --> colored module from termcolor library to print colored text

import pandas as pd
import matplotlib.pyplot as mp
from colorist import hex, bg_hex

#  First, let's make our interface more appealing by adding a header and formatting for all menus

#  Adding header
def header_style():
  print('')
  hex("꒷꒦︶꒷꒦︶ ๋ ࣭ ⭑꒷꒦"*2 + '----> ' +" 𝗖 𝗢 𝗩 𝗜 𝗗 - 𝟭 𝟵 :  𝗜 𝗠 𝗣 𝗔 𝗖 𝗧 𝗦  𝗢 𝗡  𝗧 𝗛 𝗘  𝗪 𝗢 𝗥 𝗟 𝗗  𝗩 𝗦  𝗜 𝗡 𝗗 𝗜 𝗔 " + '<---' + "꒷꒦︶꒷꒦︶ ๋ ࣭ ⭑꒷꒦"*2, "#ff3333")
  print('')
  hex("desc", '#334cff')
      
#  Displaying what options we offer
def options():
  print("")
  print("-ˋˏ✄┈┈┈┈")
  hex("Table of Contents", "FFFFFF")
  hex(" ╰┈➤ " + "Digital Growth          --> 1", '#f700ff')
  hex(" ╰┈➤ " + "Digitalization          --> 2", '#f700ff')
  hex(" ╰┈➤ " + "Dropout                 --> 3", '#f700ff')
  hex(" ╰┈➤ " + "Ecommerce Growth        --> 4", '#f700ff')
  hex(" ╰┈➤ " + "Education Spending      --> 5", '#f700ff')
  hex(" ╰┈➤ " + "Education Trends        --> 6", '#f700ff')
  hex(" ╰┈➤ " + "Global Inequality       --> 7", '#f700ff')
  hex(" ╰┈➤ " + "Healthcare Expenditure  --> 8", '#f700ff')
  hex(" ╰┈➤ " + "Tourism Revenue         --> 9", '#f700ff')
  hex(" ╰┈➤ " + "Unemployment Rate       --> 10", '#f700ff')
  hex(" ╰┈➤ " + "Vaccine Coverage        --> 11", '#f700ff')
  hex(" ╰┈➤ " + "Exit                    --> 12", '#f700ff')
  print("-ˋˏ✄┈┈┈┈")

def selection():
    while True:
      print('')
      hex("Please select the number corresponding to one of the aforementioned options: ", '#3756ff')
      a=input()
      if not a.isdigit():
        hex("Oops! Choice cannot be accepted!", '#ff0000')
        hex("Please select the number corresponding to one of the following options: ", '#3756ff')
        options()
      elif int(a)<1 or int(a)>12:
        hex("Oops! Choice cannot be accepted!", '#ff0000')
        hex("Please select the number corresponding to one of the following options: ", '#3756ff')
        options()
      else:
            return(a)
    
#  Setting formatting for each menu
def page_style(heading):
  print('')
  hex("\n"+"─── ⋆⋅☆⋅⋆ ──" + " 「 ✦ " + heading + " ✦ 」" + "─── ⋆⋅☆⋅⋆ ──"+"\n", '#d41c94')
  print('')

#  Fine shyt
#  Main program
def main():
  header_style()
  options()
  selection()
  
if __name__ == "__main__":
    main() 
