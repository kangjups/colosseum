# -*- coding: utf-8 -*-
"""
Created on Sun Jul  3 17:38:22 2022

@author: angel
"""
def colosseum():
    pygame.init()
    screen_width = 1000 
    screen_height = 800
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("colosseum")
    background = pygame.image.load("colosseum.png")
    player = pygame.image.load("player.png")
    monster = pygame.image.load("monster.png")
    door = pygame.image.load("door.png")
    
    # 플레이어
    player_size = player.get_rect().size
    player_width = player_size[0]
    player_height = player_size[1]
    player_x_pos = 40
    player_y_pos = 350
    to_x = 0
    to_y = 0
    
    # 몬스터
    monster_size = monster.get_rect().size
    monster_width = monster_size[0]
    monster_height = monster_size[1]
    monster_x_pos = 880
    monster_y_pos = 350
    monster_damage = 10
    
    # 몬스터 스킬
    m_weapon = pygame.image.load("m_weapon.png")
    m_weapon_size = m_weapon.get_rect().size
    m_weapon_width = m_weapon_size[0]
    m_weapon_height = m_weapon_size[1]
    m_weapons = []
    m_weapon_speed = 6
    m_weapon_damage = 8
    m_time = 40

    boom = pygame.image.load("boom_rl.png")
    boom_size = m_weapon.get_rect().size
    boom_width = m_weapon_size[0]
    boom_height = m_weapon_size[1]
    booms = []
    boom_damage = 18
    
    # 총알
    weapon = pygame.image.load("weapon.png")
    weapon_size = weapon.get_rect().size
    weapon_width = weapon_size[0]
    weapon_height = weapon_size[1]
    weapons = []
    weapons_lt = []
    weapons_up = []
    weapons_down = []
    weapon_speed = 10
    weapon_damage = 5
    
    # 문
    door_size = door.get_rect().size
    door_width = door_size[0]
    door_height = door_size[1]
    
    # 색
    RED = (255,0,0)
    BLUE = (0, 0, 255)
    WHITE = (255,255,255)
    
    # HP
    red_HP = 100
    blue_HP = 100
    font = pygame.font.SysFont(None,30)
    img_red = font.render(str(red_HP),True,WHITE)
    img_blue = font.render(str(blue_HP),True,WHITE)
    img_x = monster_x_pos 
    img_y = monster_y_pos 
    
    game_font = pygame.font.Font(None, 40)
    total_time = 0
    start_ticks = pygame.time.get_ticks()
    elapsed_time_ = 0
    clock = pygame.time.Clock()
    
    # 플레이어 잠시 무적 확인
    p_m = 50
    # 플레이어 스킬 방향
    direction = 0
    # 몬스터 스킬 방향
    direction2 = 0
    # 플레이어 점수
    score = 0
    
    running = True
    #- 1초 == 70 dt
    while running:
        dt = clock.tick(60)
        screen_width = 1000 
        screen_height = 800
        screen = pygame.display.set_mode((screen_width, screen_height))
        
        elapsed_time = int((pygame.time.get_ticks() - elapsed_time_) - start_ticks) / 1000  # 경과 시간을 1000으로 나누어서 초 단위로 표시
        timer = game_font.render(str(int(total_time + elapsed_time)), True, (255,255,255))
        scores = game_font.render(str(int(score)), True, (255,255,255))
        
        p_m += 1
        m_time += 1
        
        # 캐릭터 충돌
        player_rect = player.get_rect()
        player_rect.left = player_x_pos
        player_rect.top = player_y_pos
        
        monster_rect = monster.get_rect()
        monster_rect.left = monster_x_pos
        monster_rect.top = monster_y_pos
        
        door_rect = door.get_rect()
        door_rect.left = 250
        door_rect.top = 0
        
        # 캐릭터 이동        
        player_x_pos += to_x
        player_y_pos += to_y
        
        if monster_x_pos <= player_x_pos and not player_rect.colliderect(monster_rect):
            monster_x_pos += 1
        if monster_x_pos >= player_x_pos and not player_rect.colliderect(monster_rect):
            monster_x_pos -= 1  
        if monster_y_pos <= player_y_pos and not player_rect.colliderect(monster_rect):
            monster_y_pos += 0.5
        if monster_y_pos >= player_y_pos and not player_rect.colliderect(monster_rect):
            monster_y_pos -= 0.5
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False 

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a: 
                    to_x = -6
                    direction = 1
                if event.key == pygame.K_d: 
                    to_x = 6
                    direction = 0
                if event.key == pygame.K_w: 
                    to_y = -6
                    direction = 2
                if event.key == pygame.K_s: 
                    to_y = 6
                    direction = 3
                
                    
                if event.key == pygame.K_q: 
                    print(player_x_pos,player_y_pos)
                    
                    
                if event.key == pygame.K_j :
                    if direction == 0 :
                        weapon_x_pos = player_x_pos + 20
                        weapon_y_pos = player_y_pos + 40
                        weapons.append([weapon_x_pos, weapon_y_pos])
                    if direction == 1 :
                        weapon_x_pos = player_x_pos + 20
                        weapon_y_pos = player_y_pos + 40
                        weapons_lt.append([weapon_x_pos, weapon_y_pos])
                    if direction == 2 :
                        weapon_x_pos = player_x_pos + 10
                        weapon_y_pos = player_y_pos + 40
                        weapons_up.append([weapon_x_pos, weapon_y_pos])
                    if direction == 3 :
                        weapon_x_pos = player_x_pos + 10
                        weapon_y_pos = player_y_pos + 40
                        weapons_down.append([weapon_x_pos, weapon_y_pos])
                    
                if event.key == pygame.K_f and player_rect.colliderect(door_rect): 
                    slype()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a or event.key == pygame.K_d:
                    to_x = 0
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    to_y = 0
        
        # 플레이어 스킬 
        weapons = [ [w[0] + weapon_speed, w[1]] for w in weapons]
        weapons = [ [w[0], w[1]] for w in weapons if w[0] < player_x_pos + 40 + 60 ]
        
        weapons_lt = [ [w[0] - weapon_speed, w[1]] for w in weapons_lt]
        weapons_lt = [ [w[0], w[1]] for w in weapons_lt if w[0] > player_x_pos - 60 ]
        
        weapons_up = [ [w[0], w[1] - weapon_speed] for w in weapons_up]
        weapons_up = [ [w[0], w[1]] for w in weapons_up if w[1] > player_y_pos - 60 ]
        
        weapons_down = [ [w[0], w[1] + weapon_speed] for w in weapons_down]
        weapons_down = [ [w[0], w[1]] for w in weapons_down if w[1] < player_y_pos + 100 + 60 ]
        
        # 몬스터 스킬
        if m_time > 200 :
            monster = pygame.image.load("monster_2.png")
            if m_time > 250:
                m_weapon_x_pos = monster_x_pos + 50
                m_weapon_y_pos = monster_y_pos + 40
                m_weapons.append([m_weapon_x_pos, m_weapon_y_pos])
                if player_x_pos > monster_x_pos :
                    direction2 = 1
                else :
                    direction2 = 2
                m_time = 0
                monster = pygame.image.load("monster.png")
                
        #if m_time > 100 :
         #   boomx = random.randint(100,900)
          #  boomy = random.randint(100,800)
           # booms.append([boomx,boomy])
            #if m_time > 150:
             #   boom = pygame.image.load("boom.png")
              #  for i in range(13):
               #     boom_x_pos = i*80 
                #    boom_y_pos = boomy
                 #   booms.append(boom_x_pos,boom_y_pos)
               # m_time = 0
                
        if direction2 == 1:    
            m_weapons = [ [w[0] + m_weapon_speed, w[1]] for w in m_weapons]
            m_weapons = [ [w[0], w[1]] for w in m_weapons if w[0] < monster_x_pos + 500]

        if direction2 == 2:    
            m_weapons = [ [w[0] - m_weapon_speed, w[1]] for w in m_weapons]
            m_weapons = [ [w[0], w[1]] for w in m_weapons if w[0] > monster_x_pos - 500]
        
        # 몬스터 hp
        img_red = font.render(str(red_HP),True,WHITE) # 레드
        img_x = monster_x_pos + 40
        img_y = monster_y_pos + 95
        
        # 플레이어 hp
        img_blue = font.render(str(blue_HP),True,WHITE) # 블루
        img_blue_x = player_x_pos + 5
        img_blue_y = player_y_pos + 95
        
        if blue_HP <= 99:
            img_blue_x = player_x_pos + 10
        if blue_HP <= 9 :
            img_blue_x = player_x_pos + 20
        
        if red_HP <= 99: 
            img_x = monster_x_pos + 40
        if red_HP <= 9 :
            img_x = monster_x_pos + 45
        if red_HP <= 0:
            score += 1
            monster_x_pos = 880
            monster_y_pos = 350
            red_HP = 100 
        
        # 플레이어와 몬슽가 부딧쳤을때 
        if player_rect.colliderect(monster_rect) and p_m > 50:
            blue_HP -= monster_damage
            img_blue = font.render(str(red_HP),True,RED)
            p_m = 0
        
        # 몬스터 공격 체크
        for m_weapon_idx, m_weapon_val in enumerate(m_weapons):
            m_weapon_pos_x = m_weapon_val[0]
            m_weapon_pos_y = m_weapon_val[1]

            # 무기 정보
            m_weapon_rect = m_weapon.get_rect()
            m_weapon_rect.left = m_weapon_pos_x
            m_weapon_rect.top = m_weapon_pos_y
            
            if m_weapon_rect.colliderect(player_rect):
                #weapons.remove(weapon_val)
                m_weapons.pop(m_weapon_idx)
                blue_HP -= m_weapon_damage
                img_blue = font.render(str(red_HP),True,RED)
        
        # 오른쪽 공격 체크
        for weapon_idx, weapon_val in enumerate(weapons):
            weapon_pos_x = weapon_val[0]
            weapon_pos_y = weapon_val[1]

            # 무기 정보
            weapon_rect = weapon.get_rect()
            weapon_rect.left = weapon_pos_x
            weapon_rect.top = weapon_pos_y
            
            if weapon_rect.colliderect(monster_rect):
                #weapons.remove(weapon_val)
                weapons.pop(weapon_idx)
                red_HP -= weapon_damage
                img_red = font.render(str(red_HP),True,RED)
        
        # 왼쪽 공격 체크
        for weapon_idx, weapon_val in enumerate(weapons_lt):
            weapon_pos_x = weapon_val[0]
            weapon_pos_y = weapon_val[1]

            # 무기 정보
            weapon_rect = weapon.get_rect()
            weapon_rect.left = weapon_pos_x
            weapon_rect.top = weapon_pos_y
            
            if weapon_rect.colliderect(monster_rect):
                #weapons.remove(weapon_val)
                weapons_lt.pop(weapon_idx)
                red_HP -= weapon_damage
                img_red = font.render(str(red_HP),True,RED)
                
        # 위쪽 공격 체크
        for weapon_idx, weapon_val in enumerate(weapons_up):
            weapon_pos_x = weapon_val[0]
            weapon_pos_y = weapon_val[1]

            # 무기 정보
            weapon_rect = weapon.get_rect()
            weapon_rect.left = weapon_pos_x
            weapon_rect.top = weapon_pos_y
             
            if weapon_rect.colliderect(monster_rect):
                #weapons.remove(weapon_val)
                weapons_up.pop(weapon_idx)
                red_HP -= weapon_damage
                img_red = font.render(str(red_HP),True,RED)
                 
        # 아래 공격 체크
        for weapon_idx, weapon_val in enumerate(weapons_down):
            weapon_pos_x = weapon_val[0]
            weapon_pos_y = weapon_val[1]

            # 무기 정보
            weapon_rect = weapon.get_rect()
            weapon_rect.left = weapon_pos_x
            weapon_rect.top = weapon_pos_y
            
            if weapon_rect.colliderect(monster_rect):
                #weapons.remove(weapon_val)
                weapons_down.pop(weapon_idx)
                red_HP -= weapon_damage
                img_red = font.render(str(red_HP),True,RED)
                
        for boom_idx, boom_val in enumerate(booms):
            boom_pos_x = boom_val[0]
            boom_pos_y = boom_val[1]

            # 무기 정보
            boom_rect = boom.get_rect()
            boom_rect.left = boom_pos_x
            boom_rect.top = boom_pos_y
            
            if boom_rect.colliderect(player_rect):
                #weapons.remove(weapon_val)
                booms.pop(boom_idx)
                blue_HP -= boom_damage
                img_blue = font.render(str(red_HP),True,RED)
                
        screen.blit(background, (0, 0))
        screen.blit(door, (250, 0))
        
        #for boom_x_pos, boom_y_pos in booms:
         #   screen.blit(boom, (boom_x_pos, boom_y_pos))
            
        for m_weapon_x_pos, m_weapon_y_pos in m_weapons:
            screen.blit(m_weapon, (m_weapon_x_pos, m_weapon_y_pos))
        for weapon_x_pos, weapon_y_pos in weapons:
            screen.blit(weapon, (weapon_x_pos, weapon_y_pos))
        for weapon_x_pos, weapon_y_pos in weapons_lt:
            screen.blit(weapon, (weapon_x_pos, weapon_y_pos))
        for weapon_x_pos, weapon_y_pos in weapons_up:
            screen.blit(weapon, (weapon_x_pos, weapon_y_pos))
        for weapon_x_pos, weapon_y_pos in weapons_down:
            screen.blit(weapon, (weapon_x_pos, weapon_y_pos))
            
        screen.blit(monster, (monster_x_pos, monster_y_pos))
        screen.blit(player, (player_x_pos, player_y_pos))
            
        screen.blit(img_blue,(img_blue_x,img_blue_y))
        screen.blit(img_red, (img_x,img_y))
        screen.blit(timer,(0,0))
        screen.blit(scores,(100,0))
        #screen.blit(score, (10, 10))
        pygame.display.update()
        
