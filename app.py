#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask, render_template
import random

app=Flask(__name__)

def omikuji():
    event = list(["あたり","はずれ"])
    return random.choice(event)
@app.route('/')
def index():
    result = omikuji()
    #テンプレートエンジンにデータを指定
    return render_template("index.html",
                          result = result)
if __name__ =="__main__":
    app.run()


# In[ ]:




