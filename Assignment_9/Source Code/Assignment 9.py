import csv

calender = {
        '1':'January',
        '2':'February',
        '3':'March',
        '4':'April',
        '5':'May',
        '6':'June',
        '7':'July',
        '8':'August',
        '9':'September',
        '10':'October',
        '11':'November',
        '12':'December'
    }

def read_in_file(filename: str):
  file = open(filename, encoding="utf-8")
  csv_file = csv.reader(file)
  lst = list(csv_file)
  file.close()
  return lst

def month_from_number(month: int):
  if month not in range(1, 13):
    raise ValueError('Month must be 1-12')
  return calender[month]

def create_reported_date_dict(file_lst: list):
  result = {}
  for line in file_lst[1:]:
    date = line[1].strip()
    result[date] = result.get(date, 0) + 1
  return result

def create_reported_month_dict(file_lst: list):
  result = {}
  for line in file_lst[1:]:
    month = int(line[1].split('/')[0].strip())
    result[month] = result.get(month, 0) + 1
  return result

def create_offense_dict(file_lst: list):
#not finished
def create_offense_by_zip(file_lst: list):
#not finished

if __name__ == "__main__":
  invalid_file = True
  while invalid_file:
    try:
      file_name = input('Enter the name of the crime data file ==> ')
      lst = read_in_file(file_name)
      invalid_file = False
    except FileNotFoundError:
      print('Could not find the file specified. {} not found'.format(file_name))

  print()
  months = create_reported_month_dict(lst)
  print(month)
  mx = max(month,key=month.get)
  print("The month with the highest # of crimes is "+month_from_number(mx)+" with "+str(month[mx])+" offenses")

  offenses = create_offense_dict(lst)
  mx = max(offense,key=offense.get)
  print("The offense with the highest # of crimes is "+mx+" with "+str(offense[mx])+" offenses")
  offense_by_zip = create_offense_by_zip(lst)
  print()
  
  invalid_key = True
  while invalid_key:
    offense_key = input('Enter and offense: ')
    if offense_key in offense_by_zip:
      invalid_key = False
    else:
      print('Not a valid offense found, please try again')
  
  print()
  print('{} offenses by Zip Code'.format(offense_key))
  print('{:20}{:10}'.format('Zip Code', '# Offenses'))
  print('='*30)
  for key, value in offense_by_zip[offense_key].items():
    print('{:<20}{:>10}'.format(key, value))
