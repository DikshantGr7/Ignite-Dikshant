
import re
from collections import Counter, OrderedDict, defaultdict, deque, namedtuple


text = "Order #1042 was placed on 2026-03-15. Invoice #1043 on 2026-03-18."
dates = re.findall(r"\d{4}-\d{2}-\d{2}", text)
print("1A. RegEx (Findall) - Extracted Dates:", dates)

phone_raw = "(555) 019-2834"
clean_phone = re.sub(r"\D", "", phone_raw)
print("1B. RegEx (Clean Input) - Raw:", phone_raw, "-> Cleaned:", clean_phone)


class Circle:

    def __init__(self, radius: float):
        self.radius = radius

    @property
    def area(self) -> float:
        return 3.14159 * (self.radius**2)


c = Circle(5)
print(f"2A. Property (Computed Area) - Radius 5 -> Area: {c.area:.2f}")

class Temperature:

    def __init__(self, celsius: float):
        self._celsius = celsius

    @property
    def celsius(self) -> float:
        return self._celsius

    @celsius.setter
    def celsius(self, value: float):
        if value < -273.15:
            raise ValueError("Temperature below absolute zero is impossible!")
        self._celsius = value


temp = Temperature(25)
temp.celsius = 30 
print(f"2B. Property (Validated Setter) - Temperature set to: {temp.celsius}°C")


DatabaseConfig = namedtuple("DatabaseConfig", ["host", "port", "dbname"])
db_config = DatabaseConfig(host="localhost", port=5432, dbname="production_db")
print(
    f"3A. NamedTuple (Readable Config) - Connecting to {db_config.dbname} on port {db_config.port}"
)
Color = namedtuple("Color", ["red", "green", "blue"])
sky_blue = Color(135, 206, 235)
color_dict = sky_blue._asdict()  
print("3B. NamedTuple (Dict Conversion):", color_dict)

reviews = ["great", "bad", "great", "ok", "great", "bad", "excellent"]
review_counts = Counter(reviews)
print("4A. Counter (Frequency) - Total counts:", dict(review_counts))
print("    Counter (Top Item) - Most common:", review_counts.most_common(1))

store1_stock = Counter({"apples": 10, "oranges": 5})
store2_stock = Counter({"apples": 3, "oranges": 12, "bananas": 8})
total_stock = store1_stock + store2_stock
print("4B. Counter (Arithmetic) - Combined Inventory:", dict(total_stock))


recent_logs = deque(maxlen=3)
for i in range(1, 6):
    recent_logs.append(f"Event Log #{i}")
print(
    "5A. Deque (Fixed Capacity Buffer) - Last 3 logs:", list(recent_logs)
)

task_queue = deque(["Task 2", "Task 3"])
task_queue.appendleft("High Priority Task 1")
task_queue.append("Low Priority Task 4")

processed = task_queue.popleft()  #
print(f"5B. Deque (Queue Operation) - Processed: '{processed}'")
print("    Deque (Remaining Queue):", list(task_queue))



sensor_readings = [("temp", 22.5), ("humidity", 60), ("temp", 23.0)]
grouped_data = defaultdict(list)

for key, val in sensor_readings:
    grouped_data[key].append(val)  

print("6A. Defaultdict (Grouping):", dict(grouped_data))

city_populations = defaultdict(int)
city_populations["New York"] += 8400000
city_populations["Tokyo"] += 13900000
print(f"6B. Defaultdict (Safe Lookup) - Paris pop: {city_populations['Paris']}")



cache = OrderedDict([("page1", "HTML1"), ("page2", "HTML2"), ("page3", "HTML3")])
cache.move_to_end("page1")
print("7A. OrderedDict (LRU Reordering) - Order:", list(cache.keys()))

dict1 = OrderedDict([("a", 1), ("b", 2)])
dict2 = OrderedDict([("b", 2), ("a", 1)])
print(f"7B. OrderedDict (Order Equality Test) - Is dict1 == dict2? {dict1 == dict2}")