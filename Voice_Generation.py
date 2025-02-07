# voiceover.py
import re
from gtts import gTTS
from Script_Generator import generate_script  # Import the generate_script function

# Extract lines labeled as narrator
def extract_narrator_lines(script):
    # Use regular expressions to extract lines labeled as Narrator
    narrator_lines =[]
    for line in script.split('\n'):
        if line.startswith('**Narrator:**'):
            # Remove '[Narrator]' part and strip the text
            narrator_lines.append(line.replace('**Narrator:**', '').strip())

    # Join the narrator lines into a single string
    return ' '.join(narrator_lines)

def generate_voiceover(input_script, file_prefix):
    output_file = (file_prefix + '.mp3')

    # Extract only the narration lines
    filtered_script = extract_narrator_lines(input_script)

    # Use British English (' en-uk' )
    tts = gTTS(text=filtered_script, lang='en', tld='co.uk')
    tts.save(output_file)
    print(f"Voiceover saved as {output_file}")

# Example usage
if __name__ == "__main__":
    # Ask for the topic (or you could have it predefined)
    script_topic = input("Enter a script topic for a YouTube short! (: ")

    # Generate the script from the other file
    script = generate_script(script_topic)
    pretty_script = script.message.content

    file_prefix = input('Tell me what to call the voiceover file: ')
    # Generate the voiceover
    generate_voiceover(pretty_script, file_prefix)
