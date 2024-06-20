from flask import Flask, render_template, request
import nltk
from newspaper import Article
from newspaper.article import ArticleException

app = Flask(__name__)



nltk.download("punkt")

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/form_page')
def form_page():
    return render_template('form_page.html')

@app.route('/dfail')
def dfail():
    return render_template("dfail.html")


@app.route('/main_page', methods=['POST'])
def main_page():

    try:
        url = request.form['url']
        article = Article(url)
        article.download()
        article.parse()
        article.nlp()

        parameters = {"Title": article.title, "Authors": article.authors, "Published_on": article.publish_date, "Summary": article.summary}

        return render_template('main_page.html', data=parameters)
      
    except Exception as e:
        return render_template("dfail.html")
        

    
if __name__ == "__main__":
    app.run(host="0.0.0.0". port=5000)
