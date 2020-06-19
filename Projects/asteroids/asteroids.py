import arcade
import math
import random

# These are Global constants to use throughout the game
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

BULLET_RADIUS = 30
BULLET_SPEED = 10
BULLET_LIFE = 60

SHIP_TURN_AMOUNT = 3
SHIP_THRUST_AMOUNT = 0.25
SHIP_RADIUS = 30

INITIAL_ROCK_COUNT = 5

BIG_ROCK_SPIN = 1
BIG_ROCK_SPEED = 1.5
BIG_ROCK_RADIUS = 15

MEDIUM_ROCK_SPIN = -2
MEDIUM_ROCK_RADIUS = 5

SMALL_ROCK_SPIN = 5
SMALL_ROCK_RADIUS = 2


####################################
# Point class
####################################
class Point():
    
    def __init__(self):
        
        self.x = 0.0
        self.y = 0.0
        
####################################
# Velocity class
####################################
        
class Velocity():
    
    def __init__(self):
        
        self.dx = 0.0
        self.dy = 0.0
        
####################################
# Flying Objects class
####################################

class FlyingObjects:
    
    def __init__(self, img):
        
        self.center = Point()
        self.velocity = Velocity()
        self.alive = True
        self.img = img
        self.texture = arcade.load_texture(self.img)
        self.radius = SHIP_RADIUS
        self.angle = BIG_ROCK_SPIN
        #self.speed = 
        #self.direction = 90
        self.width = self.texture.width
        self.height = self.texture.height
        self.hits = 0
    
    def advance(self):
        
        self.center.x += self.velocity.dx
        self.center.y += self.velocity.dy
        
    def draw(self):
        
        arcade.draw_texture_rectangle(self.center.x, self.center.y, self.width,
                                      self.height, self.texture, self.angle, 255)
        
           
    def wrap_around_screen(self):
        
        
        if self.center.x > SCREEN_WIDTH:
            self.center.x -= SCREEN_WIDTH
            
        elif self.center.y > SCREEN_HEIGHT:
            self.center.y -= SCREEN_HEIGHT
            
        elif self.center.x < 0:
            self.center.x += SCREEN_WIDTH
        
        elif self.center.y < 0:
            self.center.y += SCREEN_HEIGHT

######################################
# Sprites class
######################################
class Sprites(FlyingObjects):
    
    def __init__(self, img):
        super().__init__(img)
        self.radius = 0.0
        self.alive = True
        self.angle = 0.0
        self.img = img
        self.texture = arcade.load_texture(self.img)
        self.center.x = random.uniform(0.0, SCREEN_WIDTH /2)
        self.center.y = random.uniform(0.0, SCREEN_HEIGHT)
        self.direction = random.uniform(0.0, 360)
        self.speed = BIG_ROCK_SPEED
        self.velocity.dx = math.cos(math.radians(self.direction)) * self.speed
        self.velocity.dy = math.sin(math.radians(self.direction)) * self.speed
        
    def advance(self):
        
        super().advance()

######################################
# TIE Fighter class
######################################
class TIE(Sprites):
    def __init__(self):
        
        super().__init__("images/TIE-Fighter-Star-Wars.png")
        self.radius = BIG_ROCK_RADIUS
        self.center.x = random.uniform(790.0, 800.0)
        self.center.y = random.uniform(300.0, SCREEN_HEIGHT)
        self.direction = random.uniform(180, 225)
        self.speed = 3.0
        self.width = 150
        self.height = 150
        
        self.velocity.dx = math.cos(math.radians(self.direction)) * self.speed
        self.velocity.dy = math.sin(math.radians(self.direction)) * self.speed
         
          
    def hit(self):
        
        self.hits += 1
        
        if self.hits == 5:
            self.alive = False
            
        else:
            pass
    
######################################
# Cruiser class
######################################
class Cruiser(Sprites):
    def __init__(self):
        
        super().__init__("images/cruiser2.png")
        self.radius = 50
        self.center.x = random.uniform(790.0, 800.0)
        self.center.y = random.uniform(300.0, SCREEN_HEIGHT)
        self.direction = random.uniform(180, 225)
        self.speed = BIG_ROCK_SPEED
        self.width = 200
        self.height = 200
        
        self.velocity.dx = math.cos(math.radians(self.direction)) * self.speed
        self.velocity.dy = math.sin(math.radians(self.direction)) * self.speed
        
        
    def hit(self):
        
        self.hits += 1
        
        if self.hits == 10:
            self.alive = False
            
        else:
            pass
        
