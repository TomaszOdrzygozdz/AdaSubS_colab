import gin
from goal_builders.sokoban import (
    bfs_goal_builder_sokoban,
    bfs_goal_builder_sokoban_pixel_diff,
    policy_goal_builder_sokoban,
    policy_goal_builder_sokoban_pixel_diff,
    trivial_goal_builder_sokoban,
)


def configure_goal_builder(goal_builder_class):
    return gin.external_configurable(
        goal_builder_class, module='goal_builders'
    )


BFSGoalBuilderSokoban = configure_goal_builder(bfs_goal_builder_sokoban.BFSGoalBuilderSokoban)
BFSGoalBuilderSokobanPixelDiff = configure_goal_builder(bfs_goal_builder_sokoban_pixel_diff.BFSGoalBuilderSokobanPixelDiff)
PolicyGoalBuilderSokobanPixelDiffC = configure_goal_builder(policy_goal_builder_sokoban_pixel_diff.PolicyGoalBuilderSokobanPixelDiff)
PolicyGoalBuilderSokoban = configure_goal_builder(policy_goal_builder_sokoban.PolicyGoalBuilderSokoban)
TrivialGoalBuilderSokoban = configure_goal_builder(trivial_goal_builder_sokoban.TrivialGoalBuilderSokoban)
