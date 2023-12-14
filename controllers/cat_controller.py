from flask import render_template, request
from models.cat import Cat
from db.cats import cats

class CatController:
    @staticmethod
    def index():
        if request.method == 'GET':
            return CatController.get()
        elif request.method == 'PUT':
            return CatController.update()
    
    @staticmethod
    def get():
        id =  int(request.args.get('id') if request.args.get('id') else 0)
        Cats = {
            'cats': cats,
            'cat': cats[id]
        }
        return render_template('cat.html', cats=Cats)
    
    @staticmethod
    def update():
        id =  int(request.args.get('id'))
        cats[id].add_count()
        print(id)
        return 'OK'
    