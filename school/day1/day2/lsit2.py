movie_list = ["아바타","왕과 사는 남자","살목지","극한직업"]
print(movie_list)

movie_list.insert(1, "범죄도시") # 리스트에 삽입
print(movie_list)

movie_list.append("슈퍼맨") # 리스트에 추가
print(movie_list)

movie_list.remove("살목지")
print(movie_list)

del movie_list[2] # del: 요소 위치 지정 삭제
print(movie_list)