class Board:
    def set_data(self, title, writer):
        self.title = title # 오른쪽 title은 호출할때 받아온 매개변수 값
                           # 왼쪽 title은 객체(붕어빵)의 멤버변수
                           # 내 자신(객체) 의미: self
        self.writer = writer
        self.cnt = 0
    
    def cntup(self): # 조회수 구하는 함수
        self.cnt += 1


# 게시판 객체 생성
#       Board board1 = new Board() 자바

board1 = Board() # 객페변수 = 클래스(매새변수)
board2 = Board()
board1.set_data("자바의 정석", "홍길동")
board2.set_data("파이썬의 정석", "이순신")

board1.cntup()
board1.cntup()
board2.cntup()

print(board1.title, board1.writer, board1.cnt)
print(board2.title, board2.writer, board2.cnt)

board3 = Board()
# oard3.cntup() # 오류 set_data() 호풀을 안 했으므로 cnt를 생성하지 않음