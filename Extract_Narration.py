import re

# Extract lines labeled as narrator
def extract_narrator_lines(script):
    # Use regular expressions to extract lines labeled as Narrator
    narrator_lines = []
    for line in script.split('\n'):
        if line.startswith('**Narrator:**'):
            # Remove 'Narrator:' part and strip the text
            narrator_lines.append(line.replace('**Narrator:**', '').strip())

    # Join the narrator lines into a single string
    return ' '.join(narrator_lines)


# Open the script file and read the content
file_name = "christian.txt"  # Replace with the name of your script file
with open(file_name, "r") as file:
    script_content = file.read()

# Extract the narrator lines from the script
narrator_script = extract_narrator_lines(script_content)

# Print the extracted narrator lines
print("Narrator's lines:", narrator_script)
