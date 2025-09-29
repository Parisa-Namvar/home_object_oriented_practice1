from house import House
from person import Person
from product import Product
from visit import Visit
from lesson import Course
from sim import Sim

House1 = House("Tehran",2500000,160)
House1.save()

Person1 = Person("parisa","namvar","0150359136")
Person1.save()

Product1 = Product("Milk","35000","pegah", "04-05-03")
Product1.save()

Lesson1 = Course("math", "mesbah", "3")
Lesson1.save()

Sim1 = Sim("09386650502", "irancel", "parisa namvar")
Sim1.save()

Visit1 = Visit("mashhad", "amirian", "250000", "04-06-20")
Visit1.save()
