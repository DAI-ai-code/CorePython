import pygame
import sys
import math
import random

# Initialize pygame
pygame.init()

# Constants
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 700
GRAVITY = 0.6
JUMP_STRENGTH = -14
PLAYER_SPEED = 5
TERMINAL_VELOCITY = 12

# Enhanced Colors
COLORS = {
    'BLUE': (0, 0, 255),
    'SKY_BLUE': (135, 206, 235),
    'GRASS_GREEN': (34, 139, 34),
    'WATER_BLUE': (30, 144, 255),
    'FIRE_RED': (255, 69, 0),
    'FIRE_ORANGE': (255, 140, 0),
    'FIRE_YELLOW': (255, 255, 0),
    'WOOD_BROWN': (139, 69, 19),
    'STONE_GRAY': (105, 105, 105),
    'GOLD': (255, 215, 0),
    'WHITE': (255, 255, 255),
    'BLACK': (0, 0, 0),
    'ICE_BLUE': (173, 216, 230),
    'DARK_BROWN': (101, 67, 33),
    'PLAYER_BLUE': (70, 130, 180),
    'GREEN': (0, 255, 0),
    'RED': (255, 0, 0),
    'PURPLE': (128, 0, 128),
    'ORANGE': (255, 165, 0)
}

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Word Power Adventure - Enhanced")
clock = pygame.time.Clock()

# Fonts
font_small = pygame.font.Font(None, 24)
font_medium = pygame.font.Font(None, 32)
font_large = pygame.font.Font(None, 48)
font_huge = pygame.font.Font(None, 64)


class Particle:
    def __init__(self, x, y, color, velocity_x=0, velocity_y=0, life=60, size=None):
        self.x = x
        self.y = y
        self.color = color
        self.velocity_x = velocity_x
        self.velocity_y = velocity_y
        self.life = life
        self.max_life = life
        self.size = size or random.randint(2, 5)
        self.gravity = 0.1

    def update(self):
        self.x += self.velocity_x
        self.y += self.velocity_y
        self.velocity_y += self.gravity
        self.life -= 1
        return self.life > 0

    def draw(self, surface):
        if self.life > 0:
            alpha = int(255 * (self.life / self.max_life))
            temp_surface = pygame.Surface((self.size * 2, self.size * 2), pygame.SRCALPHA)
            color_with_alpha = (*self.color[:3], alpha)
            pygame.draw.circle(temp_surface, color_with_alpha, (self.size, self.size), self.size)
            surface.blit(temp_surface, (int(self.x - self.size), int(self.y - self.size)))


class AnimatedSprite:
    def __init__(self, frames, frame_duration=5):
        self.frames = frames
        self.frame_duration = frame_duration
        self.current_frame = 0
        self.frame_timer = 0

    def update(self):
        self.frame_timer += 1
        if self.frame_timer >= self.frame_duration:
            self.frame_timer = 0
            self.current_frame = (self.current_frame + 1) % len(self.frames)

    def get_current_frame(self):
        return self.frames[self.current_frame]


def create_gradient_surface(width, height, color1, color2, vertical=True):
    surface = pygame.Surface((width, height))
    for i in range(height if vertical else width):
        ratio = i / (height if vertical else width)
        r = int(color1[0] * (1 - ratio) + color2[0] * ratio)
        g = int(color1[1] * (1 - ratio) + color2[1] * ratio)
        b = int(color1[2] * (1 - ratio) + color2[2] * ratio)
        color = (max(0, min(255, r)), max(0, min(255, g)), max(0, min(255, b)))
        if vertical:
            pygame.draw.line(surface, color, (0, i), (width, i))
        else:
            pygame.draw.line(surface, color, (i, 0), (i, height))
    return surface


