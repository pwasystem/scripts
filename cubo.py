import pygame
from pygame.locals import *

# Cores das faces
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
BLACK = (0, 0, 0)

# Dimensões
CUBE_SIZE = 40
OFFSET = 15

def rotate_face_clockwise(face):
    return [list(row) for row in zip(*face[::-1])]

def rotate_face_counter_clockwise(face):
    return [list(row[::-1]) for row in zip(*face)]

class RubiksCube:
    def __init__(self):
        self.reset_cube()

    def reset_cube(self):
        self.cube = {
            'F': [[GREEN]*3 for _ in range(3)],
            'B': [[BLUE]*3 for _ in range(3)],
            'U': [[WHITE]*3 for _ in range(3)],
            'D': [[YELLOW]*3 for _ in range(3)],
            'L': [[ORANGE]*3 for _ in range(3)],
            'R': [[RED]*3 for _ in range(3)]
        }

    def rotate_front(self, clockwise=True):
        face = self.cube['F']
        self.cube['F'] = rotate_face_clockwise(face) if clockwise else rotate_face_counter_clockwise(face)
        
        u_row = [self.cube['U'][2][i] for i in range(3)]
        l_col = [self.cube['L'][i][2] for i in range(3)]
        d_row = [self.cube['D'][0][i] for i in range(3)]
        r_col = [self.cube['R'][i][0] for i in range(3)]

        if clockwise:
            # Atualiza as faces adjacentes
            for i in range(3):
                self.cube['U'][2][i] = l_col[2 - i]
                self.cube['L'][i][2] = d_row[i]
                self.cube['D'][0][i] = r_col[2 - i]
                self.cube['R'][i][0] = u_row[i]
        else:
            for i in range(3):
                self.cube['U'][2][i] = r_col[i]
                self.cube['R'][i][0] = d_row[2 - i]
                self.cube['D'][0][i] = l_col[i]
                self.cube['L'][i][2] = u_row[2 - i]

    def draw(self, surface):
        self.draw_face(surface, 'F', (200, 200))
        self.draw_face(surface, 'U', (200, 200 - CUBE_SIZE*3 - OFFSET))
        self.draw_face(surface, 'R', (200 + CUBE_SIZE*3 + OFFSET, 200))

    def draw_face(self, surface, face, pos):
        x, y = pos
        for i in range(3):
            for j in range(3):
                if face == 'F':
                    rect = (x + j*CUBE_SIZE, y + i*CUBE_SIZE, CUBE_SIZE, CUBE_SIZE)
                    pygame.draw.rect(surface, self.cube[face][i][j], rect)
                elif face == 'U':
                    points = [
                        (x + j*CUBE_SIZE - i*OFFSET, y + i*CUBE_SIZE),
                        (x + (j+1)*CUBE_SIZE - i*OFFSET, y + i*CUBE_SIZE),
                        (x + (j+1)*CUBE_SIZE - (i+1)*OFFSET, y + (i+1)*CUBE_SIZE),
                        (x + j*CUBE_SIZE - (i+1)*OFFSET, y + (i+1)*CUBE_SIZE)
                    ]
                    pygame.draw.polygon(surface, self.cube[face][i][j], points)
                elif face == 'R':
                    points = [
                        (x + j*OFFSET, y + i*CUBE_SIZE + j*OFFSET),
                        (x + j*OFFSET + CUBE_SIZE, y + i*CUBE_SIZE + j*OFFSET),
                        (x + (j-1)*OFFSET + CUBE_SIZE, y + (i+1)*CUBE_SIZE + (j-1)*OFFSET),
                        (x + (j-1)*OFFSET, y + (i+1)*CUBE_SIZE + (j-1)*OFFSET)
                    ]
                    pygame.draw.polygon(surface, self.cube[face][i][j], points)
                
                # Contorno
                pygame.draw.polygon(surface, BLACK, points if face != 'F' else rect, 2)

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Cubo Mágico - Use F (horário) e V (anti-horário)")
    clock = pygame.time.Clock()
    cube = RubiksCube()
    running = True

    while running:
        screen.fill((50, 50, 50))
        
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == KEYDOWN:
                if event.key == K_f:
                    cube.rotate_front(clockwise=True)
                elif event.key == K_v:
                    cube.rotate_front(clockwise=False)
                elif event.key == K_r:
                    cube.reset_cube()

        cube.draw(screen)
        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()