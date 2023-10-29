#предположим, у нас есть так называемая «нечестная» монетка, где орёл (H, «heads») и решка (T, «tails») выпадают не с вероятностью ½, как положено, а по-другому: орёл с вероятностью p (H) = 0,2, а решка, соответственно, p (T) = 0,8.
import random


H_count = 0
for i in range(0,10000):
    new_flip = random.choices(['H', 'T'], weights=[0.2, 0.8])
    if new_flip == ['H']:  # внимание: функция choices возвращает список!
        H_count = H_count + 1

print (H_count)
