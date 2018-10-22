a = 1
def fun(a):
    print("func_in",id(a))   # func_in 41322472
    a = 2
    print("re-point",id(a), id(2))   # re-point 41322448 41322448
print("func_out",id(a), id(1))  # func_out 41322472 41322472
fun(a)
print(a)  # 1