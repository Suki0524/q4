import time
import datetime
import random
import threading
library = ["""During the first part of your life, you only become aware of happiness once you have lost it. Then an age comes, a second one, in which you already know, at the moment when you begin to experience true happiness, that you are, at the end of the day, going to lose it. When I met Belle, I understood that I had just entered this second age. I also understood that I hadn’t reached the third age, in which anticipation of the loss of happiness prevents you from living.""","""But just as I didn’t want to resent my kids, I also didn’t want to find myself too much in love with them. There are parents who don’t like to hear their little girl crying at night, at the vast approaching dark of sleep, and so in their torment think why not feed her a lollipop, and a few years later that kid’s got seven cavities and a pulled tooth. This is how we’ve arrived at the point where we give every kid on the team a trophy in the name of participation. I didn’t want to love my kids so much that I was blind to their shortcomings, limitations, and mediocre personalities, not to mention character flaws and criminal leanings. But I could, I thought, I could love a kid that much. A kid really could be everything, and that scared me. Because once a kid is everything, not only might you lose all perspective and start proudly displaying his participation trophies, you might also fear for that kid’s life every time he leaves your sight. I didn’t want to live in perpetual fear. People don’t recover from the death of a child. I knew I wouldn’t. I knew that having a kid would be my chance to improve upon my shitty childhood, that it would be a repudiation of my dad’s suicide and a celebration of life, but if that kid taught me how to love him, how to love, period, and then I lost him as I lost my dad, that would be it for me. I’d toss in the towel. Fuck it, fuck this world and all its heartbreak. I’d tell that to Connie, and she’d tell me that if that was how I felt I was already a slave to the fear, and good luck.""","""Everything failed to subdue me. Soon everything seemed dull: another sunrise, the lives of heroes, failing love, war, the discoveries people made about each other. The only thing that didn’t bore me, obviously enough, was how much money Tim Price made, and yet in its obviousness it did. There wasn’t a clear, identifiable emotion within me, except for greed and possibly, total disgust. I had all the characteristics of a human being–flesh, blood, skin, hair–but my depersonalization was so intense, had gone so deep, that the normal ability to feel compassion had been eradicated, the victim of a slow, purposeful erasure. I was simply imitating reality, a rough resemblance of a human being, with only a dim corner of my mind functioning. Something horrible was happening and yet I couldn’t figure out why–couldn’t put my finger on it. The only thing that calmed me was the satisfying sound of ice being dropped into a glass of J&B. Eventually I drowned the chow, which Evelyn didn’t miss; she didn’t even notice its absence, not even when I threw it in the walk-in freezer, wrapped in one of her sweaters from Bergdorf Goodman. We had to leave the Hamptons because I would find myself standing over our bed in the hours before dawn, with an ice pick gripped in my fist, waiting for Evelyn to open her eyes. At my suggestion, one morning over breakfast, she agreed, and on the last Sunday before Labor Day we returned to Manhattan by helicopter.""","""A secret always has a strengthening effect upon a newborn friendship, as does the shared impression than an external figure is to blame: the men of the Crown have become united less by their shared beliefs, we observe, than by their shared misgivings–which are, in the main, externally directed. In their analyses, variously made, of Alastair Lauderback, George Shepard, Lydia Wells, Francis Carver, Anna Wetherell, and Emery Staines, the Crown men have become more and more suggestive, despite the fact that nothing has been proven, no body has been tried, and no new information has come to light. Their beliefs have become more fanciful, their hypotheses less practical, their counsel less germane. Unconfirmed suspicion tends, over time, to become wilful, fallacious, and prey to the vicissitudes of mood–it acquires all the qualities of common superstition–and the men of the Crown Hotel, whose nexus of allegiance is stitched, after all, in the bright thread of time and motion, have, like all men, no immunity to influence."""]

