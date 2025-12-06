nameuno = input("Enter person 1's name")
namedos = input("Enter person 2's name"
checking_word = nameuno + namedos

checking_word = checking_word.lower()

true_count = 0

tcount = checking_word.count("t")
rcount = checking_word.count("r")
ucount = checking_word.count("u")
ecount = checking_word.count("e")
total_true_count = tcount + rcount + ucount + ecount

lcount = checking_word.count("l")
ocount = checking_word.count("o")
vcount = checking_word.count("v")
total_love_count = lcount + ocount + vcount + ecount

Total =str(total_true_count) + str(total_love_count)
int_total = int(Total)

print("The Love Calculator is calculating your score..!")
if int_total < 10 or int_total > 90
  print(f"Your score is {int_total}, you go together like peanut butter and jelly!"
elif int_total > 40 and int_total < 50
  print(f"Your score is {int_total}, y'all are okay...")
else:
  print(f"Your score is {int_total}.")
