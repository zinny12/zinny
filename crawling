import requests
import time
import os

# ── 텔레그램 설정 ──
BOT_TOKEN = "5638730978:AAErxfMUsSu37fKHFHWMmpmbuig94t1qWQo"
CHAT_ID = "5711468830"
TELEGRAM_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

# ── 네이버 API 설정 ──
# GitHub Actions: Settings → Secrets에 등록하면 env로 자동 주입
# 로컬 실행: 아래 따옴표 안에 직접 입력
NAVER_CLIENT_ID = os.environ.get("NAVER_CLIENT_ID", "V659bqCpQ3zj7yCnouN4")
NAVER_CLIENT_SECRET = os.environ.get("NAVER_CLIENT_SECRET", "GbNd66xYJ2")

# ── 검색 설정 ──
DISPLAY = 20  # 키워드당 최대 기사 수 (최대 100)
DELAY = 0.1

# ══════════════════════════════════════════
# 1) 산업 키워드
# ══════════════════════════════════════════
INDUSTRY_KEYWORDS = [
    "하이닉스", "삼성전자", "반도체", "DRAM", "NAND", "메모리",
]

# ══════════════════════════════════════════
# 2) 밸류체인 종목
# ══════════════════════════════════════════
VALUE_CHAIN = {
    "Materials": [
        "SK머티리얼즈", "한솔케미칼", "솔브레인", "동진쎄미켐", "포토레지스트",
        "이엔에프테크놀로지", "덕산테코피아", "백광산업", "경인양행", "디엔에프",
        "오션브릿지", "와이씨켐", "지오엘리먼트", "엘티씨", "코미코",
        "후성", "티이엠씨", "레이크머티리얼즈", "원익머티리얼즈", "제이아이테크",
    ],
    "Parts": [
        "티씨케이", "하나머티리얼즈", "윌덱스", "비씨엔씨", "케이엔제이",
        "에스앤에스텍", "펠리클", "에프에스티", "아스플로", "한솔아이원스",
        "뉴파워프라즈마", "원익QnC", "메카로", "미코",
    ],
    "Equipment": [
        "원익IPS", "유진테크", "주성엔지니어링", "테스", "HPSP",
        "파크시스템스", "넥스틴", "오로스테크놀로지", "케이씨텍", "피에스케이",
        "에이피티씨", "와이아이케이", "엘오티베큠", "싸이맥스", "제우스",
        "디바이스이엔지", "저스템", "원익홀딩스", "에스티아이", "씨앤지하이테크",
        "GST", "유니셈", "지앤비에스엔지니어링",
    ],
    "OSAT": [
        "SFA반도체", "하나마이크론", "네패스", "엘비세미콘", "한양디지텍",
        "아이텍", "시그네틱스", "윈팩", "두산테스나", "네패스아크",
        "에이팩트", "큐알티",
    ],
    "Packaging Materials": [
        "심텍", "아비코전자", "DDR5", "해성디에스", "엠케이전자", "덕산하이메탈",
    ],
    "Test & Inspection": [
        "리노공업", "ISC", "오킨스전자", "티에스이", "샘씨엔에스",
        "타이거일렉", "한미반도체", "이오테크닉스", "프로텍", "유니테스트",
        "피에스케이홀딩스", "코세스", "네오셈", "디아이", "엑시콘",
        "테크윙", "인텍플러스", "신성이엔지", "한양이엔지", "원방테크", "에스엠코어",
    ],
    "Distribution": [
        "미래반도체", "서플러스글로벌",
    ],
}


# ══════════════════════════════════════════
# 네이버 뉴스 API 검색
# ══════════════════════════════════════════
def fetch_news(query, filter_title=False, display=DISPLAY):
    """
    네이버 오픈 API로 뉴스 검색.
    https://developers.naver.com/docs/serviceapi/search/news/news.md
    """
    url = "https://openapi.naver.com/v1/search/news.json"
    headers = {
        "X-Naver-Client-Id": NAVER_CLIENT_ID,
        "X-Naver-Client-Secret": NAVER_CLIENT_SECRET,
    }
    params = {
        "query": query,
        "display": display,
        "sort": "date",  # 최신순
    }

    articles = []
    try:
        resp = requests.get(url, headers=headers, params=params, timeout=10)
        data = resp.json()

        if "items" not in data:
            print(f"  [API ERROR] {query}: {data.get('errorMessage', 'unknown')}")
            return articles

        for item in data["items"]:
            title = item["title"]
            # HTML 태그 제거 (<b>, </b> 등)
            title = title.replace("<b>", "").replace("</b>", "")
            title = title.replace("&quot;", '"').replace("&amp;", "&")
            title = title.replace("&lt;", "<").replace("&gt;", ">")
            link = item["originallink"] or item["link"]

            if filter_title and query not in title:
                continue

            # 마크다운 깨짐 방지
            clean_title = title.replace("[", "").replace("]", " - ")
            clean_title = clean_title.replace("(", "").replace(")", "")
            articles.append(f"[{clean_title}]({link})")

    except Exception as e:
        print(f"  [ERROR] {query}: {e}")

    time.sleep(DELAY)
    return articles


