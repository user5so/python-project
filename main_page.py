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
  print("-ˋˏ✄┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈")
  hex("Table of Contents", "FFFFFF")
  hex(" ╰┈➤ " + "Digital Growth                               --> 1", '#f700ff')
  hex(" ╰┈➤ " + "Digitalization                               --> 2", '#f700ff')
  hex(" ╰┈➤ " + "Dropout                                      --> 3", '#f700ff')
  hex(" ╰┈➤ " + "Ecommerce Growth                             --> 4", '#f700ff')
  hex(" ╰┈➤ " + "Education Spending                           --> 5", '#f700ff')
  hex(" ╰┈➤ " + "Education Trends                             --> 6", '#f700ff')
  hex(" ╰┈➤ " + "GDP                                          --> 7", '#f700ff')
  hex(" ╰┈➤ " + "Global Inequality                            --> 8", '#f700ff')
  hex(" ╰┈➤ " + "Healthcare Expenditure                       --> 9", '#f700ff')
  hex(" ╰┈➤ " + "Tourism Revenue                              --> 10", '#f700ff')
  hex(" ╰┈➤ " + "Unemployment Rate                            --> 11", '#f700ff')
  hex(" ╰┈➤ " + "Vaccine Coverage                             --> 12", '#f700ff')
  hex(" ╰┈➤ " + "Exit                                         --> 13", '#f700ff')
  print("-ˋˏ✄┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈")

def selection():
    while True:
      print('')
      hex("Please select the number corresponding to one of the aforementioned options: ", '#3756ff')
      a=input()
      if not a.isdigit():
        hex("Oops! Choice cannot be accepted!", '#ff0000')
        hex("Please select the number corresponding to one of the following options: ", '#3756ff')
        options()
      elif int(a)<1 or int(a)>13:
        hex("Oops! Choice cannot be accepted!", '#ff0000')
        hex("Please select the number corresponding to one of the following options: ", '#3756ff')
        options()
      else:
            return(int(a))


# Information
def return_values(heading, desc, df, sub_opt, opt_no, x, y, title):
  print('')
  hex("\n"+"─── ⋆⋅☆⋅⋆ ──"*3 + " 「 ✦ " + heading + " ✦ 」" + "─── ⋆⋅☆⋅⋆ ──"*3 +"\n", '#d41c94')
  print('')
  hex(desc, '#3756ff')
  print('')
  print(df)
  if sub_opt == 'y' or sub_opt == 'Y':
    print('')
    hex('This category has sub-options. Do you want to view sub-options? (select y/n)', '#ff8937')
    while True:
      i=input()
      if i == 'y' or i == 'Y':
        hex('Selected Yes!', '#00da17')
        hex(opt_no, '#ce7eff')
        break
      elif i == 'n' or i == 'N':
        hex('Selcted No!', '#ed2e2e')
        break
      else:
        hex('Not a valid option. Please select (y/n)', '#ff8937')
  else:
    print('')
  while True:
    hex('Do you want to view graphs for this dataset? (select y/n)', '#ff8937')
    j=input()
    if j == 'y' or j == 'Y':
      hex('Selected Yes!', '#00da17')
      print('')
      hex('Which type of graph do you want to see?', '#3756ff')
      print("-ˋˏ✄┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈")
      hex(' ╰┈➤ Bar                                            --> b/B', '#f700ff')
      hex(' ╰┈➤ Line                                           --> l/L', '#f700ff')
      hex(' ╰┈➤ Horizontal Bar                                 --> o/O', '#f700ff')
      hex(' ╰┈➤ Histogram                                      --> h/H', '#f700ff')
      print("-ˋˏ✄┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈")
      graph_kind=input()
     
      try:
        hex(' ╰┈➤ Displaying the requested graph: -', "#ff82db")
        graph(df, graph_kind, x, y, title)
      except Exception as e:
        hex('An error occured', '#ed2e2e')
      break
    elif j == 'n' or j == 'N':
      hex('Selected No!', '#ed2e2e')
      break
    else:
      hex('Not a valid option. Please select (y/n)', '#ff8937')


# Function for plotting graphs
def graph(df, graph_kind, x, y, title):
  try:
    if graph_kind == 'b' or graph_kind == 'B':
      mp.bar(df[x], df[y], color = '#dd1a1a', edgecolor = '#dd1a1a')
      mp.xlabel(x)
      mp.ylabel(y)
      mp.title(title)
    elif graph_kind == 'l' or graph_kind == 'L':
      mp.plot(df[x], df[y], color = '#1acedd', marker = '$\u2665$', markerfacecolor = 'w', markersize = 7)
      mp.xlabel(x)
      mp.ylabel(y)
      mp.title(title)
    elif graph_kind == 'o' or graph_kind == 'O' or graph_kind == '0' or graph_kind == 0:
      mp.barh(df[x], df[y], color='#8d6df9', edgecolor = '#8d6df9')
      mp.xlabel(x)
      mp.ylabel(y)
      mp.title(title)
    elif graph_kind == 'h' or graph_kind == 'H':
      mp.hist(df[x], df[y], color='#53d572')
      mp.xlabel(x)
      mp.ylabel(y)
      mp.title(title)
    mp.show()
  except Exception as e:
    hex('An error occured.', '#ff8937')
    

#  Setting formatting for each menu
def menu_style(heading):
  print('')
  hex("\n"+"─── ⋆⋅☆⋅⋆ ──" + " 「 ✦ " + heading + " ✦ 」" + "─── ⋆⋅☆⋅⋆ ──"+"\n", '#d41c94')
  print('')


#  Main program
def main():
  header_style()
  while True:
    options()
    selection()
    if a == 1:
      return_values('hed'
                    ,'desc'
                    , pd.read_csv(r'C:\Users\pingpong\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Python 3.12\Digital_Growth_Rates_India_vs_World.csv')
                    , 'y'
                    , 'opt'
                    , 'Year'
                    , 'India_Digital_Growth_Rate (%)'
                    , 'lallu')
    elif a == 2:
      return_values('hed2'
                    , 'desc'
                    , pd.read_csv(r'')
                    , 'y'
                    , 'opt'
                    , 'Year'
                    , ''
                    , 'lullu')
    elif a == 3:
      return_values()
  
  
  
if __name__ == "__main__":
    main()
