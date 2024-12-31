def format_car_response(car):
    return {
        "id": car.id,
        "make": car.make,
        "model": car.model,
        "productionYear": car.productionYear,
        "licensePlate": car.licensePlate,
        "garages": [
            {
                "id": garage.id,
                "name": garage.name,
                "location": garage.location,
                "city": garage.city,
                "capacity": garage.capacity,
            }
            for garage in car.garages
        ],
    }
