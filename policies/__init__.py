import gin

from policies.sokoban.policy_baseline import SokobanPolicyBaseline
from policies.sokoban.conditional_policy import SokobanConditionalPolicy


def configure_policy(policy_class):
    return gin.external_configurable(
        policy_class, module='policies'
    )


SokobanConditionalPolicy = configure_policy(SokobanConditionalPolicy)
SokobanPolicyBaseline = configure_policy(SokobanPolicyBaseline)
