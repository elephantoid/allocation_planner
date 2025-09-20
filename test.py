import psycopg2

# channel_binding 파라미터 제거한 URL 사용
DATABASE_URL = 'postgresql://neondb_owner:npg_OdMDaK6eXCs5@ep-dawn-thunder-a7sh1upy-pooler.ap-southeast-2.aws.neon.tech/neondb?sslmode=require'

try:
    conn = psycopg2.connect(DATABASE_URL)
    print("✅ Neon 데이터베이스 연결 성공!")
    
    cursor = conn.cursor()
    cursor.execute("SELECT current_database(), current_user, version();")
    result = cursor.fetchone()
    print(f"데이터베이스: {result[0]}")
    print(f"사용자: {result[1]}")
    print(f"PostgreSQL 버전: {result[2]}")
    
    cursor.close()
    conn.close()
    
except Exception as e:
    print(f"❌ 연결 실패: {e}")