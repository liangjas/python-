import pygame
import sys
import random

# 初始化Pygame
pygame.init()

# 設置屏幕大小
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("小朋友下樓梯")

clock = pygame.time.Clock()

# 加載圖片並調整大小
try:
    background = pygame.image.load(r'C:/python自學/background.png')
    player_img = pygame.image.load(r'C:\python自學\黑人.jpg')
    stair_img = pygame.image.load(r'C:/python自學/stair.png')
except FileNotFoundError as e:
    print(e)
    sys.exit()

# 調整背景圖片大小以適應屏幕
background = pygame.transform.scale(background, (screen_width, screen_height))

# 調整角色圖片大小（假設角色圖片應該是50x50像素）
player_img = pygame.transform.scale(player_img, (50, 50))

# 調整樓梯圖片大小（假設樓梯圖片應該是100x20像素）
stair_img = pygame.transform.scale(stair_img, (100, 20))

# 設置顏色
white = (255, 255, 255)
red = (255, 0, 0)

# 設置字體
font = pygame.font.Font(None, 74)

# 初始化遊戲狀態
def init_game():
    global player_pos, gravity, player_speed_y, player_speed_x, move_speed, jump_speed, on_ground, scroll_speed, score, stairs
    player_pos = [screen_width // 2, screen_height // 2]
    gravity = 0.5
    player_speed_y = 0
    player_speed_x = 0
    move_speed = 5
    jump_speed = -10
    on_ground = False
    scroll_speed = 2
    score = 0
    stairs = [(random.randint(0, screen_width - stair_img.get_width()), screen_height - i * 100) for i in range(6)]

# 顯示遊戲結束畫面
def game_over_screen():
    screen.fill(white)
    game_over_text = font.render("Game Over", True, red)
    restart_text = font.render("Press Enter to Restart", True, red)
    screen.blit(game_over_text, (screen_width // 2 - game_over_text.get_width() // 2, screen_height // 2 - game_over_text.get_height() // 2))
    screen.blit(restart_text, (screen_width // 2 - restart_text.get_width() // 2, screen_height // 2 + restart_text.get_height()))
    pygame.display.flip()

# 主遊戲循環
def main_game():
    global player_pos, player_speed_y, player_speed_x, on_ground, score, stairs
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # 獲取按鍵狀態
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player_speed_x = -move_speed
        elif keys[pygame.K_RIGHT]:
            player_speed_x = move_speed
        else:
            player_speed_x = 0

        if keys[pygame.K_SPACE] and on_ground:
            player_speed_y = jump_speed
            on_ground = False

        # 更新角色位置
        player_speed_y += gravity
        player_pos[1] += player_speed_y
        player_pos[0] += player_speed_x

        # 簡單的碰撞檢測
        on_ground = False
        player_rect = pygame.Rect(player_pos[0], player_pos[1], player_img.get_width(), player_img.get_height())
        for stair in stairs:
            stair_rect = pygame.Rect(stair[0], stair[1], stair_img.get_width(), stair_img.get_height())
            if player_rect.colliderect(stair_rect) and player_speed_y > 0:
                player_pos[1] = stair[1] - player_img.get_height()
                player_speed_y = 0
                on_ground = True

        # 自動生成新樓梯並移動樓梯
        stairs[:] = [(x, y - scroll_speed) for x, y in stairs if y + stair_img.get_height() > 0]
        while len(stairs) < 6:
            new_stair_x = random.randint(0, screen_width - stair_img.get_width())
            new_stair_y = stairs[-1][1] + 100 if stairs else screen_height - 100
            stairs.append((new_stair_x, new_stair_y))
            score += 1

        # 檢查角色是否死亡（掉出屏幕或碰到屏幕上方）
        if player_pos[1] > screen_height or player_pos[1] < 0:
            running = False
            continue

        # 清屏並繪製背景
        screen.blit(background, (0, 0))

        # 繪製樓梯
        for stair in stairs:
            screen.blit(stair_img, stair)

        # 繪製角色
        screen.blit(player_img, player_pos)

        # 繪製得分
        score_text = font.render(str(score), True, red)
        screen.blit(score_text, (10, 10))

        # 刷新屏幕
        pygame.display.flip()
        clock.tick(30)

# 遊戲主循環
while True:
    init_game()
    main_game()
    game_over_screen()
    # 等待玩家重新開始
    restart = False
    while not restart:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    restart = True
