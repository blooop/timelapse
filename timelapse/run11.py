import bencher as bch
from timelapse import BenchTimelapse

if __name__ == "__main__":
    run_cfg = bch.BenchRunCfg()
    run_cfg.use_sample_cache = True
    run_cfg.only_hash_tag = True
    run_cfg.run_tag = "run9-10-v1"
    run_cfg.level = 2
    bench = BenchTimelapse().to_bench(run_cfg)
    # consts = BenchTimelapse.get_input_defaults_override(preview=30, run=9, speedup=2, moviepy=True)
    consts = BenchTimelapse.get_input_defaults_override(run=11, speedup=2, moviepy=True)

    # res = bench.plot_sweep(input_vars=[bch.p("run",[9,10])], const_vars=consts)
    # res = bench.plot_sweep(input_vars=[bch.p("run",[11])], const_vars=consts)
    res = bench.plot_sweep(input_vars=[bch.p("run", [11])], const_vars=consts)

    bench.report.show()