def slype():
    
    def knight_room():
        pygame.init()
        background = pygame.image.load("knight_room.png")
        pygame.display.set_caption("knight_room")
        pygame.mouse.get_pos()
        clock = pygame.time.Clock()
        running = True
        while running:
            dt = clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False 
                if event.type == pygame.MOUSEBUTTONDOWN:
                    a = 4
                    running = False
            screen.blit(background, (0, 0))
            pygame.display.update()
        return a     
    def dealer_room():
        pygame.init()
        background = pygame.image.load("dealer_room.png")
        pygame.display.set_caption("dealer_room")
        clock = pygame.time.Clock()
        running = True
        while running:
            dt = clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False 
            screen.blit(background, (0, 0))
            pygame.display.update()
            
    pygame.init()
    screen_width = 900 
    screen_height = 300
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("slype")
    player = pygame.image.load("player.png")
    background = pygame.image.load("slype.png")
    knight = pygame.image.load("knight.png")
    dealer = pygame.image.load("dealer.png")
    door = pygame.image.load("door.png")
    
    # 플레이어
    player_size = player.get_rect().size
    player_width = player_size[0]
    player_height = player_size[1]
    player_x_pos = 400
    player_y_pos = 160
    to_x = 0
    to_y = 0
    
    # 기사
    knight_size = knight.get_rect().size
    knight_width = knight_size[0]
    knight_height = knight_size[1]
    
    # 상인
    dealer_size = dealer.get_rect().size
    dealer_width = dealer_size[0]
    dealer_height = dealer_size[1]    
    
    # 문
    door_size = door.get_rect().size
    door_width = door_size[0]
    door_height = door_size[1]
    
    clock = pygame.time.Clock()
    running = True
    #-
    while running:
        dt = clock.tick(60)
        
        screen_width = 900 
        screen_height = 300
        screen = pygame.display.set_mode((screen_width, screen_height))
        
        # 캐릭터 이동        
        player_x_pos += to_x
        player_y_pos += to_y
        
        if player_x_pos <= 40:
            player_x_pos = 40
        elif player_x_pos >= 760:
            player_x_pos = 760
        if player_y_pos <= 40:
            player_y_pos = 40
        elif player_y_pos >= 160:
            player_y_pos = 160
        
        # 캐릭터 충돌
        player_rect = player.get_rect()
        player_rect.left = player_x_pos
        player_rect.top = player_y_pos
        
        knight_rect = knight.get_rect()
        knight_rect.left = 740
        knight_rect.top = 140
        
        dealer_rect = dealer.get_rect()
        dealer_rect.left = 55
        dealer_rect.top = 55
        
        door_rect = door.get_rect()
        door_rect.left = 400
        door_rect.top = 255
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False 

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a: 
                    to_x = -5
                if event.key == pygame.K_d: 
                    to_x = 5
                if event.key == pygame.K_w: 
                    to_y = -5
                if event.key == pygame.K_s: 
                    to_y = 5
                if event.key == pygame.K_q: 
                    print(player_x_pos,player_y_pos)
                if event.key == pygame.K_f and player_rect.colliderect(door_rect): 
                    running = False
                if event.key == pygame.K_f and player_rect.colliderect(knight_rect): 
                    a = knight_room()
                    if a == 4:
                        colosseum()
                if event.key == pygame.K_f and player_rect.colliderect(dealer_rect): 
                    dealer_room()
                
                    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a or event.key == pygame.K_d:
                    to_x = 0
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    to_y = 0
        
        screen.blit(background, (0, 0))
        screen.blit(knight, (740, 140))
        screen.blit(dealer, (55, 55))
        screen.blit(door, (400, 255))
        screen.blit(player, (player_x_pos, player_y_pos))
        pygame.display.update()
        
