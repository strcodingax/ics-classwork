import math

def gradient_calc(start:int ,end:int, step_number:int, current_step:int):
        return math.ceil(((start - end) / step_number) * current_step) 


print(f"{gradient_calc(751,380,10,4)}")