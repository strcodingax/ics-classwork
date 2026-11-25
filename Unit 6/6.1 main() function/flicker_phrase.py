import os
import random
import time


def main():
  # Note: 100,000 iterations at 1 second each will take ~27.7 hours to finish.
  for i in range(100000):
    r = random.randrange(1, 6)

    # Write five if statements here.
    if r == 1:
      first()
    if r == 2:
      second()
    if r == 3:
      third()
    if r == 4:
      fourth()
    if r == 5:
      fifth()

    time.sleep(1)
    os.system("cls")

  print("I pledge allegiance to the flag.")


def first():
  print("I                               ")


def second():
  print("  pledge                        ")


def third():
  print("         allegiance             ")


def fourth():
  print("                    to the      ")


def fifth():
  print("                           flag.")


if __name__ == "__main__":
  main()
