import PIL
import io
import os
import __main__
from shutil import rmtree

import matplotlib.pyplot as plt
import imageio.v3 as iio
import numpy as np

from .figures import Figures
from .. import defaults
from ..utils.groups import get_group_indexes_fill

class Animate(Figures):
    
    def __init__(self, data_objects, **kwargs):
        Figures.__init__(self, data_objects, **kwargs)
        defaults.kwargs(self, kwargs)
    
    def create_animations(self, **kwargs):
        self.process_data_objects()
        self.set_figure_objects(**kwargs)
        self.prepare_animation_settings()
        self.create_partial_animations_folder()
        self.animate_data_objects()

    def prepare_animation_settings(self):
        self.output = None
        self.set_animation_axis_limits()
        self.set_figure_animation_settings()

    def set_animation_axis_limits(self):
        for figure_obj in self.figure_objects:
            figure_obj.set_animation_axis_limits()

    def set_figure_animation_settings(self):
        for figure_obj in self.figure_objects:
            figure_obj.maximise = self.maximise
            figure_obj.figure_size = self.figure_size

    def create_partial_animations_folder(self):
        self.plots_folder = True
        self.set_path(plots_folder_name="TemporaryAnimationConstructor")

    def animate_data_objects(self):
        for figure_obj in self.figure_objects:
            self.animate_figure(figure_obj)

    def animate_figure(self, figure_obj):
        self.frame_count = figure_obj.get_frame_count()
        self.set_all_data_values(figure_obj)
        self.create_partial_animations(figure_obj)
        self.merge_animations()

    def set_all_data_values(self, figure_obj):
        figure_obj.all_data_values = [data_obj.get_data_values()
                                      for data_obj in figure_obj.data_objects]

    def create_partial_animations(self, figure_obj):
        all_frame_indexes = get_group_indexes_fill(self.frame_count, self.max_figures_open)
        for index, frame_indexes in enumerate(all_frame_indexes):
            self.create_partial_animation(figure_obj, index, frame_indexes)
            plt.close("all")

    def create_partial_animation(self, figure_obj, index, frame_indexes):
        frames = self.get_frames(figure_obj, frame_indexes)
        name = f"{self.animation_name}_partial_{index}.{self.format}"
        self.save_animation(frames, name=name)

    def get_frames(self, figure_obj, frame_indexes):
        frames = [self.get_frame(figure_obj, index)
                  for index in frame_indexes]
        return frames

    def get_frame(self, figure_obj, index):
        buffer = self.get_buffer(figure_obj, index)
        image = self.get_image(buffer, figure_obj)
        return image

    def get_buffer(self, figure_obj, index):
        figure_obj.set_data_value(index)
        figure_obj.create_figure()
        buffer = io.BytesIO()
        return buffer

    def get_image(self, buffer, figure_obj):
        plt.savefig(buffer, dpi=figure_obj.fig.dpi)
        buffer.seek(0)
        image = PIL.Image.open(buffer)
        image = image.resize(figure_obj.figure_size_pixels)
        return image

    def save_animation(self, frames, name=None):
        path = self.get_animation_path(name)
        frames[0].save(path, loop=self.loop, save_all=True,
                       append_images=frames[1:], duration=self.duration)

    def get_animation_path(self, name=None):
        if name is None:
            name = f"{self.animation_name}.{self.format}"
        path = os.path.join(self.path, name)
        return path

    def merge_animations(self):
        paths = [os.path.join(self.path, name) for name in os.listdir(self.path)]
        frames = np.vstack([iio.imread(path) for path in paths])
        rmtree(self.path, ignore_errors=True)
        self.path = os.path.split(self.path)[0]
        iio.imwrite(self.get_animation_path(), frames, duration=self.duration, loop=0)

defaults.load(Animate)
