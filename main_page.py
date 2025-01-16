# --> pandas library for working with CSVs and dataframes
# --> pyplot module from matplotlib library to plot graphs
# --> colored module from termcolor library to print colored text


import pandas as pd
import matplotlib.pyplot as mp
from colorist import hex, bg_hex


# --> First, let's make our interface more appealing by adding a header and formatting for all menus Adding header
def header_style():
  print('')
  hex("─── ⋆⋅☆⋅⋆ ───── ⋆⋅☆⋅⋆ ───── ⋆⋅☆⋅⋆ ───── ⋆⋅☆⋅⋆ ──" + '> ' +" 𝗖 𝗢 𝗩 𝗜 𝗗 - 𝟭 𝟵 :  𝗜 𝗠 𝗣 𝗔 𝗖 𝗧 𝗦  𝗢 𝗡  𝗧 𝗛 𝗘  𝗪 𝗢 𝗥 𝗟 𝗗  𝗩 𝗦  𝗜 𝗡 𝗗 𝗜 𝗔 " +
      '<' + "─── ⋆⋅☆⋅⋆ ──*─── ⋆⋅☆⋅⋆ ───── ⋆⋅☆⋅⋆ ───── ⋆⋅☆⋅⋆ ──","#ff3333")
  print('')
  #hex("CoviStats: A comprehensive CLI tool for analyzing the global and India-specific impacts of COVID-19. This program provides users with real-time data, insightful visualizations, and statistical comparisons between the worldwide and Indian pandemic scenarios, helping to understand trends, and recovery patterns. Ideal for data enthusiasts, researchers, and analysts interested in exploring COVID-19's effects on a global scale.", '#334cff')


# --> Setting formatting for each menu
def menu_style(heading):
  print('')
  hex("\n"+"─── ⋆⋅☆⋅⋆ ──" + " 「 ✦ " + heading + " ✦ 」" + "─── ⋆⋅☆⋅⋆ ──"+"\n", '#d41c94')
  print('')


# --> Displaying what options we offer
def options():
  print("")
  print("-ˋˏ✄┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈")
  hex("Table of Contents", "FFFFFF")
  hex(" ╰┈➤ " + "Digital Growth                               --> 1", '#f700ff')
  hex(" ╰┈➤ " + "Digitalization                               --> 2", '#f700ff')
  hex(" ╰┈➤ " + "Dropout Rates                                --> 3", '#f700ff')
  hex(" ╰┈➤ " + "Ecommerce Growth                             --> 4", '#f700ff')
  hex(" ╰┈➤ " + "Education Spending                           --> 5", '#f700ff')
  hex(" ╰┈➤ " + "Education Trends                             --> 6", '#f700ff')
  hex(" ╰┈➤ " + "GDP                                          --> 7", '#f700ff')
  hex(" ╰┈➤ " + "Global Inequality                            --> 8", '#f700ff')
  hex(" ╰┈➤ " + "Healthcare Expenditure                       --> 9", '#f700ff')
  hex(" ╰┈➤ " + "Unemployment Rate                            --> 10", '#f700ff')
  hex(" ╰┈➤ " + "Vaccine Coverage                             --> 11", '#f700ff')
  hex(" ╰┈➤ " + "Exit                                         --> 12", '#f700ff')
  print("-ˋˏ✄┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈")


# --> Making a function for easier selection of given options
def selection():
    while True:
      print('')
      hex("Please select the number corresponding to one of the aforementioned options: ", '#3756ff')
      print('')
      a=input()
      if not a.isdigit():
        hex("Oops! Choice cannot be accepted!", '#ff0000')
        hex("Please select the number corresponding to one of the following options: ", '#3756ff')
        print('')
        options()
      elif int(a)<1 or int(a)>12:
        hex("Oops! Choice cannot be accepted!", '#ff0000')
        hex("Please select the number corresponding to one of the following options: ", '#3756ff')
        options()
      else:
        return(int(a))