# ══════════════════════════════════════════
# 텔레그램 전송
# ══════════════════════════════════════════
def send_telegram(message):
    """4096자 초과 시 자동 분할 전송"""
    MAX_LEN = 4096
    chunks = []
    current = ""
    for line in message.split("\n"):
        if len(current) + len(line) + 1 > MAX_LEN:
            chunks.append(current)
            current = line
        else:
            current = current + "\n" + line if current else line
    if current:
        chunks.append(current)

    for i, chunk in enumerate(chunks, 1):
        try:
            resp = requests.post(TELEGRAM_URL, json={
                "chat_id": CHAT_ID,
                "text": chunk,
                "parse_mode": "Markdown",
                "disable_web_page_preview": True,
            }, timeout=10)
            result = resp.json()
            if result.get("ok"):
                print(f"  ✓ 메시지 {i}/{len(chunks)} 전송 완료")
            else:
                print(f"  ✗ 메시지 {i} 실패: {result.get('description')}")
            time.sleep(1)
        except Exception as e:
            print(f"  ✗ 메시지 {i} 전송 에러: {e}")


# ══════════════════════════════════════════
# 메시지 조립
# ══════════════════════════════════════════
def build_message():
    sections = []
    total_articles = 0

    # ── Part 1: 산업 키워드 ──
    industry_lines = []
    for kw in INDUSTRY_KEYWORDS:
        articles = fetch_news(kw, filter_title=False)
        count = len(articles)
        total_articles += count
        print(f"  {kw}: {count}건")
        if articles:
            industry_lines.append(f"▶ {kw}")
            industry_lines.extend(articles)
            industry_lines.append("")

    if industry_lines:
        sections.append("━━━━━━━━━━━━━━━━━━━━")
        sections.append("📡 산업 키워드 뉴스")
        sections.append("━━━━━━━━━━━━━━━━━━━━")
        sections.extend(industry_lines)

    # ── Part 2: 밸류체인 종목 ──
    for category, companies in VALUE_CHAIN.items():
        cat_lines = []
        for company in companies:
            articles = fetch_news(company, filter_title=True)
            count = len(articles)
            total_articles += count
            if count > 0:
                print(f"  {company}: {count}건")
            if articles:
                cat_lines.append(f"▶ {company}")
                cat_lines.extend(articles)
                cat_lines.append("")

        if cat_lines:
            sections.append(f"\n⎡{category}⎤")
            sections.extend(cat_lines)

    print(f"\n총 {total_articles}건 수집")
    return "\n".join(sections) if sections else None


# ══════════════════════════════════════════
# 실행
# ══════════════════════════════════════════
if __name__ == "__main__":
    print("=" * 40)
    print("반도체 뉴스 트래커 시작")
    print("=" * 40)

    # 1) 네이버 API 연결 테스트
    print("\n[1] 네이버 API 테스트...")
    test = fetch_news("삼성전자", filter_title=False, display=3)
    if test:
        print(f"  ✓ API OK: 삼성전자 {len(test)}건")
    else:
        print("  ✗ API 실패 — Client ID/Secret을 확인하세요")
        print("  → https://developers.naver.com 에서 발급")
        exit(1)

    # 2) 텔레그램 연결 테스트
    print("\n[2] 텔레그램 연결 테스트...")
    try:
        tg_test = requests.get(
            f"https://api.telegram.org/bot{BOT_TOKEN}/getMe", timeout=10
        )
        tg_result = tg_test.json()
        if tg_result.get("ok"):
            print(f"  ✓ 봇 연결 OK: @{tg_result['result']['username']}")
        else:
            print(f"  ✗ 봇 토큰 에러: {tg_result.get('description')}")
            exit(1)
    except Exception as e:
        print(f"  ✗ 네트워크 에러: {e}")
        exit(1)

    # 3) 전체 크롤링 + 전송
    print("\n[3] 전체 크롤링 시작...")
    msg = build_message()

    if msg:
        print(f"\n[4] 텔레그램 전송 중... ({len(msg):,}자)")
        send_telegram(msg)
        print("\n완료!")
    else:
        print("\n수집된 뉴스가 없습니다.")
