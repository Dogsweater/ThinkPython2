import random

class Card:
    
    #类属性：定义在类之中，但在任何方法之外
    #将整数编码映射成对应的
    suit_names=['Clubs','Diamonds','Hearts','Spades']
    rank_names=[None,'Ace','2','3','4','5','6','7','8','9','10',
                'Jack','Queen','King']

    def __init__(self,suit=0,rank=2):
        self.suit = suit
        self.rank = rank
    
    def __str__(self):
        return '%s of %s '%(Card.rank_names[self.rank],Card.suit_names[self.suit])
     
    #重载<
    def __lt__(self,other):
        """
        if self.suit <other.suit:return True
        if self.suit >other.suit:return False
        return self.rank<other.rank
        """
        t1 =self.suit,self.rank
        t2 =other.suit,self.rank
        return t1<t2
        
class Deck:
    
    def __init__(self):
        self.cards =[]
        for suit in range(4):
            for rank in range(1,14):
                card=Card(suit,rank)
                self.cards.append(card)
    def __str__(self):
        res=[]
        for card in self.cards:
            res.append(str(card))
        #字符串.join(列表)   将字符串插入到join传入列表的字符串元素之间，
        #生成一个新的字符串
        return '\n'.join(res)
    def pop_card(self):
        #列表的pop方法
        return self.cards.pop()
    def add_card(self,card):
        return self.cards.append(card)
    def shuffle(self):
        random.shuffle(self.cards)
    #多态的好处，他直接就用了Card.__it__()方法，不用自己写
    def sort_card(self):
        self.cards.sort(reverse=True)
    def move_card(self,hand,num):
        for i in range(num):
            hand.cards.append(self.pop_card())
 
#定义一个类继承现有的类：把现有类的名称放在括号之中： 
class  Hand(Deck): 
    #重写覆盖
    def __init__(self,lable=''):
        self.cards=[]
        self.lable=lable

 
queen_of_diamonds=Card(1,12)
#card1=Card(2,11)
#print(card1)

deck=Deck()
deck.shuffle()
#deck.sort_card()
#print(deck)`

hand=Hand('new hand')
card=deck.pop_card()
hand.add_card(card)
print(hand)