from tasks.task_1 import *
from tasks.task_2 import *
from tasks.task_3 import *
from tasks.task_4 import *
from tasks.task_5 import *
from tasks.task_6 import *
from tasks.task_7 import *
from tasks.task_8 import *
from tasks.task_9 import *
from tasks.task_10 import *
from tasks.task_11 import *
from tasks.task_12 import *
from tasks.task_13 import *
from tasks.task_14 import *
from tasks.task_15 import *
from tasks.task_16 import *

print("введіть який номер:")
task = int(input())
print("\n")

match task:
    case 1:
        print(calculateRectArea(1,2))
        print(calculateRectSum(1,2))
    case 2:
        print(geom(1,2))
    case 3:
        print(calculRectArea(-4, 3, 3, -2))
        print(calculRectSum(-4, 3, 3, -2))
    case 4:
        print(calcPairNumbers(4))
    case 5:
        print(calc5a(1,2,3))
        print(calc5b(5,-2,-3))
        print(calc5c(-5,2,3))
    case 6:
        print(check_for_white(2, 3))

        for row in chess_board:
            print(" ".join(row))
    case 7:
        print(is_queen_move(3,5,6,2))
    case 8:
        solveTask8(1,6)
    case 9:
        get_reverse(32)
    case 10:
        print(solveTask10([1,2,3,4,5]))
    case 11:
        solveTask11(32)
    case 12:
        print(func(-4, 0.869, 1.276))
    case 13:
        print("Виберіть частину: ")
        abc = int(input())
        match abc:
            case 1:
                print(first13())
            case 2:
                print(second13())
            case 3:
                print(third13())
    case 14:
        solveTask14()
    case 15:
        task15()
    case 16:
        print(combined_string)
        print(multiplied_string)
        print(modified_string1)
        print(modified_string2)