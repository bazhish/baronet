import pygame

# Classe base do item
class Item:
    def __init__(self, id, icon_surface):
        self.id = id
        self.icon = icon_surface
        self.quick_item_position = None

    def use_item(self, entity_owner):
        print(f"{entity_owner} usou o item '{self.id}'.")

# Classe de inventário
class Inventory:
    def __init__(self, entity_owner):
        self.show_inventory = False
        self.items = []
        self.max_items = 10
        self.entity_owner = entity_owner
        self.quick_panel_positions = [(10 + i * 50, 10) for i in range(5)]  # posições rápidas
        self.inventory_positions = [(10 + (i % 4) * 60, 80 + (i // 4) * 60) for i in range(self.max_items)]

    def update(self, screen):
        self.draw_quick_items(screen)
        if self.show_inventory:
            self.load_inventory(screen)

    def draw_quick_items(self, screen):
        for i, pos in enumerate(self.quick_panel_positions):
            pygame.draw.rect(screen, (100, 100, 100), (*pos, 40, 40))  # slot vazio
            item = self.get_item_by_position(i + 1)
            if item:
                screen.blit(item.icon, pos)

    def load_inventory(self, screen):
        for i, pos in enumerate(self.inventory_positions):
            pygame.draw.rect(screen, (200, 200, 200), (*pos, 50, 50))  # slot padrão
            if i < len(self.items):
                screen.blit(self.items[i].icon, pos)

        # Mostrar texto com ocupação
        font = pygame.font.SysFont(None, 24)
        text = font.render(f"Espaço: {len(self.items)}/{self.max_items}", True, (255, 255, 255))
        screen.blit(text, (10, 60))

    def handle_click(self, mouse_pos):
        # Itens rápidos
        for i, pos in enumerate(self.quick_panel_positions):
            rect = pygame.Rect(*pos, 40, 40)
            if rect.collidepoint(mouse_pos):
                item = self.get_item_by_position(i + 1)
                if item:
                    item.use_item(self.entity_owner)
                return

        # Inventário
        if self.show_inventory:
            for i, pos in enumerate(self.inventory_positions):
                rect = pygame.Rect(*pos, 50, 50)
                if rect.collidepoint(mouse_pos) and i < len(self.items):
                    self.items[i].use_item(self.entity_owner)
                    return

    def add_item(self, item):
        if len(self.items) < self.max_items:
            self.items.append(item)

    def remove_item(self, item):
        self.items = [i for i in self.items if i != item]

    def set_quick_item(self, item, position):
        item.quick_item_position = position

    def get_item_by_position(self, position):
        return next((item for item in self.items if item.quick_item_position == position), None)

    def get_item_by_id(self, item_id):
        return next((item for item in self.items if item.id == item_id), None)

# === Código principal ===
pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Inventário RPG")
clock = pygame.time.Clock()

# Criar um ícone fictício (amarelo)
icon_surface1 = pygame.Surface((40, 40))
icon_surface1.fill((255, 255, 0))  # Amarelo

icon_surface2 = pygame.Surface((40, 40))
icon_surface2.fill((0, 255, 0))  # Verde

# Criar inventário
inventory = Inventory(entity_owner="Jogador")

# Criar itens e adicionar
item1 = Item(id="pocao", icon_surface=icon_surface1)
item2 = Item(id="espada", icon_surface=icon_surface2)
inventory.add_item(item1)
inventory.add_item(item2)

# Definir item rápido
inventory.set_quick_item(item1, 1)

# Loop principal
running = True
while running:
    screen.fill((30, 30, 30))  # fundo escuro

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            inventory.handle_click(pygame.mouse.get_pos())

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_i:
                inventory.show_inventory = not inventory.show_inventory

    inventory.update(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