######################################
# Death Star class
######################################
class Death_Star(Sprites):
    def __init__(self):
        
        super().__init__("images/deathstar.png")
        self.radius = 80
        self.center.x = 0.0
        self.center.y = random.uniform(0, 100)
        self.direction = random.uniform(0, 270)
        self.speed = 0.5
        self.width = 200
        self.height = 200
        
        self.velocity.dx = math.cos(math.radians(self.direction)) * self.speed
        self.velocity.dy = math.sin(math.radians(self.direction)) * self.speed
        
        
    def hit(self):
        
        self.hits += 1
        
        if self.hits == 20:
            self.alive = False
        else:
            pass
        
######################################
# Astronaut class
######################################
class Astronaut(Sprites):
    def __init__(self):
        
        super().__init__("images/astronaut.png")
        self.radius = 30
        self.center.x = random.uniform(0.0, SCREEN_WIDTH / 2)
        self.center.y = random.uniform(300.0, SCREEN_HEIGHT)
        self.direction = random.uniform(0, 90)
        self.speed = BIG_ROCK_SPEED
        self.width = 100
        self.height = 100
        self.angle = 1.5
        
        self.velocity.dx = math.cos(math.radians(self.direction)) * self.speed
        self.velocity.dy = math.sin(math.radians(self.direction)) * self.speed
        
    def advance(self):
        super().advance()
        self.angle -= 1.5
         
        
    def hit(self):
        
        self.alive = False
        
######################################
# Asteroid class
######################################
class Asteroids(FlyingObjects):
    
    def __init__(self, img):
        super().__init__(img)
        self.radius = 0.0
        self.alive = True
        self.angle = 0.0
        self.img = img
        self.texture = arcade.load_texture(self.img)
        self.center.x = random.uniform(0.0, SCREEN_WIDTH /2)
        self.center.y = random.uniform(0.0, SCREEN_HEIGHT)
        self.direction = random.uniform(0.0, 360)
        self.speed = BIG_ROCK_SPEED
        self.velocity.dx = math.cos(math.radians(self.direction)) * self.speed
        self.velocity.dy = math.sin(math.radians(self.direction)) * self.speed
        
        
######################################
# Large Asteroid class
######################################

class Large_Asteroid(Asteroids):
    def __init__(self):
        
        super().__init__("images/meteorGrey_big1.png")
        self.alive = True
        self.radius = BIG_ROCK_RADIUS
        self.angle = 0.0
        
        self.center.x = random.uniform(0.0, SCREEN_WIDTH /2)
        self.center.y = random.uniform(0.0, SCREEN_HEIGHT)
        self.direction = random.uniform(0.0, 360)
        self.speed = BIG_ROCK_SPEED
        self.velocity.dx = math.cos(math.radians(self.direction)) * self.speed
        self.velocity.dy = math.sin(math.radians(self.direction)) * self.speed
        
    def advance(self):
        
        super().advance()
        self.angle += BIG_ROCK_SPIN
        
    
        
    def break_apart(self, asteroids):
        
        med1 = Medium_Asteroid()
        med1.center.x = self.center.x
        med1.center.y = self.center.y
        med1.velocity.dx = self.velocity.dx
        med1.velocity.dy = self.velocity.dy + 2
        
        med2 = Medium_Asteroid()
        med2.center.x = self.center.x
        med2.center.y = self.center.y
        med2.velocity.dx = self.velocity.dx
        med2.velocity.dy = self.velocity.dy - 2
        
        asteroids.append(med1)
        asteroids.append(med2)
        self.alive = False
        
        
##################################
# Medium Asteroid class
##################################

