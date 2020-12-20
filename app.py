#!/usr/bin/env python
# coding: utf-8

# In[15]:


from flask import Flask, render_template
import random

app=Flask(__name__)

@app.route('/')
def index():
    #データを指定
    event = list(["あたり","はずれ"])
    result = random.choice(event)
    #テンプレートエンジンにデータを指定
    return render_template("index.html",
                          result = result)
if __name__ =="__main__":
    app.run()


# In[ ]:




