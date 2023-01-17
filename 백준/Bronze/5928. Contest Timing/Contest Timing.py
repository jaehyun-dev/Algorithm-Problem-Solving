D, H, M = map(int, input().split())
print(-1 if (D < 11 or (D == 11 and H < 11) or (D == 11 and H == 11 and M < 11)) else ((M - 11) + (H - 11) * 60 + (D - 11) * 1440))