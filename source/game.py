# -*- coding: utf-8 -*-
"""
Created on Sun Jul  3 17:38:22 2022

@author: angel
"""
import pygame
import random

def colosseum():
    pygame.init()
    screen_width = 1000 
    screen_height = 800
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("colosseum")
    background = pygame.image.load("colosseum.png")
    player = pygame.image.load("player.png")
    monster = pygame.image.load("monster_dog.png")
    #player = pygame.transform.rotate(player,30)
    door = pygame.image.load("door.png")
    
    # 플레이어
    player_size = player.get_rect().size
    player_width = player_size[0]
    player_height = player_size[1]
    player_x_pos = 40
    player_y_pos = 350
    to_x = 0
    to_y = 0
    dash_time = 40
    
    # 몬스터
    monster_size = monster.get_rect().size
    monster_width = monster_size[0]
    monster_height = monster_size[1]
    monster_x_pos = 880
    monster_y_pos = 350
    monster_damage = 10
    
    # 몬스터 스킬
    m_weapon = pygame.image.load("monster_dog_weapon.png")
    m_weapon_size = m_weapon.get_rect().size
    m_weapon_width = m_weapon_size[0]
    m_weapon_height = m_weapon_size[1]
    m_weapons = []
    m_weapon_speed = 5
    m_weapon_damage = 8
    m_time = 40
    m_time_boom = 40
    m_time_boom2 = 40
    boom = pygame.image.load("boom_rl.png")
    boom_size = m_weapon.get_rect().size
    boom_width = m_weapon_size[0]
    boom_height = m_weapon_size[1]
    booms = []
    boom_damage = 18
    m_w_time = 0
    
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
    # 몬스터 스킬 방향 2
    direction3 = 0
    # 플레이어 점수
    score = 0
    i = 0
    #음악
    background_sound = pygame.mixer.Sound("light.wav")
    background_sound.set_volume(0.3)
    background_sound.play(-1)
    
    wing = pygame.mixer.Sound("wing.wav")
    bim = pygame.mixer.Sound("bim.wav")
    
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
        m_w_time += 1
        m_time_boom += 1
        m_time_boom2 += 1
        dash_time += 1
        
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
            monster_x_pos += 2
        if monster_x_pos >= player_x_pos and not player_rect.colliderect(monster_rect):
            monster_x_pos -= 2  
        if monster_y_pos <= player_y_pos and not player_rect.colliderect(monster_rect):
            monster_y_pos += 1
        if monster_y_pos >= player_y_pos and not player_rect.colliderect(monster_rect):
            monster_y_pos -= 1
        
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
                if event.key == pygame.K_SPACE and dash_time > 100:
                    if direction == 1 : 
                        player_x_pos = player_x_pos - 140
                    if direction == 0 : 
                        player_x_pos = player_x_pos + 140 + 40
                    if direction == 2 : 
                        player_y_pos = player_y_pos - 140
                    if direction == 3 : 
                        player_y_pos = player_y_pos + 140 + 40
                    dash_time = 0
                    
                if event.key == pygame.K_SPACE and  event.key == pygame.K_d:
                    player_x_pos = player_x_pos + 140    
                if event.key == pygame.K_j :
                    wing.play()
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
            monster = pygame.image.load("monster_dog2.png")
            if m_time > 250:
                m_weapon_x_pos = monster_x_pos + 50
                m_weapon_y_pos = monster_y_pos + 40
                m_weapons.append([m_weapon_x_pos, m_weapon_y_pos])
                bim.play()
                if player_x_pos > monster_x_pos :
                    direction2 = 1
                else :
                    direction2 = 2
                m_time = 0
                monster = pygame.image.load("monster_dog.png")
      
        
        if m_time_boom > 220 and m_time_boom2 > 220:
            boom_random = random.randint(1,2)
            if boom_random == 1:
                boom = pygame.image.load("boom_rl.png")
            if boom_random == 2:
                boom = pygame.image.load("boom_ud.png")
            booms.clear()
            boomx = random.randint(120,880)
            boomy = random.randint(120,780)
            booms.append([boomx,boomy])
            m_time_boom = 0
        if m_time_boom2 > 280:
            if boom_random == 1:
                boom = pygame.image.load("boom.png")
                for i in range(14):
                    boom_x_pos = i*80
                    boom_y_pos = boomy
                    booms.append([boom_x_pos,boom_y_pos])
            if boom_random == 2:
                boom = pygame.image.load("boom2.png")
                for i in range(14):
                    boom_x_pos = boomx
                    boom_y_pos = i*80
                    booms.append([boom_x_pos,boom_y_pos])
            m_time_boom2 = 0
                
        if direction2 == 1:    
            m_weapons = [ [w[0] + m_weapon_speed, w[1]] for w in m_weapons]
            m_weapons = [ [w[0], w[1]] for w in m_weapons if w[0] < monster_x_pos + 500]
            #if :
             #   m_weapon = pygame.transform.rotate(m_weapon,15)
            
        if direction2 == 2:    
            m_weapons = [ [w[0] - m_weapon_speed, w[1]] for w in m_weapons]
            m_weapons = [ [w[0], w[1]] for w in m_weapons if w[0] > monster_x_pos - 500]
            #m_weapon = pygame.transform.rotate(m_weapon,15)
            
        if m_w_time > 20 :
            i += 1
            if i == 1: 
                m_weapon_ = pygame.transform.rotate(m_weapon,90)
            if i == 2:
                m_weapon = pygame.transform.rotate(m_weapon,-90)
                i = 0
            m_w_time = 0
            
            
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
        
        for boom_x_pos, boom_y_pos in booms:
            screen.blit(boom, (boom_x_pos, boom_y_pos))
            
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

colosseum()
pygame.quit()