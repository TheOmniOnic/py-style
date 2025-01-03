"""
Classes for Py-Style package.
This module defines _BaseObject, Theme, Console, ProgressBar and Table.
"""

from time import sleep
from os import get_terminal_size
from abc import ABC
from typing import Any
from .constants import *

# Set __all__
__all__ = ["Theme", "Console", "Table", "ProgressBar", "DEFAULT_THEME"]

class _BaseObject(ABC):
    """
    Abstract Base Class for all other classes defined here.
    Defines the help method.
    
    Args: None
    """
    
    @classmethod
    def help(cls) -> str:
        return f"""{FG_CYAN}{cls.__name__}{STOP}\n{cls.__doc__}"""

class Theme(_BaseObject):
    """
    Class for themes. 
    
    Args:
        info: str, 
        warning: str, 
        error: str, 
        **styles
    """
    
    def __init__(self, info: str = FG_CYAN, warning: str = FG_YELLOW, 
                 error: str = FG_RED, success: str = FG_GREEN, **styles) -> None:
        self.__info = info
        self.__warning = warning
        self.__error = error
        self.__success = success
        self.__styles = styles
        self.__construct()
        
    def get_style(self, target: str) -> str:
        return self.__styles[target]
        
    @property
    def info(self) -> str:
        return self.__info
    
    @property
    def warning(self) -> str:
        return self.__warning
    
    @property
    def error(self) -> str:
        return self.__error
    
    @property
    def success(self) -> str:
        return self.__success
    
    @property
    def styles(self, key: str) -> dict:
        return self.__styles[key] if key else self.__styles
    
    @info.setter
    def info(self, color: str) -> None:
        self.__info = color
        self.__construct()
        
    @warning.setter
    def warning(self, color: str) -> None:
        self.__warning = color
        self.__construct()
        
    @error.setter
    def error(self, color: str) -> None:
        self.__error = color
        self.__construct()
        
    @success.setter
    def success(self, color: str) -> None:
        self.__success = color
        
    @styles.setter
    def styles(self, **objects) -> None:
        self.__styles.update(objects)
        
    def __construct(self) -> None:
        """
        Set the info, warning, error and default keys.
        
        Args: None
        
        Returns: None
        """
        
        self.__styles["info"] = self.__info
        self.__styles["warning"] = self.__warning
        self.__styles["success"] = self.__success
        self.__styles["error"] = self.__error
        self.__styles["default"] = DEFAULT

DEFAULT_THEME = Theme(FG_CYAN, FG_YELLOW, FG_RED, FG_GREEN, bold=BOLD, dim=DIM, italic=ITALIC, underline=UNDERLINE, 
                      blink=BLINK, inverse=INVERSE, hidden=HIDDEN, strikethrough=STRIKETHROUGH, fg_black=FG_BLACK,
                      fg_white=FG_WHITE, fg_green=FG_GREEN, fg_yellow=FG_YELLOW, fg_blue=FG_BLUE, fg_magenta=FG_MAGENTA,
                      fg_cyan=FG_CYAN, bg_black=BG_BLACK, bg_red=BG_RED, bg_green=BG_GREEN,
                      bg_yellow=BG_YELLOW, bg_blue=BG_BLUE, bg_magenta=BG_MAGENTA, bg_cyan=BG_CYAN, bg_white=BG_WHITE)

class Console(_BaseObject):
    """
    Console object on which text can be printed and input can be taken.

    Args:
        title: str, 
        theme: Theme = DEFAULT_THEME
    """
    
    def __init__(self, title: str, theme: Theme = DEFAULT_THEME, print_title: bool = True) -> None:
        self.__title = title
        self.__theme = theme
        
        if print_title:
            self.print_title()
        
    def print_title(self) -> None:
        self.write(f"{BOLD}{UNDERLINE}{self.__title}{STOP}", alignment=CENTER)
        
    @property
    def theme(self) -> Theme:
        return self.__theme
    
    @theme.setter
    def theme(self, new: Theme = DEFAULT_THEME) -> None:
        self.__theme = new
        
    @property
    def title(self) -> str:
        return self.__title
    
    @title.setter
    def title(self, new: str) -> None:
        self.__title = new
    
    def clear(self, print_title: bool = True) -> None:
        """
        Clear the terminal.
        
        Args:
            print_title: bool = True
            
        Returns: None
        """
        
        print(CLEAR, end="")
        if print_title:
            self.print_title()
        
    def log(self, text: str, *, end: str = f"{STOP}\n", 
            sep: str = " ", style: str = "default", alignment: str = LEFT) -> None:
        """
        Customized log method.
        
        Args: 
            text: str, 
            end: str = f"{STOP}\\n", 
            sep: str = " ", 
            style: str = "default"
            
        Returns: None
        """
        
        print(self.__align_text(self.__theme.get_style(style) + text, alignment), end=end, sep=sep)
            
    def write(self, text: str, *, alignment: str = LEFT, end: str = f"{STOP}\n", 
              sep: str = " ", style: str = "default") -> None:
        """
        Customized print method.
        
        Args:
            text: str,
            alignment: str, 
            end: str = STOP, 
            sep: str = "", 
            style: str
        
        Returns: None
        """
        
        print(self.__align_text(self.__theme.get_style(style) + text, alignment), end=end, sep=sep)
        
    def prompt(self, text: str, *, end: str = STOP, style: str = "default") -> str:
        """
        Customized input method.
        
        Args:
            text: str, 
            alignment: str = LEFT, 
            end: str = STOP, 
            style: str
        
        Returns: str
        """
        
        return input(self.__theme.get_style(style) + text + end)
    
    @staticmethod
    def __align_text(text: str, alignment: str) -> str | None:
        """
        Private static method for text alignment
        
        Args:
            text: str, 
            alignment: str
        
        Returns: str 
        
        Raises: ValueError (if alignment is not valid)
        """
        width = get_terminal_size().columns
        
        if alignment == CENTER:
            padding = (width - len(text)) // 2
            return " " * padding + text + " " * (width - len(text) - padding)
        
        elif alignment == RIGHT:
            return (" " * (width - len(text)) + text).rstrip(" ")
        
        elif alignment == LEFT:
            return (text + " " * (width - len(text))).lstrip(" ")
        
        else:
            raise ValueError(f"Invalid argument for function 'Console.__align_text': {alignment}")
    
