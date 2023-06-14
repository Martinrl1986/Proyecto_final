from blogapp import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
    avatars = ['1.png', '2.png', '3.png', '4.png', '5.png', '6.png', '7.png', '8.png', '9.png', '10.png', '11.png', '12.png', '13.png', '14.png', '15.png', '16.png', '17.png', '18.png', '19.png', '20.png']  
    
    return render_template('index.html', avatars=avatars)

if __name__ == '__main__':
    app.run()