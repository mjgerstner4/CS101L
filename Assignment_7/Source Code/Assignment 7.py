def get_min_mpg():
    while True:
        try:
            mpg = float(input('Enter the minimum mpg ==> '))
            if mpg <= 0:
                print('Fuel economy given must be greater than 0')
            elif mpg > 100:
                print('Fuel economy given must be less than 100')
            else:
                return mpg
        except ValueError:
            print('You must enter a number for the fuel economy')

def open_file(prompt, mode="r"):
    while True:
        try:
            filename = input(prompt)
            file = open(filename, mode)
            return file
        except FileNotFoundError:
            print('Could not open file', filename)
        except IOError:
            print('There is an IO Error', filename)

mpg = get_min_mpg()
print()
file = open_file('Enter the name of the input vehicle file ==> ')
file.readline()
print()

output_file = open_file('Enter the name of the file to output to ==> ', 'w')
for line in file:
  values = line.split('\t')
  try:
    combined = float(values[7])
    if combined >= mpg:
      output_str = "{:<5}{:<20} {:<40}{:>10.3f}".format(values[0], values[1], values[2], combined)
      output_file.write(output_str+'\n')
  except ValueError:
    print("Could not convert value invalid for vehicle", values[7], values[0],values[1], values[2])

file.close()
output_file.close()