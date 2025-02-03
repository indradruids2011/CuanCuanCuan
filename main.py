from rich.console import Console

from generate.script import GenerateScript

console = Console()


def main():
    console.print("Aplikasi Automatisasi Video YouTube Sederhana")

    script = GenerateScript()
    script.generate_script()


if __name__ == "__main__":
    main()
