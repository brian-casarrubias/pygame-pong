import pygame, os, time, random

pygame.init()




WINDOW_WIDTH = 1920
WINDOW_HEIGHT = 1080
WINDOW_TITLE = 'Hell Pong'

AUDIO_PATH = 'C:\\Users\\Brian\\Desktop\\pong final\\audio'
IMAGE_PATH = 'C:\\Users\\Brian\\Desktop\\pong final\\images'


class Colors:
    pass
    custom = pygame.Color('White')
    custom1 = pygame.Color('Red')
    custom2 = pygame.Color('Green')
    custom3 = pygame.Color('Brown')
    custom4 = pygame.Color('Orange')
    custom5 = pygame.Color('Purple')
 
class GameState:

    hover_play = False
    hover_store = False
    hover_quit = False
    is_paused = True
    cheat_1 = False

    def __init__(self, is_game, is_store, is_main_menu_, is_running):
        self.is_game = is_game
        self.is_store = is_store
        self.is_main_menu = is_main_menu_
        self.is_running = is_running

    ######################GAME STATES ##################################
    @property
    def game(self):
        return self.is_game
    @game.setter
    def game(self, bool):
        self.is_game = bool

    @property
    def store(self):
        return self.is_store
    @store.setter
    def store(self, bool):
        self.is_store = bool
    
    @property
    def menu(self):
        return self.is_store
    @menu.setter
    def menu(self, bool):
        self.is_main_menu = bool

    @property
    def is_play(self):
        return self.is_running
    
    @is_play.setter
    def is_play(self, bool):
        self.is_running = bool
    
    #######################################################
    #############     Hover States ################
    @property
    def hover_is_play(self):
        return self.hover_play
    @hover_is_play.setter
    def hover_is_play(self, bool):
        self.hover_play = bool

    @property
    def hover_is_store(self):
        return self.hover_store
    
    @hover_is_store.setter
    def hover_is_store(self, bool):
        self.hover_store = bool

    @property
    def hover_is_quit(self):
        return self.hover_quit
    
    @hover_is_quit.setter
    def hover_is_quit(self, bool):
        self.hover_quit = bool

    @property
    def pause(self):
        return self.is_paused
    
    @pause.setter
    def pause(self, bool):
        self.is_paused = bool

class Player:

    def __init__(self, xlocation, ylocation, yvel, score, coins):
        self.xlocation = xlocation
        self.ylocation = ylocation
        self.yvel = yvel
        self.score = score
        self.coins = coins

    def move_up(self):
        self.yvel-=7

    def move_down(self):
        self.yvel+=7
    def stop_moving(self):
        self.yvel = 0

class Ball:

    def __init__(self, xlocation, ylocation, xvel, yvel):
        self.xlocation = xlocation
        self.ylocation = ylocation
        self.xvel = xvel
        self.yvel = yvel

class Shop:
    item_1 = False
    item_2 = False
    item_3 = False
    item_4 = False
    item_5 = False
    item_6 = False

    purchased_item_1 = False
    purchased_item_2 = False
    purchased_item_3 = False
    purchased_item_4 = False
    purchased_item_5 = False
    purchased_item_6 = False

    @property
    def item_1_selected(self):
        return self.item_1
    @item_1_selected.setter
    def item_1_selected(self, bool):
        self.item_1 = bool
       

    @property
    def item_2_selected(self):
        return self.item_2
    
    @item_2_selected.setter
    def item_2_selected(self, bool):
        self.item_2 = bool
    
    @property
    def item_3_selected(self):
        return self.item_3
    @item_3_selected.setter
    def item_3_selected(self, bool):
        self.item_3 = bool
    
    @property
    def item_4_selected(self):
        return self.item_4
    @item_4_selected.setter
    def item_4_selected(self, bool):
        self.item_4 = bool
    
    @property
    def item_5_selected(self):
        return self.item_5
    @item_5_selected.setter
    def item_5_selected(self, bool):
        self.item_5 = bool

    @property
    def item_6_selected(self):
        return self.item_6
    @item_6_selected.setter
    def item_6_selected(self, bool):
        self.item_6 = bool
    
    
  
#instance creations
game1 = GameState(False, False, False, False)
player1 = Player(0, WINDOW_HEIGHT / 2 - 75, 0, 0, 0)
player2 = Player(WINDOW_WIDTH - 15, WINDOW_HEIGHT / 2 - 75, 0, 0, 0)
ball1 = Ball(WINDOW_WIDTH / 2 - 12, WINDOW_HEIGHT / 2, 0, 0)
shop = Shop()
colors = Colors()


screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption(WINDOW_TITLE)


clock = pygame.time.Clock()


#Player drawing
player1_rect = pygame.Rect(player1.xlocation, player1.ylocation, 15, 150)
player2_rect = pygame.Rect(player2.xlocation, player2.ylocation, 15,150 )

#object drawing
ball_rect = pygame.Rect(ball1.xlocation, ball1.ylocation, 25, 25)
shop_item_1 = pygame.Rect(485, 370, 190, 140)
shop_item_2 = pygame.Rect(695, 370, 170, 140)
shop_item_3 = pygame.Rect(888, 370, 165, 140)
shop_item_4 = pygame.Rect(1075, 370, 155, 140)
shop_item_5 = pygame.Rect(1250, 370, 150, 140)
shop_6 = pygame.image.load(os.path.join(IMAGE_PATH, 'speed_item.png'))
shop_item_6 = shop_6.get_rect(center=(580, 790))


#background image
main_background = pygame.image.load(os.path.join(IMAGE_PATH, 'background_main2.jpg')).convert_alpha()
play_background = pygame.image.load(os.path.join(IMAGE_PATH,'game_background.png' )).convert_alpha()
shop_background = pygame.image.load(os.path.join(IMAGE_PATH, 'store_background.png')).convert_alpha()

#main_menu text buttons/images
play_button = pygame.image.load(os.path.join(IMAGE_PATH, 'play_text.png'))
store_button = pygame.image.load(os.path.join(IMAGE_PATH, 'store_text.png'))
quit_button = pygame.image.load(os.path.join(IMAGE_PATH, 'quit_text.png'))
confirm_purchase = pygame.image.load(os.path.join(IMAGE_PATH, 'confirm.png'))
select_ = pygame.image.load(os.path.join(IMAGE_PATH, 'select.png'))
coin = pygame.image.load(os.path.join(IMAGE_PATH, 'coin.png'))

play_button_rect = play_button.get_rect(center=(900, 300))
store_button_rect = play_button.get_rect(center=(900, 475))
quit_button_rect = quit_button.get_rect(center=(900, 650))
confirm_button_rect = confirm_purchase.get_rect(center=(1600, 750))
select_button_rect = select_.get_rect(center=(1600, 600))
#load sounds
volume = 1
pygame.mixer.music.load(os.path.join(AUDIO_PATH,'main1.mp3'))
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(1)
hover_sound = pygame.mixer.Sound(os.path.join(AUDIO_PATH, 'menutick.mp3'))
play_sound = pygame.mixer.Sound(os.path.join(AUDIO_PATH, 'play.mp3'))
collide_sound1 = pygame.mixer.Sound(os.path.join(AUDIO_PATH, 'jump1.mp3'))
score_sound1 = pygame.mixer.Sound(os.path.join(AUDIO_PATH, 'score1.mp3'))
buy_sound1 = pygame.mixer.Sound(os.path.join(AUDIO_PATH, 'coin2.mp3'))
error_sound1 = pygame.mixer.Sound(os.path.join(AUDIO_PATH, 'error1.mp3'))
selection_sound = pygame.mixer.Sound(os.path.join(AUDIO_PATH, 'selection.mp3'))

play_sound.set_volume(1)
hover_sound.set_volume(1)


#loading fonts
custom_color1 = pygame.Color(0, 145, 255) #blue

score_font = pygame.font.Font('space.otf', 100)
coins_font = pygame.font.Font('space.otf', 50)

player1_score = score_font.render(f'{player1.score}', False, 'White')
player2_score = score_font.render(f'{player2.score}', False, 'White')

player_coins = coins_font.render(f'{player1.coins}', False, custom_color1)

def deselect_all():
    shop.item_1_selected = False
    shop.item_2_selected = False
    shop.item_3_selected = False
    shop.item_4_selected = False
    shop.item_5_selected = False
    shop.item_6_selected = False

def reset():
    game1.is_paused = True
    player1_rect.y = WINDOW_HEIGHT / 2 - 75
    player2_rect.y = WINDOW_HEIGHT / 2 - 75
    ball_rect.x = WINDOW_WIDTH / 2 - 12
    ball_rect.y = WINDOW_HEIGHT / 2


