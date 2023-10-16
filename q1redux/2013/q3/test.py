def unlock_security_system(lighting):
    keypad = [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ]

    # Function to toggle the state of a button and its adjacent buttons
    def toggle_button(i, j):
        nonlocal keypad
        if keypad[i][j] == 2:
            keypad[i][j] = 0
        else:
            keypad[i][j] += 1

        if i > 0:
            if keypad[i - 1][j] == 2:
                keypad[i - 1][j] = 0
            else:
                keypad[i - 1][j] += 1
        if i < 4:
            if keypad[i + 1][j] == 2:
                keypad[i + 1][j] = 0
            else:
                keypad[i + 1][j] += 1
        if j > 0:
            if keypad[i][j - 1] == 2:
                keypad[i][j - 1] = 0
            else:
                keypad[i][j - 1] += 1
        if j < 4:
            if keypad[i][j + 1] == 2:
                keypad[i][j + 1] = 0
            else:
                keypad[i][j + 1] += 1

    # Press buttons according to the given lighting state
    for char in lighting:
        if ord(char) < 97:  # uppercase letter, press twice
            char = chr(ord(char) + 32)  # convert to lowercase
            toggle_button(ord(char) // 5, ord(char) % 5)
            toggle_button(ord(char) // 5, ord(char) % 5)
        else:  # lowercase letter, press once
            toggle_button(ord(char) // 5, ord(char) % 5)

    # Check if the system is unlocked
    is_unlocked = all(all(button == 0 for button in row) for row in keypad)

    if is_unlocked:
        # Generate the sequence of button presses to unlock the system
        sequence = ""
        for i in range(5):
            for j in range(5):
                if keypad[i][j] == 1:
                    sequence += chr(i * 5 + j + 97)
                elif keypad[i][j] == 2:
                    sequence += chr(i * 5 + j + 65)
        return sequence
    else:
        return "IMPOSSIBLE"


# Test the program
lighting_state = input("Enter the current lighting state: ")
result = unlock_security_system(lighting_state)
print("Button sequence:", result)