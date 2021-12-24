class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=40), nullable=False, unique=True)
    price = db.Column(db.Float(), nullable=False)
    indirizzo = db.Column(db.String(), nullable=False)
    provincia = db.Column(db.String(length=2), nullable=False)
    descrizione = db.Column(db.String(length=1024), nullable=False)

    def __repr__(self):
        return f'Item {self.name}'