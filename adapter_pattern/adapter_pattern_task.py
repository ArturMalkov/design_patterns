from abc import ABC, abstractmethod


class System:
    def __init__(self):
        self.map = self.grid = [[0 for i in range(30)] for _ in range(20)]
        self.map[5][7] = 1  # Источники света
        self.map[5][2] = -1  # Стены

    def get_lightening(self, light_mapper):
        self.lightmap = light_mapper.lighten(self.map)


class LightMapper(ABC):
    @abstractmethod
    def lighten(self, grid):
        pass


class Light:
    def __init__(self, dim):  # dim = (map_width, map_height)
        self.dim = dim
        self.grid = [[0 for i in range(dim[0])] for _ in range(dim[1])]
        self.lights = []
        self.obstacles = []

    def set_dim(self, dim):
        self.dim = dim
        self.grid = [[0 for i in range(dim[0])] for _ in range(dim[1])]

    def set_lights(self, lights):  # lights = [(width, height), (width, height), ...]
        self.lights = lights
        self.generate_lights()

    def set_obstacles(self, obstacles):  # obstacles = [(width, height), (width, height), ...]
        self.obstacles = obstacles
        self.generate_lights()

    def generate_lights(self):
        return self.grid.copy()


class MappingAdapter:
    def __init__(self, adaptee):
        self.adaptee = adaptee

    @staticmethod
    def _get_objects_by_grid(descriptor, grid):
        result = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == descriptor:
                    result.append((j, i))
        return result

    def lighten(self, grid):
        dim = (len(grid[0]), len(grid))
        self.adaptee.set_dim(dim)
        lights = self._get_objects_by_grid(1, grid)
        obstacles = self._get_objects_by_grid(-1, grid)
        self.adaptee.set_lights(lights)
        self.adaptee.set_obstacles(obstacles)
        return self.adaptee.generate_lights()


system = System()
