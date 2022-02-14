# Zhouyuan Li Final Project

import pandas as pd
import numpy as np

f = open('Students.txt', 'r')       # if your file's name is not 'Students.txt', please replace the file's name to your file's name

lst = []
for line in f:
    strip_line = line.strip()
    line_lst = strip_line.split('\t')
    lst.append(line_lst)
f.close()

# split the list by data and header
lst_1 = lst.copy()
lst_1.pop(0)
data_lst = lst_1
header_lst = lst[0]

# creat data frame
df = pd.DataFrame(np.array(data_lst), columns=header_lst)

# creat summary report
df1 = df.copy()
df1 = df.groupby(by=['GradYear', 'DegreeProgram']).count().add_suffix('_Count').reset_index()

df2 = df1[['GradYear', 'DegreeProgram', 'ID_Count']]

yearlst = [lst_1[0][3]]
for i in range(len(lst_1)):
    if lst_1[i][3] not in yearlst:
        yearlst.append(lst_1[i][3])

ttl = []
for y in yearlst:
    ttlstu = 0
    for i in range(len(lst_1)):
        if lst_1[i][3] == y:
            ttlstu += 1
    ttl.append(ttlstu)

per = []
for y in range(len(yearlst)):
    for i in range(len(df2)):
        if df2.iloc[i]['GradYear'] == yearlst[y]:
            per.append(round(df2.at[i, 'ID_Count'] / ttl[y] * 100, 2))

df3 = df2.copy()
df3['Percentage %'] = per

def re_menu():
  while True:
    c = input('Do you want to back to the menu? (Y for yes, N for ending the program): ')
    if c == 'Y' or c == 'y':
      co = 0
      break
    elif c == 'N' or c == 'n':
      co = 55
      break
    else: 
      print('Invalid input, please re-enter')
      continue
  return co


def re_an():
  while True:
    ans = input('search one more time? (Y for yes, N for no): ')
    if ans == 'y' or ans == 'Y':
      an = 1
      break
    elif ans == 'n' or ans == 'N':
      an = 0
      break
    else:
      print('Invalid input, please re-enter\n')
      continue
  return an

while True:
  print('\n1. Display all student records')
  print('2. Display students whose last name begins with _____')
  print('3. Display all records for students whose graduating year is _____')
  print('4. Display summary report(s)')
  print('5. Quit\n')


  try:
    choice = int(input('Please enter your choice: '))
    if choice not in range(1, 6):
      print('Please enter a valid number\n')
      continue
  except:
    print('Please enter a valid number\n')
    continue
  

  if choice == 5:
    break


  if choice == 1:
    print(f'\n{df}')
    choice = re_menu()
  

  if choice == 2:
    while True:
      lstname = input('\nLast name begins with: ').lower()
      df_name = df.loc[df['Last'].str.lower().str.startswith(lstname)]
      if df_name.empty: print('No records found')
      else: print(df_name)
      an = re_an()
      if an == 1: continue
      if an == 0: break 
    choice = re_menu()
  

  if choice == 3:
    while True:
      grayear = input(f'\nGraduating year is {yearlst}: ')
      df_gy = df.loc[df['GradYear'] == grayear]
      if df_gy.empty:
        print('No records in this year or invalid input, please re-enter')
        continue
      else: 
        print(df_gy)
      an = re_an()
      if an == 1: continue
      if an == 0: break
    choice = re_menu()
  

  if choice == 4:
    while True:
      year = input(f"\nwhich year's report or reports from which year? {yearlst}: ")
      if year not in yearlst:
        print('No records in this year or invalid input, please re-enter')
        continue
      while True:
        try:
          sin = int(input(f'Enter 1 for getting summary reports since {year}, enter 2 for {year} summary report only: '))
          if sin not in [1, 2]:
            print('Invalid input, please re-enter\n')
            continue
          break
        except:
          print('Invalid input, please re-enter\n')
          continue   
      if sin == 1:
        for y in yearlst:
          if y >= year:
            print(f'Summary Report for {y}')
            print(df3.loc[df3['GradYear'].str.match(y)])
            print(f'Total number of students: {ttl[yearlst.index(y)]}\n')
      else:
          print(f'Summary Report for {year}')
          print(df3.loc[df3['GradYear'].str.match(year)])
          print(f'Total number of students: {ttl[yearlst.index(year)]}\n')
      an = re_an()
      if an == 1: continue
      if an == 0: break
    choice = re_menu()

  if choice == 0: continue
  if choice == 55: break

