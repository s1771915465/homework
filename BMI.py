class BMI:
    def __init__(self, name, age, weight, high):
        self.name = name
        self.age = age
        self.weight = weight
        self.high = high
        self.bmi = self.weight / self.high / self.high

    def status_get(self):
        print("BMI是{:.2f}".format(self.bmi), end=",")
        if self.bmi < 18.5:
            print("健康状况:偏瘦。")
        elif 18.5 <= self.bmi < 24:
            print("健康状况:正常。")
        elif 24 <= self.bmi < 30:
            print("健康状况:偏胖。")
        elif self.bmi > 30:
            print("健康状况:肥胖。")

    def search_name(self):
        print("用户名为{n}".format(n=self.name), end=",")

    def search_age(self):
        print("年龄为{n}岁".format(n=self.age), end=",")

    def search_weight(self):
        print("体重为{n}千克".format(n=self.weight), end=",")

    def search_high(self):
        print("身高为{n}米".format(n=self.high), end=",")


if __name__ == "__main__":
    input_name = input("名字:")
    input_age = int(input("年龄:"))
    input_weight = float(input("体重:"))
    input_high = float(input("身高:"))
    person_information = BMI(input_name, input_age, input_weight, input_high)
    person_information.search_name()
    person_information.search_age()
    person_information.search_weight()
    person_information.search_high()
    person_information.status_get()

