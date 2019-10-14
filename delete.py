import os 
for i in next(os.walk('.'))[1]:
    os.rmdir(i)