def start():
    game1.is_running = True
    game1.is_main_menu = True
    global volume, player1_score, player2_score, player_coins
   

    while game1.is_running:

        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game1.is_running = False
                pygame.QUIT
            


            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_MINUS:
                    
        
                    volume-=0.10
                    if volume <= 0:
                        volume = 0
                    pygame.mixer.music.set_volume(volume)

                    print(f'Game Music Volume: {volume}')

                
                if event.key == pygame.K_EQUALS:
                    
                    volume+=0.10
                    if volume >= 1:
                        volume = 1
                    pygame.mixer.music.set_volume(volume)
                    print(f'Game Music Volume: {volume}')
                if event.key == pygame.K_i:
                    buy_sound1.play()
                    time.sleep(0.3)
                    player1.coins+=99999999
                    player_coins = coins_font.render(f'{player1.coins}', False, custom_color1)

                    


            if event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_ESCAPE:
                    if not game1.is_main_menu:
                        play_sound.play()
                        time.sleep(0.7)
                        pygame.mixer.music.load(os.path.join(AUDIO_PATH,'main1.mp3'))
                        pygame.mixer.music.play(-1)
                        pygame.mixer.music.set_volume(volume)

                    if game1.is_store:
                        play_sound.play()
                        time.sleep(0.2)

                    game1.is_game = False
                    game1.is_store = False
                    game1.is_main_menu = True
                    
                if event.key == pygame.K_SPACE and game1.is_paused:

                    game1.pause = False
                    num = random.randint(0, 1)
                    if num == 0:
                        ball1.xvel = 7
                    else:
                        ball1.xvel = -7
                    ball1.yvel = 6

                if event.key == pygame.K_w:
                    player1.move_up()

                if event.key == pygame.K_s :
                    player1.move_down()

                if event.key == pygame.K_UP:
                    player2.move_up()

                if event.key == pygame.K_DOWN:
                    player2.move_down()

            if event.type == pygame.KEYUP and game1.is_game:
                if event.key == pygame.K_w:
                    player1.stop_moving()
                if event.key == pygame.K_s:
                    player1.stop_moving()
                if event.key == pygame.K_UP:
                    player2.stop_moving()
                if event.key == pygame.K_DOWN:
                    player2.stop_moving()



            if event.type == pygame.MOUSEBUTTONDOWN:
                if game1.is_main_menu:
                    if play_button_rect.collidepoint(pygame.mouse.get_pos()):
                        play_sound.play()
                        game1.is_paused = True
                        time.sleep(0.7)
                        if not game1.is_game:
                            pygame.mixer.music.load(os.path.join(AUDIO_PATH,'main2.mp3'))
                            pygame.mixer.music.play(-1)
                            pygame.mixer.music.set_volume(volume)
                            
                        game1.is_main_menu = False
                        game1.is_game = True
                        

                    if store_button_rect.collidepoint(pygame.mouse.get_pos()):
                        game1.is_main_menu = False
                        game1.is_store = True
                        play_sound.play()
                        pygame.mixer.music.load(os.path.join(AUDIO_PATH,'main3.mp3'))
                        pygame.mixer.music.play(-1)
                        pygame.mixer.music.set_volume(volume)
                        game1.is_paused = True
                        time.sleep(0.7)
                        if not game1.is_game and not game1.is_main_menu:
                            print('in shop')
                        

                    if quit_button_rect.collidepoint(pygame.mouse.get_pos()):
                        game1.is_running = False

                elif game1.is_store:
                    if shop_item_1.collidepoint(pygame.mouse.get_pos()):
                        print('buy red')
                        hover_sound.play()
                        shop.item_1_selected = True
                        shop.item_2_selected = False
                        shop.item_3_selected = False
                        shop.item_4_selected = False
                        shop.item_5_selected = False
                        shop.item_6_selected = False

                    if shop_item_2.collidepoint(pygame.mouse.get_pos()):
                        print('buy green')
                        hover_sound.play()
                        shop.item_1_selected = False
                        shop.item_2_selected = True
                        shop.item_3_selected = False
                        shop.item_4_selected = False
                        shop.item_5_selected = False
                        shop.item_6_selected = False
                    if shop_item_3.collidepoint(pygame.mouse.get_pos()):
                        print('buy brown')
                        hover_sound.play()
                        shop.item_1_selected = False
                        shop.item_2_selected = False
                        shop.item_3_selected = True
                        shop.item_4_selected = False
                        shop.item_5_selected = False
                        shop.item_6_selected = False
                    if shop_item_4.collidepoint(pygame.mouse.get_pos()):
                        print('buy orange')
                        hover_sound.play()
                        shop.item_1_selected = False
                        shop.item_2_selected = False
                        shop.item_3_selected = False
                        shop.item_4_selected = True
                        shop.item_5_selected = False
                        shop.item_6_selected = False
                    if shop_item_5.collidepoint(pygame.mouse.get_pos()):
                        print('buy purple')
                        hover_sound.play()
                        shop.item_1_selected = False
                        shop.item_2_selected = False
                        shop.item_3_selected = False
                        shop.item_4_selected = False
                        shop.item_5_selected = True
                        shop.item_6_selected = False
                    if shop_item_6.collidepoint(pygame.mouse.get_pos()):
                        print('buy insane speeedd!!')
                        hover_sound.play()
                        shop.item_1_selected = False
                        shop.item_2_selected = False
                        shop.item_3_selected = False
                        shop.item_4_selected = False
                        shop.item_5_selected = False
                        shop.item_6_selected = True
                    if confirm_button_rect.collidepoint(pygame.mouse.get_pos()):
                        if shop.item_1_selected and player1.coins >= 3 and shop.purchased_item_1 == False:
                            shop.purchased_item_1 = True
                            buy_sound1.play()
                            player1.coins-=3
                            player_coins = coins_font.render(f'{player1.coins}', False, custom_color1)
                            deselect_all()
                            shop.item_1_selected = False
    

                        elif shop.item_2_selected and player1.coins >= 5 and shop.purchased_item_2 == False:
                            shop.purchased_item_2 = True
                            buy_sound1.play()
                            player1.coins-=5
                            player_coins = coins_font.render(f'{player1.coins}', False, custom_color1)
                            deselect_all()
   
                        elif shop.item_3_selected and player1.coins >= 10 and shop.purchased_item_3 == False:
                            shop.purchased_item_3 = True
                            buy_sound1.play()
                            player1.coins-=10
                            player_coins = coins_font.render(f'{player1.coins}', False, custom_color1)
                            deselect_all()
                        elif shop.item_4_selected and player1.coins >= 13 and shop.purchased_item_4 == False:
                            shop.purchased_item_4 = True
                            buy_sound1.play()
                            player1.coins-=13
                            player_coins = coins_font.render(f'{player1.coins}', False, custom_color1)
                            deselect_all()
                        elif shop.item_5_selected and player1.coins >= 15 and shop.purchased_item_5 == False:
                            shop.purchased_item_5 = True
                            buy_sound1.play()
                            player1.coins-=15
                            player_coins = coins_font.render(f'{player1.coins}', False, custom_color1)
                            deselect_all()
                        elif shop.item_6_selected and player1.coins >= 20 and shop.purchased_item_6 == False:
                            shop.purchased_item_6 = True
                            buy_sound1.play()
                            player1.coins-=20
                            player_coins = coins_font.render(f'{player1.coins}', False, custom_color1)
                            deselect_all()
                        else:
                            error_sound1.play()
                    if select_button_rect.collidepoint(pygame.mouse.get_pos()):
                        if shop.item_1_selected and shop.purchased_item_1:
                            selection_sound.play()
                            colors.custom = colors.custom1
                            
                            print('selected!')
                            deselect_all()
                        elif  shop.item_2_selected and shop.purchased_item_2:
                            selection_sound.play()
                            colors.custom = colors.custom2
                            print('selected!')
                            deselect_all()
                        elif shop.item_3_selected and shop.purchased_item_3:
                            selection_sound.play()
                            colors.custom = colors.custom3
                            print('selected!')
                            deselect_all()
                        elif shop.item_4_selected and shop.purchased_item_4:
                            selection_sound.play()
                            colors.custom = colors.custom4
                            print('selected!')
                            deselect_all()
                        elif shop.item_5_selected and shop.purchased_item_5:
                            selection_sound.play()
                            colors.custom = colors.custom5
                            print('selected!')
                            deselect_all()
                        elif shop.item_6_selected and shop.purchased_item_6:
                            selection_sound.play()
                            game1.cheat_1 = True
                            print('selected!')
                            deselect_all()
                        else: error_sound1.play()


           



            if event.type == pygame.MOUSEMOTION:
                if game1.is_main_menu and not game1.hover_is_play:
                    if play_button_rect.collidepoint(pygame.mouse.get_pos()):
                        
                        hover_sound.play()
                        game1.hover_is_play = True

                        game1.hover_is_quit = False
                        game1.hover_is_store = False

                if game1.is_main_menu and not game1.hover_is_store:
                    if store_button_rect.collidepoint(pygame.mouse.get_pos()):
                        hover_sound.play()
                        game1.hover_is_store = True

                        game1.hover_is_play = False
                        game1.hover_is_quit = False
                   

                if game1.is_main_menu and not game1.hover_is_quit:
                    if quit_button_rect.collidepoint(pygame.mouse.get_pos()):
                        hover_sound.play()
                        game1.hover_is_quit = True

                        game1.hover_is_play = False
                        game1.hover_is_store = False
 
        #movement player 1
        if game1.is_game and not game1.pause:
            player1_rect.y += player1.yvel

        #collision player 1 with screen

        if player1_rect.bottom >= WINDOW_HEIGHT or player1_rect.top <=0:
            player1.stop_moving()
