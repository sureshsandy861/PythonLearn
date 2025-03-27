

def multiplier(x):
    def mulitiplicand(y):
        #print(str(x)+'x'+str(y)+'='+str(x*y))
        print(f"{x} x {y} = {x*y}")
    return mulitiplicand


tables = multiplier(int(input("Enter which tables:")))
for i in range(1,13):
        tables(i)
