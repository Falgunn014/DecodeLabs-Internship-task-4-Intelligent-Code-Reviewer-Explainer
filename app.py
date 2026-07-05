from reviewer import review_code
from rich.console import Console
from rich.markdown import Markdown
import os
from datetime import datetime

console = Console()

console.rule("[bold cyan]Intelligent Code Reviewer & Explainer[/bold cyan]")

file_path = input("Enter source code file path: ").strip()

if not os.path.exists(file_path):
    console.print("[bold red]Error:[/bold red] File not found!")
    exit()

try:
    with open(file_path, "r", encoding="utf-8") as file:
        source_code = file.read()

    console.print("\n[bold yellow]Reviewing code... Please wait.[/bold yellow]\n")

    result = review_code(source_code)

    console.print(Markdown(result))

    # Save report
    os.makedirs("reports", exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    report_path = f"reports/review_{timestamp}.md"

    with open(report_path, "w", encoding="utf-8") as report:
        report.write(result)

    console.print(f"\n[bold green]✔ Review saved successfully![/bold green]")
    console.print(f"[cyan]{report_path}[/cyan]")

except Exception as e:
    console.print(f"\n[bold red]Error:[/bold red] {e}")