# --> Creating a function for information that will be displayed on selection
def return_values(heading, desc, df, sub_opt, title, col1, col2):
  print('')
  hex("\n"+"─── ⋆⋅☆⋅⋆ ──"*3 + " 「 ✦ " + heading + " ✦ 」" + "─── ⋆⋅☆⋅⋆ ──"*3 +"\n", '#d41c94')
  print('')
  hex(desc, '#3756ff')
  print('')
  print(df)
  if sub_opt == 'y' or sub_opt == 'Y':
    print('')
    hex('This category has sub-options. Do you want to view sub-options? (select y/n)', '#ff8937')
    print('')
    while True:
      i=input()
      print('')
      if i == 'y' or i == 'Y':
        hex('Selected Yes!', '#00da17')
        print('')
        subs(df, col1, col2, title)
        break
      elif i == 'n' or i == 'N':
        hex('Selcted No!', '#ed2e2e')
        print('')
        break
      else:
        hex('Not a valid option. Please select (y/n)', '#ff8937')
        print('')
  else:
    print('')
  hex(' ╰┈➤ Displaying the comparison graph for requested dataset: -', "#ff82db")
  gmain(df, col1, col2)


# --> Function for plotting graphs
def graph(df, graph_kind, y, title):
    while True:
      if graph_kind == 'b' or graph_kind == 'B' or graph_kind == 'l' or graph_kind == 'L' or graph_kind == 'o' or graph_kind == 'O':
        hex(' ╰┈➤ Displaying the requested graph: -', "#ff82db")
        try:
          if graph_kind == 'b' or graph_kind == 'B':
            mp.bar(df['Year'], df[y], color = '#dd1a1a', edgecolor = '#dd1a1a')
            mp.xlabel('Year')
            mp.ylabel(y)
            mp.title(title)
          elif graph_kind == 'l' or graph_kind == 'L':
            mp.plot(df['Year'], df[y], color = '#1acedd', marker = '$\u2665$', markerfacecolor = 'w', markersize = 7)
            mp.xlabel('Year')
            mp.ylabel(y)
            mp.title(title)
          elif graph_kind == 'o' or graph_kind == 'O' or graph_kind == '0' or graph_kind == 0:
            mp.barh(df['Year'], df[y], color='#8d6df9', edgecolor = '#8d6df9')
            mp.xlabel('Year')
            mp.ylabel(y)
            mp.title(title)
          mp.show()
        except Exception as e:
          hex('An error occured.', '#ff8937')
      else:
        hex('Not a valid option.', '#ff8937')
      break


# --> Suboptions
def subs(df, col1, col2, title):
    while True:
        hex('Do you want to view dataset for:', '#3756ff')
        print("-ˋˏ✄┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈")
        hex(' ╰┈➤ Only India                                     --> i/I', '#f700ff')
        hex(' ╰┈➤ Only World                                     --> w/W', '#f700ff')
        print("-ˋˏ✄┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈")
        q=input()
        if q == 'i' or q == 'I' or q == 'w' or q == 'W':
            if q == 'W' or q == 'w':
                y=col2
                hex('View? (y/n)', '#3756ff')
                m = input()
                if m == 'y' or m == 'Y':
                    print(df[col2][:])
                    gchoice(df,y,title)
                elif m == 'n' or m == 'N':
                    hex('Selected No!', '#ed2e2e')
                else:
                    hex('Not a valid option. Please select (y/n)', '#ff8937')
            elif q == 'i' or q =='I':
                y=col1
                hex('View? (y/n)', '#3756ff')
                m = input()
                if m == 'y' or m == 'Y':
                    print(df[col1][:])
                    gchoice(df,y,title)
                elif m == 'n' or m == 'N':
                    hex('Selected No!', '#ed2e2e')
                else:
                    hex('Not a valid option. Please select (y/n)', '#ff8937')
            break
        else:
            hex('Not a valid option. Please select (w/i)', '#ff8937')

      
# --> Graph for either India or world
def gchoice(df,y,title):
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
          print("-ˋˏ✄┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈")
          graph_kind=input()
          while True:
              if graph_kind == 'b' or graph_kind == 'B' or graph_kind == 'l' or graph_kind == 'L' or graph_kind == 'o' or graph_kind == 'O':
                  hex(' ╰┈➤ Displaying the requested graph: -', "#ff82db")
                  graph(df, graph_kind, y, title)
                  break
              else:
                  hex('Not a valid option.', '#ff8937')
                  break
        elif j == 'n' or j == 'N':
          hex('Selected No!', '#ed2e2e')
          break
        else:
            hex('Not a valid option. Please select (y/n)', '#ff8937')


