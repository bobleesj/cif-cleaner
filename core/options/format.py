from cifkit.preprocessors.error import move_files_based_on_errors
from cifkit.utils.folder import get_file_paths

from core.utils import intro, prompt


def format_files(cif_dir_path: str) -> None:
    intro.prompt_format_intro()

    # First, pre-process and move files without computing distances
    cif_file_paths = get_file_paths(cif_dir_path)
    move_files_based_on_errors(cif_dir_path, cif_file_paths)
    prompt.print_done_with_option("format files")
