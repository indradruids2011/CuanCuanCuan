from rich.console import Console

from generate.script import GenerateScript

console = Console()


def main():
    console.print("Aplikasi Generate Video Sederhana")
    niche = input("Masukkan niche video yang ingin dibuat: ")

    script = GenerateScript()
    script.generate_script(niche=niche)


if __name__ == "__main__":
    main()
