import bencher as bch
from timelapse import BenchTimelapse

if __name__ == "__main__":

    run_cfg = bch.BenchRunCfg()
    run_cfg.use_sample_cache = True
    run_cfg.only_hash_tag = True
    # run_cfg.overwrite_sample_cache = True
    run_cfg.run_tag = "8"
    # run_cfg.executor = bch.Executors.MULTIPROCESSING
    run_cfg.level = 4
    bench = BenchTimelapse().to_bench(run_cfg)
    consts = BenchTimelapse.get_input_defaults_override(preview=30, run=7, speedup=2, moviepy=False)
    # res = bench.plot_sweep(input_vars=[], const_vars=consts)
    # res = bench.plot_sweep(input_vars=["speedup"], const_vars=consts)
    # res = bench.plot_sweep(input_vars=["tmix"], const_vars=consts)
    res = bench.plot_sweep(input_vars=["tmedian"], const_vars=consts)
    # res = bench.plot_sweep(input_vars=[ "tmix","speedup"], const_vars=consts)

    # res = bench.plot_sweep(
    #     input_vars=[
    #         BenchTimelapse.param.speedup.with_sample_values([1,2,3,4]),
    #     ],
    #     const_vars=consts,
    # )

    # res = bench.plot_sweep(
    #     input_vars=[
    #         BenchTimelapse.param.tmix.with_sample_values([1, 2, 3, 5, 10, 30]),
    #     ],
    #     const_vars=consts,
    # )

    # res = bench.plot_sweep(
    #     input_vars=[
    #         BenchTimelapse.param.speedup,
    #         BenchTimelapse.param.tmix.with_sample_values([1, 2,3]),
    #     ],
    #     const_vars=consts,
    # )

    # consts["run"] = 8
    consts["crf"] = 0

    res = bench.plot_sweep(input_vars=[], const_vars=consts)

    bench.report.show()
