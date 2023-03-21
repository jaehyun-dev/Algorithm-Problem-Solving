import datetime
y_t, m_t, d_t = map(int, input().split())
y_d, m_d, d_d = map(int, input().split())
a = datetime.date(y_t, m_t, d_t)
b = datetime.date(y_d, m_d, d_d)
print(f"D-{str(b-a)[:(str(b-a).index('d'))]}" if (y_d, m_d, d_d) < (y_t + 1000, m_t, d_t) else "gg")