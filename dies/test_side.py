from dies import Die


firs_die = Die()

for i in range(10):
    print(str(i + 1) + ")", firs_die.roll_side())
print()

second_die = Die(10)

for i in range(10):
    print(str(i + 1) + ")", second_die.roll_side())
print()

die_20 = Die(20)

for i in range(10):
    print(str(i + 1) + ")", die_20.roll_side())
print()
