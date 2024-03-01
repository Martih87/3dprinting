from sense_hat import SenseHat
import time

sense = SenseHat()

while True:
    # Get the current temperature
    temp = sense.get_temperature()
    # Round the temperature to 2 decimal places
    temp = round(temp, 2)
    # Convert the temperature to a string
    temp_str = "Temp: " + str(temp)
    # Display the temperature
    sense.show_message(temp_str)

    # Wait for 5 seconds before updating
    time.sleep(5)

    # Get the current humidity
    humidity = sense.get_humidity()
    # Round the humidity to 2 decimal places
    humidity = round(humidity, 2)
    # Convert the humidity to a string
    humidity_str = "Humidity: " + str(humidity)
    # Display the humidity
    sense.show_message(humidity_str)

    # Wait for 5 seconds before updating
    time.sleep(5)
