from timelapse import BenchTimelapse


def test_init():
    b = BenchTimelapse().to_bench()
    assert b is not None
