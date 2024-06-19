import os
from moviepy.editor import ImageSequenceClip, ImageClip
from pathlib import Path
import bencher as bch
from timeit import default_timer as timer
from timelapse import BenchTimelapse

if __name__ == "__main__":

    run_cfg = bch.BenchRunCfg()
    run_cfg.use_sample_cache = True
    run_cfg.only_hash_tag = True
    # run_cfg.overwrite_sample_cache
    run_cfg.run_tag = "8"
    # run_cfg.executor = bch.Executors.MULTIPROCESSING
    run_cfg.level = 5
    bench = BenchTimelapse().to_bench(run_cfg)

    # res = bench.plot_sweep(input_vars=["crf", "format"])

    # bench.define_const_inputs("")

    # bench.const_vars = bench.define_const_inputs(preview=30)

    consts = BenchTimelapse.get_input_defaults_override(preview=30, run=6, moviepy=False)
    # consts = BenchTimelapse.get_input_defaults_override(preview=-1)

    # res = bench.plot_sweep(input_vars=["run"], const_vars=consts)
    run_cfg.level = 5
    res = bench.plot_sweep(input_vars=["tmix"], const_vars=consts)
    res = bench.plot_sweep(input_vars=["speedup"], const_vars=consts)

    run_cfg.level = 3

    consts["run"] = 7

    res = bench.plot_sweep(
        # input_vars=[BenchTimelapse.param.tmix.with_sample_values([1, 2, 3, 4, 5, 6]), "speedup"],
        input_vars=[
            BenchTimelapse.param.tmix.with_sample_values([1, 2, 3, 4, 5, 6]),
            BenchTimelapse.param.speedup.with_sample_values([1, 2, 3, 4, 5, 6]),
        ],
        const_vars=consts,
    )

    # run_cfg.level = 5
    # res = bench.plot_sweep(input_vars=["tmedian"], const_vars=consts)
    # res = bench.plot_sweep(input_vars=["tblend"], const_vars=consts)

    # res = bench.plot_sweep(input_vars=[], const_vars=consts)

    # consts = BenchTimelapse.get_input_defaults_override(preview=30, run=5, moviepy=False, tmix=2)
    # res = bench.plot_sweep(input_vars=[], const_vars=consts)

    # res = bench.plot_sweep(input_vars=["format"])

    bench.report.show()
