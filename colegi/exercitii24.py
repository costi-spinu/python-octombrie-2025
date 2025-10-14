# # task1
import math

a = float(input("DA MI UN NR: "))
try:
    if a < 0:
        raise ValueError
    print(math.sqrt(a))
except ValueError:
    print("wrong number cause it can not have an squae root")
    exit

# # task2
import math

a = float(input("DA MI UN NR: "))


def square_root(a) -> int:
    try:
        if a < 0:
            raise ValueError
        return math.sqrt(a)
    except ValueError:
        print("wrong number cause it can not have an squae root")
        return


f = square_root(a)
print(f)

# task 3
a = dict()
n = int(input("da mi marime baza de date: "))
for i in range(n):
    key = input("da mi cheia")
    value = input("da mi valoarea")
    a.update({key: value})
print(a)


def dictionaire(n: int, a: dict):
    print("1. Display dictionary")
    print("2. Search for a value")
    print("3. Replace a value (by key)")
    print("4. Display a value (by key)")
    print("5. Delete a value (by key)")
    print("6. Exit")
    option = input("da mi optiunea pe care o vrei")
    match option:
        case 1:
            print("dictionarul este {}".format(a))
        case 2:
            k = input("da mi valoarea pe care vrei sa o cauti: ")
            try:
                for key, value in a.items():
                    if key == k:
                        print("value of the {} key is {}".format(k, a[k]))
                    elif value == k:
                        print("the key for this velue is {}".format(a.keys(k)))
                    else:
                        raise ValueError
            except ValueError as e:
                print("aveti aceasta eroare {} datorita valorii gresite".format(e))
        case 5:
            try:
                if key in a:
                    del a[key]
            except:
                print("Value not found")
        case 4:
            val = input("da mi val dorita")
            try:
                print(a.get(val))
            except:
                print("key not found")
        case 3:
            try:
                val = input("da mi noua val")
                key = input("da mi cheia cautata: ")
                if key in a.keys():
                    a[key] = val
                else:
                    raise ValueError
            except ValueError:
                print("val nepotrivita")
