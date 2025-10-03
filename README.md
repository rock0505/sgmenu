# sgmenu
通过分析行首缩进将字符串定义转换为 PySimpleGUI 菜单结构。
格式:
- 每行代表一个菜单项。
- 使用空格缩进（建议每级4个空格）表示层级。
- 行首或行尾的 '#' 及其后内容被视为注释并被忽略。
- 示例:
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
返回:
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

参数:
text (str): 使用缩进表示层级的菜单定义字符串。

返回:
list: PySimpleGUI 兼容的菜单数据结构。

Convert a string definition into a PySimpleGUI menu structure by analyzing the indentation at the beginning of lines.
Format:
- Each line represents a menu item.
- Use space indentation (recommend 4 spaces per level) to indicate hierarchy.
- Any '#' at the beginning or end of a line and the content following it are considered comments and ignored.- 
-Example:
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
Returns: list: A PySimpleGUI-compatible menu data structure.
