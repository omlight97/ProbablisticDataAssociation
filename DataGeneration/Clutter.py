import scipy.stats as dist
import numpy as np


# class clutter - choose the dist (with switches) and have it with mean 0
# generation - create the data then move it to desired mean then returns it


class Clutter:
    """creates a clutter of measurements based on chosen distribution. choose the distribution
    then to center it around a desired point using the generate_clutter function"""
    CLUTTER_SIZE = 100

    def __init__(self,
                 dist_type: str,
                 std: float) -> None:
        """Args:
            dist_type(str): Distribution of the clutter. the options are:
                            "normal" - for normal distribution.
                            "uniform" - for uniform distribution.
            std(float): Standard deviation of the distribution.
         """
        self.dist = dist_type
        self.std = std
        mean_x = 0
        mean_y = 0

        match self.dist.lower():
            case "normal":
                self._x_dist = dist.norm(loc=mean_x, scale=self.std)
                self._y_dist = dist.norm(loc=mean_y, scale=self.std)

            case "uniform":
                # mean = (a+b)/2 , var = (b-a)^2 / 12
                # if we want mean = 0 then a = -b, meaning: var = 4b^2 / 12 = b^2 / 3
                # therefore  b = -a = sqrt(3*var)
                high_bound = np.sqrt(3 * self.std)
                low_bound = -high_bound
                self._x_dist = dist.uniform(loc=low_bound, scale=high_bound - low_bound)
                self._y_dist = dist.uniform(loc=low_bound, scale=high_bound - low_bound)

    def generate_clutter(self, mean: tuple) -> set:
        """Returns a clutter with chosen distribution for object Clutter and a given mean
            Args:
                mean - the (x,y) coordinate that are then mean of the distribution """
        x_clutter = self._x_dist.rvs(size=self.CLUTTER_SIZE) + mean[0]
        y_clutter = self._y_dist.rvs(size=self.CLUTTER_SIZE) + mean[1]
        clutter = {(x_clutter[idx], y_clutter[idx])
                   for idx in range(self.CLUTTER_SIZE)}
        return clutter
