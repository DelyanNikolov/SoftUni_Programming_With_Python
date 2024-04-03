from typing import List

from project.route import Route
from project.user import User
from project.vehicles.base_vehicle import BaseVehicle
from project.vehicles.cargo_van import CargoVan
from project.vehicles.passenger_car import PassengerCar


class ManagingApp:
    VALID_VEHICLE_TYPES = {"PassengerCar": PassengerCar, "CargoVan": CargoVan}

    def __init__(self):
        self.users: List[User] = []
        self.vehicles: List[BaseVehicle] = []
        self.routes: List[Route] = []

    def register_user(self, first_name: str, last_name: str, driving_license_number: str):

        user = next((filter(lambda u: u.driving_license_number == driving_license_number, self.users)), None)
        if user is not None:
            return f"{driving_license_number} has already been registered to our platform."

        new_user = User(first_name, last_name, driving_license_number)
        self.users.append(new_user)
        return f"{first_name} {last_name} was successfully registered under DLN-{driving_license_number}"

    def upload_vehicle(self, vehicle_type: str, brand: str, model: str, license_plate_number: str):
        try:
            vehicle = self.VALID_VEHICLE_TYPES[vehicle_type](brand, model, license_plate_number)
        except KeyError:
            return f"Vehicle type {vehicle_type} is inaccessible."

        plate = next((filter(lambda v: v.license_plate_number == license_plate_number, self.vehicles)), None)
        if plate is not None:
            return f"{license_plate_number} belongs to another vehicle."

        self.vehicles.append(vehicle)
        return f"{brand} {model} was successfully uploaded with LPN-{license_plate_number}."

    def allow_route(self, start_point: str, end_point: str, length: float):
        route_to_check = next((filter(lambda r: r.start_point == start_point and r.end_point == end_point, self.routes)),
                              None)
        if route_to_check is not None:
            if route_to_check.length == length:
                return f"{start_point}/{end_point} - {length} km had already been added to our platform."
            elif route_to_check.length < length:
                return f"{start_point}/{end_point} shorter route had already been added to our platform."
            elif route_to_check.length > length:
                route_to_check.is_locked = True
        route_id = len(self.routes) + 1
        route = Route(start_point, end_point, length, route_id)

        self.routes.append(route)
        return f"{start_point}/{end_point} - {length} km is unlocked and available to use."

    def make_trip(self, driving_license_number: str, license_plate_number: str, route_id: int, is_accident_happened: bool):
        user = next(filter(lambda u: u.driving_license_number == driving_license_number, self.users))
        vehicle = next(filter(lambda v: v.license_plate_number == license_plate_number, self.vehicles))
        route = next(filter(lambda r: r.route_id == route_id, self.routes))

        if user.is_blocked:
            return f"User {driving_license_number} is blocked in the platform! This trip is not allowed."

        if vehicle.is_damaged:
            return f"Vehicle {license_plate_number} is damaged! This trip is not allowed."

        if route.is_locked:
            return f"Route {route_id} is locked! This trip is not allowed."

        vehicle.drive(route.length)

        if is_accident_happened:
            vehicle.change_status()
            user.decrease_rating()
        else:
            user.increase_rating()

        vehicle_status = "OK" if vehicle.is_damaged is False else "Damaged"
        return f"{vehicle.brand} {vehicle.model} License plate: {vehicle.license_plate_number} " \
               f"Battery: {vehicle.battery_level}% Status: {vehicle_status}"

    def repair_vehicles(self, count: int):
        vehicles_to_repair = [v for v in self.vehicles if v.is_damaged]
        sorted_vehicles = sorted(vehicles_to_repair, key=lambda c: (c.brand, c.model))[:count]

        for car in sorted_vehicles:
            car.change_status()
            car.recharge()

        return f"{len(sorted_vehicles)} vehicles were successfully repaired!"

    def users_report(self):
        result = ["*** E-Drive-Rent ***"]
        for user in sorted(self.users, key=lambda u: -u.rating):
            result.append(f"{str(user)}")

        return '\n'.join(result)
