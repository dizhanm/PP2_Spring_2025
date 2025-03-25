import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    
    radius = 15
    mode = 'blue'
    points = []
    drawing_shape = None  # 'rectangle' or 'circle'
    shape_start = None  # Начальная точка фигуры
    eraser_mode = False
    
    while True:
        pressed = pygame.key.get_pressed()
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return
                if event.key == pygame.K_r:
                    mode = 'red'
                elif event.key == pygame.K_g:
                    mode = 'green'
                elif event.key == pygame.K_b:
                    mode = 'blue'
                elif event.key == pygame.K_c:
                    drawing_shape = 'circle'
                elif event.key == pygame.K_v:
                    drawing_shape = 'rectangle'
                elif event.key == pygame.K_e:
                    eraser_mode = not eraser_mode  # Переключение ластика
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Левая кнопка
                    if drawing_shape:
                        shape_start = event.pos
                    else:
                        radius = min(200, radius + 1)
                elif event.button == 3:  # Правая кнопка уменьшает радиус
                    if not drawing_shape:
                        radius = max(1, radius - 1)
                
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1 and drawing_shape and shape_start:
                    shape_end = event.pos
                    if drawing_shape == 'rectangle':
                        pygame.draw.rect(screen, get_color(mode), pygame.Rect(shape_start, (shape_end[0] - shape_start[0], shape_end[1] - shape_start[1])))
                    elif drawing_shape == 'circle':
                        center = shape_start
                        radius = int(((shape_end[0] - shape_start[0])**2 + (shape_end[1] - shape_start[1])**2)**0.5)
                        pygame.draw.circle(screen, get_color(mode), center, radius)
                    drawing_shape = None
                    shape_start = None
                
            if event.type == pygame.MOUSEMOTION:
                if eraser_mode:
                    pygame.draw.circle(screen, (0, 0, 0), event.pos, radius)
                elif not drawing_shape:
                    points.append(event.pos)
                    points = points[-256:]
                    
        screen.fill((0, 0, 0))
        
        for i in range(len(points) - 1):
            drawLineBetween(screen, i, points[i], points[i + 1], radius, mode)
        
        pygame.display.flip()
        clock.tick(60)

def drawLineBetween(screen, index, start, end, width, color_mode):
    c1 = max(0, min(255, 2 * index - 256))
    c2 = max(0, min(255, 2 * index))
    
    if color_mode == 'blue':
        color = (c1, c1, c2)
    elif color_mode == 'red':
        color = (c2, c1, c1)
    elif color_mode == 'green':
        color = (c1, c2, c1)
    
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))
    
    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(screen, color, (x, y), width)

def get_color(mode):
    if mode == 'blue':
        return (0, 0, 255)
    elif mode == 'red':
        return (255, 0, 0)
    elif mode == 'green':
        return (0, 255, 0)
    return (255, 255, 255)

main()
