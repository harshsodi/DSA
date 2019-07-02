x = int(raw_input().strip())

while x:

    n, s, t = map(int, raw_input().strip().split())

    s_ = n - s
    t_ = n - t

    print max(s_, t_) + 1

    x -= 1