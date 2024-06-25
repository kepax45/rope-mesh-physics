import pygame
import math

class Node:
    nodes = []
    def draw_nodes(window):
        for node in Node.nodes:
            pygame.draw.circle(window, node.color, (node.x, node.y), node.r)
            for connection in node.connections:
                pygame.draw.line(window, (0, 255, 255), (connection.x, connection.y), (node.x, node.y))
    def update_nodes():
        for node in Node.nodes:
            node.update()
    def constrain_nodes():
        for node in Node.nodes:
            node.spring_constrain()
    def __init__(self, x, y, r, color, max_dist, gravity, damping, k=0.9):
        self.x = x
        self.y = y
        self.r = r
        self.old_x = x
        self.old_y = y
        self.k = k
        self.connections = []
        Node.nodes.append(self)
        self.color = color
        self.friction = damping
        self.gravity = gravity
        self.max_dist = max_dist
        self.fixed = False
    def connect(self, node):
        self.connections.append(node)
        node.connections.append(self)
    def spring_constrain(self):
        for node in self.connections:
            dx = self.x - node.x
            dy = self.y - node.y
            distance = math.sqrt(dx*dx + dy*dy)
            percentage = (self.max_dist - distance) / (distance+0.00001) / 2
            offsetX = percentage*dx
            offsetY = percentage*dy
            if not self.fixed:
                self.x += offsetX
                self.y += offsetY
            if not node.fixed:
                node.x -= offsetX
                node.y -= offsetY
    def update(self):
        if not self.fixed:
            vx = (self.x - self.old_x)*self.friction
            vy = (self.y - self.old_y)*self.friction
            self.old_y = self.y
            self.old_x = self.x
            self.x += vx
            self.y += vy
            self.y += self.gravity
    def get_clicked_node():
        for node in Node.nodes:
            if Node.distance((node.x, node.y), pygame.mouse.get_pos()) <= node.r:
                return node
        return None
    def distance(a, b):
        return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)
    def node_distance(a, b):
        return math.sqrt((a.x-b.x)**2 + (a.y-b.y)**2)

