from utils import Math
import utils
while True:
    selection = utils.select()
    if selection == 1:  # ascending order
        unsorted_list = []
        print("Keep typing numbers until you want to stop, then just type anything else.")
        while True:
            appending_num = input("-> ")
            try:
                appending_num = float(appending_num)
            except:
                pass
            if type(appending_num) != float:
                break
            if type(appending_num) == float:
                unsorted_list.append(appending_num)
        print(Math.ascending(Math(unsorted_list)))

    elif selection == 2:  # ascending order
        unsorted_list = []
        print("Keep typing numbers until you want to stop, then just type anything else.")
        while True:
            appending_num = input("-> ")
            try:
                appending_num = float(appending_num)
            except:
                pass
            if type(appending_num) != float:
                break
            if type(appending_num) == float:
                unsorted_list.append(appending_num)
        print(Math.descending(Math(unsorted_list)))
    
    # IMPORTANT NOTE
    # FOR CASE 1 & 2:
    # THERE IS A FUNCTION IN UTILS TO DO THIS, BUT IT IS FOR OTHER FUNCTIONS.
    # AS THIS IS FOR ENTERING, THE SAME FUNCTION WILL NOT WORK.

    elif selection == 3:  # square area
        a = utils.check_float("side-length")
        a = Math.Geometry.Square(a)
        print(a.Math.Geometry.Square.area())

    elif selection == 4:  # square perimeter
        a = utils.check_float("side-length")
        a = Math.Geometry.Square(a)
        print(a.Math.Geometry.Square.perimeter())

    elif selection == 5:  # rectangle area
        l = utils.check_float("l")
        b = utils.check_float("b")
        print(Math.Geometry.Rectangle.area(Math.Geometry.Rectangle(l, b)))
        
