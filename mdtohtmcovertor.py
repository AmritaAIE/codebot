import os
import markdown

filename = "team_01"
md_file_loc = f'mdfileshere/{filename}.md'
html_file_loc = f'htmlfileshere/{filename}.html'

print(md_file_loc)

with open(md_file_loc, 'r') as f:
    text = f.read()
    html = markdown.markdown(text)

if not os.path.exists(html_file_loc):
    with open(html_file_loc, 'w') as f:
        f.write(html)