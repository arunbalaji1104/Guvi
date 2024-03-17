# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nfXQDB1hCz9hDa7gDDeb_rZpnLUvA14T

Using the Python's Object Oriented Programming Scheme (OOPS) kindly complete the
following tasks which is given as below:-
1) Create a Python Class called Circle with Constructor which will take a List as an
argument for the task. The List is [10, 501, 22, 37, 100, 999, 87, 351]
"""

class Circle:
    def __init__(self, radius_list):
        self.radius_list = radius_list

# Given list of radii
radius_list = [10, 501, 22, 37, 100, 999, 87, 351]

# Create an instance of the Circle class
circle = Circle(radius_list)

# Test the constructor by accessing the radius list
print("Radii:", circle.radius_list)

"""2.Create proper member variables inside the task if required and use them when
necessary. For example for this task create a class private variable named pi = 3.141



"""

class Circle:
    # Class private variable pi
    __pi = 3.141

    def __init__(self, radius_list):
        self.radius_list = radius_list

    def area(self):
        areas = []
        for radius in self.radius_list:
            # Using the class private variable pi
            area = Circle.__pi * radius ** 2
            areas.append(area)
        return areas

    def perimeter(self):
        perimeters = []
        for radius in self.radius_list:
            # Using the class private variable pi
            perimeter = 2 * Circle.__pi * radius
            perimeters.append(perimeter)
        return perimeters

# Given list of radii
radius_list = [10, 501, 22, 37, 100, 999, 87, 351]

# Create an instance of the Circle class
circle = Circle(radius_list)

# Calculate and print areas and perimeters
areas = circle.area()
perimeters = circle.perimeter()

print("Areas:", areas)
print("Perimeters:", perimeters)

"""3.From the given List create two class Methods Area and Perimeter which will be going to
calculate the Area and Perimeter.

"""

class Circle:
    # Class private variable pi
    __pi = 3.141

    def __init__(self, radius_list):
        self.radius_list = radius_list

    @classmethod
    def area(cls, radius):
        # Using the class private variable pi
        return cls.__pi * radius ** 2

    @classmethod
    def perimeter(cls, radius):
        # Using the class private variable pi
        return 2 * cls.__pi * radius

# Given list of radii
radius_list = [10, 501, 22, 37, 100, 999, 87, 351]

# Calculate and print areas and perimeters
for radius in radius_list:
    print("Radius:", radius)
    print("Area:", Circle.area(radius))
    print("Perimeter:", Circle.perimeter(radius))
    print()

class TV:
    def __init__(self, brand):
        self.brand = brand
        self.channel = 1
        self.volume = 50
        self.on_off = False

    def increase_volume(self):
        if self.on_off and self.volume < 100:
            self.volume += 1

    def decrease_volume(self):
        if self.on_off and self.volume > 0:
            self.volume -= 1

    def set_channel(self, channel):
        if self.on_off and 1 <= channel <= 50:
            self.channel = channel

    def reset_tv(self):
        self.channel = 1
        self.volume = 50

    def status(self):
        return f"{self.brand} at channel {self.channel}, volume {self.volume}, {'ON' if self.on_off else 'OFF'}"


class LedTV(TV):
    def __init__(self, brand, screen_thickness, energy_usage, lifespan, refresh_rate):
        super().__init__(brand)
        self.screen_thickness = screen_thickness
        self.energy_usage = energy_usage
        self.lifespan = lifespan
        self.refresh_rate = refresh_rate

    def display_details(self):
        return f"Screen Thickness: {self.screen_thickness} mm\nEnergy Usage: {self.energy_usage}W\nLifespan: {self.lifespan} years\nRefresh Rate: {self.refresh_rate}Hz"


class PlasmaTV(TV):
    def __init__(self, brand, screen_thickness, energy_usage, lifespan, viewing_angle, backlight):
        super().__init__(brand)
        self.screen_thickness = screen_thickness
        self.energy_usage = energy_usage
        self.lifespan = lifespan
        self.viewing_angle = viewing_angle
        self.backlight = backlight

    def display_details(self):
        return f"Screen Thickness: {self.screen_thickness} mm\nEnergy Usage: {self.energy_usage}W\nLifespan: {self.lifespan} years\nViewing Angle: {self.viewing_angle} degrees\nBacklight: {self.backlight}"


# Example usage
led_tv = LedTV("Samsung", 10, 50, 5, 120)
print("LED TV Status:", led_tv.status())
led_tv.increase_volume()
led_tv.set_channel(8)
print("LED TV Status:", led_tv.status())
print("LED TV Details:")
print(led_tv.display_details())
print()

plasma_tv = PlasmaTV("Sony", 20, 70, 8, 180, "OLED")
print("Plasma TV Status:", plasma_tv.status())
plasma_tv.decrease_volume()
plasma_tv.set_channel(15)
print("Plasma TV Status:", plasma_tv.status())
print("Plasma TV Details:")
print(plasma_tv.display_details())