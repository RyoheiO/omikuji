#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask, render_template
import random

app=Flask(__name__)

def omikuji():
    event = list(["あたり","はずれ"])
    return random.choice(event)

@app.route('/')
def start():
        return """
        <html>
        <head>
            <meta charset="utf-8">
            <title>おみくじ</title>
        </head>
        <body>
            おみくじ開始</br>
            <form action="/result" method="GET">
                <input type="submit" value="開始" >
            </form>
        </body>
        </html>"""
    
@app.route('/result')
def index():
    result = omikuji()
    #テンプレートエンジンにデータを指定
    return render_template("index.html",
                          result = result)

if __name__ =="__main__":
    app.run()


# In[ ]:




