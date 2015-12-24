# Numbers of car
cars = 100
# Numbers of people that one car can take
space_in_a_car = 4.0
# Numbers of drivers
drivers =30
# Numbers of passengers
passengers = 90
# The driver of the lack of
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers/cars_driven

print "There are", cars ,"cars available."
print "There are only",drivers,"drivers available."
print "There will be", cars_not_driven,"empty cars today."
print "We can transport",carpool_capacity,"people today."
print "We have", passengers,"to carpool today."
print "We need to put about",average_passengers_per_car,"in each car."