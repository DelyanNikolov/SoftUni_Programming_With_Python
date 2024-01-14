from collections import deque

bullet_price = int(input())
barrel_size = int(input())
bullets = deque([int(bul) for bul in input().split()])
locks = deque([int(lock) for lock in input().split()])
intelligence = int(input())

shots_fired = 0
bullets_in_barrel = barrel_size
while bullets and locks:
    current_lock = locks.popleft()
    current_bullet = bullets.pop()
    if current_bullet > current_lock:
        print("Ping!")
        locks.appendleft(current_lock)
    else:
        print("Bang!")
    bullets_in_barrel -= 1
    shots_fired += 1
    if bullets_in_barrel == 0 and bullets:
        if len(bullets) >= barrel_size:
            bullets_in_barrel = barrel_size
        else:
            bullets_in_barrel = len(bullets)
        print("Reloading!")

if not locks:
    money_earned = intelligence - (shots_fired * bullet_price)
    print(f"{len(bullets)} bullets left. Earned ${money_earned}")
else:
    print(f"Couldn't get through. Locks left: {len(locks)}")