def create_player_sprite(width, height):
    surface = pygame.Surface((width, height), pygame.SRCALPHA)
    # Body gradient
    body_rect = pygame.Rect(5, 15, width - 10, height - 25)
    pygame.draw.ellipse(surface, COLORS['PLAYER_BLUE'], body_rect)
    pygame.draw.ellipse(surface,
                        (COLORS['PLAYER_BLUE'][0] + 20, COLORS['PLAYER_BLUE'][1] + 20, COLORS['PLAYER_BLUE'][2] + 20),
                        (7, 17, width - 14, height - 29))

    # Head with gradient
    pygame.draw.circle(surface, COLORS['PLAYER_BLUE'], (width // 2, 12), 10)
    pygame.draw.circle(surface,
                       (COLORS['PLAYER_BLUE'][0] + 20, COLORS['PLAYER_BLUE'][1] + 20, COLORS['PLAYER_BLUE'][2] + 20),
                       (width // 2, 12), 8)

    # Eyes with shine
    pygame.draw.circle(surface, COLORS['WHITE'], (width // 2 - 4, 10), 3)
    pygame.draw.circle(surface, COLORS['WHITE'], (width // 2 + 4, 10), 3)
    pygame.draw.circle(surface, COLORS['BLACK'], (width // 2 - 4, 10), 2)
    pygame.draw.circle(surface, COLORS['BLACK'], (width // 2 + 4, 10), 2)
    pygame.draw.circle(surface, COLORS['WHITE'], (width // 2 - 3, 9), 1)
    pygame.draw.circle(surface, COLORS['WHITE'], (width // 2 + 5, 9), 1)

    # Legs
    pygame.draw.rect(surface, COLORS['PLAYER_BLUE'], (width // 2 - 8, height - 15, 5, 12))
    pygame.draw.rect(surface, COLORS['PLAYER_BLUE'], (width // 2 + 3, height - 15, 5, 12))

    return surface


def create_fire_frames():
    frames = []
    for frame in range(6):
        surface = pygame.Surface((80, 50), pygame.SRCALPHA)

        # Multiple fire layers for depth
        for layer in range(3):
            flame_points = []
            base_y = 45
            base_width = 60 - layer * 15

            # Create flame shape
            for i in range(8):
                angle = i * math.pi / 7
                height_var = random.randint(-3, 8) + (2 - layer) * 5
                x = 40 + math.cos(angle) * (base_width / 2)
                y = base_y - height_var - layer * 5
                flame_points.append((x, y))

            # Draw flame layers
            if layer == 0:
                color = COLORS['FIRE_RED']
            elif layer == 1:
                color = COLORS['FIRE_ORANGE']
            else:
                color = COLORS['FIRE_YELLOW']

            if len(flame_points) > 2:
                pygame.draw.polygon(surface, color, flame_points)

        frames.append(surface)
    return frames


def create_water_surface(width, height):
    surface = pygame.Surface((width, height))
    time_offset = pygame.time.get_ticks() * 0.005

    for y in range(height):
        # Create wave pattern
        wave1 = math.sin(y * 0.1 + time_offset) * 15
        wave2 = math.sin(y * 0.05 + time_offset * 1.5) * 10

        # Color variation based on waves
        base_color = COLORS['WATER_BLUE']
        variation = int(20 * math.sin(y * 0.1 + time_offset))

        water_color = (
            max(10, min(255, base_color[0] + variation)),
            max(10, min(255, base_color[1] + variation)),
            max(200, min(255, base_color[2] + variation))
        )

        # Draw wave lines
        start_x = max(0, int(wave1 + wave2))
        end_x = min(width, width + int(wave1 + wave2))
        pygame.draw.line(surface, water_color, (start_x, y), (end_x, y))

    return surface


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = create_player_sprite(40, 60)
        self.rect = self.image.get_rect()
        self.start_x = 100
        self.start_y = SCREEN_HEIGHT - 200
        self.rect.x = self.start_x
        self.rect.y = self.start_y
        self.velocity_x = 0
        self.velocity_y = 0
        self.on_ground = False
        self.has_key = False
        self.can_jump = True
        self.jump_buffer = 0
        self.coyote_time = 0
        self.facing_right = True
        self.animation_timer = 0
        self.particles = []

    def update(self, platforms, obstacles):
        # Don't update player physics when input dialog is open
        if hasattr(self, 'game_paused') and self.game_paused:
            return

        # Smooth horizontal movement
        self.velocity_x *= 0.9

        # Apply gravity
        if not self.on_ground:
            self.velocity_y += GRAVITY
            if self.velocity_y > TERMINAL_VELOCITY:
                self.velocity_y = TERMINAL_VELOCITY

        # Update position
        old_x, old_y = self.rect.x, self.rect.y
        self.rect.x += self.velocity_x
        self.rect.y += self.velocity_y

        # Check platform collisions
        self.check_platform_collisions(platforms)

        # Check for gaps (falling through)
        self.check_gap_collisions(obstacles)

        # Check deadly obstacle collisions
        for obstacle in obstacles:
            if self.rect.colliderect(obstacle.rect):
                if obstacle.obstacle_type in ['fire', 'water_deadly']:
                    self.create_death_particles()
                    self.respawn()

        # Update jump mechanics
        if self.jump_buffer > 0:
            self.jump_buffer -= 1
            if self.on_ground or self.coyote_time > 0:
                self.velocity_y = JUMP_STRENGTH
                self.can_jump = False
                self.coyote_time = 0
                self.jump_buffer = 0

        if self.on_ground:
            self.coyote_time = 8
            self.can_jump = True
        elif self.coyote_time > 0:
            self.coyote_time -= 1

        # Screen boundaries
        if self.rect.left < 0:
            self.rect.left = 0
            self.velocity_x = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
            self.velocity_x = 0
        if self.rect.top < 0:
            self.rect.top = 0
            self.velocity_y = 0
        if self.rect.bottom > SCREEN_HEIGHT:
            self.respawn()

        # Create movement particles
        if abs(self.velocity_x) > 2 and self.on_ground:
            self.create_movement_particles()

        # Update particles
        self.particles = [p for p in self.particles if p.update()]

        self.animation_timer += 1

    def check_platform_collisions(self, platforms):
        self.on_ground = False

        for platform in platforms:
            if self.rect.colliderect(platform.rect):
                # Calculate overlap amounts
                overlap_left = self.rect.right - platform.rect.left
                overlap_right = platform.rect.right - self.rect.left
                overlap_top = self.rect.bottom - platform.rect.top
                overlap_bottom = platform.rect.bottom - self.rect.top

                # Find the smallest overlap to determine collision direction
                min_overlap = min(overlap_left, overlap_right, overlap_top, overlap_bottom)

                # Vertical collision (landing on top or hitting from below)
                if min_overlap == overlap_top and self.velocity_y > 0:  # Landing on top
                    self.rect.bottom = platform.rect.top
                    self.velocity_y = 0
                    self.on_ground = True
                elif min_overlap == overlap_bottom and self.velocity_y < 0:  # Hitting from below
                    self.rect.top = platform.rect.bottom
                    self.velocity_y = 0
                # Horizontal collision
                elif min_overlap == overlap_left and self.velocity_x > 0:  # Moving right
                    self.rect.right = platform.rect.left
                    self.velocity_x = 0
                elif min_overlap == overlap_right and self.velocity_x < 0:  # Moving left
                    self.rect.left = platform.rect.right
                    self.velocity_x = 0

    def check_gap_collisions(self, obstacles):
        for obstacle in obstacles:
            if obstacle.obstacle_type == "gap":
                if (self.rect.centerx > obstacle.rect.left and
                        self.rect.centerx < obstacle.rect.right and
                        self.rect.bottom >= obstacle.rect.top):
                    # Player is in the gap area and should fall
                    if self.rect.bottom > SCREEN_HEIGHT - 100:
                        self.create_death_particles()
                        self.respawn()

    def jump(self):
        if self.on_ground or self.coyote_time > 0:
            self.velocity_y = JUMP_STRENGTH
            self.can_jump = False
            self.coyote_time = 0
            self.create_jump_particles()
        else:
            self.jump_buffer = 8

    def move_left(self):
        self.velocity_x -= 0.8
        self.facing_right = False
        if self.velocity_x < -PLAYER_SPEED:
            self.velocity_x = -PLAYER_SPEED

    def move_right(self):
        self.velocity_x += 0.8
        self.facing_right = True
        if self.velocity_x > PLAYER_SPEED:
            self.velocity_x = PLAYER_SPEED

    def create_movement_particles(self):
        if random.random() < 0.3:
            self.particles.append(Particle(
                self.rect.centerx + random.randint(-5, 5),
                self.rect.bottom - 5,
                (200, 200, 200),
                random.uniform(-1, 1),
                random.uniform(-2, 0),
                20,
                2
            ))

    def create_jump_particles(self):
        for _ in range(8):
            self.particles.append(Particle(
                self.rect.centerx + random.randint(-10, 10),
                self.rect.bottom,
                COLORS['WHITE'],
                random.uniform(-2, 2),
                random.uniform(-1, -3),
                30,
                random.randint(2, 4)
            ))

    def create_death_particles(self):
        for _ in range(15):
            self.particles.append(Particle(
                self.rect.centerx + random.randint(-20, 20),
                self.rect.centery + random.randint(-20, 20),
                random.choice([COLORS['RED'], COLORS['ORANGE'], COLORS['FIRE_YELLOW']]),
                random.uniform(-4, 4),
                random.uniform(-6, -2),
                60,
                random.randint(3, 6)
            ))

    def respawn(self):
        self.rect.x = self.start_x
        self.rect.y = self.start_y
        self.velocity_x = 0
        self.velocity_y = 0
        self.has_key = False

    def draw_particles(self, surface):
        for particle in self.particles:
            particle.draw(surface)


class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, platform_type="normal", color=None):
        super().__init__()
        self.platform_type = platform_type
        self.creation_time = pygame.time.get_ticks()

        if platform_type == "bridge":
            self.image = self.create_bridge_sprite(width, height)
        elif platform_type == "ladder":
            self.image = self.create_ladder_sprite(width, height)
        elif platform_type == "ice":
            self.image = self.create_ice_sprite(width, height)
        else:
            self.image = self.create_normal_platform(width, height, color or COLORS['GRASS_GREEN'])

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.scale = 0.1 if platform_type in ["bridge", "ladder", "ice"] else 1.0

    def update(self):
        # Smooth appearance animation for created platforms
        if self.scale < 1.0:
            self.scale = min(1.0, self.scale + 0.1)
            if self.platform_type in ["bridge", "ladder", "ice"]:
                original_center = self.rect.center
                scaled_surface = pygame.transform.scale(self.image,
                                                        (int(self.rect.width * self.scale),
                                                         int(self.rect.height * self.scale)))
                self.rect = scaled_surface.get_rect()
                self.rect.center = original_center

    def create_normal_platform(self, width, height, color):
        surface = pygame.Surface((width, height))
        # Gradient effect
        gradient = create_gradient_surface(width, height, color,
                                           (max(0, color[0] - 40), max(0, color[1] - 40), max(0, color[2] - 40)))
        surface.blit(gradient, (0, 0))

        # Texture lines
        for i in range(0, width, 15):
            pygame.draw.line(surface, (color[0] - 30, color[1] - 30, color[2] - 30),
                             (i, 0), (i, height), 2)
        # Top highlight
        pygame.draw.line(surface, (min(255, color[0] + 50), min(255, color[1] + 50), min(255, color[2] + 50)),
                         (0, 0), (width, 0), 2)
        return surface

    def create_bridge_sprite(self, width, height):
        surface = pygame.Surface((width, height))
        # Wood gradient
        wood_gradient = create_gradient_surface(width, height, COLORS['WOOD_BROWN'], COLORS['DARK_BROWN'])
        surface.blit(wood_gradient, (0, 0))

        # Planks
        for i in range(0, width, 25):
            pygame.draw.line(surface, COLORS['DARK_BROWN'], (i, 0), (i, height), 3)

        # Rope details
        pygame.draw.line(surface, (101, 67, 33), (0, 2), (width, 2), 2)
        pygame.draw.line(surface, (101, 67, 33), (0, height - 2), (width, height - 2), 2)

        # Nails/bolts
        for i in range(12, width, 25):
            pygame.draw.circle(surface, (60, 40, 20), (i, height // 2), 2)

        return surface

    def create_ladder_sprite(self, width, height):
        surface = pygame.Surface((width, height), pygame.SRCALPHA)

        # Vertical supports with gradient
        for x in [4, width - 8]:
            pygame.draw.rect(surface, COLORS['WOOD_BROWN'], (x, 0, 6, height))
            pygame.draw.rect(surface, COLORS['DARK_BROWN'], (x + 1, 0, 2, height))

        # Horizontal rungs
        for y in range(8, height, 18):
            pygame.draw.rect(surface, COLORS['WOOD_BROWN'], (0, y, width, 5))
            pygame.draw.rect(surface, COLORS['DARK_BROWN'], (0, y + 1, width, 2))

        return surface

    def create_ice_sprite(self, width, height):
        surface = pygame.Surface((width, height))

        # Ice gradient
        ice_gradient = create_gradient_surface(width, height,
                                               (min(255, COLORS['ICE_BLUE'][0] + 40),
                                                min(255, COLORS['ICE_BLUE'][1] + 40),
                                                min(255, COLORS['ICE_BLUE'][2] + 40)),
                                               COLORS['ICE_BLUE'])
        surface.blit(ice_gradient, (0, 0))

        # Ice shine effects
        for i in range(0, width, 30):
            pygame.draw.line(surface, COLORS['WHITE'], (i, 3), (i + 15, 3), 2)
            pygame.draw.line(surface, (200, 230, 255), (i + 5, height // 2), (i + 20, height // 2), 1)

        # Crystalline pattern
        for i in range(0, width, 15):
            for j in range(0, height, 10):
                if random.random() < 0.3:
                    pygame.draw.circle(surface, COLORS['WHITE'], (i, j), 1)

        return surface


class Obstacle(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, obstacle_type):
        super().__init__()
        self.obstacle_type = obstacle_type
        self.rect = pygame.Rect(x, y, width, height)
        self.particles = []

        if obstacle_type == "fire":
            self.fire_animation = AnimatedSprite(create_fire_frames(), 6)
            self.image = self.fire_animation.get_current_frame()
        elif obstacle_type == "water_deadly":
            self.image = create_water_surface(width, height)
        elif obstacle_type == "gap":
            # Gap is invisible but deadly
            self.image = pygame.Surface((width, height), pygame.SRCALPHA)
        else:
            self.image = pygame.Surface((width, height))
            self.image.fill(COLORS['STONE_GRAY'])

    def update(self):
        if self.obstacle_type == "fire":
            self.fire_animation.update()
            self.image = self.fire_animation.get_current_frame()

            # Create fire particles
            if random.random() < 0.4:
                self.particles.append(Particle(
                    self.rect.centerx + random.randint(-25, 25),
                    self.rect.top + random.randint(0, 10),
                    random.choice([COLORS['FIRE_RED'], COLORS['FIRE_ORANGE'], COLORS['FIRE_YELLOW']]),
                    random.uniform(-1, 1),
                    random.uniform(-4, -1),
                    random.randint(40, 80),
                    random.randint(2, 4)
                ))

            self.particles = [p for p in self.particles if p.update()]

        elif self.obstacle_type == "water_deadly":
            self.image = create_water_surface(self.rect.width, self.rect.height)

    def draw_particles(self, surface):
        for particle in self.particles:
            particle.draw(surface)


class InteractiveObject(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, object_type):
        super().__init__()
        self.object_type = object_type
        self.rect = pygame.Rect(x, y, width, height)
        self.collected = False
        self.float_offset = 0
        self.creation_time = pygame.time.get_ticks()
        self.scale = 0.1
        self.particles = []

        if object_type == "key":
            self.image = self.create_key_sprite(width, height)
        elif object_type == "door":
            self.image = self.create_door_sprite(width, height)
            self.locked = True
            self.scale = 1.0

    def create_key_sprite(self, width, height):
        surface = pygame.Surface((width, height), pygame.SRCALPHA)

        # Key body with gradient
        body_rect = (2, 2, width - 4, height // 2)
        pygame.draw.ellipse(surface, COLORS['GOLD'], body_rect)
        pygame.draw.ellipse(surface, (255, 235, 50), (4, 4, width - 8, height // 2 - 4))

        # Key shaft
        shaft_rect = (width // 2 - 2, height // 2, 4, height // 2)
        pygame.draw.rect(surface, COLORS['GOLD'], shaft_rect)
        pygame.draw.rect(surface, (255, 235, 50), (width // 2 - 1, height // 2, 2, height // 2))

        # Key teeth with detail
        pygame.draw.rect(surface, COLORS['GOLD'], (width // 2 + 2, height - 10, 8, 5))
        pygame.draw.rect(surface, COLORS['GOLD'], (width // 2 + 2, height - 5, 10, 5))

        return surface

    def create_door_sprite(self, width, height):
        surface = pygame.Surface((width, height))

        # Door gradient
        door_gradient = create_gradient_surface(width, height, COLORS['WOOD_BROWN'], COLORS['DARK_BROWN'])
        surface.blit(door_gradient, (0, 0))

        # Door frame
        pygame.draw.rect(surface, COLORS['DARK_BROWN'], (0, 0, width, height), 3)

        # Door panels
        panel1 = pygame.Rect(6, 6, width - 12, height // 2 - 8)
        panel2 = pygame.Rect(6, height // 2 + 2, width - 12, height // 2 - 8)
        pygame.draw.rect(surface,
                         (COLORS['WOOD_BROWN'][0] + 20, COLORS['WOOD_BROWN'][1] + 20, COLORS['WOOD_BROWN'][2] + 20),
                         panel1)
        pygame.draw.rect(surface,
                         (COLORS['WOOD_BROWN'][0] + 20, COLORS['WOOD_BROWN'][1] + 20, COLORS['WOOD_BROWN'][2] + 20),
                         panel2)
        pygame.draw.rect(surface, COLORS['DARK_BROWN'], panel1, 2)
        pygame.draw.rect(surface, COLORS['DARK_BROWN'], panel2, 2)

        # Door handle
        pygame.draw.circle(surface, COLORS['GOLD'], (width - 15, height // 2), 5)
        pygame.draw.circle(surface, (255, 235, 50), (width - 15, height // 2), 3)

        # Keyhole
        if hasattr(self, 'locked') and self.locked:
            pygame.draw.circle(surface, COLORS['BLACK'], (width - 15, height // 2 + 12), 4)
            pygame.draw.rect(surface, COLORS['BLACK'], (width - 17, height // 2 + 12, 4, 6))

        return surface

    def update(self):
        # Scale animation for new objects
        if self.scale < 1.0:
            self.scale = min(1.0, self.scale + 0.08)

        if self.object_type == "key" and not self.collected:
            self.float_offset += 0.08
            float_y = math.sin(self.float_offset) * 3
            self.rect.y += float_y

            # Create sparkle particles
            if random.random() < 0.2:
                self.particles.append(Particle(
                    self.rect.centerx + random.randint(-8, 8),
                    self.rect.centery + random.randint(-8, 8),
                    COLORS['GOLD'],
                    random.uniform(-0.5, 0.5),
                    random.uniform(-1, 1),
                    30,
                    1
                ))

        self.particles = [p for p in self.particles if p.update()]

    def draw_particles(self, surface):
        for particle in self.particles:
            particle.draw(surface)


class Game:
    def __init__(self):
        self.player = Player()
        self.platforms = pygame.sprite.Group()
        self.obstacles = pygame.sprite.Group()
        self.interactive_objects = pygame.sprite.Group()
        self.current_level = 1
        self.max_level = 5
        self.input_text = ""
        self.show_input = False
        self.message = ""
        self.message_timer = 0
        self.level_complete = False
        self.particles = []
        self.camera_shake = 0
        self.word_hints = {
            1: "You need to cross the water gap. What structure helps you cross?",
            2: "The platform is too high to jump. What helps you climb?",
            3: "Fire blocks your path. What can extinguish fire?",
            4: "The door is locked. What do you need? Then how do you use it?",
            5: "Multiple obstacles! Use what you've learned."
        }
        self.setup_level()

    def setup_level(self):
        # Clear existing objects
        self.platforms.empty()
        self.obstacles.empty()
        self.interactive_objects.empty()
        self.level_complete = False
        self.input_text = ""
        self.show_input = False
        self.message = ""
        self.player.has_key = False
        self.particles = []

        # Reset player
        self.player.start_x = 100
        self.player.start_y = SCREEN_HEIGHT - 200
        self.player.rect.x = self.player.start_x
        self.player.rect.y = self.player.start_y
        self.player.velocity_x = 0
        self.player.velocity_y = 0

        # Level-specific setup
        if self.current_level == 1:
            self.setup_bridge_level()
        elif self.current_level == 2:
            self.setup_ladder_level()
        elif self.current_level == 3:
            self.setup_fire_level()
        elif self.current_level == 4:
            self.setup_door_level()
        elif self.current_level == 5:
            self.setup_final_level()

        # Goal flag
        self.goal_rect = pygame.Rect(SCREEN_WIDTH - 80, SCREEN_HEIGHT - 130, 60, 80)

    def setup_bridge_level(self):
        # Ground platforms with gap
        self.platforms.add(Platform(0, SCREEN_HEIGHT - 50, 280, 50))
        self.obstacles.add(Obstacle(280, SCREEN_HEIGHT - 100, 440, 100, "gap"))
        self.platforms.add(Platform(720, SCREEN_HEIGHT - 50, 480, 50))

    def setup_ladder_level(self):
        # Ground and high platform
        self.platforms.add(Platform(0, SCREEN_HEIGHT - 50, 450, 50))
        self.platforms.add(Platform(650, SCREEN_HEIGHT - 280, 250, 30))
        self.platforms.add(Platform(950, SCREEN_HEIGHT - 50, 250, 50))

    def setup_fire_level(self):
        # Ground with fire obstacle
        self.platforms.add(Platform(0, SCREEN_HEIGHT - 50, 400, 50))
        self.obstacles.add(Obstacle(400, SCREEN_HEIGHT - 80, 80, 30, "fire"))
        self.platforms.add(Platform(500, SCREEN_HEIGHT - 50, 700, 50))

    def setup_door_level(self):
        # Ground, key platform, and door
        self.platforms.add(Platform(0, SCREEN_HEIGHT - 50, 350, 50))
        self.platforms.add(Platform(450, SCREEN_HEIGHT - 180, 120, 30))
        self.platforms.add(Platform(700, SCREEN_HEIGHT - 50, 200, 50))
        self.interactive_objects.add(InteractiveObject(920, SCREEN_HEIGHT - 150, 60, 100, "door"))
        self.platforms.add(Platform(1000, SCREEN_HEIGHT - 50, 200, 50))

    def setup_final_level(self):
        # Combined challenges
        self.platforms.add(Platform(0, SCREEN_HEIGHT - 50, 180, 50))
        # Gap 1
        self.obstacles.add(Obstacle(180, SCREEN_HEIGHT - 100, 140, 100, "gap"))
        self.platforms.add(Platform(320, SCREEN_HEIGHT - 50, 120, 50))
        # Fire
        self.obstacles.add(Obstacle(440, SCREEN_HEIGHT - 80, 80, 30, "fire"))
        self.platforms.add(Platform(540, SCREEN_HEIGHT - 50, 120, 50))
        # High platform requiring ladder
        self.platforms.add(Platform(750, SCREEN_HEIGHT - 250, 200, 30))
        self.platforms.add(Platform(1000, SCREEN_HEIGHT - 50, 200, 50))

    def handle_input(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if self.show_input:
                    self.process_word()
                    self.show_input = False
                    self.input_text = ""
                else:
                    self.show_input = True
            elif event.key == pygame.K_BACKSPACE:
                if len(self.input_text) > 0:
                    self.input_text = self.input_text[:-1]
            elif event.key == pygame.K_ESCAPE:
                self.show_input = False
                self.input_text = ""
            else:
                if self.show_input and len(self.input_text) < 15:
                    if event.unicode.isalpha() or event.unicode == ' ':
                        self.input_text += event.unicode

    def process_word(self):
        word = self.input_text.lower().strip()
        player_x = self.player.rect.centerx
        success = False

        # Level 1: Bridge
        if self.current_level == 1 and word == "bridge":
            if 200 < player_x < 400:
                self.platforms.add(Platform(280, SCREEN_HEIGHT - 70, 440, 20, "bridge"))
                self.remove_obstacles("gap")
                self.show_success_message("A sturdy bridge appears!")
                success = True

        # Level 2: Ladder
        elif self.current_level == 2 and word == "ladder":
            if 500 < player_x < 700:
                for i in range(15):
                    self.platforms.add(Platform(670, SCREEN_HEIGHT - 60 - i * 15, 25, 8, "ladder"))
                self.show_success_message("A ladder materializes!")
                success = True

        # Level 3: Water or Ice
        elif self.current_level == 3 and word in ["water", "ice"]:
            if 350 < player_x < 450:
                self.remove_obstacles("fire")
                self.platforms.add(Platform(400, SCREEN_HEIGHT - 80, 100, 30, "ice"))
                self.show_success_message(f"{word.capitalize()} extinguishes the fire!")
                success = True

        # Level 4: Key
        elif self.current_level == 4 and word == "key":
            if 400 < player_x < 600:
                key = InteractiveObject(490, SCREEN_HEIGHT - 210, 25, 35, "key")
                self.interactive_objects.add(key)
                self.show_success_message("A golden key appears!")
                success = True

        # Level 4: Open door
        elif self.current_level == 4 and word == "open" and self.player.has_key:
            if 850 < player_x < 980:
                self.remove_interactive_objects("door")
                self.show_success_message("The door swings open!")
                success = True

        # Level 5: Multiple solutions
        elif self.current_level == 5:
            if word == "bridge" and 150 < player_x < 220:
                self.platforms.add(Platform(180, SCREEN_HEIGHT - 70, 140, 20, "bridge"))
                self.remove_obstacles("gap")
                self.show_success_message("Bridge built!")
                success = True
            elif word in ["water", "ice"] and 400 < player_x < 500:
                self.remove_obstacles("fire")
                self.platforms.add(Platform(440, SCREEN_HEIGHT - 80, 80, 30, "ice"))
                self.show_success_message("Fire extinguished!")
                success = True
            elif word == "ladder" and 680 < player_x < 780:
                for i in range(12):
                    self.platforms.add(Platform(720, SCREEN_HEIGHT - 60 - i * 18, 25, 8, "ladder"))
                self.show_success_message("Ladder erected!")
                success = True

        if success:
            self.create_success_particles(player_x, self.player.rect.centery)
            self.camera_shake = 10
        else:
            self.show_error_message(f"'{word}' doesn't work here. Think about what you need!")

    def remove_obstacles(self, obstacle_type):
        for obstacle in list(self.obstacles):
            if obstacle.obstacle_type == obstacle_type:
                obstacle.kill()

    def remove_interactive_objects(self, object_type):
        for obj in list(self.interactive_objects):
            if obj.object_type == object_type:
                obj.kill()

    def create_success_particles(self, x, y):
        for _ in range(20):
            self.particles.append(Particle(
                x + random.randint(-30, 30),
                y + random.randint(-30, 30),
                random.choice([COLORS['GOLD'], COLORS['WHITE'], COLORS['GREEN']]),
                random.uniform(-3, 3),
                random.uniform(-5, -1),
                80,
                random.randint(3, 6)
            ))

    def show_success_message(self, msg):
        self.message = msg
        self.message_timer = 180

    def show_error_message(self, msg):
        self.message = msg
        self.message_timer = 120

    def update(self):
        # Pause player physics when input dialog is open
        self.player.game_paused = self.show_input

        # Update player
        self.player.update(self.platforms, self.obstacles)

        # Update platforms
        for platform in self.platforms:
            platform.update()

        # Update obstacles
        for obstacle in self.obstacles:
            obstacle.update()

        # Update interactive objects
        for obj in self.interactive_objects:
            obj.update()
            if (obj.object_type == "key" and not obj.collected and
                    self.player.rect.colliderect(obj.rect)):
                self.player.has_key = True
                obj.collected = True
                obj.kill()
                self.show_success_message("Key collected! Find the door and say 'open'!")

        # Update particles
        self.particles = [p for p in self.particles if p.update()]

        # Camera shake
        if self.camera_shake > 0:
            self.camera_shake -= 1

        # Goal check
        if self.player.rect.colliderect(self.goal_rect) and not self.level_complete:
            self.level_complete = True
            if self.current_level < self.max_level:
                self.message = f"Level {self.current_level} Complete! Press SPACE for next level"
            else:
                self.message = "🎉 All levels complete! Press SPACE to restart"
            self.message_timer = 300
            self.create_success_particles(self.goal_rect.centerx, self.goal_rect.centery)

        # Message timer
        if self.message_timer > 0:
            self.message_timer -= 1
            if self.message_timer == 0:
                self.message = ""

    def draw(self):
        # Camera shake offset
        shake_x = random.randint(-self.camera_shake, self.camera_shake) if self.camera_shake > 0 else 0
        shake_y = random.randint(-self.camera_shake, self.camera_shake) if self.camera_shake > 0 else 0

        # Dynamic background
        self.draw_background()

        # Draw all game objects with shake offset
        self.draw_platforms(shake_x, shake_y)
        self.draw_obstacles(shake_x, shake_y)
        self.draw_interactive_objects(shake_x, shake_y)
        self.draw_goal(shake_x, shake_y)
        self.draw_player(shake_x, shake_y)
        self.draw_particles()

        # UI elements (not affected by shake)
        self.draw_ui()

        pygame.display.flip()

    def draw_background(self):
        time_factor = pygame.time.get_ticks() * 0.001

        if self.current_level == 1:
            # Animated water theme
            color1 = (135 + int(20 * math.sin(time_factor)), 206, 235)
            color2 = (30, 144 + int(30 * math.sin(time_factor * 0.5)), 255)
        elif self.current_level == 3:
            # Fire theme with flickering
            color1 = (255, 200 + int(30 * math.sin(time_factor * 2)), 150)
            color2 = (255, 150 + int(50 * math.sin(time_factor)), 100)
        else:
            # Sky theme
            color1 = (135, 206, 235)
            color2 = (200, 230, 255)

        bg = create_gradient_surface(SCREEN_WIDTH, SCREEN_HEIGHT, color1, color2)
        screen.blit(bg, (0, 0))

        # Add floating background particles
        if len(self.particles) < 50:
            if random.random() < 0.02:
                self.particles.append(Particle(
                    random.randint(0, SCREEN_WIDTH),
                    -10,
                    (255, 255, 255, 50),
                    random.uniform(-0.5, 0.5),
                    random.uniform(0.5, 2),
                    300,
                    random.randint(1, 3)
                ))

    def draw_platforms(self, shake_x, shake_y):
        for platform in self.platforms:
            screen.blit(platform.image, (platform.rect.x + shake_x, platform.rect.y + shake_y))

    def draw_obstacles(self, shake_x, shake_y):
        for obstacle in self.obstacles:
            if obstacle.obstacle_type != "gap":
                screen.blit(obstacle.image, (obstacle.rect.x + shake_x, obstacle.rect.y + shake_y))
            obstacle.draw_particles(screen)

    def draw_interactive_objects(self, shake_x, shake_y):
        for obj in self.interactive_objects:
            if not obj.collected:
                screen.blit(obj.image, (obj.rect.x + shake_x, obj.rect.y + shake_y))
                obj.draw_particles(screen)

    def draw_goal(self, shake_x, shake_y):
        # Animated goal flag
        flag_surface = pygame.Surface((60, 80))
        time_wave = pygame.time.get_ticks() * 0.01

        # Flag pole
        pygame.draw.line(flag_surface, COLORS['DARK_BROWN'], (10, 10), (10, 80), 4)

        # Animated flag
        flag_points = [
            (10, 10),
            (50 + int(5 * math.sin(time_wave)), 10),
            (48 + int(3 * math.sin(time_wave + 0.5)), 25),
            (10, 25)
        ]
        pygame.draw.polygon(flag_surface, COLORS['RED'], flag_points)
        pygame.draw.polygon(flag_surface, COLORS['WHITE'], [
            (15, 13), (45 + int(3 * math.sin(time_wave)), 13),
            (43 + int(2 * math.sin(time_wave + 0.5)), 22), (15, 22)
        ])

        screen.blit(flag_surface, (self.goal_rect.x + shake_x, self.goal_rect.y + shake_y))

    def draw_player(self, shake_x, shake_y):
        # Draw player with facing direction
        player_image = self.player.image
        if not self.player.facing_right:
            player_image = pygame.transform.flip(player_image, True, False)

        screen.blit(player_image, (self.player.rect.x + shake_x, self.player.rect.y + shake_y))
        self.player.draw_particles(screen)

        # Draw key inventory
        if self.player.has_key:
            key_bg = pygame.Surface((60, 35))
            key_bg.fill(COLORS['WHITE'])
            key_bg.set_alpha(200)
            screen.blit(key_bg, (15, 15))

            key_icon = pygame.Surface((20, 20))
            key_icon.fill(COLORS['GOLD'])
            screen.blit(key_icon, (20, 20))

            key_text = font_small.render("KEY", True, COLORS['BLACK'])
            screen.blit(key_text, (45, 25))

    def draw_particles(self):
        for particle in self.particles:
            particle.draw(screen)

    def draw_ui(self):
        # Level indicator with style
        level_bg = pygame.Surface((180, 50))
        level_bg.fill(COLORS['WHITE'])
        level_bg.set_alpha(220)
        screen.blit(level_bg, (SCREEN_WIDTH - 200, 15))

        level_text = font_medium.render(f"Level {self.current_level}/{self.max_level}", True, COLORS['BLACK'])
        screen.blit(level_text, (SCREEN_WIDTH - 190, 25))

        # Input dialog
        if self.show_input:
            self.draw_input_dialog()

        # Message display
        if self.message:
            self.draw_message()

        # Instructions
        if not self.show_input:
            self.draw_instructions()

    def draw_input_dialog(self):
        # Overlay
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 180))
        screen.blit(overlay, (0, 0))

        # Dialog box with animation
        box_width, box_height = 700, 150
        box_x = (SCREEN_WIDTH - box_width) // 2
        box_y = (SCREEN_HEIGHT - box_height) // 2

        # Box with gradient
        dialog_surface = pygame.Surface((box_width, box_height))
        dialog_gradient = create_gradient_surface(box_width, box_height, COLORS['WHITE'], (240, 240, 255))
        dialog_surface.blit(dialog_gradient, (0, 0))
        pygame.draw.rect(dialog_surface, COLORS['BLUE'], (0, 0, box_width, box_height), 4)
        screen.blit(dialog_surface, (box_x, box_y))

        # Prompt
        prompt = font_large.render("What word will help you here?", True, COLORS['BLACK'])
        screen.blit(prompt, (box_x + 20, box_y + 20))

        # Input field
        input_bg = pygame.Rect(box_x + 20, box_y + 70, box_width - 40, 40)
        pygame.draw.rect(screen, COLORS['WHITE'], input_bg)
        pygame.draw.rect(screen, COLORS['BLUE'], input_bg, 2)

        # Input text with cursor
        cursor_blink = int(pygame.time.get_ticks() / 500) % 2
        display_text = self.input_text + ("|" if cursor_blink else "")
        input_surface = font_large.render(display_text, True, COLORS['BLUE'])
        screen.blit(input_surface, (box_x + 30, box_y + 80))

        # Hint
        hint = self.word_hints.get(self.current_level, "")
        hint_surface = font_small.render(hint, True, COLORS['STONE_GRAY'])
        screen.blit(hint_surface, (box_x + 20, box_y + 120))

    def draw_message(self):
        msg_width = len(self.message) * 14 + 60
        msg_height = 60
        msg_x = (SCREEN_WIDTH - msg_width) // 2
        msg_y = 70

        # Message background
        msg_bg = pygame.Surface((msg_width, msg_height))
        msg_bg.fill(COLORS['WHITE'])
        msg_bg.set_alpha(240)
        screen.blit(msg_bg, (msg_x, msg_y))
        pygame.draw.rect(screen, COLORS['GREEN'], (msg_x, msg_y, msg_width, msg_height), 3)

        # Message text
        msg_surface = font_medium.render(self.message, True, COLORS['BLACK'])
        msg_rect = msg_surface.get_rect(center=(SCREEN_WIDTH // 2, msg_y + msg_height // 2))
        screen.blit(msg_surface, msg_rect)

    def draw_instructions(self):
        instructions = [
            "ARROW KEYS / WASD: Move  •  SPACE: Jump  •  ENTER: Type word",
            "Stand near obstacles and type the right word to overcome them!"
        ]

        for i, instruction in enumerate(instructions):
            inst_surface = font_small.render(instruction, True, COLORS['WHITE'])
            inst_rect = inst_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 50 + i * 25))

            # Text shadow
            shadow = font_small.render(instruction, True, COLORS['BLACK'])
            screen.blit(shadow, (inst_rect.x + 2, inst_rect.y + 2))
            screen.blit(inst_surface, inst_rect)

    def next_level(self):
        if self.level_complete:
            if self.current_level < self.max_level:
                self.current_level += 1
            else:
                self.current_level = 1
            self.setup_level()


def main():
    game = Game()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            game.handle_input(event)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if game.level_complete:
                        game.next_level()
                    else:
                        game.player.jump()

        # Continuous movement (only when not in input mode)
        if not game.show_input:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                game.player.move_left()
            if keys[pygame.K_RIGHT]:
                game.player.move_right()

        game.update()
        game.draw()
        clock.tick(60)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()