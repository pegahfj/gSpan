"""The main program that runs gSpan."""
# -*- coding=utf-8 -*-
from __future__ import absolute_import, division, print_function

import os
import sys

from gSpanAlgorithm.gSpan.gspan_mining.config import parser
from gSpanAlgorithm.gSpan.gspan_mining.gspan import gSpan


def main(FLAGS=None):
    """Run gSpan."""

    if FLAGS is None:
        FLAGS, _ = parser.parse_known_args(args=sys.argv[1:])


    # Check if the database_file_name path is provided, otherwise exit program
    if not os.path.exists(FLAGS.database_file_name):
        print('{} does not exist.'.format(FLAGS.database_file_name))
        sys.exit()

    patient_txt_file_path = FLAGS.database_file_name 
    print(f"FLAGS Output Path: {patient_txt_file_path}")

    print("Initializing gSpan instance...")
    gs = gSpan(
        database_file_name=FLAGS.database_file_name,
        min_support=FLAGS.min_support,
        min_num_vertices=FLAGS.lower_bound_of_num_vertices,
        max_num_vertices=FLAGS.upper_bound_of_num_vertices,
        max_ngraphs=FLAGS.num_graphs,
        is_undirected=(not FLAGS.directed),
        verbose=FLAGS.verbose,
        visualize=FLAGS.plot,
        where=FLAGS.where
    )

    print("Running gSpan...")
    gs.run()
    gs.time_stats()
    gs.save_results(patient_txt_file_path)  # Pass patient input file


    return gs

if __name__ == '__main__':
    main()
