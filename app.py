import bcrypt
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, current_user, logout_user, login_required
from datetime import datetime
from models.user import User
from models.meal import Meal
from database import db

# Configuração do Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://admin:admin123@localhost:3306/daily-diet'

# Inicialização de extensões
login_manager = LoginManager()
db.init_app(app)
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

# Função auxiliar para responder com erro
def error_response(message, status=400):
    return jsonify({'message': message}), status

# USER ROUTES
@app.route('/user', methods=['POST'])
def create_user():
    data = request.json
    username, password = data.get('username'), data.get('password')
    
    if not username or not password:
        return error_response('Invalid data')
    
    hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    user = User(username=username, password=hashed_password, role='user')
    db.session.add(user)
    db.session.commit()
    return jsonify({'message': 'User successfully created.'})

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username, password = data.get('username'), data.get('password')
    
    if not username or not password:
        return error_response('Invalid credentials')
    
    user = User.query.filter_by(username=username).first()
    if user and bcrypt.checkpw(password.encode(), user.password.encode()):
        login_user(user)
        return jsonify({'message': 'The user signed in successfully.'})
    
    return error_response('Invalid credentials')

@app.route('/logout', methods=['GET'])
@login_required
def logout():
    logout_user()
    return jsonify({'message': 'User logout successfully'})

# MEAL ROUTES
@app.route('/meals/<int:id_meal>', methods=['GET'])
def get_meal(id_meal):
    meal = Meal.query.get(id_meal)
    if not meal:
        return error_response('Meal not found.')
    
    return jsonify({
        'name': meal.name,
        'description': meal.description,
        'date': meal.date.strftime('%m/%d/%y'),
        'time': meal.time.strftime('%H:%M'),
        'is_in_diet': meal.is_in_diet,
        'user_id': meal.user_id
    })

@app.route('/meals', methods=['POST'])
@login_required
def create_meal():
    data = request.json
    try:
        meal = Meal(
            name=data.get('name'),
            description=data.get('description'),
            date=datetime.strptime(data.get('date'), '%m/%d/%y'),
            time=datetime.strptime(data.get('time'), '%H:%M').time(),
            is_in_diet=data.get('is_in_diet'),
            user_id=current_user.id
        )
        db.session.add(meal)
        db.session.commit()
        return jsonify({'message': f'The meal {meal.name} was successfully created'})
    except (ValueError, TypeError):
        return error_response('Invalid date or time format')

@app.route('/meals/<int:id_meal>', methods=['PATCH'])
@login_required
def update_meal(id_meal):
    meal = Meal.query.get(id_meal)
    if not meal or meal.user_id != current_user.id:
        return error_response('Action not allowed.', 403)
    
    data = request.json
    try:
        meal.name = data.get('name', meal.name)
        meal.description = data.get('description', meal.description)
        meal.date = datetime.strptime(data.get('date'), '%m/%d/%y') if 'date' in data else meal.date
        meal.time = datetime.strptime(data.get('time'), '%H:%M').time() if 'time' in data else meal.time
        meal.is_in_diet = data.get('is_in_diet', meal.is_in_diet)
        db.session.commit()
        return jsonify({'message': f'Meal {meal.name} successfully updated.'})
    except (ValueError, TypeError):
        return error_response('Invalid date or time format')

@app.route('/meals/<int:id_meal>', methods=['DELETE'])
@login_required
def delete_meal(id_meal):
    meal = Meal.query.get(id_meal)
    if not meal or meal.user_id != current_user.id:
        return error_response('Action not allowed', 403)
    
    db.session.delete(meal)
    db.session.commit()
    return jsonify({'message': 'Meal successfully deleted.'})

@app.route('/meals/user/<int:id_user>', methods=['GET'])
def show_user_meals(id_user):
    user = User.query.get(id_user)
    if not user:
        return error_response('User not found')
    
    meals = Meal.query.filter_by(user_id=id_user).all()
    if not meals:
        return jsonify({'message': 'No meals found for this user.'})
    
    total_meals = len(meals)
    total_meals_on_diet = sum(1 for meal in meals if meal.is_in_diet)
    percentage_on_diet = (total_meals_on_diet / total_meals) * 100
    percentage_not_on_diet = 100 - percentage_on_diet
    
    response_data = {
        'meals_data': [{
            'id': meal.id,
            'name': meal.name,
            'description': meal.description,
            'date': meal.date.strftime('%m/%d/%y'),
            'time': meal.time.strftime('%H:%M'),
            'is_in_diet': meal.is_in_diet
        } for meal in meals],
        'user_dashboard': {
            'total_meals': total_meals,
            'percentage_on_diet': percentage_on_diet,
            'percentage_not_on_diet': percentage_not_on_diet
        }
    }
    return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True)