class Medium_Asteroid(Asteroids):
    
    def __init__(self):
        
        super().__init__("images/meteorGrey_med1.png")
        self.alive = True
        self.radius = MEDIUM_ROCK_RADIUS
        self.angle = 0.0
        
        #self.center.x = random.uniform(0, SCREEN_WIDTH)
        #self.center.y = random.uniform(0, SCREEN_HEIGHT)
        self.direction = random.uniform(0, 360)
        self.speed = BIG_ROCK_SPEED
        self.velocity.dx = math.cos(math.radians(self.direction)) * self.speed
        self.velocity.dy = math.sin(math.radians(self.direction)) * self.speed
    
    def advance(self):
        
        super().advance()
        self.angle += MEDIUM_ROCK_SPIN
    
           
    def break_apart(self, asteroids):
        
        small1 = Small_Asteroid()
        small1.center.x = self.center.x
        small1.center.y = self.center.y
        small1.velocity.dx = self.velocity.dx + 1.5
        small1.velocity.dy = self.velocity.dy + 1.5
        
        small2 = Small_Asteroid()
        small2.center.x = self.center.x
        small2.center.y = self.center.y
        small2.velocity.dx = self.velocity.dx - 1.5
        small2.velocity.dy = self.velocity.dy - 1.5
        
        asteroids.append(small1)
        asteroids.append(small2)
        self.alive = False
        

##################################
# Small Asteroid class
##################################
class Small_Asteroid(Asteroids):
    
    def __init__(self):
        
        super().__init__("images/meteorGrey_small1.png")
        self.alive = True
        self.radius = SMALL_ROCK_RADIUS
        self.angle = 0.0
        
        self.center.x = random.uniform(0, SCREEN_WIDTH)
        self.center.y = random.uniform(0, SCREEN_HEIGHT)
        self.direction = random.uniform(0, 360)
        self.speed = BIG_ROCK_SPEED
        self.velocity.dx = math.cos(math.radians(self.direction)) * self.speed
        self.velocity.dy = math.sin(math.radians(self.direction)) * self.speed
        
    def advance(self):
        
        super().advance()
        self.angle += SMALL_ROCK_SPIN
        
    
    def break_apart(self, asteroids):
        
        self.alive = False

##################################
# Bullet class
##################################           
        
class Bullet(FlyingObjects):
    
    def __init__(self, ship_angle, ship_x, ship_y):
        #Inherit varibales from FlyingObjects class.
        super().__init__("images/laserBlue01.png")
        self.alive = True
        self.radius = BULLET_RADIUS
        self.speed = BULLET_SPEED
        self.life = BULLET_LIFE
        self.angle = ship_angle + 90
        self.center.x = ship_x
        self.center.y = ship_y
        
        self.velocity.dx = math.cos(math.radians(self.angle)) * self.speed
        self.velocity.dy = math.sin(math.radians(self.angle)) * self.speed
        
    def advance(self):
        
        super().advance()
        self.life -= 1
        
        if self.life <= 0:
            self.alive = False
        else:
            self.alive = True
        
        
    def fire(self):
        
        #self.angle = angle
        #Code provided by instructor. I just manipulated it to suit.
        self.velocity.dx = math.cos(math.radians(self.angle + 90)) * BULLET_SPEED * self.ship.thrust()
        self.velocity.dy = math.sin(math.radians(self.angle + 90)) * BULLET_SPEED * self.ship.thrust()
     
        
##################################
# Ship class
##################################

class Ship(FlyingObjects):
    
    def __init__(self):
        
        super().__init__("images/playerShip1_orange.png")
        self.angle = 1
        self.center.x = (SCREEN_WIDTH / 2)
        self.center.y = (SCREEN_HEIGHT / 2)
        self.radius = SHIP_RADIUS
        self.speed = SHIP_THRUST_AMOUNT
        
        #self.velocity.dx = math.cos(math.radians(self.angle)) * SHIP_THRUST_AMOUNT
        #self.velocity.dy = math.sin(math.radians(self.angle)) * SHIP_THRUST_AMOUNT        
        
    def rotate_left(self):
        
        self.angle += SHIP_TURN_AMOUNT
    
    def rotate_right(self):
        
        self.angle -= SHIP_TURN_AMOUNT
    
    def thrust(self):
        
        self.velocity.dx -= math.sin(math.radians(self.angle)) * SHIP_THRUST_AMOUNT
        self.velocity.dy += math.cos(math.radians(self.angle)) * SHIP_THRUST_AMOUNT
        
    def reverse(self):
        
        self.velocity.dx += math.sin(math.radians(self.angle)) * SHIP_THRUST_AMOUNT
        self.velocity.dy -= math.cos(math.radians(self.angle)) * SHIP_THRUST_AMOUNT
        
    

##################################
# Game class
##################################

