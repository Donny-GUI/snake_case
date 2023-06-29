# snake_case
Converts Pascal case and Camel case to snake case. Can identify when some things should be Uppercase. For example, PY3FunctionCase is PY3_function_case.



# Examples

```Python3
from snakecase import *

insane_case = "addTacoToBell"
snake = LinkedSnake(insane_case)
snakecase = snake.snakecase()
print(snakecase)  # add_taco_to_bell


what = "TESTthisOutForGood"
snake = LinkedSnake(what)
snakecase = snake.snakecase()
print(snakecase) # TEST_this_out_for_good

test = "fOURTHtest"
snake = LinkedSnake(test)
snakecase = snake.snakecase()
print(snakecase) # f_OURTH_test

bill_gates = "BillGates"
snake = LinkedSnake(bill_gates)
snakecase = snake.snakecase()
print(snakecase) # bill_gates


```
