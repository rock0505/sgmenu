# sgmenu.py
"""
    通过分析行首缩进将字符串定义转换为 PySimpleGUI 菜单结构。


    格式:
        - 每行代表一个菜单项。
        - 使用空格缩进（建议每级4个空格）表示层级。
        - 行首或行尾的 '#' 及其后内容被视为注释并被忽略。
        - 示例:
            File
                New
                Open
                Exit
            Edit
                Undo

    参数:
        text (str): 使用缩进表示层级的菜单定义字符串。

    返回:
        list: PySimpleGUI 兼容的菜单数据结构。
"""
def sgmenu(text):
    lines = [line for line in text.strip().splitlines() if line.strip()]
    items = [(len(line) - len(line.lstrip()), f"{line.lstrip()}") for line in lines]

    def parse_level(start, indent):
        nodes = []
        i = start
        n = len(items)
        while i < n:
            ind, label = items[i]
            if ind < indent:
                break
            if ind != indent:
                i += 1
                continue
            if i + 1 < n and items[i + 1][0] > ind:
                children, next_i = parse_level(i + 1, items[i + 1][0])
                nodes.append((label, children))
                i = next_i
            else:
                nodes.append(label)
                i += 1
        return nodes, i

    def nodes_to_flat(children_nodes):
        flat = []
        for c in children_nodes:
            if isinstance(c, tuple):
                clabel, cchildren = c
                flat.append(clabel)
                flat.append(nodes_to_flat(cchildren))
            else:
                flat.append(c)
        return flat

    def nodes_to_menu(nodes):
        menu = []
        for node in nodes:
            if isinstance(node, tuple):
                label, children_nodes = node
                menu.append([label, nodes_to_flat(children_nodes)])
            else:
                menu.append([node])
        return menu

    if not items:
        return []
    parsed_nodes, _ = parse_level(0, items[0][0])
    return nodes_to_menu(parsed_nodes)

##Menu Builder Demo
if __name__ == '__main__':
    import PySimpleGUI as sg
    menu_str = '''
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
    built_menu = sgmenu(menu_str)    
    import pprint
    pprint.pprint(built_menu)

    layout = [
        [sg.MenuBar(built_menu, key='-MENU-')],
        [sg.Text("Menu built from indent-based definition!")],
        [sg.Multiline(size=(60, 15), key='-MLINE-', write_only=True, autoscroll=True, echo_stdout_stderr=True)],
        [sg.Button("OK")]
    ]
    window = sg.Window("Menu Builder Demo", layout)
    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, "OK", "Exit"):
            break
        elif event != "__TIMEOUT__" and event != '-MLINE-':
            window['-MLINE-'].print(f"Menu Event Triggered: '{event}'")
    window.close()