#########################################################################################
          #movement player 2
        if game1.is_game and not game1.pause:
            player2_rect.y+= player2.yvel


        #collision player 2 with screen
        if player2_rect.bottom >= WINDOW_HEIGHT or player2_rect.top <=0:
            player2.stop_moving()
#######################################################################################
        #ball movement
        if game1.is_game and not game1.pause:
            ball_rect.x+= ball1.xvel
            ball_rect.y+= ball1.yvel

        if ball_rect.top >= WINDOW_HEIGHT -25 or ball_rect.bottom - 25  <= 0:
            ball1.yvel*=-1


        if ball_rect.right >= WINDOW_WIDTH:
            player1.score+=1
            player1_score = score_font.render(f'{player1.score}', False, 'White')
            score_sound1.play()
            reset()

        if player1.score >=3:
            player1.coins+=1  
            player_coins = coins_font.render(f'{player1.coins}', False, custom_color1)
            player1.score = 0
            player2.score = 0
            
            player1_score = score_font.render(f'{player1.score}', False, 'White')
            player2_score = score_font.render(f'{player2.score}', False, 'White')
            reset() 

        if player2.score >=3:
            player1_score = 0
            player2.score = 0
            player1_score = score_font.render(f'{player1.score}', False, 'White')
            player2_score = score_font.render(f'{player2.score}', False, 'White')
            reset() 
        

            
            
            

        if ball_rect.left <= 0:
             player2.score+=1
             player2_score = score_font.render(f'{player2.score}', False, 'White')
             score_sound1.play()
             reset()
             
             
             
 
