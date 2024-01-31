class Person:
    instance_count = 0

    def __init__(self, full_name, date_of_birth, phone_number, city, country, adress):
        self.full_name = full_name
        self.date_of_birth = date_of_birth
        self.phone_number = phone_number
        self.city = city
        self.country = country
        self.adress = adress
        Person.instance_count += 1

    def display_info(self):
        print("ПІБ: ", self.full_name)
        print("Дата народження: ", self.date_of_birth)
        print("Контактний телефон: ", self.phone_number)
        print("Місто: ", self.city)
        print("Країна: ", self.country)
        print("Домашня адреса: ", self.adress)

    def update_phone_number(self, new_phone_number):
        self.phone_number = new_phone_number
        print("Контактний телефон оновлено.")

    def update_adress(self, new_city, new_country, new_address):
        self.city = new_city
        self.country = new_country
        self.adress = new_address
        print("Адресу проживання оновлено.")

    @staticmethod
    def get_instance_count():
        return Person.instance_count



person1 = Person("Олексій", "06.12.2006", "+380765870090", "Київ", "Україна", "вул. Академіка Янгеля 16/2")
person2 = Person("Іван", "15.05.1990", "+380987654321", "Львів", "Україна", "вул. Шевченка, 5")

print("Кількість створених об'єктів класу Людина:", Person.get_instance_count())
