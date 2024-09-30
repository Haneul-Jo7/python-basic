
# 인사말 관련 모듈
# 셀에서 파일로 저장하는 방법 / jupyter notebook feature. magic command
__version__ = 1.0

def print_greeting(name):
    print(f"{name}님 안녕하세요.")

def print_welcome(name):
    print(f"{name}님 환영합니다.")

def get_greeting(name):
    return f"{name}님 안녕하세요."

class Hello:

    def __init__(self, name):
        self.name = name

    def kor_greet(self):
        return f"{self.name}님 안녕하세요."

    def eng_greet(self):
        return f"Hello {self.name}~!"

print("준비가 완료되었습니다.")

# main module 일 때만 아래에 코드가 실행되었으면 좋겠다. 
print(__name__) 
if __name__ == "__main__": # main module 일 때만 실행. 
    g = get_greeting("홍길동")
    print(g)
    print_welcome("유관순")