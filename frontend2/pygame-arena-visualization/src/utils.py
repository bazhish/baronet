def load_image(file_path):
    """Load an image from the specified file path."""
    try:
        image = pygame.image.load(file_path)
        return image
    except pygame.error as e:
        print(f"Unable to load image at {file_path}: {e}")
        return None

def check_collision(rect1, rect2):
    """Check for collision between two rectangles."""
    return rect1.colliderect(rect2)

def clamp(value, min_value, max_value):
    """Clamp a value between a minimum and maximum."""
    return max(min_value, min(value, max_value))