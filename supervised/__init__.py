import gin

from supervised import data_creator_sokoban
from supervised import data_creator_sokoban_pixel_diff
from supervised.sokoban import data_creator_policy_baseline, data_creator_conditional_policy


def configure_supervised(goal_generator_class):
    return gin.external_configurable(
        goal_generator_class, module='supervised'
    )


DataCreatorSokoban = configure_supervised(data_creator_sokoban.DataCreatorSokoban)
DataCreatorSokobanPixelDiff = configure_supervised(data_creator_sokoban_pixel_diff.DataCreatorSokobanPixelDiff)
DataCreatorPolicyBaselineSokoban = configure_supervised(data_creator_policy_baseline.DataCreatorPolicyBaselineSokoban)
DataCreatorConditionalPolicySokoban = configure_supervised(data_creator_conditional_policy.DataCreatorConditionalPolicySokoban)
