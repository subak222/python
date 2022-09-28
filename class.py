class human:
    def __init__(self, height, age):
        self.height = height    #멤버변수
        self.age = age

    def how_old(self):              #메소드
        print(self.age, "살 입니다")

    def how_tall(self):             #메서드
        print(self.height, "cm 입니다")
    
soobin = human(170, 17)         #인스턴스 생성
leedongwook = human(183, 42)    #인스턴스 생성


soobin.how_old()
human.how_old(soobin)


leedongwook.how_old()

print(soobin.height)