###################################################################################

        #player and ball collision
        if player1_rect.colliderect(ball_rect):
            collide_sound1.play()
            if game1.cheat_1:
                ball1.xvel*=-5
                ball1.yvel*=-4
            else: ball1.xvel*=-1
            
        if player2_rect.colliderect(ball_rect):
            collide_sound1.play()
            ball1.xvel*=-1
           


        screen.fill('Black')

        if game1.is_main_menu:
            pygame.mouse.set_cursor(3)
            #sets the velocity for players and ball to zero when we pause
            player1.yvel = 0
            
            screen.blit(main_background, (0, 0))
            screen.blit(play_button, (play_button_rect))
            screen.blit(store_button, (store_button_rect))
            screen.blit(quit_button, (quit_button_rect))
            screen.blit(coin, (1700, 50))
            screen.blit(player_coins, (1800, 60))
           
        
        if game1.is_game:
            
            screen.blit(play_background, (0, 0))
            pygame.draw.line(screen, 'white', (WINDOW_WIDTH / 2, 0), (WINDOW_WIDTH / 2, WINDOW_HEIGHT), 3)
            screen.blit(player1_score, (WINDOW_WIDTH / 2 - 100, 100))
            screen.blit(player2_score, (WINDOW_WIDTH / 2 + 65, 100))
            pygame.draw.rect(screen, colors.custom, player1_rect)
            pygame.draw.rect(screen, 'white', player2_rect)
            pygame.draw.ellipse(screen, 'gray', ball_rect)
            
        if game1.is_store:
            screen.blit(shop_background, (0, 0))
            #####REFERNCE
            # pygame.draw.rect(screen, 'red', (1500, 710, 185, 100)) 

            screen.blit(shop_6, (shop_item_6))
            screen.blit(confirm_purchase, (confirm_button_rect))
            screen.blit(select_, (select_button_rect))
            pygame.draw.rect(screen, 'red', shop_item_1)
            pygame.draw.rect(screen, 'green', shop_item_2)
            pygame.draw.rect(screen, 'brown', shop_item_3)
            pygame.draw.rect(screen, 'orange', shop_item_4)
            pygame.draw.rect(screen, 'purple', shop_item_5)
            screen.blit(coin, (1700, 50))
            screen.blit(player_coins, (1800, 60))


        pygame.display.update()
        clock.tick(144)
       


start()