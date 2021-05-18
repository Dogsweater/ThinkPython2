import dbm
import pickle

db = dbm.open('captions','c')
db['cleese.png']='Photo of John Cleese'

t=[1,2,3]
pickle.dumps(t)



for key in db:
    print(key,db[key])
  
db.close()