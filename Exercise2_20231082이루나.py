import os

# 파일 이름 정의
FILE_NAME = "contacts.txt"

def load_contacts():
    """
    프로그램 시작 시 파일에서 연락처를 불러오는 함수
    요구사항: 예외 처리(try/except) 사용 
    """
    contacts = {}
    try:
        # 파일이 있으면 읽기 모드로 열기
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            for line in f:
                # 파일 포맷이 "이름:전화번호"라고 가정
                if ":" in line:
                    name, phone = line.strip().split(":", 1)
                    contacts[name] = phone
        print(f"-> 기존 파일에서 {len(contacts)}개의 연락처를 불러왔습니다.")
    except FileNotFoundError:
        # 파일이 없으면 빈 딕셔너리 반환
        print("-> 저장된 파일이 없어 새로 시작합니다.")
    return contacts

def save_contacts(contacts):
    """
    프로그램 종료 시 연락처를 파일에 저장하는 함수
    요구사항: 파일 핸들링 사용 [cite: 256]
    """
    try:
        with open(FILE_NAME, "w", encoding="utf-8") as f:
            for name, phone in contacts.items():
                f.write(f"{name}:{phone}\n")
        print("-> 연락처가 파일(contacts.txt)에 안전하게 저장되었습니다.")
    except Exception as e:
        print(f"-> 저장 중 오류가 발생했습니다: {e}")

def add_contact(contacts):
    """연락처 추가 함수"""
    name = input("이름 입력: ").strip()
    if name in contacts:
        print("이미 존재하는 이름입니다.")
        return
    
    phone = input("전화번호 입력: ").strip()
    # 요구사항: 딕셔너리에 이름(키)과 전화번호(값) 저장 
    contacts[name] = phone
    print(f"-> '{name}'님이 추가되었습니다.")

def view_contacts(contacts):
    """전체 연락처 보기 함수"""
    print("\n--- 연락처 목록 ---")
    if not contacts:
        print("저장된 연락처가 없습니다.")
    else:
        for name, phone in contacts.items():
            print(f"이름: {name} | 전화번호: {phone}")
    print("-------------------")

def search_contact(contacts):
    """연락처 검색 함수"""
    name = input("검색할 이름 입력: ").strip()
    # 요구사항: 딕셔너리에서 이름으로 찾기 [cite: 263]
    if name in contacts:
        print(f"-> 검색 결과: {name}님의 번호는 {contacts[name]} 입니다.")
    else:
        print(f"-> '{name}'님을 찾을 수 없습니다.")

def main():
    """메인 실행 함수"""
    # 1. 시작 시 파일 로드 (선택 사항 구현) [cite: 265]
    my_contacts = load_contacts()

    while True:
        # 2. 메뉴 출력 (반복문 사용) [cite: 260]
        print("\n=== 연락처부 (Contact Book) ===")
        print("1. 연락처 추가 (Add)")
        print("2. 전체 보기 (View)")
        print("3. 검색 (Search)")
        print("4. 종료 (Quit)")
        
        choice = input("선택하세요 (1-4): ")

        if choice == '1':
            add_contact(my_contacts)
        elif choice == '2':
            view_contacts(my_contacts)
        elif choice == '3':
            search_contact(my_contacts)
        elif choice == '4':
            # 3. 종료 전 파일 저장 
            save_contacts(my_contacts)
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 입력입니다. 1~4번 중 하나를 입력해주세요.")

if __name__ == "__main__":
    main()
