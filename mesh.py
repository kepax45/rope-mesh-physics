from node_verlet import *

rows = 30
cols = 30

mat = []
max_dist = 2
for i in range(rows):
    mat.append([])
    for j in range(cols):
        mat[i].append(Node(100+max_dist*i, 100+max_dist*j, 2, (255, 0, 0), max_dist, 1))
for i in range(rows):
    for j in range(cols):
        if j-1 >= 0:
            mat[i][j].connect(mat[i][j-1])
            mat[i][j-1].connect(mat[i][j])
        if j+1 < cols:
            mat[i][j].connect(mat[i][j+1])
            mat[i][j+1].connect(mat[i][j])
        if i-1 >= 0:
            mat[i][j].connect(mat[i-1][j])
            mat[i-1][j].connect(mat[i][j])
        if i+1 < rows:
            mat[i][j].connect(mat[i+1][j])
            mat[i+1][j].connect(mat[i][j])
mat[0][0].fixed = True
mat[rows-1][0].fixed = True
mat[0][cols-1].fixed = True
mat[rows-1][cols-1].fixed = True
    
window = pygame.display.set_mode((800, 600))
running = True
clicked_node = None
while running:
    window.fill((0, 0, 0))
    pygame.time.Clock().tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
        if event.type == pygame.MOUSEBUTTONDOWN:
            clicked_node = Node.get_clicked_node()
        if event.type == pygame.MOUSEBUTTONUP:
            clicked_node = None
    if clicked_node and pygame.key.get_pressed()[pygame.K_f]:
        clicked_node.fixed = not clicked_node.fixed
        print('yes')
    if clicked_node:
        clicked_node.x = pygame.mouse.get_pos()[0]
        clicked_node.y = pygame.mouse.get_pos()[1]
        clicked_node.old_x = clicked_node.x
        clicked_node.old_y = clicked_node.y
    Node.update_nodes()
    Node.constrain_nodes()
    Node.draw_nodes(window)
    pygame.display.flip()
pygame.quit()
