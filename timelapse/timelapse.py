import os
from moviepy.editor import ImageSequenceClip
import bencher as bch
from timeit import default_timer as timer


class BenchTimelapse(bch.ParametrizedSweep):

    speedup = bch.FloatSweep(default=1, bounds=(1, 10))
    fps = bch.IntSweep(default=60, bounds=(30, 60))
    crf = bch.IntSweep(default=23, bounds=[0, 40])
    run = bch.IntSweep(default=6, bounds=[1, 8])
    format = bch.StringSweep([".mp4", ".webm"])
    preview = bch.IntSweep(default=-1, bounds=[-1, 50])
    moviepy = bch.BoolSweep(default=True)
    tmix = bch.IntSweep(default=0, bounds=[0, 30])
    tblend = bch.IntSweep(default=0, bounds=(0, 5))
    tmedian = bch.IntSweep(default=0, bounds=(0, 9))

    timelapse = bch.ResultVideo()
    file_size = bch.ResultVar("MB")
    duration = bch.ResultVar("s")
    encoding_time = bch.ResultVar("s")

    def gen_tmix(self, num_frames):
        # weights = " ".join(["1"] * num_frames)
        # weights = f'"{weights}"'
        # cmd = f"tmix=frames={num_frames}:weights=\"1\",select='not(mod(n\,5))'"
        cmd = f'tmix=frames={num_frames}:weights="1"'
        return cmd

    def gen_tblend(self, num_tblends):
        cmd = "tblend=all_mode=average,framestep=2"
        multi = ",".join([cmd] * num_tblends)
        return f'"{multi}"'

    def __call__(self, **kwargs):
        self.update_params_from_kwargs(**kwargs)
        self.timelapse = bch.gen_video_path(extension=self.format)
        path = f"raw/run{self.run}"
        print(path)
        start = timer()
        if self.moviepy:
            print("loading images...")

            files = sorted(os.listdir(path))
            if self.preview > 0:
                preview_len = min(len(files), self.preview)
                files = files[:preview_len]
            selected_files = [os.path.join(path, f) for f in files]

            clip = ImageSequenceClip(selected_files, fps=self.fps)

            # modified = []
            # for p, r in zip(selected_files, files):
            #     img = bch.VideoWriter.label_image(p, r)
            #     new_path = Path(f"cachedir/img/{p}")
            #     new_path.mkdir(parents=True, exist_ok=True)
            #     print(new_path)
            #     img.save(new_path.as_posix())
            #     modified.append(new_path)

            # clip = ImageSequenceClip(modified, fps=self.fps)

            # for frm, fn in zip(clip.iter_frames(), selected_files):
            # label = bch.VideoWriter.create_label(fn)
            clip.write_videofile(self.timelapse, ffmpeg_params=["-crf", f"{self.crf}"])
            self.duration = clip.duration
        else:
            # vf = '"tblend=all_mode=average,framestep=2"'
            # tmix = f"tmix=frames=5:weights=\"1 1 1 1 1\",select='not(mod(n\,5))'"
            vf = "-vf "
            if self.tmix > 0:
                vf += f"{self.gen_tmix(self.tmix)}"
            if self.tblend > 0:
                vf += self.gen_tblend(self.tblend)
            if self.tmedian > 0:
                vf += f'"tmedian=radius={self.tmedian}"'

            speedup = ""
            if self.speedup > 1:
                speedup = f'-filter:v "setpts=PTS/{self.speedup},fps=60"'

            print(vf)
            if len(vf) == 4:
                vf = ""

            cmd = f"ffmpeg -framerate 60 -pattern_type glob -i '{path}/*.jpg' {vf} {speedup} -r 60 {self.timelapse}"
            print(f"running command: {cmd}")
            os.system(cmd)
        self.encoding_time = timer() - start
        self.file_size = os.stat(self.timelapse).st_size / (1024.0 * 1024.0)
        return super().__call__()
