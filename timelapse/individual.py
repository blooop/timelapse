import bencher as bch
from timelapse import BenchTimelapse


if __name__ == "__main__":

    run_cfg = bch.BenchRunCfg()
    run_cfg.use_sample_cache = True
    run_cfg.only_hash_tag = True
    # run_cfg.overwrite_sample_cache = True
    run_cfg.run_tag = "8"
    # run_cfg.executor = bch.Executors.MULTIPROCESSING
    run_cfg.level = 6
    bench = BenchTimelapse().to_bench(run_cfg)
    consts = BenchTimelapse.get_input_defaults_override(preview=30, run=6, moviepy=False)
    consts["run"] = 7
    res = bench.plot_sweep(input_vars=[], const_vars=consts)
    # consts["run"] = 8
    # res = bench.plot_sweep(input_vars=[], const_vars=consts)

    bench.report.show()
