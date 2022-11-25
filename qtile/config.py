import os
import re
import subprocess
import socket
import time
from typing import List  # noqa: F401
from libqtile import layout, bar, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen, Rule, ScratchPad, DropDown
from libqtile.command import lazy
from libqtile.widget import Spacer
import asyncio

@hook.subscribe.client_new
async def move_spotify(client):
    await asyncio.sleep(0.01)
    if client.name == 'Spotify':
        client.togroup("4")

@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/scripts/autostart.sh'])

@hook.subscribe.startup
def start_always():
    # Set the cursor to something sane in X
    subprocess.Popen(['xsetroot', '-cursor_name', 'left_ptr'])
    subprocess.run(['setxkbmap','-option','caps:escape'])

@hook.subscribe.client_new
def set_floating(window):
    if (window.window.get_wm_transient_for()
            or window.window.get_wm_type() in floating_types):
        window.floating = True

mod = "mod4"
keys=[
    Key([mod], "f", lazy.window.toggle_fullscreen()),
    Key([mod], "q", lazy.window.kill()),

    Key([mod, "shift"], "q", lazy.window.kill()),
    Key([mod, "shift"], "r", lazy.restart()),

    Key([mod], "n", lazy.layout.normalize()),
    Key([mod], "space", lazy.next_layout()),

    Key([mod], "k", lazy.layout.up()),
    Key([mod], "j", lazy.layout.down()),
    Key([mod], "h", lazy.layout.left()),
    Key([mod], "l", lazy.layout.right()),

    Key([mod, "control"], "l",
        lazy.layout.grow_right(),
        lazy.layout.grow(),
        lazy.layout.increase_ratio(),
        lazy.layout.delete(),
        ),
    Key([mod, "control"], "h",
        lazy.layout.grow_left(),
        lazy.layout.shrink(),
        lazy.layout.decrease_ratio(),
        lazy.layout.add(),
        ),
    Key([mod, "control"], "k",
        lazy.layout.grow_up(),
        lazy.layout.grow(),
        lazy.layout.decrease_nmaster(),
        ),
    Key([mod, "control"], "j",
        lazy.layout.grow_down(),
        lazy.layout.shrink(),
        lazy.layout.increase_nmaster(),
        )
        ]

groups = [ScratchPad("0", [DropDown("Passwords", ['emacs' , '-f', 'pass', '-f', 'doom/window-maximize-buffer'], width=0.3),
                                 DropDown("Terminal", "alacritty", width=0.3),
                                 DropDown("Browser", "firefox --new-instance", width=0.3)]),
          Group(name="1", layout="monadtall", label="Main", matches=Match(wm_class=["Emacs"])),
          Group(name="2", layout="monadtall", label="Backup"),
          Group(name="3", layout="monadtall", label="Communication", matches=Match(wm_class=["Microsoft Teams - Preview", "discord"])),
          Group(name="4", layout="monadtall", label="Music"),
          Group(name="5", layout="monadtall", label="Video"),
          Group(name="6", layout="monadtall", label="Gaming", matches= Match(wm_class=["Minecraft Launcher"]))]

keys.extend([
    Key([mod], "1", lazy.group["1"].toscreen()),
    Key([mod], "2", lazy.group["2"].toscreen()),
    Key([mod], "3", lazy.group["3"].toscreen()),
    Key([mod], "4", lazy.group["4"].toscreen()),
    Key([mod], "5", lazy.group["5"].toscreen()),
    Key([mod], "6", lazy.group["6"].toscreen()),
    Key([mod], "Tab", lazy.screen.next_group()),
    Key([mod, "shift" ], "Tab", lazy.screen.prev_group()),
    Key([mod, "shift"], "1", lazy.window.togroup("1"), lazy.group["1"].toscreen()),
    Key([mod, "shift"], "2", lazy.window.togroup("2"), lazy.group["2"].toscreen()),
    Key([mod, "shift"], "3", lazy.window.togroup("3"), lazy.group["3"].toscreen()),
    Key([mod, "shift"], "4", lazy.window.togroup("4"), lazy.group["4"].toscreen()),
    Key([mod, "shift"], "5", lazy.window.togroup("5"), lazy.group["5"].toscreen()),
    Key([mod, "shift"], "6", lazy.window.togroup("6"), lazy.group["6"].toscreen()),
    Key([mod], "p", lazy.group["0"].dropdown_toggle('Passwords')),
    Key([mod], "t", lazy.group["0"].dropdown_toggle('Terminal')),
    Key([mod, 'shift'], 'b', lazy.group['0'].dropdown_toggle('Browser'))
])

