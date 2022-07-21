import tkinter as tk
from tkinter import ttk
from tkinter import font
from tkinter.ttk import Button, Checkbutton, Combobox
from tkinter.ttk import Entry, Frame, Label
from tkinter.ttk import Labelframe, LabelFrame, Menubutton
from tkinter.ttk import Notebook, OptionMenu, PanedWindow
from tkinter.ttk import Panedwindow, Progressbar, Radiobutton
from tkinter.ttk import Scale, Scrollbar, Separator
from tkinter.ttk import Sizegrip, Spinbox, Treeview
from ttkbootstrap.constants import *

# date entry imports
from ttkbootstrap.popups import Querybox
from .scrolledtext import ScrolledText
from .scrolledframe import ScrolledFrame
from .floodgauge import Floodgauge
from .meter import Meter
from .tableview import Tableview
from .dateentry import DateEntry
from datetime import datetime

# floodgauge imports
import math

# meter imports
from PIL import Image, ImageTk, ImageDraw
from ttkbootstrap.style import Colors
from ttkbootstrap import utility
from ttkbootstrap.style import Bootstyle



TTK_WIDGETS = (
    ttk.Button,
    ttk.Checkbutton,
    ttk.Combobox,
    ttk.Entry,
    ttk.Frame,
    ttk.Labelframe,
    ttk.Label,
    ttk.Menubutton,
    ttk.Notebook,
    ttk.Panedwindow,
    ttk.Progressbar,
    ttk.Radiobutton,
    ttk.Scale,
    ttk.Scrollbar,
    ttk.Separator,
    ttk.Sizegrip,
    ttk.Spinbox,
    ttk.Treeview,
    ttk.OptionMenu,
)

TK_WIDGETS = (
    tk.Tk,
    tk.Toplevel,
    tk.Button,
    tk.Label,
    tk.Text,
    tk.Frame,
    tk.Checkbutton,
    tk.Radiobutton,
    tk.Entry,
    tk.Scale,
    tk.Listbox,
    tk.Menu,
    tk.Menubutton,
    tk.LabelFrame,
    tk.Canvas,
    tk.OptionMenu,
    tk.Spinbox,
)





