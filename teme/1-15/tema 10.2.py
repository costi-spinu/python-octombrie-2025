#  Task 2
# Print the multiplication table for all numbers from 1 to 10. For example:
# 1*1 = 1 1*2 = 2 ….. 1*10 = 10
# ..................................
# 10*1 = 10 10*2 = 20 …. 10*10 = 100


for i in range(1, 11):
    for j in range(1, 11):
        print(
            f"{i}*{j} = {i*j}", end="; "
        )  # am pus ; pentru citirea mai lizibila a textului printat in consola.
    print()
