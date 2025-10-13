def text_spacer(msg1, msg2, space):
    if space < 0:
        print("The space must be positive value.")
        return

    print(f"{"\t" * space}{msg1}\n{"\t" * space}{msg2}\n")

text_spacer("Message 1", "Message 2", 5)