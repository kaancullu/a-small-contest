import pandas as pd
import numpy as np

df = pd.read_excel("contest.xlsx",encoding="utf-8").astype(str)

seq = np.arange(0,len(df))
np.random.shuffle(seq)

import string
class questions:
    
    def __init__(self,*liste):
        self.text = liste[0]
        self.choices = liste[1]
        self.answer = liste[2]
        
    def check(self, answer):
        return self.answer == answer


class contest:
    
    def __init__(self,questions):
        self.questions = questions
        self.score = 0
        self.index = 0
        self.result = []
        
    def get_question(self):
        return self.questions[self.index]
        
    def disp_question(self):
        question = self.get_question()
        print(f"Soru {self.index+1}: {question.text}\n")
        self.choi = string.ascii_lowercase
        self.tem = []
        for i,x in enumerate(question.choices):
            print(f"{self.choi[i]}) {x}")
            self.tem.append(x)            
        
        cevap = input("Cevap:")
        print("\n")
        self.guess(cevap)
        self.load_question()
        
    def guess(self,answer):
        question = self.get_question()
        answer = self.tem[self.choi.find(answer)]
        if question.check(answer):
            self.score += 10
            self.result.append(("Doğru",answer,question.answer))
        else:
            self.score -= 5
            self.result.append(("Yanlış",answer,question.answer))
        
        self.index += 1
        
        
        
    def load_question(self):
        if self.index == len(self.questions):
            self.show_score()
        else:            
            self.disp_progress()
            self.disp_question()    
        
        
    def show_score(self):
        print("YARISMA BITTI".center(50,"*"))
        print(f"Puaniniz: {self.score}")
        print(pd.DataFrame(sinav.result,columns=["Sonuçlar","Verilen Cevap","Doğru Cevap"],index=range(1,len(self.questions)+1)))
                
    
        
    def disp_progress(self):
        hepsi = len(self.questions)
        
        if (self.index+1)>hepsi:
            pass
        else:
            print(f"Soru({self.index+1}/{hepsi})".center(50,"*"))
        

sorular = []
for i in seq:
    q = [df.iloc[i,0],[df.iloc[i,1],df.iloc[i,2],df.iloc[i,3]],df.iloc[i,4]]
    sorular.append(q)

soru = []
for i in sorular:
    soru.append(questions(*i))

sinav = contest(soru)

sinav.load_question()

