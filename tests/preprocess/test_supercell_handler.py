from numpy import round as round
from cifcleaner.preprocess import cif_parser, supercell_handler
from cifcleaner.util.folder import get_cif_file_path_list_from_directory
from cifcleaner.util.unit import round_to_three_decimal
from cifcleaner.util.folder import (
    get_cif_file_count_from_directory,
    get_cif_file_path_list_from_directory,
)


def test_get_shortest_dist_list_and_skipped_indices():
    cif_dir = "tests/cifs/supercell_handler/check_correct_dist"
    filepath_list = get_cif_file_path_list_from_directory(cif_dir)
    assert (
        get_cif_file_count_from_directory(cif_dir) == 2
    ), "Wrong number of files in the folder"
    loop_tags = cif_parser.get_loop_tags()
    MAX_ATOMS_COUNT = 100000  # process files below 1m atoms in the supercell
    (
        shortest_dist_list,
        _,
    ) = supercell_handler.get_shortest_dist_list_and_skipped_indices(
        filepath_list, loop_tags, MAX_ATOMS_COUNT
    )
    assert round_to_three_decimal(shortest_dist_list[0]) == 2.697  # URhin.cif
    assert round_to_three_decimal(shortest_dist_list[1]) == 3.332  # ThSb.cif


def test_shortest_dist_greater_than_min_dist_threshold():
    cif_dir = "tests/cifs/supercell_handler/check_shortest_dist"
    filepath_list = get_cif_file_path_list_from_directory(cif_dir)
    assert (
        get_cif_file_count_from_directory(cif_dir) == 4
    ), "Wrong number of files in the folder"
    loop_tags = cif_parser.get_loop_tags()
    MAX_ATOMS_COUNT = 100000  # process files below 1m atoms in the supercell
    (
        shortest_dist_list,
        _,
    ) = supercell_handler.get_shortest_dist_list_and_skipped_indices(
        filepath_list, loop_tags, MAX_ATOMS_COUNT
    )
    assert shortest_dist_list[0] > 1.000
