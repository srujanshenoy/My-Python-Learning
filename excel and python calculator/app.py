import openpyxl as xl
from openpyxl.chart import Reference

# def outcell_to_sum(cell,incell,outcell):
#     pass




workbook = xl.load_workbook("excelsheet.xlsx")
sheet = workbook["Sheet1"]

operator_cell = sheet.cell(2, 2)
operator_cell = operator_cell.value

# define in_1
in_1 = sheet.cell(2, 1)
in_1 = in_1.value
in_1 = str(in_1)
in_1 = float(in_1)
# end

# define in_2
in_2 = sheet.cell(2, 3)
in_2 = in_2.value
in_2 = str(in_2)
in_2 = float(in_2)
# end

outcell = sheet.cell(2, 5)
if operator_cell == "+":
    sum_of_ins = in_1 + in_2
    outcell.value = sum_of_ins
elif operator_cell == "-":
    difference_of_ins = in_1 - in_2
    outcell.value = difference_of_ins
elif operator_cell.lower == "x":
    product_of_ins = in_1 * in_2
    outcell.value = product_of_ins
elif operator_cell == "/":
    if in_2 == 0:
        outcell.value = "Error: cannot divide by zero"
    quotient_of_ins = in_1 / in_2
# # elif in_1.__class__ == "str":
#     outcell.value = "kindly enter a different value for input 1"
# elif in_2.__class__ == "str":
#     outcell.value = "kindly enter a different value for input 2"
# elif in_1.__class__ == str &  in_2.__class__ == str:
#     outcell.value = "kindly enter a different value for input 1 and 2"

workbook.save("excelsheet.xlsx")

