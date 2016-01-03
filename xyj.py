from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash
from contextlib import closing
from flask import send_from_directory

app = Flask(__name__)





@app.route('/index')
@app.route('/')
def show_index():
    return render_template('index.html', title="house")

@app.route('/gswh')
def show_gswh():
    return render_template('gswh.html', title="house")



@app.route('/team')
def show_team():
    return render_template('team.html', title="house")


@app.route('/hire')
def show_hire():
    return render_template('hire.html', title="house")


@app.route('/about')
def show_about():
    return render_template('about.html', title="house")


@app.route('/fyzs')
def show_fyzs():
    return render_template('fyzs.html', title="house")

@app.route('/gsys')
def show_gsys():
    return render_template('gsys.html', title="house")

@app.route('/tedf')
def show_tdfc():
    return render_template('tdfc.html', title="house")

@app.route('/zpzw')
def show_zpzw():
    return render_template('zpzw.html', title="house")





@app.route('/news')
def show_news():
    return render_template('news.html', title="house")


@app.route('/news1')
def show_news1():
    return render_template('news1.html', title="house")

@app.route('/news2')
def show_news2():
    return render_template('news2.html', title="house")

@app.route('/news3')
def show_news3():
    return render_template('news3.html', title="house")

@app.route('/news4')
def show_news4():
    return render_template('news4.html', title="house")

@app.route('/news5')
def show_news5():
    return render_template('news5.html', title="house")

@app.route('/news6')
def show_news6():
    return render_template('news6.html', title="house")

@app.route('/news7')
def show_news7():
    return render_template('news7.html', title="house")

@app.route('/news8')
def show_news8():
    return render_template('news8.html', title="house")

@app.route('/news9')
def show_news9():
    return render_template('news9.html', title="house")

@app.route('/news10')
def show_news10():
    return render_template('news10.html', title="house")

@app.route('/news11')
def show_news11():
    return render_template('news11.html', title="house")

@app.route('/news12')
def show_news12():
    return render_template('news12.html', title="house")

@app.route('/news13')
def show_news13():
    return render_template('news13.html', title="house")

@app.route('/news14')
def show_news14():
    return render_template('news14.html', title="house")
@app.route('/rwjs')
def show_rwjs():
    return render_template('rwjs.html', title="house")

@app.route('/jpfy')
def show_jpfy():
    return render_template('jpfy.html', title="house")










if __name__ == '__main__':
    app.run()
