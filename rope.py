from node_verlet import *

n_of_nodes = 10
prev = None
for i in range(n_of_nodes):
    n = Node(200, 200, 5, (255, 255, 255), 10, 2, 0.95)
    if(prev):
        prev.connect(n)
    prev = n
Node.nodes[0].fixed = True
    
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