class ProgressBar(_BaseObject):
    """
    Class for representing basic progress bars.
    
    Args:
        values: int,
        theme: Theme = DEFAULT_THEME
        symbol: str = "-",
        delay: float = 1
    """
    
    def __init__(self, values: int, *, theme: Theme = DEFAULT_THEME, symbol: str = "-", 
                 delay: float = 1) -> None:
        self.__values = values
        self.__theme = theme
        self.__symbol = symbol
        self.__delay = delay
        
    @property
    def values(self) -> int:
        return self.__values
    
    @values.setter
    def values(self, new: int) -> None:
        self.__values = new
        
    @property
    def theme(self) -> Theme:
        return self.__theme
    
    @theme.setter
    def theme(self, new: Theme) -> None:
        self.__theme = new
        
    @property
    def symbol(self) -> str:
        return self.__symbol
    
    @symbol.setter
    def symbol(self, new: str) -> None:
        self.__symbol = new
        
    @property
    def delay(self) -> float:
        return self.__delay
    
    @delay.setter
    def delay(self, new: float) -> None:
        self.__delay = new
        
    def run(self, style: str = "default", del_self: bool = False) -> None:
        """
        Run the progress bar.
        
        Args:
            style: str = "default",
            del_self: bool = False
            
        Returns: None
        """
        
        for _ in range(self.__values):
            print(self.__theme.get_style(style) + self.__symbol, end=STOP, flush=True)
            sleep(self.__delay)
            
        if del_self:
            del self
            
class Table(_BaseObject):
    """
    Table class for representing data.
    
    Args: columns: int = 0
    """
    
    def __init__(self, columns: int = 0) -> None:
        self.__columns = columns
        self.__rows = 0
        self.__table = []
        
    def add_row(self, *objects: Any) -> None:
        """
        Add a row to self.__table.
        
        Args:
            *objects: Any
            
        Returns: None
        """
        
        objects = list(objects)
        
        while len(objects) < self.__columns:
            objects.append(None)
            
        while len(objects) > self.__columns:
            objects.pop()
            
        self.__table.append(objects)
        self.__rows += 1
        
    def del_row(self, index: int) -> None:
        """
        Delete a row in self.__table.
        
        Args:
            index: int
            
        Returns: None    
        """
        
        del self.__table[index]
        self.__rows -= 1
        
    def del_column(self, index: int) -> None:
        """
        Delete a column in self.__table.
        
        Args:
            index: int
            
        Returns: None
        """
        
        for row in self.__table:
            del row[index]
            
        self.__columns -= 1
        
    def add_column(self, placeholder: Any = "") -> None:
        """
        Add a column in self.__table.
        
        Args:
            placeholder: Any = ""
            
        Returns: None
        """
        
        for row in self.__table:
            row.append(placeholder)
        
        self.__columns += 1
            
    def get_column(self, row_index: int, column_index: int) -> Any:
        """
        Get the information in a column in self.__table.
        
        Args:
            row_index: int,
            column_index: int
            
        Returns: Any
        """
        
        return self.__table[row_index][column_index]
    
    def set_column(self, info: Any, row_index: int, column_index: int) -> None:
        """
        Set the information in a column in self.__table.
        
        Args:
            row_index: int,
            column_index: int
            
        Returns: None
        """
        
        self.__table[row_index][column_index] = info
        
    def get_row(self, index: int) -> list:
        """
        Returns a row in self.__table.
        
        Args:
            index: int
            
        Returns: list
        """
        
        return self.__table[index]
    
    def get_table(self) -> str:
        """
        Return a string representation of self.__table.
        
        Args: None
        
        Returns: str
        """
        
        return_str = ""
        
        for row in self.__table:
            return_str += "| " + " | ".join(str(cell) if cell is not None else "" for cell in row) + " |" + "\n"
            
        return return_str
        
    @property
    def rows(self) -> int:
        return self.__rows
    
    @property
    def columns(self) -> int:
        return self.__columns
    
    @property
    def table(self) -> list[list]:
        return self.__table
    