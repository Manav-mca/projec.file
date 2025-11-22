import pyfiglet, pyttsx3, random , time 
from rich.console import Console
from rich.text import Text

console = Console()
halloween_fonts = ['slant', 'big', 'ghost', 'doom', 'standerd' ]

font = random.choice(halloween_fonts)
art = pyfiglet.figlet_format("Happy Halloween!", font=font)
console.print(art, style="bold orange_red1")

pumpkin_art = """

       .-''''-.
     .'        '.
    /            \\
   |              |
   |,  .-.  .-.  ,|
   | )(_o/  \o_)( |
   |/     /\     \|
   (_     ^^     _)
    \__|IIIIII|__/
     | \IIIIII/ |
     \          /
      `--------`
      """

console.print(Text(pumpkin_art, style="bold orange1"))
engine = pyttsx3.init()
engine.say("Happy Halloween! Wishing you a spooky and fun-filled day!")
engine.runAndWait()
