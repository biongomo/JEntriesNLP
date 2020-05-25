import nltk
import re
from nltk.sentiment.vader import SentimentIntensityAnalyzer 


class SentimentAnalysis ():
    def __init__(self, sent, count):
        self.sentence = self.get_sentence(sent)
        self.yellow_count = count
        
        self.main()

    def get_sentence(self,sen):
        return re.split('[.!?;\n]',sen)
    
    def check_polarity(self):
        sid =  SentimentIntensityAnalyzer()
        for sentence in self.sentence:
             #print(sentence)
             ss = sid.polarity_scores(sentence)
             if ss['compound'] < -0.5:
                 self.yellow_count += 1
                 print(sentence, self.yellow_count)
#             for k in ss:
#                 print('{0}: {1}, '.format(k, ss[k]), end='')
#        
#             print()
        return
    
    def check_yellow_flags(self):
        if self.yellow_count > 10:
            print("do you need help")
            
    def check_red_flags(self):
        red_flags_words = "suicidal; suicide; kill myself; my suicide note; my suicide letter; end my life;\
         never wake up; can't go on; not worth living; ready to jump;sleep forever; want to die; be dead;\
         better off without me; better off dead; suicide plan; suicide pact; tired of living; don't want to be here; die alone; go to sleep forever"
        words = red_flags_words.split(";")
        
        for w in words:
            if w in sen:
                print("!!", w)
                
    def main(self):
        self.check_polarity()
        self.check_yellow_flags()
        self.check_red_flags()
            
            
sen = "Finally had a chance to catch up with Jenny after a month. How it felt seeing old friends:). Good food. New sofa coming! Be less distracted. I very much want to die. I am so so tired"
a = SentimentAnalysis(sen, 0)
b = SentimentAnalysis(sen, a.yellow_count)