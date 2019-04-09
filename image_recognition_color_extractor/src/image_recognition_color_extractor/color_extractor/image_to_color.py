import numpy as np

from .back import Back
from .cluster import Cluster
from .name import Name
from .resize import Resize
from .selector import Selector
from .skin import Skin
from .task import Task


class ImageToColor(Task):
    def __init__(self, samples, labels, settings=None):

        if settings is None:
            settings = {}

        super(ImageToColor, self).__init__(settings)
        self._resize = Resize(self._settings['resize'])
        self._back = Back(self._settings['back'])
        self._skin = Skin(self._settings['skin'])
        self._cluster = Cluster(self._settings['cluster'])
        self._selector = Selector(self._settings['selector'])
        self._name = Name(samples, labels, self._settings['name'])

    def get(self, img):
        resized = self._resize.get(img)
        back_mask = self._back.get(resized)
        skin_mask = self._skin.get(resized)
        mask = back_mask | skin_mask
        k, labels, clusters_centers = self._cluster.get(resized[~mask])
        centers = self._selector.get(k, labels, clusters_centers)
        colors = [self._name.get(c) for c in centers]
        return ",".join(list({c for l in colors for c in l}))

    @staticmethod
    def _default_settings():
        return {
            'resize': {},
            'back': {},
            'skin': {},
            'cluster': {},
            'selector': {},
            'name': {},
        }
