def insert_Sort(list):
    for i in range(1,len(list)):
        insert_left(list,i)

def insert_left(list,end):
    temp = list[end]
    i = end - 1
    while i >= 0 and temp < list[i]:
        list[i + 1] = list[i]
        i -= 1
    list[i + 1] = temp

if __name__ == "__main__":
    list = [3,2,1]
    insert_Sort(list)
    print(list)