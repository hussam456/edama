from flask import Flask, render_template

app = Flask(__name__)

# رابط الصفحة الرئيسية
@app.route('/')
def index():
    return render_template('index.html')

# رابط صفحة الإنجازات
@app.route('/achievements')
def achievements():
    return render_template('achievements.html')

# رابط صفحة المتجر
@app.route('/shop')
def shop():
    return render_template('shop.html')

if __name__ == '__main__':
    app.run(debug=True)
