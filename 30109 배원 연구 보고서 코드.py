class Prescription:
    def __init__(self):
        self.patient_name = ""
        self.age = 0
        self.medications = []

    def enter(self):
        self.patient_name = input("환자 이름을 입력하세요: ")
        self.age = int(input("환자 나이를 입력하세요: "))
        print("처방된 약을 선택하세요:")
        print("1. 디아제팜(Diazepam)")
        print("2. 아미트립틸린(Amitriptyline)")
        print("3. 와파린(Warfarin)")
        print("4. 글리메피리드(Glimepiride)")
        print("5. 아세트아미노펜(Acetaminophen)")
        choices = input("선택 (쉼표로 구분하여 번호 입력): ")
        choice_list = choices.split(",")
        for choice in choice_list:
            if choice == "1":
                self.medications.append("디아제팜(Diazepam)")
            elif choice == "2":
                self.medications.append("아미트립틸린(Amitriptyline)")
            elif choice == "3":
                self.medications.append("와파린(Warfarin)")
            elif choice == "4":
                self.medications.append("글리메피리드(Glimepiride)")
            elif choice == "5":
                self.medications.append("아세트아미노펜(Acetaminophen)")

    def pp(self):
        print(f"환자: {self.patient_name} ({self.age}세)")
        print("처방된 약물:", ", ".join(self.medications))
        print("-" * 30)
        for med in self.medications:
            if med == "디아제팜(Diazepam)":
                print("🔴 디아제팜(Diazepam) - 고위험군")
                print("  - 졸음과 어지럼증 유발")
                print("  - 인지 기능 저하로 낙상 위험 증가")
                print("  📌 복약 일정: 취침 30분 전 복용 (낙상 예방)")
            elif med == "아미트립틸린(Amitriptyline)":
                print("🔴 아미트립틸린(Amitriptyline) - 고위험군")
                print("  - 심혈관 부작용 위험 증가")
                print("  - 인지 기능 저하 가능성")
                print("  📌 복약 일정: 취침 전 복용 권장")
            elif med == "와파린(Warfarin)":
                print("🔴 와파린(Warfarin) - 고위험군")
                print("  - 출혈 위험 증가")
                print("  - 다른 약물과 상호작용 가능성 높음")
                print("  📌 복약 일정: 매일 같은 시간 복용 (출혈 위험 관리)")
            elif med == "글리메피리드(Glimepiride)":
                print("🟠 글리메피리드(Glimepiride) - 중위험군")
                print("  - 저혈당 위험 증가")
                print("  📌 복약 일정: 아침 식사 직전 복용")
            elif med == "아세트아미노펜(Acetaminophen)":
                print("🟢 아세트아미노펜(Acetaminophen) - 저위험군")
                print("  - 일반적으로 안전하나 과다 복용 시 간 손상 위험")
                print("  📌 복약 일정: 필요 시 복용하되, 1일 최대 4g 초과하지 않도록 주의")
            print("-" * 30)

    def main(self):
        self.enter()
        print("\n[결과 출력]")
        self.pp()

if __name__ == "__main__":
    p = Prescription()
    p.main()
