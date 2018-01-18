#!/usr/bin/env python

from phase import Phase


def main():

    # Track 1
    #     {
    #     "end_align": false,
    #     "end_pad_duration": 0.0,
    #     "fade": "in-out",
    #     "gap": 0.25,
    #     "initial_gap": 0,
    #     "input_file": "/Users/jmarmor/repos/jonathanmarmor/phase/py/test_input_files/CPEFlute1.wav",
    #     "n_tracks": 24,
    #     "output_folder": "output/",
    #     "quietest": -40.0,
    #     "repeat_count": 40,
    #     "start_pad_duration": 0.0,
    #     "temp_folder": "tmp/"
    # }


    track1 = Phase(
        'input_files/CPEFlute1.wav',
        n_tracks=24,
        gap=0.25,
        # initial_gap=0.0,
        repeat_count=34,  # Previously 40
        end_align=False,
        start_pad_duration=0.0,
        end_pad_duration=0.0,
        fade='in-out',
        quietest=-39.0,  # These values (-39, -4.9) for quietest and gain are good for n_tracks=24, gap=0.25
        gain=-4.9,
        trim_start=False,
        trim_end=False,
        # solo_repetition_number=0,
        # solo_track_number=0,
        )




# {
#     "end_align": false,
#     "end_pad_duration": 0.75,
#     "fade": "in-out",
#     "gap": 0.16,
#     "initial_gap": 0,
#     "input_file": "/Users/jmarmor/repos/jonathanmarmor/phase/py/test_input_files/CPEFlute2.wav",
#     "n_tracks": 32,
#     "output_folder": "output/",
#     "quietest": -60.0,
#     "repeat_count": 40,
#     "start_pad_duration": 0.75,
#     "temp_folder": "tmp/"
# }

    # track2 = Phase(
    #     'input_files/CPEFlute2.wav',
    #     n_tracks=32,
    #     gap=0.16,
    #     # initial_gap=0.0,
    #     repeat_count=40,
    #     end_align=False,
    #     start_pad_duration=0.75,
    #     end_pad_duration=0.75,
    #     fade='in-out',
    #     quietest=-60.0,
    #     gain=-7.0,
    #     trim_start=False,
    #     trim_end=False)

    # track3 = Phase(
    #     ' .wav',
    #     n_tracks=,
    #     gap=,
    #     # initial_gap=0.0,
    #     repeat_count=,
    #     end_align=,
    #     start_pad_duration=,
    #     end_pad_duration=,
    #     fade=,
    #     quietest=,
    #     gain=,
    #     trim_start=,
    #     trim_end=)

    # track4 = Phase(
    #     ' .wav',
    #     n_tracks=,
    #     gap=,
    #     # initial_gap=0.0,
    #     repeat_count=,
    #     end_align=,
    #     start_pad_duration=,
    #     end_pad_duration=,
    #     fade=,
    #     quietest=,
    #     gain=,
    #     trim_start=,
    #     trim_end=)

    # track5 = Phase(
    #     ' .wav',
    #     n_tracks=,
    #     gap=,
    #     # initial_gap=0.0,
    #     repeat_count=,
    #     end_align=,
    #     start_pad_duration=,
    #     end_pad_duration=,
    #     fade=,
    #     quietest=,
    #     gain=,
    #     trim_start=,
    #     trim_end=)

    # track6 = Phase(
    #     ' .wav',
    #     n_tracks=,
    #     gap=,
    #     # initial_gap=0.0,
    #     repeat_count=,
    #     end_align=,
    #     start_pad_duration=,
    #     end_pad_duration=,
    #     fade=,
    #     quietest=,
    #     gain=,
    #     trim_start=,
    #     trim_end=)

    # track7 = Phase(
    #     ' .wav',
    #     n_tracks=17,
    #     gap=0.282312432,
    #     # initial_gap=0.0,
    #     repeat_count=14,
    #     end_align=True,
    #     start_pad_duration=1.112,
    #     end_pad_duration=0.8,
    #     fade='in-out',
    #     quietest=-30.0,
    #     gain=-8.0,
    #     trim_start=True,
    #     trim_end=True)

    # track8 = Phase(
    #     ' .wav',

    #     start_pad_duration=0.0,
    #     end_pad_duration=0.286,

    #     n_tracks=12,
    #     gap=0.018,
    #     repeat_count=21,
    #     end_align=True,

    #     fade='in-out',
    #     quietest=-16.0,
    #     gain=-8.0,

    #     trim_start=False,
    #     trim_end=False,
    #     # initial_gap=0.0,
    #     )



if __name__ == '__main__':
    main()