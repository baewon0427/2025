class Prescription:
    def __init__(self):
        self.patient_name = "이름"
        self.age = 0
        self.medications = []

    def enter(self):
        self.patient_name = input("환자 이름을 입력하세요: ")
        self.age = int(input("환자 나이를 입력하세요: "))
        meds = input("처방된 약을 쉼표(,)로 구분하여 입력하세요: ")
        self.medications = meds.split(",")

    def pp(self):
        print(f"환자: {self.patient_name} ({self.age}세)")
        print("처방된 약:", ", ".join(self.medications))
        print("-" * 30)

    def main(self):
        num = int(input("몇 개의 처방전을 입력하시겠습니까? "))
        plist = []

        for _ in range(num):
            p = Prescription()
            p.enter()
            plist.append(p)

        print("\n📄 모든 처방전 목록:")
        for p in plist:
            p.pp()

p = Prescription()
p.main()
