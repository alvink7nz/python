import turtle

def draw_commands(commands):
    t = turtle.Turtle()
    pen_down = True  # Initialize pen state to down

    for command in commands:
        action = command[0]
        value = int(command[1:])
        
        if action == 'F':
            if pen_down:
                t.pendown()
            else:
                t.penup()
            t.forward(value)
        elif action == 'B':
            if pen_down:
                t.pendown()
            else:
                t.penup()
            t.backward(value)
        elif action == 'R':
            t.right(value)
        elif action == 'L':
            t.left(value)
        elif action == 'P':
            if value == 1:
                pen_down = True
            else:
                pen_down = False

def main():
    command_str = input("Enter drawing commands (e.g., REPEAT,4-F,100-P,0-R,90-ENDREPEAT): ")
    
    # Split commands into individual instructions
    commands = command_str.split('-')

    # Process each command
    for command in commands:
        if 'REPEAT' in command:
            repeat_count = int(command.split(',')[1])
            repeat_commands = command.split(',')[2:-1]
            for _ in range(repeat_count):
                draw_commands(repeat_commands)
        else:
            draw_commands([command])

    turtle.done()

if __name__ == "__main__":
    main()
