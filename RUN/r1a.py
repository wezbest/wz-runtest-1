#!/usr/bin/env python
# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "rich",
# ]
# ///

from rich.console import Console
from rich.panel import Panel

console = Console()


def main() -> None:
    print("Hello from r1.py!")
    panel()


def panel() -> None:
    panel = Panel(
        """
Enjoy StinlySmellySWeaty women
""",
        title="Mistress",
        subtitle="ToiletSlave",
        style="Italic",
        border_style="magenta",
    )
    # Print the Panel
    console.print(panel)


if __name__ == "__main__":
    main()
