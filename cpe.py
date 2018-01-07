#!/usr/bin/env python

from phase import Phase


def main():
    # WARNING: These are not the real config values for movement 1
    Phase(
        'input_files/CPEFlute1.wav',
        n_tracks=7,
        gap=0.01,
        initial_gap=0.0,
        repeat_count=4,
        end_align=False,
        start_pad_duration=0.0,
        end_pad_duration=0.0,
        fade=None,
        quietest=-60.0,
        gain=0.0,
        trim_start=False,
        trim_end=False)

    # WARNING: These are not the real config values for movement 2
    Phase(
        'input_files/CPEFlute2.wav',
        n_tracks=7,
        gap=0.01,
        initial_gap=0.0,
        repeat_count=4,
        end_align=False,
        start_pad_duration=0.0,
        end_pad_duration=0.0,
        fade=None,
        quietest=-60.0,
        gain=0.0,
        trim_start=False,
        trim_end=False)


if __name__ == '__main__':
    main()