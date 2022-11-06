"""Helper functions to build visualizations using HTML/web frameworks."""
import random
import subprocess
from pathlib import Path

from filehash.filehash import FileHash
from IPython.display import Javascript, display, HTML


def install_if_necessary() -> None:
    """Install npm modules if they're missing."""
    react_dir = Path(__file__).parent.parent.parent / "react"
    node_modules = react_dir / "node_modules"
    if not node_modules.exists():
        print("Running npm install...")
        subprocess.run(
            ["yarn"], cwd=react_dir.absolute(),  capture_output=True,
            text=True,
            check=True)


def bundle_source() -> None:
    """Bundle up the JavaScript/TypeScript source

    Requires the source file to have a default export of a HTML element. This
    will then be converted into a web custom element.

    Supports common frameworks including Lit and React.

    Args:
        entry (Path): Source path, which must have a default export of a
        HTML element.

    Returns:
        Path: Path to the bundled JavaScript output
    """
    # Get the package.json path (the bundler script is setup here)
    react_dir = Path(__file__).parent.parent.parent / "react"

    # Bundle the source
    subprocess.run([
        "yarn",
        "build"
    ],
        cwd=react_dir.absolute(),
        # capture_output=True,
        # text=True,
        check=True  # Raise an exception if bundling fails
    )


def create_script() -> HTML:
    """Create a script that will create the custom element

    Returns:
        str: HTML that imports the script and creates the custom element
    """
    # Read the bundled JavaScript file
    bundled_js_path = Path(__file__).parent.parent.parent / \
        "react" / "dist" / "web-components.js"
    print("web")
    with open(bundled_js_path, encoding="utf8") as file:
        bundled_js = file.read()

    print("is_html")
    return HTML(f"<script module>{bundled_js}</script>")


def create_custom_element(custom_element_name: str, **kwargs: str) -> str:
    """Create the custom element

    Args:
        custom_element_name (str): Name for the custom element (must be globally
        unique for the user so keep long and descriptive).
        **kwargs (str): Parameters to be provided to the custom element.

    Returns:
        str: Custom element with parameters
    """
    # Format the custom element parameters
    params_list = [f"{name}='{value}'" for name, value in kwargs.items()]
    params = " ".join(params_list)

    # Return the custom element
    return f"<{custom_element_name} {params}/>"


def render(custom_element_name: str, **kwargs) -> HTML:
    """Render a visualization as a HTML custom element

    https://developer.mozilla.org/en-US/docs/Web/Web_Components/Using_custom_elements

    Returns:
        HTML: HTML Visualization
    """
    # Bundle the source code
    install_if_necessary()
    bundle_source()
    js = create_script()
    display(js)

    custom_element = create_custom_element(custom_element_name, **kwargs)
    return HTML(custom_element)
