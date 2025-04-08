import pygame
import math

pygame.init()

WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

radius = 5
cur_color = (0, 0, 255)  
shape = None
start_pos = None
end_pos = None
rectangles = []
circles = []
squares = []
right_triangles = []
equilateral_triangles = []
rhombuses = []
points = []

running = True
while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                cur_color = (255, 0, 0)
            elif event.key == pygame.K_g:
                cur_color = (0, 255, 0)  
            elif event.key == pygame.K_b:
                cur_color = (0, 0, 255)  
            elif event.key == pygame.K_v:
                shape = 'rectangle'
            elif event.key == pygame.K_c:
                shape = 'circle'
            elif event.key == pygame.K_s:
                shape = 'square'
            elif event.key == pygame.K_t:
                shape = 'right_triangle'
            elif event.key == pygame.K_e:
                shape = 'equilateral_triangle'
            elif event.key == pygame.K_r:
                shape = 'rhombus'
            elif event.key == pygame.K_1:
                shape = None
            elif event.key == pygame.K_q:
                rectangles.clear()
                circles.clear()
                squares.clear()
                right_triangles.clear()
                equilateral_triangles.clear()
                rhombuses.clear()
                points.clear()

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            start_pos = event.pos
            end_pos = event.pos
            if shape is None:
                points.append((event.pos, cur_color))

        if event.type == pygame.MOUSEMOTION and event.buttons[0]:
            end_pos = event.pos
            if shape is None:
                points.append((event.pos, cur_color))

        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            if shape == 'rectangle' and start_pos:
                rectangles.append((start_pos, end_pos, cur_color))
            elif shape == 'circle' and start_pos:
                r = int(math.dist(start_pos, end_pos))
                circles.append((start_pos, r, cur_color))
            elif shape == 'square' and start_pos:
                size = max(abs(end_pos[0] - start_pos[0]), abs(end_pos[1] - start_pos[1]))
                # Determine direction
                end_x = start_pos[0] + size if end_pos[0] > start_pos[0] else start_pos[0] - size
                end_y = start_pos[1] + size if end_pos[1] > start_pos[1] else start_pos[1] - size
                squares.append((start_pos, (end_x, end_y), cur_color))
            elif shape == 'right_triangle' and start_pos:
                right_triangles.append((start_pos, end_pos, cur_color))
            elif shape == 'equilateral_triangle' and start_pos:
                side_length = math.dist(start_pos, end_pos)
                equilateral_triangles.append((start_pos, end_pos, cur_color))
            elif shape == 'rhombus' and start_pos:
                rhombuses.append((start_pos, end_pos, cur_color))
            start_pos = None
            end_pos = None

    # Draw freehand points
    for i in range(1, len(points)):
        pos1, color1 = points[i - 1]
        pos2, color2 = points[i]
        pygame.draw.line(screen, color1, pos1, pos2, radius)

    # Draw rectangles
    for rect in rectangles:
        start, end, rect_color = rect
        pygame.draw.rect(screen, rect_color, pygame.Rect(
            min(start[0], end[0]),
            min(start[1], end[1]),
            abs(end[0] - start[0]),
            abs(end[1] - start[1])
        ), 2)

    # Draw circles
    for circ in circles:
        center, r, circ_color = circ
        pygame.draw.circle(screen, circ_color, center, r, 2)

    # Draw squares
    for sq in squares:
        start, end, sq_color = sq
        size = abs(end[0] - start[0])
        pygame.draw.rect(screen, sq_color, pygame.Rect(
            min(start[0], end[0]),
            min(start[1], end[1]),
            size, size
        ), 2)

    # Draw right triangles
    for tri in right_triangles:
        start, end, tri_color = tri
        points_list = [
            start,
            (start[0], end[1]),
            end
        ]
        pygame.draw.polygon(screen, tri_color, points_list, 2)

    # Draw equilateral triangles
    for tri in equilateral_triangles:
        start, end, tri_color = tri
        side_length = math.dist(start, end)
        height = (math.sqrt(3)/2) * side_length
        
        # Calculate the third point
        angle = math.atan2(end[1] - start[1], end[0] - start[0])
        point2 = end
        point3 = (
            start[0] + side_length * math.cos(angle + math.pi/3),
            start[1] + side_length * math.sin(angle + math.pi/3)
        )
        
        pygame.draw.polygon(screen, tri_color, [start, point2, point3], 2)

    # Draw rhombuses
    for rhomb in rhombuses:
        start, end, rhomb_color = rhomb
        mid_x = (start[0] + end[0]) / 2
        mid_y = (start[1] + end[1]) / 2
        dx = end[0] - start[0]
        dy = end[1] - start[1]
        
    
        other_dx = -dy * 0.7
        other_dy = dx * 0.7
        
        point1 = (mid_x - other_dx, mid_y - other_dy)
        point2 = end
        point3 = (mid_x + other_dx, mid_y + other_dy)
        point4 = start
        
        pygame.draw.polygon(screen, rhomb_color, [point1, point2, point3, point4], 2)

    # Draw preview of current shape
    if start_pos and end_pos:
        if shape == 'rectangle':
            pygame.draw.rect(screen, cur_color, pygame.Rect(
                min(start_pos[0], end_pos[0]),
                min(start_pos[1], end_pos[1]),
                abs(end_pos[0] - start_pos[0]),
                abs(end_pos[1] - start_pos[1])
            ), 2)
        elif shape == 'circle':
            r = int(math.dist(start_pos, end_pos))
            pygame.draw.circle(screen, cur_color, start_pos, r, 2)
        elif shape == 'square':
            size = max(abs(end_pos[0] - start_pos[0]), abs(end_pos[1] - start_pos[1]))
            end_x = start_pos[0] + size if end_pos[0] > start_pos[0] else start_pos[0] - size
            end_y = start_pos[1] + size if end_pos[1] > start_pos[1] else start_pos[1] - size
            pygame.draw.rect(screen, cur_color, pygame.Rect(
                min(start_pos[0], end_x),
                min(start_pos[1], end_y),
                abs(end_x - start_pos[0]),
                abs(end_y - start_pos[1])
            ), 2)
        elif shape == 'right_triangle':
            points_list = [
                start_pos,
                (start_pos[0], end_pos[1]),
                end_pos
            ]
            pygame.draw.polygon(screen, cur_color, points_list, 2)
        elif shape == 'equilateral_triangle':
            side_length = math.dist(start_pos, end_pos)
            angle = math.atan2(end_pos[1] - start_pos[1], end_pos[0] - start_pos[0])
            point2 = end_pos
            point3 = (
                start_pos[0] + side_length * math.cos(angle + math.pi/3),
                start_pos[1] + side_length * math.sin(angle + math.pi/3)
            )
            pygame.draw.polygon(screen, cur_color, [start_pos, point2, point3], 2)
        elif shape == 'rhombus':
            mid_x = (start_pos[0] + end_pos[0]) / 2
            mid_y = (start_pos[1] + end_pos[1]) / 2
            dx = end_pos[0] - start_pos[0]
            dy = end_pos[1] - start_pos[1]
            other_dx = -dy * 0.7
            other_dy = dx * 0.7
            point1 = (mid_x - other_dx, mid_y - other_dy)
            point2 = end_pos
            point3 = (mid_x + other_dx, mid_y + other_dy)
            point4 = start_pos
            pygame.draw.polygon(screen, cur_color, [point1, point2, point3, point4], 2)

    pygame.display.flip()
    clock.tick(120)

pygame.quit()