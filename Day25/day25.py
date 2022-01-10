# To continue, please consult the code grid in the manual.  Enter the code at row 2947, column 3029.


code = 20151125


number_of_rows = 1
number_of_columns = 1

while True:
  number_of_rows += 1

  col = 1
  row = number_of_rows
  while row > 0:
    code *= 252533
    code =  code % 33554393
    if row == 2947 and col == 3029:
      print(col, row, code)
      break
    col += 1
    row -= 1