import gin

from value_estimators import value_estimator


def configure_value_estimator(value_estimator_class):
    return gin.external_configurable(
        value_estimator_class, module='value_estimators'
    )

configure_value_estimator(value_estimator.ValueEstimator)