def init_colors():
    return [["#2F343F", "#2F343F"], # color 0
            ["#2F343F", "#2F343F"], # color 1
            ["#c0c5ce", "#c0c5ce"], # color 2
            ["#fba922", "#fba922"], # color 3
            ["#3384d0", "#3384d0"], # color 4
            ["#f3f4f5", "#f3f4f5"], # color 5
            ["#cd1f3f", "#cd1f3f"], # color 6
            ["#62FF00", "#62FF00"], # color 7
            ["#6790eb", "#6790eb"], # color 8
            ["#a9a9a9", "#a9a9a9"]] # color 9
colors = init_colors()

def init_widgets_defaults():
    return dict(font="Noto Sans",
                fontsize = 12,
                padding = 2,
                background=colors[1])

widget_defaults = init_widgets_defaults()

def init_widgets_list():
    prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())
    widgets_list = [
               widget.GroupBox(font="FontAwesome",
                        fontsize = 16,
                        margin_y = -1,
                        margin_x = 0,
                        padding_y = 6,
                        padding_x = 5,
                        borderwidth = 0,
                        disable_drag = True,
                        active = colors[9],
                        inactive = colors[5],
                        rounded = False,
                        highlight_method = "text",
                        this_current_screen_border = colors[8],
                        foreground = colors[2],
                        background = colors[1]
                        ),
               widget.Sep(
                        linewidth = 1,
                        padding = 10,
                        foreground = colors[2],
                        background = colors[1]
                        ),
               widget.CurrentLayout(
                        font = "Noto Sans Bold",
                        foreground = colors[5],
                        background = colors[1]
                        ),
               widget.Sep(
                        linewidth = 1,
                        padding = 10,
                        foreground = colors[2],
                        background = colors[1]
                        ),
               widget.WindowName(font="Noto Sans",
                        fontsize = 12,
                        foreground = colors[5],
                        background = colors[1],
                        ),
               widget.TextBox(
                        font="FontAwesome",
                        text="  ",
                        foreground=colors[3],
                        background=colors[1],
                        padding = 0,
                        fontsize=16
                        ),
               widget.Clock(
                        foreground = colors[5],
                        background = colors[1],
                        fontsize = 12,
                        format="%Y-%m-%d %H:%M"
                        ),
               widget.Systray(
                        background=colors[1],
                        icon_size=20,
                        padding = 4
                        ),
              ]
    return widgets_list

widgets_list = init_widgets_list()

def init_widgets_screen1():
    widgets_screen1 = init_widgets_list()
    return widgets_screen1

widgets_screen1 = init_widgets_screen1()

def init_screens():
    return [Screen(top=bar.Bar(widgets=init_widgets_screen1(), size=26, opacity=0.8))]

screens = init_screens()

mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size())
]

dgroups_key_binder = None
dgroups_app_rules = []

floating_types = ["notification", "toolbar", "splash", "dialog"]
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
    Match(wm_class='Arcolinux-welcome-app.py'),
    Match(wm_class='Arcolinux-calamares-tool.py'),
    Match(wm_class='confirm'),
    Match(wm_class='dialog'),
    Match(wm_class='download'),
    Match(wm_class='error'),
    Match(wm_class='file_progress'),
    Match(wm_class='notification'),
    Match(wm_class='splash'),
    Match(wm_class='toolbar'),
    Match(wm_class='Arandr'),
    Match(wm_class='feh'),
    Match(wm_class='Galculator'),
    Match(wm_class='archlinux-logout'),
    Match(wm_class='xfce4-terminal'),

],  fullscreen_border_width = 0, border_width = 0)






auto_fullscreen = True

focus_on_window_activation = "focus" # or smart

wmname = "LG3D"
