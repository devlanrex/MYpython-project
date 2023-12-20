text=''' Colby Daniel Lopez (born May 28, 1986) is an American professional wrestler. He is currently signed to WWE.
 He performs on the Raw brand under the ring name Seth "Freakin" Rollins and is the current and inaugural World Heavyweight Champion in his first reign. Rollins is generally considered to be one of the best currently active professional wrestlers in the world,[6][7][8] being credited for his in-ring ability and aptness of reinventing his on-screen character.

Prior to signing with WWE, Lopez wrestled under the ring name Tyler Black for Ring of Honor (ROH) and was part of the Age of the Fall stable with Jimmy Jacobs. During his time in ROH, he held the ROH World Championship once and the ROH World Tag Team Championship twice with Jacobs, and won the 2009 Survival of the Fittest tournament. Lopez also wrestled for various independent promotions including Full Impact Pro, where he was a one-time FIP World Heavyweight Champion, as well as Pro Wrestling Guerrilla, where he was a one-time PWG World Tag Team Champion, also with Jacobs.

Lopez signed with WWE in 2010 and was sent to its former developmental territory Florida Championship Wrestling (FCW), where he was renamed Seth Rollins and became the inaugural FCW Grand Slam Champion. After WWE rebranded FCW into NXT, he became the inaugural NXT Champion. Lopez debuted on WWE's main roster at the 2012 Survivor Series as part of a faction called Th'''
text=text.lower()
stop_word=['the','a','is']
i=0
while i<len(stop_word):
  text=text.replace(' '+ stop_word[i]+' ',' ')
  i+=1
raw=text.split( )
words=[ ]
j=0
while j<len(raw):
     if raw[j].isalpha( ):
         words.append(raw[j])
     j+=1
item=[ ]
word_count=[ ]
i=0
while i<len(words):
    if item.__contains__(words[i]):
        index=item.index(words[i])
        word_count[index]+=1
    else:
        item.append(words[i])
        word_count.append(1)
    i+=1

j=0
while j<len(item):
    print(f'{item[j]}: {word_count[j]}')
    j+=1