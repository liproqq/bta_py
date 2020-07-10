import itertools as it

dice_sides = range(1, 7)

two_die_roll = it.product(dice_sides, repeat=2)

sum_dice_sides = [sum(i) for i in two_die_roll]
sum_dice_sides.sort()

overview_rolls = {k: sum_dice_sides.count(k) for k in sum_dice_sides}

print(overview_rolls)
