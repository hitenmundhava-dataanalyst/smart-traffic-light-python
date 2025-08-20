import time

# Generator for traffic light cycle
def traffic_light_cycle():
    while True:
        yield "Red"
        yield "Green"
        yield "Yellow"

# TrafficLight Class
class TrafficLight:
    def __init__(self):
        self.cycle = traffic_light_cycle()
        self.running = True

    def start(self):
        print("Traffic Light Started ")
        while self.running:
            color = next(self.cycle)

            # if-else → red/green control
            if color == "Red":
                print("STOP")
                time.sleep(2)
            elif color == "Green":
                print("GO")
                time.sleep(2)
            elif color == "Yellow":
                print("SLOW DOWN")
                time.sleep(1)

    def stop(self):
        print("Emergency Stop!")
        self.running = False


# Run Simulation
if __name__ == "__main__":
    light = TrafficLight()
    try:
        light.start()
    except KeyboardInterrupt:
        light.stop()
