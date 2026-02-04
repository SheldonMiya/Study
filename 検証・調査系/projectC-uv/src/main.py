"""Sample main module for projectC-uv."""


def greet(name: str) -> str:
    """Greet someone by name.
    
    Args:
        name: The name of the person to greet.
        
    Returns:
        A greeting message.
    """
    return f"Hello, {name}! Welcome to projectC-uv."


def add(a: int, b: int) -> int:
    """Add two numbers.
    
    Args:
        a: First number.
        b: Second number.
        
    Returns:
        The sum of a and b.
    """
    return a + b


if __name__ == "__main__":
    print(greet("World"))
    print(f"1 + 2 = {add(1, 2)}")
