from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    movies = []

    if request.method == 'POST':
        search_query = request.form['search_query']
        search_query_year = request.form['search_query_year']
        search_query_type = request.form['search_query_type']

        api_key = "f0674f3f"
        year = "2000"
        url = f"http://www.omdbapi.com/?s={search_query}&y={search_query_year}&type={search_query_type}&apikey={api_key}"
        response = requests.get(url)
        data = response.json()
        print(data) #look in the terminal at the data go to json lint to see the structure
        
        movies = data["Search"] # this gets the array of movies using the key Search
        #If the response is true from the JSON then send the movies to the webpage...
        if data.get('Response') == 'True':
            return render_template('index.html', movies=movies)

    return render_template('index.html', movies=movies)


if __name__ == "__main__":
    app.run(debug=True)
