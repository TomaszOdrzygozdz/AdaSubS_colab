import gin

from solvers import solver_sokoban
from solvers import iterative_solver_sokoban


def configure_solver(goal_generator_class):
    return gin.external_configurable(
        goal_generator_class, module='solvers'
    )


configure_solver(solver_sokoban.BestFSSolverSokoban)
configure_solver(iterative_solver_sokoban.BestFSIterativeSolverSokoban)