alphabet = {'a':0,'A':0,'b':0,'B':0,'c':0,'C':0,'d':0,'D':0,'e':0,'E':0,'f':0,'F':0,'g':0,'G':0,'h':0,'H':0,'i':0,'I':0,'J':0,'j':0,'k':0,'K':0,'l':0,'L':0,'m':0,'M':0,'n':0,'N':0,'o':0,'O':0,'p':0,'P':0,'q':0,'Q':0,'r':0,'R':0,'s':0,'S':0,'t':0,'T':0,'u':0,'U':0,'v':0,'V':0,'w':0,'W':0,'x':0,'X':0,'y':0,'Y':0,'z':0,'Z':0,',':0,'.':0,'-':0,"'":0,":":0}
alphabet2 = {'a':0,'A':0,'b':0,'B':0,'c':0,'C':0,'d':0,'D':0,'e':0,'E':0,'f':0,'F':0,'g':0,'G':0,'h':0,'H':0,'i':0,'I':0,'J':0,'j':0,'k':0,'K':0,'l':0,'L':0,'m':0,'M':0,'n':0,'N':0,'o':0,'O':0,'p':0,'P':0,'q':0,'Q':0,'r':0,'R':0,'s':0,'S':0,'t':0,'T':0,'u':0,'U':0,'v':0,'V':0,'w':0,'W':0,'x':0,'X':0,'y':0,'Y':0,'z':0,'Z':0,',':0,'.':0,'-':0,"'":0,"!":0,":":0}
def countdown1(h, m, s):

  total_seconds = h * 3600 + m * 60 + s

  while total_seconds > 0:

      # Timer represents time left on countdown
      timer = datetime.timedelta(seconds = total_seconds)

      print(timer, end="\r")
      # Delays the program one second
      time.sleep(1)

      # Reduces total time by one second
      total_seconds -= 1
  print("Start now!")

#done = False
def countdown2():
  c = 0
  if done:
    print("You used "+str(c)+" seconds to type!! Good Job!!")
  while not done:
    time.sleep(1)
    c += 1

print("""
▄▄▄█████▓▓██   ██▓ ██▓███   ██▓ ███▄    █   ▄████      ▄████  ▄▄▄       ███▄ ▄███▓▓█████ 
▓  ██▒ ▓▒ ▒██  ██▒▓██░  ██▒▓██▒ ██ ▀█   █  ██▒ ▀█▒    ██▒ ▀█▒▒████▄    ▓██▒▀█▀ ██▒▓█   ▀ 
▒ ▓██░ ▒░  ▒██ ██░▓██░ ██▓▒▒██▒▓██  ▀█ ██▒▒██░▄▄▄░   ▒██░▄▄▄░▒██  ▀█▄  ▓██    ▓██░▒███   
░ ▓██▓ ░   ░ ▐██▓░▒██▄█▓▒ ▒░██░▓██▒  ▐▌██▒░▓█  ██▓   ░▓█  ██▓░██▄▄▄▄██ ▒██    ▒██ ▒▓█  ▄ 
  ▒██▒ ░   ░ ██▒▓░▒██▒ ░  ░░██░▒██░   ▓██░░▒▓███▀▒   ░▒▓███▀▒ ▓█   ▓██▒▒██▒   ░██▒░▒████▒
  ▒ ░░      ██▒▒▒ ▒▓▒░ ░  ░░▓  ░ ▒░   ▒ ▒  ░▒   ▒     ░▒   ▒  ▒▒   ▓▒█░░ ▒░   ░  ░░░ ▒░ ░
    ░     ▓██ ░▒░ ░▒ ░      ▒ ░░ ░░   ░ ▒░  ░   ░      ░   ░   ▒   ▒▒ ░░  ░      ░ ░ ░  ░
  ░       ▒ ▒ ░░  ░░        ▒ ░   ░   ░ ░ ░ ░   ░    ░ ░   ░   ░   ▒   ░      ░      ░   
          ░ ░               ░           ░       ░          ░       ░  ░       ░      ░  ░
          ░ ░                                                                            
""")
ans = input("Welcome! If you want to play, enter Yes")
if ans == "Yes":
  print('You have 1 minute to type the following text:')
  print("\n")
  c = random.randint(0,len(library)-1)
  print(library[c])
  print("\n")
  print('Type after countdown, hit return after finishing or when the time is up')
  print("\n")
  countdown1(0,0,3)
  #threading.Thread(target=countdown2,daemon = True).start()
  #word = input().replace(" ", "")
  passage = library[c].replace(" ","")
  def check(passage,alphabet,alphabet2,word):
    count = 0
    total = len(passage)
    for i in passage:
      if i in alphabet2:
        alphabet2[i] += 1
    letter1 = []
    letter2 = []
    for i in word:
      if i in alphabet:
        alphabet[i] += 1
    for key in alphabet.values():
      letter1.append(int(key))
    for key in alphabet2.values():
      letter2.append(int(key))
    for j in range(57):
      count += min(letter1[j],letter2[j])
    return 'Congrats! You got '+str(count)+'/'+str(total)+' right!'
  import signal
  def interrupted(signum, frame):
    #print(check(passage,alphabet,alphabet2,word))
    print ("Timeout!")
  
  signal.signal(signal.SIGALRM, interrupted)
  signal.alarm(10)
  try:
    word = input().replace(" ", "")
    print(check(passage,alphabet,alphabet2,word))
  except:
    print("An Error occured")
  signal.alarm(0)
  #done = True
else:
  print("What a pity! Good bye")
  
