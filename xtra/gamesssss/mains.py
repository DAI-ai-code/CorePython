import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Game constants
WIDTH, HEIGHT = 1440, 1000
FPS = 60
GRAVITY = 0.2
JUMP_STRENGTH = -15 -5
PLAYER_SPEED = 15

# Colors
SKY_BLUE = (135, 206, 235)
BROWN = (139, 69, 19)
GREEN = (34, 139, 34)
RED = (255, 0, 0)
YELLOW = (255, 215, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


class Player:
    def __init__(self):
        self.width = 40
        self.height = 60
        self.x = 100
        self.y = HEIGHT - 200
        self.vel_y = 0
        self.jumping = False
        self.direction = 1  # 1 for right, -1 for left
        self.coins = 0
        self.lives = 3

    def update(self, platforms):
        # Apply gravity
        self.vel_y += GRAVITY
        self.y += self.vel_y

        # Check platform collisions
        on_ground = False
        for platform in platforms:
            if (self.y + self.height >= platform.y and
                    self.y + self.height <= platform.y + 10 and
                    self.x + self.width > platform.x and
                    self.x < platform.x + platform.width and
                    self.vel_y > 0):
                self.y = platform.y - self.height
                self.vel_y = 0
                on_ground = True
                self.jumping = False

        # Floor collision
        if self.y + self.height > HEIGHT - 50:
            self.y = HEIGHT - 50 - self.height
            self.vel_y = 0
            on_ground = True
            self.jumping = False

        return on_ground

    def jump(self):
        if not self.jumping:
            self.vel_y = JUMP_STRENGTH
            self.jumping = True

    def move(self, direction):
        self.direction = direction
        self.x += direction * PLAYER_SPEED
        self.x = max(0, min(WIDTH - self.width, self.x))

    def draw(self, screen):
        # Draw player body
        pygame.draw.rect(screen, RED, (self.x, self.y, self.width, self.height))

        # Draw face (simple eyes)
        eye_x = self.x + 10 if self.direction == 1 else self.x + self.width - 15
        pygame.draw.circle(screen, WHITE, (eye_x, self.y + 20), 5)
        pygame.draw.circle(screen, BLACK, (eye_x, self.y + 20), 2)


class Platform:
    def __init__(self, x, y, width, has_coin=False):
        self.x = x
        self.y = y
        self.width = width
        self.height = 20
        self.has_coin = has_coin
        self.coin_collected = False

    def draw(self, screen):
        pygame.draw.rect(screen, BROWN, (self.x, self.y, self.width, self.height))
        if self.has_coin and not self.coin_collected:
            pygame.draw.circle(screen, YELLOW, (self.x + self.width // 2, self.y - 15), 10)


class Coin:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 8
        self.collected = False

    def draw(self, screen):
        if not self.collected:
            pygame.draw.circle(screen, YELLOW, (self.x, self.y), self.radius)
            pygame.draw.circle(screen, (200, 170, 0), (self.x, self.y), self.radius - 3)


class Enemy:
    def __init__(self, x, y, move_range):
        self.x = x
        self.y = y
        self.width = 30
        self.height = 30
        self.move_range = move_range
        self.start_x = x
        self.speed = 2
        self.direction = 1

    def update(self):
        self.x += self.speed * self.direction
        if self.x > self.start_x + self.move_range or self.x < self.start_x - self.move_range:
            self.direction *= -1

    def draw(self, screen):
        pygame.draw.rect(screen, (150, 0, 0), (self.x, self.y, self.width, self.height))
        # Draw simple eyes
        eye_offset = 5 if self.direction == 1 else -5
        pygame.draw.circle(screen, WHITE, (self.x + 10 + eye_offset, self.y + 10), 4)
        pygame.draw.circle(screen, BLACK, (self.x + 10 + eye_offset, self.y + 10), 2)


def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Pixel Jumper")
    clock = pygame.time.Clock()

    # Create game objects
    player = Player()

    # Create platforms
    platforms = [
        Platform(100, 400, 200, True),
        Platform(400, 350, 150),
        Platform(200, 250, 100, True),
        Platform(500, 200, 200),
        Platform(100, 150, 150, True),
        Platform(0, HEIGHT - 50, WIDTH)  # Ground
    ]

    # Create coins
    coins = [Coin(platform.x + platform.width // 2, platform.y - 30)
             for platform in platforms if platform.has_coin]

    # Create enemies
    enemies = [
        Enemy(300, HEIGHT - 80, 100),
        Enemy(550, 150, 80)

    ]

    # Game state
    score = 0
    game_over = False
    font = pygame.font.Font(None, 36)

    # Main game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not game_over:
                    player.jump()
                if event.key == pygame.K_r and game_over:
                    # Restart game
                    player = Player()
                    for coin in coins:
                        coin.collected = False
                    for platform in platforms:
                        platform.coin_collected = False
                    score = 0
                    game_over = False

        if not game_over:
            # Player movement
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                player.move(-1)
            if keys[pygame.K_RIGHT]:
                player.move(1)

            # Update game objects
            player.update(platforms)

            # Update enemies
            for enemy in enemies:
                enemy.update()

                # Check enemy collision
                if (player.x < enemy.x + enemy.width and
                        player.x + player.width > enemy.x and
                        player.y < enemy.y + enemy.height and
                        player.y + player.height > enemy.y):
                    if player.vel_y > 0 and player.y + player.height < enemy.y + 20:
                        # Jump on enemy
                        enemies.remove(enemy)
                        player.vel_y = JUMP_STRENGTH * 0.7
                        score += 100
                    else:
                        # Lose life
                        player.lives -= 1
                        player.x = 100
                        player.y = HEIGHT - 200
                        if player.lives <= 0:
                            game_over = True

            # Check coin collection
            for coin in coins:
                if not coin.collected:
                    distance = math.sqrt((player.x + player.width // 2 - coin.x) ** 2 +
                                         (player.y + player.height // 2 - coin.y) ** 2)
                    if distance < 30:
                        coin.collected = True
                        score += 50
                        player.coins += 1

            # Check if player falls off
            if player.y > HEIGHT:
                player.lives -= 1
                player.x = 100
                player.y = HEIGHT - 200
                if player.lives <= 0:
                    game_over = True

        # Draw everything
        screen.fill(SKY_BLUE)

        # Draw clouds (background decoration)
        for i in range(3):
            cloud_x = (pygame.time.get_ticks() // 50 + i * 300) % (WIDTH + 200) - 100
            pygame.draw.circle(screen, WHITE, (cloud_x, 80), 30)
            pygame.draw.circle(screen, WHITE, (cloud_x + 25, 70), 25)
            pygame.draw.circle(screen, WHITE, (cloud_x + 50, 80), 30)

        # Draw platforms and coins
        for platform in platforms:
            platform.draw(screen)

        for coin in coins:
            coin.draw(screen)

        # Draw enemies
        for enemy in enemies:
            enemy.draw(screen)

        # Draw player
        player.draw(screen)

        # Draw UI
        score_text = font.render(f"Score: {score}", True, WHITE)
        lives_text = font.render(f"Lives: {player.lives}", True, WHITE)
        coins_text = font.render(f"Coins: {player.coins}", True, WHITE)

        screen.blit(score_text, (10, 10))
        screen.blit(lives_text, (10, 50))
        screen.blit(coins_text, (WIDTH - 150, 10))

        if game_over:
            game_over_text = font.render("GAME OVER! Press R to restart", True, RED)
            screen.blit(game_over_text, (WIDTH // 2 - 180, HEIGHT // 2))

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()