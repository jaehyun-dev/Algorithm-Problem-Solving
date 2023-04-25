import datetime
a = input()
h_a = int(a[0:2])
m_a = int(a[3:5])
s_a = int(a[6:8])
sec_a = h_a * 3600 + m_a * 60 + s_a
m = datetime.timedelta(seconds= sec_a)
b = input()
h_b = int(b[0:2])
m_b = int(b[3:5])
s_b = int(b[6:8])
sec_b = h_b * 3600 + m_b * 60 + s_b
n = datetime.timedelta(seconds= sec_b)
print(str(n - m)[-8:].strip().zfill(8) if m != n else "24:00:00")