# Space Shooter

An Asteroids-style arcade game built with **Pygame**.

Fly a triangular ship, dodge incoming asteroids and shoot them down. Large asteroids split into two smaller, faster pieces when hit, and the smallest ones are destroyed. Touching an asteroid ends the game.

## Controls

| Key | Action |
|---|---|
| `W` / `S` | Thrust forward / backward |
| `A` / `D` | Rotate left / right |
| `Space` | Shoot (0.5 s cooldown) |

## Design

The game is organized around a shared `CircleShape` base class (a `pygame.sprite.Sprite` with position, velocity, radius and circle-to-circle collision detection). `Player`, `Asteroid` and `Shot` all extend it. Sprites register themselves in `updatable` and `drawable` groups, so the main loop stays short: update everything, check collisions, draw everything, then tick at 60 FPS with a frame-time `dt` for frame-rate-independent movement.

```
main.py          # game loop, sprite groups, collision checks
circleshape.py   # base class: position, velocity, radius, collision test
player.py        # ship movement, rotation, shooting
asteroid.py      # asteroid movement and splitting
asteroidfield.py # spawns asteroids from the screen edges
shooting.py      # projectile
constants.py     # screen size, speeds, spawn rate, cooldowns
```

## Running it

```bash
pip install -r requirements.txt
python main.py
```

## Tech stack

Python · Pygame 2.6
