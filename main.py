import pyinputplus as pyip
from replit import db
import os
import random
import time

ply = "y"

while ply == "y":
  print("\033[34mRandom Number Game\033[0m\n")
  time.sleep(0.6)
  ply_g = input("\033[33m1. Guess the Number (This Mode Has a Leaderboard That Ends Every Season)\n2. Let the Computer Guess Your Number \n3. See the All-Time Leaderboard\n4. Delete an Existing Account\n5. Exit Application\n\n> ").strip().lower()
  print("\033[0m")

  if ply_g != "1" and ply_g != "2" and ply_g != "3" and ply_g != "4" and ply_g != "5" and ply_g != "db":
    print("\n\033[31m\nInvalid Input.\033[0m\n\nplease try again")
    time.sleep(1)
    os.system("clear")
    continue

  while ply_g == "1":
    menu = input("\n\033[33m\n1. Play\n2. See the Leaderboard\n3. Exit\n\n> ")
    if menu == "1":
      player = input("\n\033[32mInput Name: \033[0m").strip().capitalize()
      
      if "Hannu" and "poo" in player or "Hannu" and "stinky" in player or "Hannu" and "smelly" in player:
        exit("\033[31mINVALID INPUT.\nOFFENCE TO THE GRAND CREATOR OF THE GAME\nTEMINATING PROGRAM\033[0m")
  
      else:
        if player not in db['users'].keys():
          s = input("\033[32mAre you sure? (y/n) \033[0m").strip().lower()
  
          if s == "y":
            print("\n\n\033[33mNew Account Registered!\033[0m\n\n")
            db['users'][player] = 100
            high = 100
  
          else:
            time.sleep(0.5)
            os.system("clear")
            continue
            
      if db['users'] and db['users'].get(player) is not None and db['users'].get(player) == 100:
        print("\n\033[33mYour high score was automatically set to 100 attempts.\033[0m\n")
        high = 100
        
      else:
        print(f"\n\033[32myour current high score is {db['users'][player]}!\033[0m\n")
        high = int(db['users'][player])
  
  
      gme_atts = 0
  
      with open("leader.txt", "r") as f:
        leader = f.read().split("\n")
        leader.remove("")
        track = []
        for i in leader:
          n = i.split(" ")
          track.append(n[1])

        track.sort()

        for item in track:
          for i in leader:
            if item in i:
              del leader
              n = i.split(" ")
              leader = [n[0], n[1]]
              break

            else:
              continue

          break

      f.close()
  
      if leader:
        print(f"\033[33mThe current leader is {leader[0]}, with {leader[1]} attempts!\033[0m")
  
      else:
        print("\n\033[33mThere is no leader yet!\nYou are safe to take the title!\033[0m\n")
  
      time.sleep(4)
  
      for round in range(1, 4):
        g = []
        os.system("clear")
        print("\033[34mRandom Number Game\033[0m")
        time.sleep(0.32)
        print(f"\n\033[31mRound {round}\033[0m\n")
        time.sleep(0.3)
        attempt = 0
        rand = random.randint(1, 100)
  
        while True:
          gme_atts += 1
          attempt += 1
          num = pyip.inputNum("\033[32mGuess a number: \033[0m")
          
          if num in g:
            print(f"\n\033[31mYou already guessed {num}.\033[0m\n")
            time.sleep(1)
            os.system("clear")
            gme_atts -= 1
            attempt -= 1
            continue
  
          elif num > 100 or num < 1:
            print("\033[31mInvalid Input\033[0m\n")
            time.sleep(1)
            os.system("clear")
            gme_atts -= 1
            attempt -= 1
            continue
  
          elif num < rand:
            res = "Too low"
  
          elif num > rand:
            res = "Too high"
  
          else:
            break
  
          if num not in g:
            g.append(num)
    
          print(f"\n\033[31m{res}\033[0m")
          time.sleep(1)
          os.system("clear")
          print(num)
          print(f"\n\033[31m{res}\033[0m\n")
  
        print("\n\033[33mCorrect!\033[0m\n")
        print(f"\033[33mYou got it in {attempt} attempts!\033[0m")
        time.sleep(1.5)
  
      print(f"\n\033[33mYou played 3 rounds and ended with a total of {gme_atts} attempts!\033[0m\n")
  
      with open("leader.txt", "r") as f:
        board = f.read().split("\n")

        for i in board:
          if i == "" or player not in i:
            f.close()
            
            with open("leader.txt", "a+") as f:
              f.write(f"{player} {gme_atts}\n")
    
            f.close()
    
          elif player in board and gme_atts < int(board[board.index(player) + 1]):
            print("\n\033[33mYou have a new leaderboard high score!\033[0m\n")
            
            with open("leader.txt", "w") as f:
              f.write(i if i != f"{player} {gme_atts}" else f"{player} {gme_atts}\n")
    
            f.close()
            
      f.close()
      
      if gme_atts < high:
        print("\n\033[33mYou have a new high score!\033[0m\n")
        db['users'][player] = gme_atts
  
      elif gme_atts == high:
        print("\033[33mYou are tied with your current high score!\033[0m\n")
  
      gme_avg = gme_atts / 3
      print(f"\033[33mYou got an average of {gme_atts//3} (rounded) attempts per round!\033[0m\n")
      rnd = input("\033[35mwould you like to see the non-rounded average? (y/n): \033[0m").strip().lower()
  
      if rnd == "y":
        print(f"\n\033[33mYou got an unrounded average of {gme_avg} attempts per round!\033[0m")
  
      ply = input("\n\033[34mWould you like to play again? (y/n): \033[0m").strip().lower()
      time.sleep(0.7)
      os.system("clear")
  
      if ply == "n":
        exit("\n\033[33mThanks for playing!\033[0m")
  
      elif ply == "y":
        break

    elif menu == "2":
      time.sleep(1)
      os.system("clear")

      with open("leader.txt", "r") as f:
        scores = f.read()
        print("\033[33mLeaderboard\n".center(150))
        score = scores.split("\n")
        counter = 1
        tracker = []

        for i in score:
          n = i.split(" ")
          if n != ['']:
            tracker.append(n[1])

          else:
            continue

        tracker.sort()

        track = []
        
        for i in tracker:
          for item in score:
            iitem = item.split(" ")
            if iitem == ['']:
              break
              
            elif i == iitem[1]:
              if iitem[0] not in track:
                print(f"{counter}. {iitem[0]}: {iitem[1]}\n".center(145))
                counter += 1
                track.append(iitem[0])

              else:
                continue

            else:
              continue

        print("\033[0m")

      f.close()
      input()
      os.system("clear")

    elif menu == "3":
      time.sleep(1)
      os.system("clear")
      break

    else:
      print("\n\033[31mInvalid Input.\033[0m\n\nplease try again")
      time.sleep(1)
      os.system("clear")
      continue

  while ply_g == "2":
    gme_atts = 0
    list_num = -1

    def list_debg(list_num, g):
      while True:
        if list_num > len(g) - 1:
          while list_num > len(g) - 1:
            list_num -= 1

        elif list_num < len(g) - 1:
          while list_num < len(g) - 1:
            list_num += 1

        else:
          break

    for round in range(1, 4):
      g = []
      time.sleep(0.5)
      os.system("clear")
      print(f"\033[31mRound {round}\033[0m\n")
      time.sleep(0.5)
      attempt = 0
      enter = pyip.inputNum("\033[33mInput a random number between 1 and 100 for the computer to guess: \033[0m")

      if enter < 1 or enter > 100:
        print("\033[31mInvalid Input.\nPlease try again\033[0m")
        round -= 1
        continue
      time.sleep(0.6)
      num1 = 1
      num2 = 100
      guess = None
      co = False

      while True:
        attempt += 1
        gme_atts += 1
        guess = guess if co else random.randint(min(num1, num2), max(num1, num2))
        co = False

        try:
          if guess == g[list_num] and list_num > 0:
            num1 += 1
            num2 -= 1
            co = True
            continue
            
        except IndexError:
          list_debg(list_num, g)

        rand = input(f"\n\033[36mis the number {guess}? (y/n)\033[0m ").strip().lower()
        time.sleep(0.6)

        if rand == "y":
          print(f"\n\033[34mThe computer guessed your number in {attempt} attempts!\033[0m")
          time.sleep(1.5)
          os.system("clear")
          break

        elif rand == "n":
          g.append(guess)
          list_num += 1

          if num1 == enter + 1 and num2 == enter - 1:
            num1 += 1
            num2 -= 1

        else:
          print("Invalid input.\nPlease try again.\n")
          attempt -= 1
          gme_atts -= 1
          g.remove(list_num)
          list_num -= 1
          co = True
          continue

        is_hl = input("\n\033[32mis it higher or lower? (h/l)\033[0m ").strip().lower()
        time.sleep(1)
        os.system("clear")

        try:
          if is_hl == "h":
            num1 = g[list_num]
            list_debg(list_num, g)

          elif is_hl == "l":
            num2 = g[list_num]
            list_debg(list_num, g)           

          elif is_hl != "l" and is_hl != "h":
            print("\033[31mInvalid Input.\033[0m\nPlease try again.\n")
            attempt -= 1
            gme_atts -= 1
            g.remove(list_num)
            list_num -= 1
            time.sleep(1)
            os.system("clear")
            co = True
            continue

        except IndexError:
          list_debg(list_num, g)

        try:
          if g[list_num] == g[list_num-1]:
            if num1 == g[list_num] and num1 == g[list_num-1]:
              num1 += 1

            elif num2 == g[list_num] and num2 == g[list_num-1]:    
              num2 -= 1

            else:
              num1 += 1
              num2 -= 1

        except IndexError:
          list_debg(list_num, g)

    print(f"\033[33mThe computer played 3 rounds and ended with a total of {gme_atts} attempts!\033[0m\n")
    print(f"\033[33mThe computer got an average of {gme_atts // 3} (rounded) attempts per round!\033[0m\n")
    if gme_atts % 3 != 0:
      rnd = input("\033[35mwould you like to see the non-rounded average? (y/n): \033[0m").strip().lower()

      if rnd == "y":
        print(f"\n\033[33mThe computer got an unrounded average of {gme_atts / 3} attempts per round!\033[0m\n")

    ply = input("\n\033[34mWould you like to play again? (y/n): \033[0m").strip().lower()
    time.sleep(0.7)
    os.system("clear")

    if ply == "n":
      exit("\n\033[33mThanks for playing!\033[0m")

    elif ply == "y":
      break

  if ply_g == "3":
    time.sleep(1)
    os.system("clear")
    list = []
    print("\033[33mLeaderboard\n".center(150))

    for value in db['users'].values():
      list.append(value)

    list.sort()
    counter = 1
    llist = []
    for item in list:
      for key, value in db['users'].items():
        if value == item:
          if key not in llist:
            print(f"{counter}. {key}: {value}\n".center(145))
            llist.append(key)
            counter += 1

          else:
            continue
    
        else:
          continue

    print("\033[0m")
      

    input()
    os.system("clear")

  elif ply_g == "4":
    time.sleep(1)
    os.system("clear")
    acc = input("What account do you want to delete? ").strip().capitalize()
    
    if acc in db['users']:
      s = input("\nAre you sure? (y/n) ").strip().lower()

      if s == "y":
        del db['users'][acc]
        print(f"\n\033[33m{acc} has been deleted.\033[0m")
        time.sleep(1)
        os.system("clear")
        
        with open("leader.txt", "r") as file:
          user = file.read().split("\n")
          
          for u in user:
            f = u.split(" ")
            
            if f[0] == acc:
              user.remove(u)
              file.close()
              
              with open("leader.txt", "w") as file:
                file.write("\n".join(user))

              file.close()
              break
              
            else:
              file.close()

      else:
        time.sleep(1)
        os.system("clear")
        continue

    else:
      print("\033[31mInvalid Input.\033[0m\nPlease try again.\n")
      time.sleep(1)
      os.system("clear")
      continue

  elif ply_g == "5":
    time.sleep(1)
    os.system("clear")
    exit("\033[32mThanks for playing!\033[0m")
    
  elif ply_g == "db":
    time.sleep(1)
    os.system("clear")
    print(db['users'])
    input()
    time.sleep(0)
    os.system("clear")
    continue
    