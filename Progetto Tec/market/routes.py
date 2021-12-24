@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/annunci')
def annunci_page():
    items = Item.query.all()
    return render_template('annunci.html', items=items)