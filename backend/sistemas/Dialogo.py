import pygame
import os
import sys

pygame.init()
tela = pygame.display.set_mode((1, 1))


def mostrar_dialogo(dialogues, screen, pach_dialogo1, pach_dialogo2, typing_speed=50, font_path="p"):
    """
    Mostra uma sequência de diálogos em tela com digitação automática e botão 'Próximo'.

    dialogues: lista de strings
    screen: superfície Pygame
    typing_speed: velocidade da digitação (ms por letra)
    font_path: caminho para a fonte, se None usa fonte padrão
    """

    # Configurações de cores
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    BOX_COLOR = (30, 30, 30)
    BUTTON_COLOR = (70, 130, 180)
    BUTTON_HOVER = (100, 180, 250)
    PHOTO_BOX_COLOR = (80, 80, 80)

    pach_dialogo = pach_dialogo1

    # Fonte
    if font_path is None:
        font = pygame.font.SysFont(None, 24)
    else:
        endereço= os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
        font = pygame.font.Font(fr"{endereço}\frontend\recursos\fontes\Minha fonte.ttf", 16)

    # Caixas e posições
    box_x, box_y, box_w, box_h = 400, 650, 1120, 580
    text_x, text_y = box_x + 100, box_y + 190
    max_text_width = box_w - 520

    photo_box_x, photo_box_y, photo_box_w, photo_box_h = box_x + 10, box_y + 10, 80, 80

    button_w, button_h = 120, 30
    button_x = 970
    button_y = 980
    button_rect = pygame.Rect(button_x, button_y, button_w, button_h)

    # Controle de digitação
    dialogue_index = 0
    dialogue_text = dialogues[dialogue_index]
    displayed_text = ""
    char_index = 0
    last_update_time = pygame.time.get_ticks()

    clock = pygame.time.Clock()
    running = True

    def wrap_text(text, font, max_width):
        words = text.split(' ')
        lines = []
        current_line = ""
        for word in words:
            test_line = current_line + ("" if current_line == "" else " ") + word
            if font.size(test_line)[0] <= max_width:
                current_line = test_line
            else:
                if current_line:
                    lines.append(current_line)
                current_line = word
        if current_line:
            lines.append(current_line)
        return lines

    while running:

        screen.blit(pach_dialogo, (400, 650))

        # Atualiza digitação
        current_time = pygame.time.get_ticks()
        if char_index < len(dialogue_text) and current_time - last_update_time > typing_speed:
            displayed_text += dialogue_text[char_index]
            char_index += 1
            last_update_time = current_time

        # Desenha texto quebrado em linhas
        lines = wrap_text(displayed_text, font, max_text_width)
        for i, line in enumerate(lines):
            text_surface = font.render(line, True, WHITE)
            line_height = font.get_height()
            y = text_y + i * (line_height + 15)
            if y + line_height > box_y + box_h - 10:
                break
            screen.blit(text_surface, (text_x, y))

        # Botão próximo
        mouse_pos = pygame.mouse.get_pos()
        if button_rect.collidepoint(mouse_pos):
            pygame.draw.rect(screen, BUTTON_HOVER, button_rect)
        else:
            pygame.draw.rect(screen, BUTTON_COLOR, button_rect)
        pygame.draw.rect(screen, WHITE, button_rect, 2)
        button_text = font.render("Próximo", True, WHITE)
        text_rect = button_text.get_rect(center=button_rect.center)
        screen.blit(button_text, text_rect)

        # Eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    if char_index < len(dialogue_text):
                        # Completa texto instantaneamente
                        displayed_text = dialogue_text
                        char_index = len(dialogue_text)
                    else:
                        # Próximo diálogo ou sair
                        if dialogue_index < len(dialogues) - 1:
                            dialogue_index += 1
                            dialogue_text = dialogues[dialogue_index]
                            displayed_text = ""
                            char_index = 0
                            last_update_time = pygame.time.get_ticks()
                            if pach_dialogo == pach_dialogo1:
                                pach_dialogo = pach_dialogo2
                            else:
                                pach_dialogo = pach_dialogo1
                        else:
                            running = False

        pygame.display.update()
        clock.tick(60)  # Limita FPS a 60

endereço= os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

dialogo_agnes = pygame.image.load(fr"{endereço}\frontend\recursos\imagens\dialogos\dialogo_agnes.png").convert_alpha()
dialogo_agnes = pygame.transform.scale(dialogo_agnes, (1120, 580))

dialogo_fazendeiro = pygame.image.load(fr"{endereço}\frontend\recursos\imagens\dialogos\dialogo_fazendeiro.png").convert_alpha()
dialogo_fazendeiro = pygame.transform.scale(dialogo_fazendeiro, (1120, 580))

dialogo_slime = pygame.image.load(fr"{endereço}\frontend\recursos\imagens\dialogos\dialogo_slime.png").convert_alpha()
dialogo_slime = pygame.transform.scale(dialogo_slime, (1120, 580))