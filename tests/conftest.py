import pytest
from app import create_app
from app import db
from app.models.planet import Planet

@pytest.fixture
def app():
    app = create_app({"TESTING": True})

    with app.app_context():
        db.create_all()
        yield app

    with app.app_context():
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def two_saved_planets(app):
    # Arrange
    pluto = Planet(name="pluto",
                    description="Neil sucks",
                    position_from_sun = 9)
    venus = Planet(name="Venus",
                    description="She's got it",
                    position_from_sun = 3)

    db.session.add_all([pluto, venus])
    # Alternatively, we could do
    # db.session.add(ocean_book)
    # db.session.add(mountain_book)
    db.session.commit()

