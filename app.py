from flask import Flask, jsonify, request, abort
from models import db, Customer

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://flaskuser:flaskpassword@db:5432/customerdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Function to initialize the database when the app starts
def init_db():
    with app.app_context():
        db.create_all()

# Get all customers or filter by city
@app.route('/customers', methods=['GET'])
def get_customers():
    city = request.args.get('city')
    # first_name = request.args.get('first_name')
    # last_name = request.args.get('last_name')
    if city:
        customers = Customer.query.filter_by(city=city).all()
    # if first_name:
    #     query = query.filter_by(first_name=first_name)
    # if last_name:
    #     query = query.filter_by(last_name=last_name)
    else:
        customers = Customer.query.all()
    return jsonify([customer.to_dict() for customer in customers]), 200

# Get a customer by ID
@app.route('/customers/<int:customer_id>', methods=['GET'])
def get_customer_by_id(customer_id):
    customer = Customer.query.get_or_404(customer_id)
    return jsonify(customer.to_dict()), 200

# Create a new customer
@app.route('/customers', methods=['POST'])
def create_customer():
    data = request.get_json()

    if not data or not all(k in data for k in ("first_name", "last_name", "email", "address", "city", "state", "zip")):
        abort(400, "Missing required customer fields")

    new_customer = Customer(
        first_name=data['first_name'],
        last_name=data['last_name'],
        email=data['email'],
        address=data['address'],
        city=data['city'],
        state=data['state'],
        zip=data['zip']
    )

    db.session.add(new_customer)
    db.session.commit()

    return jsonify(new_customer.to_dict()), 200

# Error handler for 404 errors
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Customer not found"}), 404

# Error handler for 400 errors
@app.errorhandler(400)
def bad_request(error):
    return jsonify({"error": str(error)}), 400

# 400 Bad Request is to be used in cases where the request was successfully
# received by the application, and the application determined that something
# was wrong about the request: Either the endpoint doesn't exist, or the format
# or nature of request parameters/variables was incorrect/malformed in some way,
# rendering the request invalid.

if __name__ == '__main__':
    init_db()  # Call this function to create tables when the app starts
    app.run(host='0.0.0.0', port=5000)