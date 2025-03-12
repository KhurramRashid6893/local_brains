from flask import Flask, render_template, request
import google.generativeai as genai

# Configure Google Gemini AI API
genai.configure(api_key="AIzaSyD7yvvskWyuzMypw9AyaGQ1BF54yNjIgl4")
model = genai.GenerativeModel("gemini-1.5-flash")

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/collaborate')
def collaborate():
    return render_template('collaborate.html')

@app.route('/insights')
def insights():
    return render_template('insights.html')

@app.route('/community')
def community():
    return render_template('community.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        query = request.form['query']
        response = model.generate_content(query)
        return render_template('search.html', query=query, result=response.text.replace("\n", "<br>"))  
    return render_template('search.html', query=None, result=None)

if __name__ == '__main__':
    app.run(debug=True)
