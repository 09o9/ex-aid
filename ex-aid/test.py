import time
def main():
    print('\033[91m _______  ___ ___          _______  _______  _____')
    print('\033[91m|    ___||   |   | ______ |   _   ||_     _||     ')
    print('\033[91m[|    ___||-     -||______||       | _|   |_ |  --  |')
    print('\033[91m|_______||___|___|        |___|___||_______||_____/\n\n\n')
     

    username = input("\033[92mAdministrator ID: ")
    password = input("\033[92mAdministrator Pssword: ")

    # 예시 계정 아이디, 비밀번호 (수정가능)
    valid_username = "qwer"
    valid_password = "qwer1"

    
    if username == valid_username and password == valid_password:
        print("\033[31m[system] log-in succeed!")
        print("\n\n\n\n\033[31m[system]ex-aid package downloading...")

        for i in range(30):
            
            if i < 6:
                color_code = '\033[31m'  # 빨간색
            elif i < 11:
                color_code = '\033[33m'  # 노란색
            elif i < 16:
                color_code = '\033[32m'  # 녹색
            elif i < 21:
                color_code = '\033[36m'  # 청록색
            elif i < 26:
                color_code = '\033[34m'  # 파란색
            else:
                color_code = '\033[35m'  # 자주색

            
            print(f"{color_code}[{'#' * i}{' ' * (29 - i)}]\033[0m", end="\r")
            time.sleep(1)

        print("\033[31m[##############################]")
        print("\033[31m[system] Download completed!")
    else:
        print("\033[31m[system] Invalid username or password.")

    
    input("\033[95m[system] Press Enter to join.")


if __name__ == "__main__":
    main()