# --> Graph for comparison between India and the world
def gmain(df, col1, col2):
    a=df['Year'].tolist()
    b=df[col1].tolist()
    c=df[col2].tolist()
    mp.plot(a,b, color = '#ffc0de', label = 'India', marker = '$\u2665$')
    mp.plot(a,c, color = '#97fdee', label = 'World', marker = 'o')
    mp.legend()
    mp.show()


# --> Main program
def main():
  header_style()
  while True:
    options()
    a=selection()
    if a == 1:
      return_values('Digital Growth Rate (%)'
                    , 'Digital Growth: This option in CoviStats explores the rapid expansion of digital technologies and online platforms during and after the COVID-19 pandemic. Users can analyze data on the acceleration of digital adoption globally and in India, helping to understand the long-term impact of these shifts on economies and societies.'
                    , pd.read_csv(r'C:\Users\pingpong\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Python 3.12\Digital_Growth_Rates_India_vs_World.csv')
                    , 'y'
                    , 'Digital Growth Rate (%)'
                    , 'India_Digital_Growth_Rate (%)'
                    , 'World_Digital_Growth_Rate (%)')
    elif a == 2:
      return_values('Digitalization (%)'
                    , 'Digitalization: This option in CoviStats provides an analysis of how the COVID-19 pandemic accelerated digital transformation across the globe and in India. By comparing pre-pandemic and post-pandemic statistics, users can explore the profound shifts in digital engagement and how technology played a critical role in adapting to the challenges posed by the pandemic.Digitalization: This option in CoviStats provides an analysis of how the COVID-19 pandemic accelerated digital transformation across the globe and in India. By comparing pre-pandemic and post-pandemic statistics, users can explore the profound shifts in digital engagement and how technology played a critical role in adapting to the challenges posed by the pandemic.'
                    , pd.read_csv(r'C:\Users\pingpong\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Python 3.12\India_vs_World_Digitalization_1999_2024.csv')
                    , 'y'
                    , 'Digitalization (%)'
                    , 'India_Digitalization_Percentage'
                    , 'World_Digitalization_Percentage')
    elif a == 3:
        return_values('Dropout Rate (%)'
                      , 'Dropout Rates: This option in CoviStats examines the impact of the COVID-19 pandemic on education systems, focusing on the increase in student dropout rates globally and in India. Users can explore trends over time and assess the long-term effects on education outcomes and inequality.'
                      , pd.read_csv(r'C:\Users\pingpong\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Python 3.12\dropout_rate_india_vs_world_2001_2023.csv')
                      , 'y'
                      , 'Dropout Rate (%)'
                      , 'India_Dropout_Rate (%)'
                      , 'World_Dropout_Rate (%)')
    elif a == 4:
        return_values('E-commerce Growth Rate (%)'
                      , 'E-Commerce Growth Rate: This option in CoviStats analyzes the surge in e-commerce activity during and after the COVID-19 pandemic, both globally and in India. Users can explore key data points and trends, comparing pre-pandemic and post-pandemic e-commerce performance to understand the long-term shift in the retail industry.'
                      , pd.read_csv(r'C:\Users\pingpong\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Python 3.12\ECommerce_Growth_Rates_India_vs_World.csv')
                      , 'y'
                      , 'E-commerce Growth Rate (%)'
                      , 'India_E-Commerce_Growth_Rate (%)'
                      , 'World_E-Commerce_Growth_Rate (%)')
    elif a == 5:
        return_values('Education Spending'
                      , 'Education Spending: This option in CoviStats examines the financial impact of the COVID-19 pandemic on education systems worldwide and in India. Users can explore how the pandemic reshaped education budgets and investments, and assess the long-term implications for educational equity and quality.'
                      , pd.read_csv(r'C:\Users\pingpong\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Python 3.12\education_spending_india_vs_world_2001_2023.csv')
                      , 'y'
                      , 'Education Spending'
                      , 'India_Public_Spending_on_Education (% of GDP)'
                      , 'World_Public_Spending_on_Education (% of GDP)')
    elif a == 6:
        return_values('Primary Enrollment (%)'
                      , 'Primary Enrollment: This option in CoviStats explores the trends in primary school enrollment rates globally and in India, highlighting the impact of the COVID-19 pandemic on early education. Users can analyze data on enrollment increases or declines, and assess the broader implications for primary education systems and child development.'
                      , pd.read_csv(r'C:\Users\pingpong\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Python 3.12\India_vs_World_Primary_Enrollment_2001_2023.csv')
                      , 'y'
                      , 'Primary Enrollment (%)'
                      , 'India (%)'
                      , 'World (%)')
    elif a == 7:
        return_values('GDP growth (gross domestic product)'
                      , 'GDP Growth: This option in CoviStats provides an analysis of the impact of the COVID-19 pandemic on the economic growth of countries, with a particular focus on global and Indian GDP trends. Users can explore GDP growth rates over time.'
                      , pd.read_csv(r'C:\Users\pingpong\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Python 3.12\GDP india vs world sourced from IMF.csv')
                      , 'y'
                      , 'GDP growth (%)'
                      , 'Real GDP growth (Annual percent change)India'
                      , 'Real GDP growth (Annual percent change)World')
    elif a == 8:
        return_values('Poverty Rate (%)'
                      , 'This option in CoviStats analyzes the impact of the COVID-19 pandemic on poverty rates globally and in India. Users can explore changes in poverty statistics, understand the socio-economic effects of the pandemic, and assess the long-term challenges.'
                      , pd.read_csv(r'C:\Users\pingpong\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Python 3.12\Global_Inequality_India_vs_World.csv')
                      , 'y'
                      , 'Poverty Rate (%)'
                      , 'India_Poverty_Rate (%)'
                      , 'Global_Poverty_Rate (%)')
    elif a == 9:
        return_values('Healthcare Expenditure (% of GDP)'
                      , 'Healthcare Expenditure: This option in CoviStats examines the changes in healthcare spending during and after the COVID-19 pandemic, both globally and in India. Users can explore shifts in healthcare budgets, the prioritization of public health, and the long-term financial implications of the pandemic on healthcare systems worldwide.'
                      , pd.read_csv(r'C:\Users\pingpong\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Python 3.12\India_vs_World_Healthcare_Expenditure.csv')
                      , 'y'
                      , 'Healthcare Expenditure (% of GDP)'
                      , 'India (% of GDP)'
                      , 'World (% of GDP)')
    elif a == 10:
        return_values('Unemployment Rate (%)'
                      , 'Unemployment Rate: This option in CoviStats analyzes the impact of the COVID-19 pandemic on global and Indian unemployment rates. Users can explore trends in unemployment, examine the effects of government policies, and understand the broader economic and social consequences of the pandemic on workforce participation.'
                      , pd.read_csv(r'C:\Users\pingpong\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Python 3.12\India_vs_World_Unemployment_2001_2024.csv')
                      , 'y'
                      , 'Unemployment Rate (%)'
                      , 'India_Unemployment_Rate' 
                      , 'World_Unemployment_Rate')
    elif a == 11:
        return_values('Vaccine Coverage (%)'
                      , 'Vaccine Coverage: This option in CoviStats provides an in-depth analysis of COVID-19 vaccine distribution and coverage rates globally and in India. Users can assess the impact of vaccination efforts on pandemic control and public health outcomes.'
                      , pd.read_csv(r'C:\Users\pingpong\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Python 3.12\India_vs_World_Vaccine_Coverage_1999_2024.csv')
                      , 'y'
                      , 'Vaccine Coverage (%)'
                      , 'India_Vaccine_Coverage(%)'
                      , 'World_Vaccine_Coverage(%)')
    elif a == 12:
      hex('Exiting...! Thank you for using CoviStats!', '#00da17')
      break


# --> Finally it's time to run our program!!
if __name__ == "__main__":
    main()