def room():
    def mentor_room():
        pygame.init()
        background = pygame.image.load("mentor_room.png")
        pygame.display.set_caption("mentor_room")
        clock = pygame.time.Clock()
        running = True
        while running:
            dt = clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False 
            screen.blit(background, (0, 0))
            pygame.display.update()
            
    pygame.init()
    screen_width = 500 
    screen_height = 500
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("room")
    background = pygame.image.load("room.png")
    player = pygame.image.load("player.png")
    mentor = pygame.image.load("mentor.png")
    door = pygame.image.load("door.png")
    
    # 플레이어
    player_size = player.get_rect().size
    player_width = player_size[0]
    player_height = player_size[1]
    player_x_pos = 350
    player_y_pos = 350
    to_x = 0
    to_y = 0
    
    # 스승
    mentor_size = mentor.get_rect().size
    mentor_width = mentor_size[0]
    mentor_height = mentor_size[1]
    
    # 문
    door_size = door.get_rect().size
    door_width = door_size[0]
    door_height = door_size[1]
    
    clock = pygame.time.Clock()
    running = True
    #-
    while running:
        dt = clock.tick(60)
        screen_width = 500 
        screen_height = 500
        screen = pygame.display.set_mode((screen_width, screen_height))
       
        # 캐릭터 이동        
        player_x_pos += to_x
        player_y_pos += to_y
        
        if player_x_pos <= 45:
            player_x_pos = 45
        elif player_x_pos >= 360:
            player_x_pos = 360
        if player_y_pos <= 40:
            player_y_pos = 40
        elif player_y_pos >= 365:
            player_y_pos = 365
        
        # 캐릭터 충돌
        player_rect = player.get_rect()
        player_rect.left = player_x_pos
        player_rect.top = player_y_pos
        
        mentor_rect = mentor.get_rect()
        mentor_rect.left = 65
        mentor_rect.top = 65
        
        door_rect = door.get_rect()
        door_rect.left = 250
        door_rect.top = 15
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False 

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a: 
                    to_x = -5
                if event.key == pygame.K_d: 
                    to_x = 5
                if event.key == pygame.K_w: 
                    to_y = -5
                if event.key == pygame.K_s: 
                    to_y = 5
                if event.key == pygame.K_q: 
                    print(player_x_pos,player_y_pos)
                    
                if event.key == pygame.K_f and player_rect.colliderect(door_rect): 
                    slype()
                if event.key == pygame.K_f and player_rect.colliderect(mentor_rect): 
                    mentor_room()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a or event.key == pygame.K_d:
                    to_x = 0
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    to_y = 0
                    
        screen.blit(background, (0, 0))
        screen.blit(door, (250, 15))
        screen.blit(mentor,(65,65))
        screen.blit(player, (player_x_pos, player_y_pos))
        pygame.display.update()
        
import pygame
import random
colosseum()
pygame.quit()