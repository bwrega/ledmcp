import morse_talk
import time
from led import turn_on, turn_off

SPEED: float = 0.1

def send_message(text: str) -> None:
    code: str = _encode(text)
    for char in code:
        match char:
            case '.':
                turn_on()
                time.sleep(SPEED)
                turn_off()
                time.sleep(SPEED)
            case '-':
                turn_on()
                time.sleep(SPEED * 3)
                turn_off()
                time.sleep(SPEED)
            case ' ':
                time.sleep(SPEED * 1.5)

def _encode(text: str) -> str:
    encoded: str = morse_talk.encode(text, letter_sep=" ")
    return encoded.replace('?', '').replace("   ", "  ")
