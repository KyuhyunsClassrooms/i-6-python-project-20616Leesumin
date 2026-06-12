# AI 활용 자유 주제 파이썬 미니 프로젝트
# 이름 또는 학번: 20616 이수민
# 프로젝트 주제: 패션 스타일 추천 프로그램

# [1단계] 데이터 창고 (2차원 리스트)
fashion = [
    ["후드티 + 청바지", "캐주얼", "봄", "학교", "편하고 활동하기 좋은 스타일"],
    ["니트 + 슬랙스", "단정", "겨울", "학교", "따뜻하면서 깔끔한 스타일"],
    ["블라우스 + 롱스커트", "러블리", "봄", "데이트", "부드럽고 여성스러운 느낌"],
    ["크롭티 + 와이드팬츠", "스트릿", "여름", "외출", "개성 있고 시원한 스타일"],
    ["셔츠 + 슬랙스", "단정", "가을", "발표", "차분하고 신뢰감을 주는 스타일"],
    ["가디건 + 원피스", "러블리", "가을", "데이트", "따뜻하고 부드러운 스타일"],
    ["반팔티 + 반바지", "캐주얼", "여름", "외출", "가볍고 편한 스타일"],
    ["가죽자켓 + 검정바지", "스트릿", "가을", "외출", "강한 개성이 드러나는 스타일"]
]


# [2단계] 안내 담당 함수
def show_intro():
    print("=============================================")
    print("👔 패션 스타일 맞춤 추천 프로그램 👗")
    print("원하는 스타일, 계절, 상황에 맞는 옷을 추천합니다.")
    print("=============================================")


# [3단계] 입력 담당 함수
def get_user_input():
    style = input("원하는 스타일을 입력하세요(캐주얼/단정/러블리/스트릿): ")
    season = input("계절을 입력하세요(봄/여름/가을/겨울): ")
    situation = input("상황을 입력하세요(학교/외출/데이트/발표): ")
    return style, season, situation


# [4단계] 점수 계산 함수 (가장 기본적이고 직관적인 구조)
def calculate_score(item, style, season, situation):
    score = 0
    
    if item[1] == style:
        score = score + 1
        
    if item[2] == season:
        score = score + 1
        
    if item[3] == situation:
        score = score + 1
        
    return score


# [5단계] 베스트 패션 검색 함수 (복잡한 정렬 제외, 점수순 배치)
def find_best_fashion(style, season, situation):
    results = []

    # 1등(3점 만점) 짜리 먼저 찾아서 넣기
    for item in fashion:
        score = calculate_score(item, style, season, situation)
        if score == 3:
            results.append([item[0], item[1], item[2], item[3], item[4], score])

    # 2등(2점) 짜리 나중에 찾아서 넣기 (자연스럽게 점수 높은 순 정렬)
    for item in fashion:
        score = calculate_score(item, style, season, situation)
        if score == 2:
            results.append([item[0], item[1], item[2], item[3], item[4], score])

    return results


# [6단계] 결과 출력 담당 함수 (기본 문자열 더하기 사용)
def print_result(results):
    print("\n[추천 결과]")

    if len(results) == 0:
        print("조건에 맞는 패션 스타일이 없습니다.")
        print("다른 조건으로 다시 입력해 보세요.")
    else:
        for item in results:
            print("- 옷차림: " + item[0] + " (일치 점수: " + str(item[5]) + "점)")
            print("  스타일: " + item[1] + " | 계절: " + item[2] + " | 상황: " + item[3])
            print("  설명: " + item[4])
            print("-" * 45)


# [7단계] 메인 총괄 함수
def main():
    show_intro()
    style, season, situation = get_user_input()
    results = find_best_fashion(style, season, situation)
    print_result(results)


# 프로그램 진짜 실행하기
main()