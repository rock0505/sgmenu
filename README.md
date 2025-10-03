# sgmenu
Convert string definitions into a PySimpleGUI menu structure by analyzing leading indentation.
Convert a string definition into a PySimpleGUI menu structure by analyzing the indentation at the beginning of lines.Format:- Each line represents a menu item.- Use space indentation (recommend 4 spaces per level) to indicate hierarchy.- Any '#' at the beginning or end of a line and the content following it are considered comments and ignored.- 
Example:
'''
File
    New
        New Project
        New File
    Open
        Open Project
        Open File
    Save
    Save As
Edit
    Undo
    Cut
    Copy
    Paste
    Find
        Find...
        Replace...
Help
    Contents
    About
Exit
    Exit & Save
    Exit
'''
Returns:
[['File',
  ['New',
   ['New Project', 'New File'],
   'Open',
   ['Open Project', 'Open File'],
   'Save',
   'Save As']],
 ['Edit', ['Undo', 'Cut', 'Copy', 'Paste', 'Find', ['Find...', 'Replace...']]],
 ['Help', ['Contents', 'About']],
 ['Exit', ['Exit & Save', 'Exit']]]
 
Parameters:text (str): A menu definition string that uses indentation to indicate hierarchy.
Returns:
    list: A PySimpleGUI-compatible menu data structure.