class Game(arcade.Window):
    """
    This class handles all the game callbacks and interaction
    This class will then call the appropriate functions of
    each of the above classes.
    You are welcome to modify anything in this class.
    """

    def __init__(self, width, height):
        """
        Sets up the initial conditions of the game
        :param width: Screen width
        :param height: Screen height
        """
        super().__init__(width, height)
        self.background = arcade.load_texture("images/galaxy_%20background.jpg")
        #arcade.set_background_color(arcade.color.SMOKY_BLACK)

        self.held_keys = set()
        self.lives = 5

        # TODO: declare anything here you need the game class to track
        self.sprites = []
        self.asteroids = []
        
        for i in range(INITIAL_ROCK_COUNT):
            large_Rock = Large_Asteroid()
            self.asteroids.append(large_Rock)
            
        self.bullets = []
            
        self.ship = Ship()
        
        
        
    def on_draw(self):
        """
        Called automatically by the arcade framework.
        Handles the responsibility of drawing all elements.
        """

        # clear the screen to begin drawing
        arcade.start_render()
        
        #arcade.draw_lrwh_rectangle_texture(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, self_background)

        # TODO: draw each object
            
        for asteroid in self.asteroids:
            asteroid.draw()
        
        if self.ship.alive != False:
            self.ship.draw()
        else:
            arcade.draw_text("GAME OVER!",
                         SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, arcade.color.RED, 50,
                             width=400, align="center", anchor_x="center", anchor_y="center")
            
        for bullet in self.bullets:
            bullet.draw()
                    
        for sprite in self.sprites:
            sprite.draw()
            
        self.draw_lives()

    def update(self, delta_time):
        """
        Update each object in the game.
        :param delta_time: tells us how much time has actually elapsed
        """
        self.check_keys()
        
        if random.randint(1, 300) == 1:
            self.create_asteroid()

        # TODO: Tell everything to advance or move forward one step in time
        for asteroid in self.asteroids:
            asteroid.advance()
            asteroid.wrap_around_screen()
            
        for bullet in self.bullets:
            bullet.advance()
            bullet.wrap_around_screen()
            if (not bullet.alive):
                self.bullets.remove(bullet)
                
        if random.randint(1, 500) == 1:
            self.create_sprites()
                
        for sprite in self.sprites:
            sprite.advance()
            sprite.wrap_around_screen()
            
        # TODO: Check for collisions
        self.ship.advance()
        self.ship.wrap_around_screen()
                          
        self.check_collisions()
        
        self.cleanup_zombies()
        
    def draw_lives(self):
        """
        Puts the current lives on the screen
        """
        if self.lives <= 0:
            self.lives = 0
        
        current_lives = "Lives left: {}".format(self.lives)
        start_x = 10
        start_y = SCREEN_HEIGHT - 40
        arcade.draw_text(current_lives, start_x=start_x, start_y=start_y, font_size=20,
                         color=arcade.color.YELLOW)
    
    def create_sprites(self):
                           
        new_sprite = random.randint(1,4)
        
        if new_sprite == 1:
            tie = TIE()
            self.sprites.append(tie)
            
        elif new_sprite == 4:
            star = Cruiser()
            self.sprites.append(star)
            
        elif new_sprite == 2:
            dstar = Death_Star()
            self.sprites.append(dstar)
            
        elif new_sprite == 3:
            astro = Astronaut()
            self.sprites.append(astro)
        
        
    def create_asteroid(self):
        
        new_Rock = random.randint(1, 3)
        
        if new_Rock == 1:
            large = Large_Asteroid()
            self.asteroids.append(large)
            
        elif new_Rock == 2:
            medium = Medium_Asteroid()
            self.asteroids.append(medium)
            
        elif new_Rock == 3:
            small = Small_Asteroid()
            self.asteroids.append(small)
            
            
    def check_collisions(self):
        """
        Checks to see if bullets have hit targets.
        Updates scores and removes dead items.
        :return:
        """

        # NOTE: This assumes you named your targets list "targets"
        for bullet in self.bullets:
            for asteroid in self.asteroids:

                # Make sure they are both alive before checking for a collision
                if bullet.alive and asteroid.alive:
                    too_close = bullet.radius + asteroid.radius

                    if (abs(bullet.center.x - asteroid.center.x) < too_close and
                                abs(bullet.center.y - asteroid.center.y) < too_close):
                        # its a hit!
                        bullet.alive = False
                        asteroid.break_apart(self.asteroids)
        #Using the skeet code I manipulate it to assist me when asteroids hit the ship.                 
        for asteroid in self.asteroids:
            #Check if both ship and asteroid are alive
            if self.ship.alive and asteroid.alive:
                #close_enough is the max distance between the two objects before it hits 
                close_enough = self.ship.radius + asteroid.radius
                #now for the code to determine if both x values are closer than the close_enough dist
                #now for the code to determine if both y values are closer than the close_enough dist
                if (abs(self.ship.center.x - asteroid.center.x) < close_enough and
                    abs(self.ship.center.y - asteroid.center.y) < close_enough):
                    #Kill off both ship and asteroid.
                    self.lives -= 1
                    if self.lives <= 0:
                        self.ship.alive = False
                    asteroid.break_apart(self.asteroids)
                        
        for sprite in self.sprites:
            for asteroid in self.asteroids:
            #Check if both sprite and asteroid are alive
                if sprite.alive and asteroid.alive:
                #close_enough is the max distance between the two objects before it hits 
                    close_enough = sprite.radius + asteroid.radius
                #now for the code to determine if both x values are closer than the close_enough dist
                #now for the code to determine if both y values are closer than the close_enough dist
                    if (abs(sprite.center.x - asteroid.center.x) < close_enough and
                        abs(sprite.center.y - asteroid.center.y) < close_enough):
                    #Kill off both ship and asteroid.
                        asteroid.break_apart(self.asteroids)
                    
        for sprite in self.sprites:
            for bullet in self.bullets:
            #Check if both sprite and asteroid are alive
                if sprite.alive and bullet.alive:
                #close_enough is the max distance between the two objects before it hits 
                    close_enough = sprite.radius + bullet.radius
                #now for the code to determine if both x values are closer than the close_enough dist
                #now for the code to determine if both y values are closer than the close_enough dist
                    if (abs(sprite.center.x - bullet.center.x) < close_enough and
                        abs(sprite.center.y - bullet.center.y) < close_enough):
                    #Kill off both ship and asteroid.
                        bullet.alive = False
                        sprite.hit()
                        
        for sprite in self.sprites:
            #Check if both ship and sprite are alive
            if self.ship.alive and sprite.alive:
                #close_enough is the max distance between the two objects before it hits 
                close_enough = self.ship.radius + sprite.radius
                #now for the code to determine if both x values are closer than the close_enough dist
                #now for the code to determine if both y values are closer than the close_enough dist
                if (abs(self.ship.center.x - sprite.center.x) < close_enough and
                    abs(self.ship.center.y - sprite.center.y) < close_enough):
                    #Kill off both ship and sprite.
                    sprite.alive = False
                    self.lives -= 3
                    if self.lives <= 0:
                        self.ship.alive = False
                    
                             
    
    def cleanup_zombies(self):
        """
        Removes any dead bullets or targets from the list.
        :return:
        """
        for bullet in self.bullets:
            if not bullet.alive:
                self.bullets.remove(bullet)

        for asteroid in self.asteroids:
            if not asteroid.alive:
                self.asteroids.remove(asteroid)
                
        for sprite in self.sprites:
            if not sprite.alive:
                self.sprites.remove(sprite)
        

    def check_keys(self):
        """
        This function checks for keys that are being held down.
        You will need to put your own method calls in here.
        """
        if arcade.key.LEFT in self.held_keys:
            self.ship.rotate_left()
            

        if arcade.key.RIGHT in self.held_keys:
            self.ship.rotate_right()

        if arcade.key.UP in self.held_keys:
            self.ship.thrust()

        if arcade.key.DOWN in self.held_keys:
            self.ship.reverse()

        # Machine gun mode...
        #if arcade.key.SPACE in self.held_keys:
        #    pass


    def on_key_press(self, key: int, modifiers: int):
        """
        Puts the current key in the set of keys that are being held.
        You will need to add things here to handle firing the bullet.
        """
        if self.ship.alive:
            self.held_keys.add(key)

            if key == arcade.key.SPACE:
                # TODO: Fire the bullet here!
                bullet = Bullet(self.ship.angle, self.ship.center.x, self.ship.center.y)
                self.bullets.append(bullet)
                bullet.fire()
                

    def on_key_release(self, key: int, modifiers: int):
        """
        Removes the current key from the set of held keys.
        """
        if key in self.held_keys:
            self.held_keys.remove(key)


# Creates the game and starts it going
window = Game(SCREEN_WIDTH, SCREEN_HEIGHT)
arcade.run()
