
def table():
    print('| Allocation | Max | Available | Need |')
    for j in range(10):
        for i in range(39):
            if(i==0 or i==13 or i==19 or i==31 or i==38):
                print('|', end='')
            else:
                print(' ',end='')
        print('')

def main():
    table()
main()