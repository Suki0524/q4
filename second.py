import random

library = ["""During the first part of your life, you only become aware of happiness once you have lost it. Then an age comes, a second one, in which you already know, at the moment when you begin to experience true happiness, that you are, at the end of the day, going to lose it. When I met Belle, I understood that I had just entered this second age. I also understood that I hadn’t reached the third age, in which anticipation of the loss of happiness prevents you from living.""","""But just as I didn’t want to resent my kids, I also didn’t want to find myself too much in love with them. There are parents who don’t like to hear their little girl crying at night, at the vast approaching dark of sleep, and so in their torment think why not feed her a lollipop, and a few years later that kid’s got seven cavities and a pulled tooth. This is how we’ve arrived at the point where we give every kid on the team a trophy in the name of participation. I didn’t want to love my kids so much that I was blind to their shortcomings, limitations, and mediocre personalities, not to mention character flaws and criminal leanings. But I could, I thought, I could love a kid that much. A kid really could be everything, and that scared me. Because once a kid is everything, not only might you lose all perspective and start proudly displaying his participation trophies, you might also fear for that kid’s life every time he leaves your sight. I didn’t want to live in perpetual fear. People don’t recover from the death of a child. I knew I wouldn’t. I knew that having a kid would be my chance to improve upon my shitty childhood, that it would be a repudiation of my dad’s suicide and a celebration of life, but if that kid taught me how to love him, how to love, period, and then I lost him as I lost my dad, that would be it for me. I’d toss in the towel. Fuck it, fuck this world and all its heartbreak. I’d tell that to Connie, and she’d tell me that if that was how I felt I was already a slave to the fear, and good luck.""","""Everything failed to subdue me. Soon everything seemed dull: another sunrise, the lives of heroes, failing love, war, the discoveries people made about each other. The only thing that didn’t bore me, obviously enough, was how much money Tim Price made, and yet in its obviousness it did. There wasn’t a clear, identifiable emotion within me, except for greed and possibly, total disgust. I had all the characteristics of a human being–flesh, blood, skin, hair–but my depersonalization was so intense, had gone so deep, that the normal ability to feel compassion had been eradicated, the victim of a slow, purposeful erasure. I was simply imitating reality, a rough resemblance of a human being, with only a dim corner of my mind functioning. Something horrible was happening and yet I couldn’t figure out why–couldn’t put my finger on it. The only thing that calmed me was the satisfying sound of ice being dropped into a glass of J&B. Eventually I drowned the chow, which Evelyn didn’t miss; she didn’t even notice its absence, not even when I threw it in the walk-in freezer, wrapped in one of her sweaters from Bergdorf Goodman. We had to leave the Hamptons because I would find myself standing over our bed in the hours before dawn, with an ice pick gripped in my fist, waiting for Evelyn to open her eyes. At my suggestion, one morning over breakfast, she agreed, and on the last Sunday before Labor Day we returned to Manhattan by helicopter.""","""A secret always has a strengthening effect upon a newborn friendship, as does the shared impression than an external figure is to blame: the men of the Crown have become united less by their shared beliefs, we observe, than by their shared misgivings–which are, in the main, externally directed. In their analyses, variously made, of Alastair Lauderback, George Shepard, Lydia Wells, Francis Carver, Anna Wetherell, and Emery Staines, the Crown men have become more and more suggestive, despite the fact that nothing has been proven, no body has been tried, and no new information has come to light. Their beliefs have become more fanciful, their hypotheses less practical, their counsel less germane. Unconfirmed suspicion tends, over time, to become wilful, fallacious, and prey to the vicissitudes of mood–it acquires all the qualities of common superstition–and the men of the Crown Hotel, whose nexus of allegiance is stitched, after all, in the bright thread of time and motion, have, like all men, no immunity to influence."""]

c = random.randint(0,len(library)-1)
print(library[c])
l = len(library[c])
import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
timeout = 10
time_left = timeout
label = tk.Label(window, text=time_left)
label.config(font=('Courier', 44))
label.pack()
text = tk.Text(window)
text.pack()


def update():
    global time_left
    global text
    time_left -= 1
    label.configure(text=time_left)
    if time_left > 0:
        window.after(1000, update)
    else:
        tk.messagebox.showinfo('Your score', str(len(text.get('1.0', 'end-1c'))))


window.after(1000, update)
window.mainloop()
