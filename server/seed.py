from .app import create_app, db
from .models.restaurant import Restaurant
from .models.pizza import Pizza
from .models.restaurant_pizza import RestaurantPizza

app = create_app()

with app.app_context():
    db.drop_all()
    db.create_all()

    r1 = Restaurant(name="Kiki's Pizza", address="123 Main St")
    r2 = Restaurant(name="Luigi's", address="456 Side St")

    p1 = Pizza(name="Margherita", ingredients="Tomato, Mozzarella, Basil")
    p2 = Pizza(name="Pepperoni", ingredients="Tomato, Mozzarella, Pepperoni")

    db.session.add_all([r1, r2, p1, p2])
    db.session.commit()

    rp1 = RestaurantPizza(price=10, pizza_id=p1.id, restaurant_id=r1.id)
    rp2 = RestaurantPizza(price=12, pizza_id=p2.id, restaurant_id=r1.id)

    db.session.add_all([rp1, rp2])
    db.session.commit()

    print("Seeded database!")
