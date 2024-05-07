import moviepy
from moviepy.editor import ImageSequenceClip
from pathlib import Path
import bencher as bch


class BenchTimelapse(bch.ParametrizedSweep):

    speedup = bch.FloatSweep(default=100, bounds=(50, 400))
    fps = bch.IntSweep(default=60, bounds=(30, 60))

    timelapse = bch.ResultVideo()

    def __call__(self, **kwargs):
        self.update_params_from_kwargs(**kwargs)
        clip = ImageSequenceClip("raw/run3", fps=60)
        self.timelapse = bch.gen_video_path(extension=".mp4")
        clip.write_videofile(self.timelapse)
        return super().__call__()


if __name__ == "__main__":

    run_cfg = bch.BenchRunCfg()
    run_cfg.use_sample_cache = True
    run_cfg.only_hash_tag = True
    run_cfg.level = 2
    bench = BenchTimelapse().to_bench(run_cfg)
    bench.plot_sweep(input_vars=["fps"])
    bench.report.show()
